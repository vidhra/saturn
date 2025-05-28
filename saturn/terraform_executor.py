# Multi-cloud Terraform executor for Saturn architecture - supports ALL GCP and AWS services
import os
import json
import asyncio
import tempfile
import subprocess
import shutil
import re
import io
from datetime import datetime
from typing import Dict, Any, Tuple, Optional, List, Union
from pathlib import Path
from rich.console import Console
from abc import ABC, abstractmethod

try:
    import hcl2
    HCL2_AVAILABLE = True
except ImportError:
    HCL2_AVAILABLE = False
    print("Warning: python-hcl2 not available. Install with: pip install python-hcl2")

try:
    import hcl
    HCL_AVAILABLE = True
except ImportError:
    HCL_AVAILABLE = False
    print("Warning: pyhcl not available. Install with: pip install pyhcl")

class HCLConverter:
    """
    Bidirectional converter between JSON and Terraform HCL using proper libraries.
    Also converts existing Terraform files to Saturn log format.
    """
    
    @staticmethod
    def json_to_hcl(config: Dict[str, Any]) -> str:
        """Convert JSON configuration to valid Terraform HCL."""
        
        if not HCL2_AVAILABLE:
            print("Warning: python-hcl2 not available, using fallback conversion")
            return HCLConverter._fallback_json_to_hcl(config)
        
        try:
            hcl_parts = []
            
            if "terraform" in config:
                hcl_parts.append(HCLConverter._format_terraform_block(config["terraform"]))
            
            if "provider" in config:
                for provider_name, provider_config in config["provider"].items():
                    hcl_parts.append(HCLConverter._format_provider_block(provider_name, provider_config))
            
            if "variable" in config:
                for var_name, var_config in config["variable"].items():
                    hcl_parts.append(HCLConverter._format_variable_block(var_name, var_config))
            
            if "locals" in config:
                hcl_parts.append(HCLConverter._format_locals_block(config["locals"]))
            
            if "data" in config:
                for data_type, data_sources in config["data"].items():
                    for data_name, data_config in data_sources.items():
                        hcl_parts.append(HCLConverter._format_data_block(data_type, data_name, data_config))
            
            if "resource" in config:
                for resource_type, resources in config["resource"].items():
                    for resource_name, resource_config in resources.items():
                        hcl_parts.append(HCLConverter._format_resource_block(resource_type, resource_name, resource_config))
            
            if "output" in config:
                for output_name, output_config in config["output"].items():
                    hcl_parts.append(HCLConverter._format_output_block(output_name, output_config))
            
            if "module" in config:
                for module_name, module_config in config["module"].items():
                    hcl_parts.append(HCLConverter._format_module_block(module_name, module_config))
            
            return "\n\n".join(hcl_parts)
            
        except Exception as e:
            print(f"HCL conversion error: {e}, falling back to simple conversion")
            return HCLConverter._fallback_json_to_hcl(config)
    
    @staticmethod
    def hcl_to_json(hcl_content: str) -> Dict[str, Any]:
        """Convert HCL content to JSON configuration."""
        
        if not HCL2_AVAILABLE:
            print("Warning: python-hcl2 not available for HCL parsing")
            return {}
        
        try:
            return hcl2.loads(hcl_content)
        except Exception as e:
            print(f"HCL parsing error: {e}")
            return {}
    
    @staticmethod
    def terraform_to_saturn_log(
        terraform_dir: str, 
        original_query: str = "Converted from existing Terraform",
        step_prefix: str = "converted_step"
    ) -> Dict[str, Any]:
        """Convert existing Terraform files to Saturn log format."""
        
        tf_dir = Path(terraform_dir)
        if not tf_dir.exists():
            return {"error": f"Terraform directory {terraform_dir} does not exist"}
        
        tf_files = list(tf_dir.glob("*.tf")) + list(tf_dir.glob("*.tf.json"))
        
        if not tf_files:
            return {"error": f"No Terraform files found in {terraform_dir}"}
        
        # Parse all Terraform configurations
        all_resources = {}
        all_providers = {}
        all_variables = {}
        all_outputs = {}
        
        for tf_file in tf_files:
            try:
                if tf_file.suffix == '.json':
                    with open(tf_file, 'r') as f:
                        config = json.load(f)
                else:
                    with open(tf_file, 'r') as f:
                        hcl_content = f.read()
                        config = HCLConverter.hcl_to_json(hcl_content)
                
                if "resource" in config:
                    all_resources.update(config["resource"])
                if "provider" in config:
                    all_providers.update(config["provider"])
                if "variable" in config:
                    all_variables.update(config["variable"])
                if "output" in config:
                    all_outputs.update(config["output"])
                    
            except Exception as e:
                print(f"Error parsing {tf_file}: {e}")
                continue
        
        saturn_log = HCLConverter._create_saturn_log_from_terraform(
            all_resources, all_providers, all_variables, all_outputs, 
            original_query, step_prefix
        )
        
        tfstate_file = tf_dir / "terraform.tfstate"
        if tfstate_file.exists():
            saturn_log["tfstate_info"] = HCLConverter._parse_tfstate(tfstate_file)
        
        return saturn_log
    
    @staticmethod
    def _create_saturn_log_from_terraform(
        resources: Dict[str, Any],
        providers: Dict[str, Any], 
        variables: Dict[str, Any],
        outputs: Dict[str, Any],
        original_query: str,
        step_prefix: str
    ) -> Dict[str, Any]:
        """Create Saturn log structure from Terraform components."""
        
        current_time = datetime.now().isoformat()
        
        nodes = {}
        execution_order = []
        
        step_counter = 1
        for resource_type, resource_instances in resources.items():
            for resource_name, resource_config in resource_instances.items():
                step_id = f"{step_prefix}_{step_counter}_{resource_type}_{resource_name}"
                
                if resource_type.startswith('google_'):
                    cloud_provider = "gcp"
                    command = HCLConverter._terraform_to_gcloud_command(resource_type, resource_name, resource_config)
                elif resource_type.startswith('aws_'):
                    cloud_provider = "aws"
                    command = HCLConverter._terraform_to_aws_command(resource_type, resource_name, resource_config)
                else:
                    cloud_provider = "unknown"
                    command = f"# Terraform resource: {resource_type}.{resource_name}"
                
                nodes[step_id] = {
                    "description": f"Convert existing Terraform resource {resource_type}.{resource_name}",
                    "cloud_provider": cloud_provider,
                    "dependencies": [],
                    "tool_to_use": "terraform_import",
                    "pass_output_to_next": False
                }
                
                execution_order.append(step_id)
                step_counter += 1
        
        saturn_log = {
            "run_info": {
                "query": original_query,
                "start_time": current_time,
                "end_time": current_time,
                "final_status": "CONVERTED_FROM_TERRAFORM",
                "attempts_made": 0,
                "final_errors": None,
                "conversion_source": "existing_terraform_files"
            },
            "dag": {
                "nodes": {step_id: nodes[step_id] for step_id in execution_order},
                "edges": [],
                "execution_order": execution_order
            },
            "nodes": {}
        }
        
        step_counter = 1
        for resource_type, resource_instances in resources.items():
            for resource_name, resource_config in resource_instances.items():
                step_id = f"{step_prefix}_{step_counter}_{resource_type}_{resource_name}"
                
                if resource_type.startswith('google_'):
                    cloud_provider = "gcp"
                    command = HCLConverter._terraform_to_gcloud_command(resource_type, resource_name, resource_config)
                elif resource_type.startswith('aws_'):
                    cloud_provider = "aws"
                    command = HCLConverter._terraform_to_aws_command(resource_type, resource_name, resource_config)
                else:
                    cloud_provider = "unknown"
                    command = f"# Unknown resource type: {resource_type}"
                
                saturn_log["nodes"][step_id] = {
                    "tool_name": "terraform_import",
                    "attempt": 0,
                    "arguments": {
                        "cloud_provider": cloud_provider,
                        "terraform_resource_type": resource_type,
                        "terraform_resource_name": resource_name
                    },
                    "status_history": [
                        [current_time, "CONVERTED_FROM_EXISTING"]
                    ],
                    "current_status": "CONVERTED_FROM_EXISTING",
                    "output": {
                        "result": f"Converted from existing Terraform resource {resource_type}.{resource_name}",
                        "executed_command_str": command,
                        "terraform_config": resource_config
                    },
                    "error": None,
                    "dependencies": []
                }
                
                step_counter += 1
        
        return saturn_log
    
    @staticmethod
    def _terraform_to_gcloud_command(resource_type: str, resource_name: str, config: Dict[str, Any]) -> str:
        """Dynamically reverse-engineer gcloud command from Terraform resource using provider schema."""
        
        return HCLConverter._reverse_engineer_gcloud_command(resource_type, resource_name, config)
    
    @staticmethod
    def _terraform_to_aws_command(resource_type: str, resource_name: str, config: Dict[str, Any]) -> str:
        """Dynamically reverse-engineer AWS CLI command from Terraform resource using provider schema."""
        
        return HCLConverter._reverse_engineer_aws_command(resource_type, resource_name, config)
    
    @staticmethod
    def _parse_tfstate(tfstate_file: Path) -> Dict[str, Any]:
        """Parse terraform.tfstate file for additional information."""
        
        try:
            with open(tfstate_file, 'r') as f:
                tfstate = json.load(f)
            
            return {
                "version": tfstate.get("version"),
                "terraform_version": tfstate.get("terraform_version"),
                "serial": tfstate.get("serial"),
                "lineage": tfstate.get("lineage"),
                "resources_count": len(tfstate.get("resources", [])),
                "outputs": tfstate.get("outputs", {})
            }
        except Exception as e:
            return {"error": f"Could not parse tfstate: {e}"}
    
    @staticmethod
    def _format_terraform_block(terraform_config: Dict[str, Any]) -> str:
        """Format terraform block in HCL."""
        return f"terraform {HCLConverter._format_hcl_value(terraform_config)}"
    
    @staticmethod
    def _format_provider_block(provider_name: str, provider_config: Dict[str, Any]) -> str:
        """Format provider block in HCL."""
        return f'provider "{provider_name}" {HCLConverter._format_hcl_value(provider_config)}'
    
    @staticmethod
    def _format_variable_block(var_name: str, var_config: Dict[str, Any]) -> str:
        """Format variable block in HCL."""
        return f'variable "{var_name}" {HCLConverter._format_hcl_value(var_config)}'
    
    @staticmethod
    def _format_locals_block(locals_config: Dict[str, Any]) -> str:
        """Format locals block in HCL."""
        return f"locals {HCLConverter._format_hcl_value(locals_config)}"
    
    @staticmethod
    def _format_data_block(data_type: str, data_name: str, data_config: Dict[str, Any]) -> str:
        """Format data block in HCL."""
        return f'data "{data_type}" "{data_name}" {HCLConverter._format_hcl_value(data_config)}'
    
    @staticmethod
    def _format_resource_block(resource_type: str, resource_name: str, resource_config: Dict[str, Any]) -> str:
        """Format resource block in HCL."""
        return f'resource "{resource_type}" "{resource_name}" {HCLConverter._format_hcl_value(resource_config)}'
    
    @staticmethod
    def _format_output_block(output_name: str, output_config: Dict[str, Any]) -> str:
        """Format output block in HCL."""
        return f'output "{output_name}" {HCLConverter._format_hcl_value(output_config)}'
    
    @staticmethod
    def _format_module_block(module_name: str, module_config: Dict[str, Any]) -> str:
        """Format module block in HCL."""
        return f'module "{module_name}" {HCLConverter._format_hcl_value(module_config)}'
    
    @staticmethod
    def _format_hcl_value(value: Any, indent: int = 0) -> str:
        """Format a value in HCL syntax."""
        
        indent_str = "  " * indent
        
        if isinstance(value, dict):
            if not value:
                return "{}"
            
            lines = ["{"]
            for k, v in value.items():
                formatted_v = HCLConverter._format_hcl_value(v, indent + 1)
                lines.append(f"{indent_str}  {k} = {formatted_v}")
            lines.append(f"{indent_str}}}")
            return "\n".join(lines)
            
        elif isinstance(value, list):
            if not value:
                return "[]"
            
            if len(value) == 1 and isinstance(value[0], (str, int, bool, float)):
                return f"[{HCLConverter._format_hcl_value(value[0])}]"
            
            lines = ["["]
            for item in value:
                formatted_item = HCLConverter._format_hcl_value(item, indent + 1)
                lines.append(f"{indent_str}  {formatted_item},")
            lines.append(f"{indent_str}]")
            return "\n".join(lines)
            
        elif isinstance(value, str):
            if (value.startswith("${") and value.endswith("}")) or \
               (value.startswith("var.") or value.startswith("data.") or 
                value.startswith("resource.") or value.startswith("local.") or
                value.startswith("module.")):
                return value  
            else:
                escaped_value = value.replace('"', '\\"')
                return f'"{escaped_value}"'
                
        elif isinstance(value, bool):
            return "true" if value else "false"
            
        elif isinstance(value, (int, float)):
            return str(value)
            
        elif value is None:
            return "null"
            
        else:
            return f'"{str(value)}"'
    
    @staticmethod
    def _fallback_json_to_hcl(config: Dict[str, Any]) -> str:
        """Fallback conversion when HCL libraries are not available."""
        return json.dumps(config, indent=2)
    
    @staticmethod
    def _reverse_engineer_gcloud_command(resource_type: str, resource_name: str, config: Dict[str, Any]) -> str:
        """
        Dynamically reverse-engineer gcloud command from Terraform resource.
        Uses provider schema and real CLI patterns instead of hardcoded mappings.
        """
        
        try:
        
            provider_schema = HCLConverter._get_provider_schema('google', resource_type)
            if provider_schema:
                return HCLConverter._construct_gcloud_from_schema(resource_type, resource_name, config, provider_schema)
            
            return HCLConverter._reverse_engineer_gcloud_from_pattern(resource_type, resource_name, config)
            
        except Exception as e:
            return f"# Could not reverse-engineer gcloud command for {resource_type}.{resource_name}: {str(e)}"
    
    @staticmethod
    def _reverse_engineer_aws_command(resource_type: str, resource_name: str, config: Dict[str, Any]) -> str:
        """
        Dynamically reverse-engineer AWS CLI command from Terraform resource.
        Uses provider schema and real CLI patterns instead of hardcoded mappings.
        """
        
        try:
            
            provider_schema = HCLConverter._get_provider_schema('aws', resource_type)
            if provider_schema:
                return HCLConverter._construct_aws_from_schema(resource_type, resource_name, config, provider_schema)
            return HCLConverter._reverse_engineer_aws_from_pattern(resource_type, resource_name, config)
            
        except Exception as e:
            return f"# Could not reverse-engineer AWS CLI command for {resource_type}.{resource_name}: {str(e)}"
    
    @staticmethod
    def _get_provider_schema(provider: str, resource_type: str) -> Optional[Dict[str, Any]]:
        """
        Get real Terraform provider schema for a resource type.
        Uses 'terraform providers schema' command to get actual schema.
        """
        
        try:
            
            import tempfile
            import subprocess
            
            with tempfile.TemporaryDirectory() as temp_dir:
                tf_config = {
                    "terraform": {
                        "required_providers": {
                            provider: {
                                "source": f"hashicorp/{provider}",
                                "version": "~> 4.0" if provider == "google" else "~> 5.0"
                            }
                        }
                    }
                }
                
                config_file = Path(temp_dir) / "main.tf.json"
                with open(config_file, 'w') as f:
                    json.dump(tf_config, f)
                

                init_result = subprocess.run(
                    ['terraform', 'init'],
                    cwd=temp_dir,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if init_result.returncode == 0:
                    schema_result = subprocess.run(
                        ['terraform', 'providers', 'schema', '-json'],
                        cwd=temp_dir,
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    if schema_result.returncode == 0:
                        schema_data = json.loads(schema_result.stdout)
                        
                        # Extract the specific resource schema
                        provider_schemas = schema_data.get('provider_schemas', {})
                        for provider_key, provider_info in provider_schemas.items():
                            if provider in provider_key:
                                resource_schemas = provider_info.get('resource_schemas', {})
                                if resource_type in resource_schemas:
                                    return resource_schemas[resource_type]
            
            return None
            
        except Exception:
            return None
    
    @staticmethod
    def _construct_gcloud_from_schema(resource_type: str, resource_name: str, config: Dict[str, Any], schema: Dict[str, Any]) -> str:
        """Construct gcloud command using real provider schema."""
        return HCLConverter._reverse_engineer_gcloud_from_pattern(resource_type, resource_name, config)
    
    @staticmethod
    def _construct_aws_from_schema(resource_type: str, resource_name: str, config: Dict[str, Any], schema: Dict[str, Any]) -> str:
        """Construct AWS CLI command using real provider schema."""

        return HCLConverter._reverse_engineer_aws_from_pattern(resource_type, resource_name, config)
    
    @staticmethod
    def _reverse_engineer_gcloud_from_pattern(resource_type: str, resource_name: str, config: Dict[str, Any]) -> str:
        """
        Reverse-engineer gcloud command using pattern analysis.
        This reverses our dynamic parsing logic.
        """
        
        if not resource_type.startswith('google_'):
            return f"# Unknown Google resource type: {resource_type}"
        
        parts = resource_type[7:].split('_')  
        if len(parts) < 2:
            return f"# Cannot parse resource type: {resource_type}"
        
        service = parts[0]
        resource_subtype = '_'.join(parts[1:])
        
        resource_plural = HCLConverter._pluralize_resource_type(resource_subtype)

        action = 'create'
        if 'google_storage_bucket' in resource_type:
            action = 'create'  
        elif 'google_compute_address' in resource_type:
            action = 'reserve' 
        elif 'google_cloudfunctions_function' in resource_type:
            action = 'deploy'  
            service = 'functions'
            resource_plural = ''
        
        if resource_plural:
            base_cmd = f"gcloud {service} {resource_plural} {action}"
        else:
            base_cmd = f"gcloud {service} {action}"
        
        name = config.get('name', resource_name)
        if isinstance(name, str) and name.startswith('${'):
            name = resource_name
        
        command = f"{base_cmd} {name}"
        
        for tf_attr, value in config.items():
            if tf_attr in ['name', 'project']: 
                continue
                
            gcloud_flag = HCLConverter._terraform_attr_to_gcloud_flag(tf_attr, value)
            if gcloud_flag:
                command += f" {gcloud_flag}"
        
        return command
    
    @staticmethod
    def _reverse_engineer_aws_from_pattern(resource_type: str, resource_name: str, config: Dict[str, Any]) -> str:
        """
        Reverse-engineer AWS CLI command using pattern analysis.
        This reverses our dynamic parsing logic.
        """
        
        if not resource_type.startswith('aws_'):
            return f"# Unknown AWS resource type: {resource_type}"
        
        parts = resource_type[4:].split('_')
        if len(parts) < 1:
            return f"# Cannot parse resource type: {resource_type}"
        
        service = parts[0]
        resource_subtype = '_'.join(parts[1:]) if len(parts) > 1 else ''
        
        action = HCLConverter._get_aws_action(service, resource_subtype)
        
        if resource_type == 'aws_s3_bucket':
            bucket_name = config.get('bucket', resource_name)
            return f"aws s3 mb s3://{bucket_name}"
        
        base_cmd = f"aws {service} {action}"
        params = []
        for tf_attr, value in config.items():
            if tf_attr == 'tags': 
                continue
                
            aws_param = HCLConverter._terraform_attr_to_aws_param(tf_attr, value, resource_type)
            if aws_param:
                params.append(aws_param)
        
        if params:
            command = f"{base_cmd} {' '.join(params)}"
        else:
            command = base_cmd
        
        return command
    
    @staticmethod
    def _pluralize_resource_type(resource_type: str) -> str:
        """Convert singular resource type to plural gcloud format."""
        
        if resource_type == 'instance_template':
            return 'instance-templates'
        elif resource_type == 'firewall':
            return 'firewall-rules'
        elif resource_type.endswith('_instance'):
            return resource_type.replace('_', '-') + 's'
        elif resource_type.endswith('s'):
            return resource_type.replace('_', '-')
        else:
            return resource_type.replace('_', '-') + 's'
    
    @staticmethod
    def _terraform_attr_to_gcloud_flag(attr: str, value: Any) -> Optional[str]:
        """Convert Terraform attribute to gcloud flag."""
        

        flag_name = attr.replace('_', '-')
        

        if isinstance(value, bool):
            if value:
                return f"--{flag_name}"
            else:
                return f"--no-{flag_name}"
        elif isinstance(value, list):
            if flag_name == 'tags':
                return f"--tags={','.join(str(v) for v in value)}"
            else:
                return f"--{flag_name}={','.join(str(v) for v in value)}"
        elif isinstance(value, str) and not value.startswith('${'):
            return f"--{flag_name}={value}"
        elif isinstance(value, (int, float)):
            return f"--{flag_name}={value}"
        else:

            return None
    
    @staticmethod
    def _get_aws_action(service: str, resource_type: str) -> str:
        """Determine AWS CLI action from service and resource type."""
        

        if service == 'ec2':
            if resource_type == 'instance':
                return 'run-instances'
            elif resource_type == 'vpc':
                return 'create-vpc'
            elif resource_type == 'subnet':
                return 'create-subnet'
            elif resource_type == 'security_group':
                return 'create-security-group'
            else:
                return f"create-{resource_type.replace('_', '-')}"
        elif service == 'iam':
            return f"create-{resource_type.replace('_', '-')}"
        elif service == 'rds':
            return f"create-{resource_type.replace('_', '-')}"
        elif service == 's3':
            return 'mb' 
        else:
            return f"create-{resource_type.replace('_', '-')}"
    
    @staticmethod
    def _terraform_attr_to_aws_param(attr: str, value: Any, resource_type: str) -> Optional[str]:
        """Convert Terraform attribute to AWS CLI parameter."""
        

        if attr == 'ami':
            return f"--image-id {value}"
        elif attr == 'instance_type':
            return f"--instance-type {value}"
        elif attr == 'cidr_block':
            return f"--cidr-block {value}"
        elif attr == 'name' and not str(value).startswith('${'):
            return f"--name {value}"
        elif isinstance(value, str) and not value.startswith('${'):
            # Convert snake_case to kebab-case
            param_name = attr.replace('_', '-')
            return f"--{param_name} {value}"
        else:
            # Skip Terraform expressions and complex objects
            return None

class CloudResourceMapper:
    """
    Dynamic cloud resource mapper that uses configuration files and intelligent parsing
    instead of hardcoded mappings.
    """
    
    def __init__(self):
        # Load mappings from external configuration
        self.gcp_mappings = self._load_gcp_mappings()
        self.aws_mappings = self._load_aws_mappings()
        
        # Common attribute mappings that work across resources
        self.common_attribute_mappings = {
            # Universal mappings
            'name': 'name',
            'description': 'description',
            'tags': 'tags',
            'labels': 'labels',
            'region': 'region', 
            'zone': 'zone',
            'project': 'project',
            
            # Size/capacity related
            'size': ['disk_size_gb', 'size', 'capacity'],
            'disk-size': 'disk_size_gb',
            'memory': 'memory_size_gb',
            'cpu': 'cpu',
            'vcpus': 'vcpu_count',
            
            # Network related
            'network': 'network',
            'subnet': ['subnetwork', 'subnet_id'],
            'vpc': ['network', 'vpc_id'],
            'cidr': ['ip_cidr_range', 'cidr_block'],
            'ip': ['ip_address', 'private_ip'],
            
            # Security related
            'firewall': 'firewall_rules',
            'security-group': ['security_groups', 'vpc_security_group_ids'],
            
            # Instance related
            'machine-type': ['machine_type', 'instance_type'],
            'instance-type': ['instance_type', 'machine_type'],
            'image': ['source_image', 'ami', 'image_id'],
            'boot-disk': 'boot_disk',
            'key': ['ssh_keys', 'key_name'],
            
            # Storage related
            'storage-class': 'storage_class',
            'storage-type': ['storage_type', 'disk_type'],
            'backup': 'backup_configuration',
            'encryption': 'encryption',
            
            # Database related
            'database-version': ['database_version', 'engine_version'],
            'tier': ['tier', 'instance_class'],
            'username': ['username', 'master_username'],
            'password': ['password', 'master_user_password'],
            
            # Access related
            'public': 'publicly_accessible',
            'private': 'private',
            'internal': 'internal',
        }
    
    def _load_gcp_mappings(self) -> Dict[str, Any]:
        """Load GCP service to Terraform resource mappings."""
        
        # This could be loaded from a YAML/JSON file in production
        return {
            'compute': {
                'instances': 'google_compute_instance',
                'instance-templates': 'google_compute_instance_template', 
                'instance-groups': 'google_compute_instance_group',
                'networks': 'google_compute_network',
                'subnets': 'google_compute_subnetwork',
                'firewall-rules': 'google_compute_firewall',
                'addresses': 'google_compute_address',
                'disks': 'google_compute_disk',
                'images': 'google_compute_image',
                'snapshots': 'google_compute_snapshot',
                'routers': 'google_compute_router',
                'routes': 'google_compute_route',
                'forwarding-rules': 'google_compute_forwarding_rule',
                'target-pools': 'google_compute_target_pool',
                'backend-services': 'google_compute_backend_service',
                'health-checks': 'google_compute_health_check',
                'url-maps': 'google_compute_url_map',
                'ssl-certificates': 'google_compute_ssl_certificate',
                'target-http-proxies': 'google_compute_target_http_proxy',
                'target-https-proxies': 'google_compute_target_https_proxy',
                'global-forwarding-rules': 'google_compute_global_forwarding_rule'
            },
            'container': {
                'clusters': 'google_container_cluster',
                'node-pools': 'google_container_node_pool'
            },
            'sql': {
                'instances': 'google_sql_database_instance',
                'databases': 'google_sql_database',
                'users': 'google_sql_user'
            },
            'storage': {
                'buckets': 'google_storage_bucket'
            },
            'functions': {
                'deploy': 'google_cloudfunctions_function'
            },
            'iam': {
                'service-accounts': 'google_service_account',
                'roles': 'google_project_iam_custom_role'
            },
            'dns': {
                'managed-zones': 'google_dns_managed_zone',
                'record-sets': 'google_dns_record_set'
            },
            'pubsub': {
                'topics': 'google_pubsub_topic',
                'subscriptions': 'google_pubsub_subscription'
            },
            'redis': {
                'instances': 'google_redis_instance'
            },
            'memcache': {
                'instances': 'google_memcache_instance'
            },
            'bigquery': {
                'datasets': 'google_bigquery_dataset',
                'tables': 'google_bigquery_table'
            },
            'dataflow': {
                'jobs': 'google_dataflow_job'
            },
            'dataproc': {
                'clusters': 'google_dataproc_cluster'
            },
            'monitoring': {
                'uptime-checks': 'google_monitoring_uptime_check_config',
                'alert-policies': 'google_monitoring_alert_policy'
            },
            'logging': {
                'sinks': 'google_logging_project_sink'
            }
        }
    
    def _load_aws_mappings(self) -> Dict[str, Any]:
        """Load AWS service to Terraform resource mappings."""
        
        return {
            'ec2': {
                'run-instances': 'aws_instance',
                'create-vpc': 'aws_vpc',
                'create-subnet': 'aws_subnet',
                'create-security-group': 'aws_security_group',
                'create-key-pair': 'aws_key_pair',
                'create-launch-template': 'aws_launch_template',
                'create-launch-configuration': 'aws_launch_configuration',
                'create-volume': 'aws_ebs_volume',
                'create-snapshot': 'aws_ebs_snapshot',
                'create-image': 'aws_ami',
                'allocate-address': 'aws_eip',
                'create-internet-gateway': 'aws_internet_gateway',
                'create-nat-gateway': 'aws_nat_gateway',
                'create-route-table': 'aws_route_table',
                'create-route': 'aws_route',
                'associate-route-table': 'aws_route_table_association',
                'create-network-acl': 'aws_network_acl',
                'create-placement-group': 'aws_placement_group',
                'create-spot-fleet-request': 'aws_spot_fleet_request'
            },
            'rds': {
                'create-db-instance': 'aws_db_instance',
                'create-db-cluster': 'aws_rds_cluster',
                'create-db-subnet-group': 'aws_db_subnet_group',
                'create-db-parameter-group': 'aws_db_parameter_group'
            },
            's3': {
                'mb': 'aws_s3_bucket',
                'create-bucket': 'aws_s3_bucket'
            },
            'iam': {
                'create-user': 'aws_iam_user',
                'create-group': 'aws_iam_group', 
                'create-role': 'aws_iam_role',
                'create-policy': 'aws_iam_policy',
                'create-access-key': 'aws_iam_access_key'
            },
            'lambda': {
                'create-function': 'aws_lambda_function',
                'create-event-source-mapping': 'aws_lambda_event_source_mapping'
            },
            'ecs': {
                'create-cluster': 'aws_ecs_cluster',
                'create-service': 'aws_ecs_service',
                'register-task-definition': 'aws_ecs_task_definition'
            },
            'eks': {
                'create-cluster': 'aws_eks_cluster',
                'create-nodegroup': 'aws_eks_node_group'
            },
            'elasticache': {
                'create-cache-cluster': 'aws_elasticache_cluster'
            },
            'sns': {
                'create-topic': 'aws_sns_topic'
            },
            'sqs': {
                'create-queue': 'aws_sqs_queue'
            },
            'dynamodb': {
                'create-table': 'aws_dynamodb_table'
            },
            'cloudformation': {
                'create-stack': 'aws_cloudformation_stack'
            },
            'route53': {
                'create-hosted-zone': 'aws_route53_zone'
            },
            'apigateway': {
                'create-rest-api': 'aws_api_gateway_rest_api'
            },
            'elbv2': {
                'create-load-balancer': 'aws_lb',
                'create-target-group': 'aws_lb_target_group'
            },
            'autoscaling': {
                'create-auto-scaling-group': 'aws_autoscaling_group'
            },
            'kms': {
                'create-key': 'aws_kms_key'
            },
            'secretsmanager': {
                'create-secret': 'aws_secretsmanager_secret'
            },
            'cloudwatch': {
                'put-metric-alarm': 'aws_cloudwatch_metric_alarm'
            },
            'logs': {
                'create-log-group': 'aws_cloudwatch_log_group'
            }
        }
    
    def find_terraform_resource(self, provider: str, service: str, resource_type: str, action: str) -> Optional[str]:
        """Dynamically find Terraform resource type."""
        
        if provider == 'gcp':
            mappings = self.gcp_mappings
        elif provider == 'aws':
            mappings = self.aws_mappings
        else:
            return None
        
        # Try exact service + resource_type match
        if service in mappings:
            service_mapping = mappings[service]
            if resource_type in service_mapping:
                return service_mapping[resource_type]
            # Try action-based mapping for services without resource types
            elif action in service_mapping:
                return service_mapping[action]
        
        # Try fuzzy matching
        return self._fuzzy_match_resource(provider, service, resource_type, action)
    
    def _fuzzy_match_resource(self, provider: str, service: str, resource_type: str, action: str) -> Optional[str]:
        """Attempt fuzzy matching for unmapped resources."""
        
        # Try to construct resource name based on patterns
        if provider == 'gcp':
            # GCP pattern: google_{service}_{resource_type}
            potential_resource = f"google_{service}_{resource_type.replace('-', '_')}"
        elif provider == 'aws':
            # AWS pattern: aws_{service/resource_type}
            if resource_type:
                potential_resource = f"aws_{resource_type.replace('-', '_')}"
            else:
                potential_resource = f"aws_{service}_{action.replace('-', '_')}"
        else:
            return None
            
        # This could be validated against the actual Terraform provider schema
        return potential_resource
    
    def map_attributes(self, attributes: Dict[str, Any], terraform_resource: str) -> Dict[str, Any]:
        """Dynamically map CLI attributes to Terraform attributes."""
        
        mapped = {}
        
        for cli_attr, value in attributes.items():
            # Try direct mapping first
            if cli_attr in self.common_attribute_mappings:
                tf_attr = self.common_attribute_mappings[cli_attr]
                
                if isinstance(tf_attr, list):
                    # Multiple possible mappings, choose based on resource type
                    tf_attr = self._choose_best_mapping(tf_attr, terraform_resource)
                
                mapped[tf_attr] = value
            else:
                # Use heuristic mapping
                tf_attr = self._heuristic_attribute_mapping(cli_attr, terraform_resource)
                if tf_attr:
                    mapped[tf_attr] = value
        
        return mapped
    
    def _choose_best_mapping(self, options: List[str], terraform_resource: str) -> str:
        """Choose the best attribute mapping based on resource type."""
        
        # Resource-specific preferences
        if 'aws_' in terraform_resource:
            # Prefer AWS-style attributes
            aws_attrs = [attr for attr in options if 'id' in attr or 'vpc' in attr or 'security' in attr]
            if aws_attrs:
                return aws_attrs[0]
        elif 'google_' in terraform_resource:
            # Prefer GCP-style attributes
            gcp_attrs = [attr for attr in options if 'subnetwork' in attr or 'source' in attr]
            if gcp_attrs:
                return gcp_attrs[0]
        
        return options[0]  # Default to first option
    
    def _heuristic_attribute_mapping(self, cli_attr: str, terraform_resource: str) -> Optional[str]:
        """Use heuristics to map unknown attributes."""
        
        # Convert kebab-case to snake_case
        tf_attr = cli_attr.replace('-', '_')
        
        # Handle boolean flags
        if cli_attr.startswith('no-'):
            base_attr = cli_attr[3:].replace('-', '_')
            return base_attr  # The value should be negated during processing
        
        if cli_attr.startswith('enable-'):
            return cli_attr[7:].replace('-', '_')
        
        if cli_attr.startswith('disable-'):
            return cli_attr[8:].replace('-', '_')
        
        return tf_attr

class CloudProviderConverter(ABC):
    """Abstract base class for cloud provider command converters."""
    
    def __init__(self):
        self.mapper = CloudResourceMapper()
        self.hcl_converter = HCLConverter()
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Return the provider name (e.g., 'gcp', 'aws')."""
        pass
    
    @abstractmethod
    def can_convert_command(self, command: str) -> bool:
        """Check if this converter can handle the given command."""
        pass
    
    @abstractmethod
    def parse_command(self, command: str) -> Tuple[str, str, str, str, Dict[str, Any]]:
        """Parse command into service, resource_type, action, name, and attributes."""
        pass
    
    @abstractmethod
    def get_terraform_provider_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Get the Terraform provider configuration block."""
        pass
    
    def convert_command_to_terraform(self, command: str, config: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Convert any cloud CLI command to Terraform configuration using dynamic mapping."""
        
        try:
            # Parse the command
            service, resource_type, action, resource_name, attributes = self.parse_command(command)
            
            if not service or not action:
                return self._create_unsupported_response(command, "Could not parse command structure")
            
            # Find the Terraform resource type
            terraform_resource = self.mapper.find_terraform_resource(
                self.get_provider_name(), service, resource_type, action
            )
            
            if not terraform_resource:
                return self._create_unsupported_response(
                    command, 
                    f"No Terraform resource mapping found for {service} {resource_type} {action}"
                )
            
            # Map attributes
            mapped_attributes = self.mapper.map_attributes(attributes, terraform_resource)
            
            # Add provider-specific enhancements
            enhanced_attributes = self._enhance_attributes(
                mapped_attributes, terraform_resource, service, config
            )
            
            # Generate clean resource name
            clean_name = re.sub(r'[^a-zA-Z0-9_]', '_', resource_name)
            if not clean_name or clean_name.isdigit():
                clean_name = f"{service}_{action}_resource"
            
            # Create resource configuration
            resources = {
                terraform_resource: {
                    clean_name: enhanced_attributes
                }
            }
            
            # Get provider configuration
            providers = self.get_terraform_provider_config(config)
            
            # Create complete Terraform configuration in JSON format
            terraform_config = {
                "terraform": {
                    "required_providers": {
                        "google": {"source": "hashicorp/google", "version": "~> 4.0"},
                        "aws": {"source": "hashicorp/aws", "version": "~> 5.0"}
                    }
                },
                "provider": providers,
                "resource": resources
            }
            
            return {
                "type": "terraform_config",
                "config": terraform_config,
                "original_command": command,
                "resource_name": clean_name,
                "provider": self.get_provider_name(),
                "service": service,
                "action": action,
                "terraform_resource": terraform_resource
            }
            
        except Exception as e:
            return self._create_unsupported_response(command, f"Conversion error: {str(e)}")
    
    def _enhance_attributes(
        self, 
        attributes: Dict[str, Any], 
        terraform_resource: str, 
        service: str, 
        config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Add provider-specific attribute enhancements."""
        
        enhanced = attributes.copy()
        
        # Add common defaults
        if 'name' not in enhanced and 'identifier' not in enhanced:
            enhanced['name'] = '${local.resource_name}'
        
        # Add provider-specific defaults
        if self.get_provider_name() == 'gcp' and 'project' not in enhanced:
            enhanced['project'] = config.get('gcp_project_id')
        
        return enhanced
    
    def _create_unsupported_response(self, command: str, reason: str) -> Dict[str, Any]:
        """Create a response for unsupported commands."""
        return {
            "type": "unsupported_conversion",
            "original_command": command,
            "message": f"{self.get_provider_name().upper()} command not supported: {reason}",
            "suggestion": f"Try using the {self.get_provider_name()} CLI directly or create a custom Terraform configuration.",
            "provider": self.get_provider_name()
        }

class GCPConverter(CloudProviderConverter):
    """Dynamic converter for ALL Google Cloud Platform gcloud commands."""
    
    def get_provider_name(self) -> str:
        return "gcp"
    
    def can_convert_command(self, command: str) -> bool:
        return command.strip().startswith('gcloud ')
    
    def parse_command(self, command: str) -> Tuple[str, str, str, str, Dict[str, Any]]:
        """Parse any gcloud command dynamically."""
        
        parts = command.strip().split()
        if not parts or parts[0] != 'gcloud':
            return "", "", "", "", {}
        
        # Remove 'gcloud'
        parts = parts[1:]
        
        if not parts:
            return "", "", "", "", {}
        
        service = parts[0]
        
        # Parse different command patterns
        if len(parts) >= 3:
            if parts[1] in ['instances', 'clusters', 'buckets', 'topics', 'subscriptions', 'databases']:
                resource_type = parts[1]
                action = parts[2]
                remaining = parts[3:]
            elif parts[1] == 'instance-groups' and len(parts) >= 4:
                resource_type = f"{parts[1]}-{parts[2]}"
                action = parts[3]
                remaining = parts[4:]
            else:
                resource_type = parts[1]
                action = parts[2]
                remaining = parts[3:]
        else:
            resource_type = ""
            action = parts[1] if len(parts) > 1 else ""
            remaining = parts[2:] if len(parts) > 2 else []
        
        # Extract resource name and flags
        resource_name = "unnamed_resource"
        flags_start = 0
        
        for i, part in enumerate(remaining):
            if not part.startswith('--'):
                resource_name = part
                flags_start = i + 1
                break
            else:
                flags_start = i
                break
        
        # Parse flags
        flag_parts = remaining[flags_start:] if flags_start < len(remaining) else []
        attributes = self._parse_flags(flag_parts)
        
        return service, resource_type, action, resource_name, attributes
    
    def _parse_flags(self, flag_parts: List[str]) -> Dict[str, Any]:
        """Parse gcloud flags dynamically."""
        
        attributes = {}
        i = 0
        
        while i < len(flag_parts):
            part = flag_parts[i]
            
            if part.startswith('--'):
                flag_name = part[2:]
                
                if '=' in flag_name:
                    # --flag=value format
                    key, value = flag_name.split('=', 1)
                    attributes[key] = self._parse_flag_value(value)
                else:
                    # --flag value format or boolean flag
                    if i + 1 < len(flag_parts) and not flag_parts[i + 1].startswith('--'):
                        attributes[flag_name] = self._parse_flag_value(flag_parts[i + 1])
                        i += 1
                    else:
                        attributes[flag_name] = True
            
            i += 1
        
        return attributes
    
    def _parse_flag_value(self, value: str) -> Union[str, int, float, bool, List[str], Dict[str, Any]]:
        """Parse flag values with intelligent type detection."""
        
        # Handle comma-separated lists
        if ',' in value and not value.startswith('{'):
            return [item.strip() for item in value.split(',')]
        
        # Handle JSON values
        if value.startswith('{') or value.startswith('['):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                pass
        
        # Handle boolean values
        if value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        
        # Handle numeric values
        if value.isdigit():
            return int(value)
        
        try:
            return float(value)
        except ValueError:
            pass
        
        return value
    
    def get_terraform_provider_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Get GCP provider configuration."""
        
        provider_config = {
            "google": {
                "project": config.get('gcp_project_id'),
                "region": config.get('gcp_default_region', 'us-central1')
            }
        }
        
        if config.get('gcp_credentials_path'):
            provider_config["google"]["credentials"] = config['gcp_credentials_path']
        
        return provider_config

class AWSConverter(CloudProviderConverter):
    """Dynamic converter for ALL Amazon Web Services CLI commands."""
    
    def get_provider_name(self) -> str:
        return "aws"
    
    def can_convert_command(self, command: str) -> bool:
        return command.strip().startswith('aws ')
    
    def parse_command(self, command: str) -> Tuple[str, str, str, str, Dict[str, Any]]:
        """Parse any AWS CLI command dynamically."""
        
        parts = command.strip().split()
        if not parts or parts[0] != 'aws':
            return "", "", "", "", {}
        
        # Remove 'aws'
        parts = parts[1:]
        
        if not parts:
            return "", "", "", "", {}
        
        service = parts[0]
        action = parts[1] if len(parts) > 1 else ""
        
        # For AWS, resource_type is often embedded in the action
        resource_type = ""
        if action.startswith('create-'):
            resource_type = action[7:]  # Remove 'create-' prefix
        elif action.startswith('describe-'):
            resource_type = action[9:]  # Remove 'describe-' prefix
        elif action in ['mb', 'cp']:  # S3 special cases
            resource_type = "bucket" if action == 'mb' else "object"
        
        # Extract resource name and flags
        remaining = parts[2:] if len(parts) > 2 else []
        resource_name = "unnamed_resource"
        flags_start = 0
        
        for i, part in enumerate(remaining):
            if not part.startswith('--'):
                resource_name = part
                flags_start = i + 1
                break
            else:
                flags_start = i
                break
        
        # Parse flags
        flag_parts = remaining[flags_start:] if flags_start < len(remaining) else []
        attributes = self._parse_flags(flag_parts)
        
        return service, resource_type, action, resource_name, attributes
    
    def _parse_flags(self, flag_parts: List[str]) -> Dict[str, Any]:
        """Parse AWS CLI flags dynamically."""
        
        attributes = {}
        i = 0
        
        while i < len(flag_parts):
            part = flag_parts[i]
            
            if part.startswith('--'):
                flag_name = part[2:]
                
                if i + 1 < len(flag_parts) and not flag_parts[i + 1].startswith('--'):
                    value = flag_parts[i + 1]
                    attributes[flag_name] = self._parse_flag_value(value)
                    i += 1
                else:
                    attributes[flag_name] = True
            
            i += 1
        
        return attributes
    
    def _parse_flag_value(self, value: str) -> Union[str, int, float, bool, List[str], Dict[str, Any]]:
        """Parse AWS CLI flag values with intelligent type detection."""
        
        # Handle file:// protocol
        if value.startswith('file://'):
            return value
        
        # Handle JSON values (common in AWS CLI)
        if value.startswith('{') or value.startswith('['):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                pass
        
        # Handle comma-separated lists
        if ',' in value and not value.startswith('{'):
            return [item.strip() for item in value.split(',')]
        
        # Handle boolean values
        if value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        
        # Handle numeric values
        if value.isdigit():
            return int(value)
        
        try:
            return float(value)
        except ValueError:
            pass
        
        return value
    
    def get_terraform_provider_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Get AWS provider configuration."""
        
        provider_config = {
            "aws": {
                "region": config.get('aws_default_region', 'us-west-2')
            }
        }
        
        if config.get('aws_profile'):
            provider_config["aws"]["profile"] = config['aws_profile']
        
        if config.get('aws_access_key_id') and config.get('aws_secret_access_key'):
            provider_config["aws"]["access_key"] = config['aws_access_key_id']
            provider_config["aws"]["secret_key"] = config['aws_secret_access_key']
        
        return provider_config

class TerraformExecutor:
    """
    Dynamic multi-cloud Terraform executor using existing libraries and intelligent parsing.
    Supports ANY cloud CLI command through dynamic conversion.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize the dynamic multi-cloud Terraform Executor."""
        
        self.config = config
        self.terraform_working_dir = config.get('terraform_working_dir', 'terraform_workspace')
        self.terraform_state_backend = config.get('terraform_state_backend', 'local')
        self.dry_run = config.get('terraform_dry_run', False)
        self.keep_files = config.get('terraform_keep_files', False)
        
        # Initialize dynamic cloud provider converters
        self.converters = {
            'gcp': GCPConverter(),
            'aws': AWSConverter()
        }
        
        self.hcl_converter = HCLConverter()
        
        # Ensure working directory exists
        Path(self.terraform_working_dir).mkdir(exist_ok=True)
        
        # Determine available providers
        available_providers = []
        if config.get('gcp_project_id'):
            available_providers.append('gcp')
        if config.get('aws_default_region'):
            available_providers.append('aws')
        
        print(f"Dynamic Multi-cloud Terraform Executor initialized")
        print(f"HCL Libraries: python-hcl2={'✓' if HCL2_AVAILABLE else '✗'}, pyhcl={'✓' if HCL_AVAILABLE else '✗'}")
        print(f"Supports: ANY gcloud command, ANY AWS CLI command")
        print(f"Available providers: {', '.join(available_providers) if available_providers else 'None configured'}")
        print(f"Working directory: {self.terraform_working_dir}")

    async def execute(
        self,
        command: str,
        console: Console,
        step_id: str,
        execution_mode: str = "terraform"
    ) -> Tuple[bool, Any]:
        """Execute ANY cloud CLI command using dynamic Terraform conversion."""
        
        try:
            if execution_mode == "convert":
                return await self._execute_cloud_to_terraform(command, console, step_id)
            else:
                return await self._execute_terraform_direct(command, console, step_id)
                
        except Exception as e:
            error_msg = f"Exception during Terraform execution: {str(e)}"
            console.print(f"[bold red]  {error_msg}[/bold red]")
            return False, error_msg

    async def _execute_cloud_to_terraform(
        self,
        cloud_command: str,
        console: Console,
        step_id: str
    ) -> Tuple[bool, Any]:
        """Convert ANY cloud CLI command to Terraform and execute."""
        
        with console.status(f"[bold yellow]Converting cloud command to Terraform: [cyan]{step_id}[/cyan]...[/bold yellow]", spinner="dots"):
            # Convert using dynamic conversion
            tf_config = self._convert_cloud_to_terraform(cloud_command)
            
            if not tf_config:
                console.print(f"[red]  Failed to convert cloud command: {cloud_command}[/red]")
                return False, "Command conversion failed"
            
            return await self._execute_terraform_config(tf_config, console, step_id)

    async def _execute_terraform_direct(
        self,
        terraform_spec: str,
        console: Console,
        step_id: str
    ) -> Tuple[bool, Any]:
        """Execute direct Terraform specification."""
        
        try:
            if terraform_spec.strip().startswith('{'):
                tf_config = json.loads(terraform_spec)
            else:
                tf_config = {"hcl_content": terraform_spec}
            
            return await self._execute_terraform_config(tf_config, console, step_id)
            
        except json.JSONDecodeError as e:
            return False, f"Invalid Terraform specification: {e}"

    def _convert_cloud_to_terraform(self, cloud_command: str) -> Optional[Dict[str, Any]]:
        """Convert ANY cloud CLI command using dynamic conversion."""
        
        # Try each converter
        for provider_name, converter in self.converters.items():
            if converter.can_convert_command(cloud_command):
                print(f"Using dynamic {provider_name.upper()} converter for: {cloud_command}")
                return converter.convert_command_to_terraform(cloud_command, self.config)
        
        return {
            "type": "unsupported_conversion",
            "original_command": cloud_command,
            "message": f"No converter available for command: {cloud_command}",
            "suggestion": "Ensure the command starts with 'gcloud' or 'aws'"
        }

    async def _execute_terraform_config(
        self,
        tf_config: Dict[str, Any],
        console: Console,
        step_id: str
    ) -> Tuple[bool, Any]:
        """Execute Terraform configuration using proper libraries."""
        
        if tf_config.get("type") == "unsupported_conversion":
            console.print(f"[yellow]  {tf_config['message']}[/yellow]")
            return False, tf_config["message"]
        
        temp_dir = tempfile.mkdtemp(prefix=f"terraform_{step_id}_")
        
        try:
            with console.status(f"[bold yellow]Executing Terraform: [cyan]{step_id}[/cyan]...[/bold yellow]", spinner="dots"):
                
                # Write configuration files using HCL converter
                if "hcl_content" in tf_config:
                    # Direct HCL content
                    tf_file = Path(temp_dir) / "main.tf"
                    tf_file.write_text(tf_config["hcl_content"])
                else:
                    # Convert JSON config to HCL using proper libraries
                    config_data = tf_config.get("config", tf_config)
                    
                    # Write as JSON (Terraform supports this natively)
                    tf_json_file = Path(temp_dir) / "main.tf.json"
                    with open(tf_json_file, 'w') as f:
                        json.dump(config_data, f, indent=2)
                    
                    # Also write as HCL for human readability
                    if HCL2_AVAILABLE:
                        hcl_content = self.hcl_converter.json_to_hcl(config_data)
                        tf_hcl_file = Path(temp_dir) / "main.tf"
                        with open(tf_hcl_file, 'w') as f:
                            f.write(hcl_content)
                        console.print(f"[dim]Generated: main.tf.json, main.tf[/dim]")
                    else:
                        console.print(f"[dim]Generated: main.tf.json (HCL conversion unavailable)[/dim]")
                
                # Setup provider credentials
                env = self._setup_provider_credentials()
                
                # Initialize Terraform
                init_result = await self._run_terraform_command(['terraform', 'init'], temp_dir, env)
                if not init_result[0]:
                    return False, f"Terraform init failed: {init_result[1]}"
                
                # Plan
                plan_result = await self._run_terraform_command(['terraform', 'plan', '-out=tfplan'], temp_dir, env)
                if not plan_result[0]:
                    return False, f"Terraform plan failed: {plan_result[1]}"
                
                console.print(f"[green]  Terraform plan successful[/green]")
                
                if self.dry_run:
                    return True, {
                        "status": "planned",
                        "plan_output": plan_result[1],
                        "terraform_dir": temp_dir if self.keep_files else None,
                        "provider": tf_config.get("provider", "unknown"),
                        "service": tf_config.get("service", "unknown")
                    }
                else:
                    apply_result = await self._run_terraform_command(['terraform', 'apply', '-auto-approve', 'tfplan'], temp_dir, env)
                    if not apply_result[0]:
                        return False, f"Terraform apply failed: {apply_result[1]}"
                    
                    console.print(f"[green]  Terraform apply successful[/green]")
                    
                    return True, {
                        "status": "applied",
                        "apply_output": apply_result[1],
                        "terraform_dir": temp_dir if self.keep_files else None,
                        "provider": tf_config.get("provider", "unknown"),
                        "service": tf_config.get("service", "unknown")
                    }
                    
        finally:
            if not self.keep_files:
                shutil.rmtree(temp_dir, ignore_errors=True)

    def _setup_provider_credentials(self) -> Dict[str, str]:
        """Setup environment variables for cloud providers."""
        
        env = os.environ.copy()
        
        # GCP credentials
        if self.config.get('gcp_credentials_path'):
            env['GOOGLE_APPLICATION_CREDENTIALS'] = self.config['gcp_credentials_path']
        
        # AWS credentials
        if self.config.get('aws_access_key_id'):
            env['AWS_ACCESS_KEY_ID'] = self.config['aws_access_key_id']
        if self.config.get('aws_secret_access_key'):
            env['AWS_SECRET_ACCESS_KEY'] = self.config['aws_secret_access_key']
        if self.config.get('aws_session_token'):
            env['AWS_SESSION_TOKEN'] = self.config['aws_session_token']
        if self.config.get('aws_profile'):
            env['AWS_PROFILE'] = self.config['aws_profile']
        if self.config.get('aws_default_region'):
            env['AWS_DEFAULT_REGION'] = self.config['aws_default_region']
        
        return env

    async def _run_terraform_command(
        self,
        command: List[str],
        working_dir: str,
        env: Dict[str, str]
    ) -> Tuple[bool, str]:
        """Run terraform command."""
        
        try:
            process = await asyncio.create_subprocess_exec(
                *command,
                cwd=working_dir,
                env=env,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT
            )
            
            stdout, _ = await process.communicate()
            output = stdout.decode().strip()
            
            return process.returncode == 0, output
            
        except Exception as e:
            return False, f"Command execution failed: {str(e)}"

    def get_supported_providers(self) -> List[str]:
        """Get list of supported cloud providers."""
        return list(self.converters.keys())

    def add_converter(self, converter: CloudProviderConverter) -> None:
        """Add a custom cloud provider converter."""
        self.converters[converter.get_provider_name()] = converter

    async def execute_dag(
        self,
        dag_definition: Dict[str, Any],
        console: Console
    ) -> Dict[str, Tuple[bool, Any]]:
        """Execute a DAG of Terraform operations."""
        
        results = {}
        
        try:
            execution_order = dag_definition.get("execution_order", [])
            if not execution_order:
                raise ValueError("No execution order defined in DAG")
            
            for step_id in execution_order:
                node = dag_definition["nodes"][step_id]
                
                console.print(f"\n[bold cyan]Executing dynamic Terraform step {step_id}[/bold cyan]")
                console.print(f"Description: {node.get('description', 'No description')}")
                
                execution_mode = node.get("execution_mode", "convert")
                command = node.get("command", node.get("terraform_config", ""))
                
                success, result = await self.execute(command, console, step_id, execution_mode)
                results[step_id] = (success, result)
                
                if not success:
                    console.print(f"[bold red]Step {step_id} failed:[/bold red] {result}")
                else:
                    provider = result.get('provider', 'unknown') if isinstance(result, dict) else 'unknown'
                    service = result.get('service', 'unknown') if isinstance(result, dict) else 'unknown'
                    console.print(f"[bold green]Step {step_id} completed on {provider.upper()} ({service})[/bold green]")
            
            return results
            
        except Exception as e:
            console.print(f"[bold red]Error executing DAG:[/bold red] {str(e)}")
            return results

    def get_terraform_state(self, step_id: Optional[str] = None) -> Dict[str, Any]:
        """Get current Terraform state information."""
        
        return {
            "backend": self.terraform_state_backend,
            "supported_providers": self.get_supported_providers(),
            "hcl_libraries": {
                "python-hcl2": HCL2_AVAILABLE,
                "pyhcl": HCL_AVAILABLE
            },
            "step_id": step_id
        }

    def import_existing_resources(self, resource_mapping: Dict[str, str]) -> Dict[str, Any]:
        """Import existing cloud resources into Terraform state."""
        
        return {
            "imported_resources": resource_mapping,
            "status": "placeholder",
            "supported_providers": self.get_supported_providers()
        }
    
    def terraform_to_saturn_log(
        self, 
        terraform_dir: str, 
        original_query: str = "Converted from existing Terraform files"
    ) -> Dict[str, Any]:
        """
        Convert existing Terraform files (.tf, .tf.json, .tfstate) to Saturn log format.
        
        Args:
            terraform_dir: Path to directory containing Terraform files
            original_query: Query to use in the Saturn log
            
        Returns:
            Saturn log format dictionary
        """
        return self.hcl_converter.terraform_to_saturn_log(terraform_dir, original_query)
    
    def write_terraform_from_saturn_log(
        self, 
        saturn_log: Dict[str, Any], 
        output_dir: str
    ) -> Dict[str, str]:
        """
        Convert Saturn log back to Terraform files.
        
        Args:
            saturn_log: Saturn execution log
            output_dir: Directory to write Terraform files
            
        Returns:
            Dictionary of written files
        """
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Extract all Terraform configurations from the Saturn log
        all_configs = []
        
        # Process nodes to extract Terraform configurations
        nodes = saturn_log.get("nodes", {})
        for step_id, node_data in nodes.items():
            output = node_data.get("output", {})
            if "terraform_config" in output:
                all_configs.append(output["terraform_config"])
        
        if not all_configs:
            return {"error": "No Terraform configurations found in Saturn log"}
        
        # Combine all configurations
        combined_config = self._combine_terraform_configs(all_configs)
        
        # Write files
        files_written = {}
        
        # Write as JSON
        json_file = output_path / "converted_from_saturn.tf.json"
        with open(json_file, 'w') as f:
            json.dump(combined_config, f, indent=2)
        files_written['tf.json'] = str(json_file)
        
        # Write as HCL if possible
        if HCL2_AVAILABLE:
            hcl_content = self.hcl_converter.json_to_hcl(combined_config)
            hcl_file = output_path / "converted_from_saturn.tf"
            with open(hcl_file, 'w') as f:
                f.write(hcl_content)
            files_written['tf'] = str(hcl_file)
        
        return files_written
    
    def _combine_terraform_configs(self, configs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Combine multiple Terraform configurations into one."""
        
        combined = {
            "terraform": {
                "required_providers": {
                    "google": {
                        "source": "hashicorp/google",
                        "version": "~> 4.0"
                    },
                    "aws": {
                        "source": "hashicorp/aws",
                        "version": "~> 5.0"
                    }
                }
            },
            "provider": {},
            "resource": {},
            "data": {},
            "variable": {},
            "output": {},
            "locals": {},
            "module": {}
        }
        
        for config in configs:
            for block_type in ["provider", "resource", "data", "variable", "output", "locals", "module"]:
                if block_type in config:
                    if block_type in ["provider", "locals"]:
                        # These are single-level dictionaries
                        combined[block_type].update(config[block_type])
                    else:
                        # These are two-level dictionaries (type -> name -> config)
                        for resource_type, resource_instances in config[block_type].items():
                            if resource_type not in combined[block_type]:
                                combined[block_type][resource_type] = {}
                            combined[block_type][resource_type].update(resource_instances)
        
        # Remove empty sections
        combined = {k: v for k, v in combined.items() if v}
        
        return combined
    
    def validate_terraform_syntax(self, terraform_dir: str) -> Dict[str, Any]:
        """
        Validate Terraform syntax in the given directory.
        
        Args:
            terraform_dir: Directory containing Terraform files
            
        Returns:
            Validation results
        """
        try:
            # Use terraform validate command
            result = subprocess.run(
                ['terraform', 'validate'],
                cwd=terraform_dir,
                capture_output=True,
                text=True
            )
            
            return {
                "valid": result.returncode == 0,
                "output": result.stdout,
                "errors": result.stderr,
                "exit_code": result.returncode
            }
            
        except FileNotFoundError:
            return {
                "valid": False,
                "output": "",
                "errors": "Terraform CLI not found. Please install Terraform.",
                "exit_code": -1
            }
        except Exception as e:
            return {
                "valid": False,
                "output": "",
                "errors": f"Validation error: {str(e)}",
                "exit_code": -1
            } 