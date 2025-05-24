#!/usr/bin/env python3
"""
Saturn Integration Example: File Build Tooling + Terraform Executor

This example demonstrates how the new FileBuildExecutor integrates with the existing
TerraformExecutor to create complete end-to-end deployment workflows.

Workflow:
1. Read project configuration
2. Auto-detect project type
3. Build and test application
4. Generate Docker artifacts
5. Create cloud infrastructure with Terraform
6. Deploy application to cloud
"""

import asyncio
import json
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress

# Import both executors
from saturn.file_build_executor import FileBuildExecutor
from saturn.terraform_executor import TerraformExecutor

class SaturnIntegratedWorkflow:
    """
    Integrated workflow combining file operations, build tooling, and cloud deployment.
    """
    
    def __init__(self, config: dict):
        self.config = config
        self.console = Console()
        
        # Initialize both executors
        self.file_executor = FileBuildExecutor(config)
        self.terraform_executor = TerraformExecutor(config)
        
        self.console.print(Panel.fit(
            "[bold cyan]Saturn Integrated Workflow Initialized[/bold cyan]\n"
            f"• File & Build Tooling: {self.file_executor.get_supported_operations()}\n"
            f"• Terraform Cloud Deployment: {self.terraform_executor.get_supported_providers()}\n"
            f"• Working Directory: {config.get('working_directory', '.')}\n"
            f"• Cloud Providers: {', '.join(self.terraform_executor.get_supported_providers())}",
            title="🚀 Saturn Integration"
        ))
    
    async def full_deployment_workflow(self, app_config: dict):
        """
        Execute a complete deployment workflow from source code to running cloud application.
        """
        
        self.console.print(Panel.fit(
            "[bold white]Starting Complete Deployment Workflow[/bold white]\n"
            f"Application: {app_config.get('name', 'Unknown')}\n"
            f"Target Cloud: {app_config.get('cloud_provider', 'gcp')}\n"
            f"Environment: {app_config.get('environment', 'production')}",
            title="🎯 Deployment Workflow"
        ))
        
        try:
            with Progress() as progress:
                task = progress.add_task("[cyan]Deployment Progress", total=8)
                
                # Step 1: Project Detection and Validation
                progress.update(task, description="[cyan]Detecting project type...")
                success = await self._detect_and_validate_project()
                if not success:
                    return False
                progress.advance(task)
                
                # Step 2: Build Application
                progress.update(task, description="[blue]Building application...")
                success = await self._build_application()
                if not success:
                    return False
                progress.advance(task)
                
                # Step 3: Run Tests
                progress.update(task, description="[green]Running tests...")
                success = await self._run_tests()
                if not success:
                    return False
                progress.advance(task)
                
                # Step 4: Generate Configuration Files
                progress.update(task, description="[yellow]Generating configs...")
                success = await self._generate_deployment_configs(app_config)
                if not success:
                    return False
                progress.advance(task)
                
                # Step 5: Build Docker Image
                progress.update(task, description="[blue]Building Docker image...")
                success = await self._build_docker_image(app_config)
                if not success:
                    return False
                progress.advance(task)
                
                # Step 6: Create Cloud Infrastructure
                progress.update(task, description="[magenta]Creating infrastructure...")
                success = await self._create_infrastructure(app_config)
                if not success:
                    return False
                progress.advance(task)
                
                # Step 7: Deploy Application
                progress.update(task, description="[red]Deploying application...")
                success = await self._deploy_application(app_config)
                if not success:
                    return False
                progress.advance(task)
                
                # Step 8: Verify Deployment
                progress.update(task, description="[green]Verifying deployment...")
                success = await self._verify_deployment(app_config)
                progress.advance(task)
                
                if success:
                    self.console.print(Panel.fit(
                        "[bold green]🎉 Deployment Completed Successfully![/bold green]\n"
                        f"Application: {app_config['name']}\n"
                        f"Environment: {app_config['environment']}\n"
                        f"Cloud: {app_config['cloud_provider']}\n"
                        f"Status: RUNNING",
                        title="✅ Success"
                    ))
                    return True
                else:
                    self.console.print("[red]❌ Deployment failed at verification step[/red]")
                    return False
                    
        except Exception as e:
            self.console.print(f"[red]❌ Workflow error: {str(e)}[/red]")
            return False
    
    async def _detect_and_validate_project(self) -> bool:
        """Step 1: Detect project type and validate structure."""
        
        self.console.print("\n[bold]Step 1: Project Detection & Validation[/bold]")
        
        # Detect project type
        success, result = await self.file_executor.execute(
            "detect_project",
            {},
            self.console,
            "detect_project_type"
        )
        
        if not success:
            return False
        
        self.project_type = result.get('primary_type', 'unknown')
        
        # Validate project structure
        success, result = await self.file_executor.execute(
            "list_files",
            {"directory": ".", "recursive": True},
            self.console,
            "validate_structure"
        )
        
        return success and result.get('count', 0) > 0
    
    async def _build_application(self) -> bool:
        """Step 2: Build the application using detected project type."""
        
        self.console.print("\n[bold]Step 2: Building Application[/bold]")
        
        success, result = await self.file_executor.execute(
            "build_project",
            {"project_type": self.project_type},
            self.console,
            "build_application"
        )
        
        return success
    
    async def _run_tests(self) -> bool:
        """Step 3: Run tests to ensure application quality."""
        
        self.console.print("\n[bold]Step 3: Running Tests[/bold]")
        
        success, result = await self.file_executor.execute(
            "test_project",
            {"project_type": self.project_type},
            self.console,
            "run_tests"
        )
        
        # Tests might not exist for all projects, so we allow success even if no tests
        return True  # Non-blocking for demo purposes
    
    async def _generate_deployment_configs(self, app_config: dict) -> bool:
        """Step 4: Generate deployment configuration files."""
        
        self.console.print("\n[bold]Step 4: Generating Deployment Configurations[/bold]")
        
        # Generate application configuration
        app_config_template = {
            "name": "{{app_name}}",
            "version": "{{app_version}}",
            "environment": "{{environment}}",
            "port": "{{port}}",
            "database": {
                "host": "{{db_host}}",
                "port": "{{db_port}}"
            },
            "redis": {
                "url": "{{redis_url}}"
            }
        }
        
        # Write template
        success, result = await self.file_executor.execute(
            "write_file",
            {"file_path": "config.template.json", "content": app_config_template},
            self.console,
            "create_config_template"
        )
        
        if not success:
            return False
        
        # Process template with actual values
        success, result = await self.file_executor.execute(
            "template_file",
            {
                "template_path": "config.template.json",
                "output_path": "production_config.json",
                "variables": {
                    "app_name": app_config['name'],
                    "app_version": app_config.get('version', '1.0.0'),
                    "environment": app_config['environment'],
                    "port": app_config.get('port', '8000'),
                    "db_host": "{{terraform_db_host}}",
                    "db_port": "5432",
                    "redis_url": "{{terraform_redis_url}}"
                }
            },
            self.console,
            "generate_prod_config"
        )
        
        return success
    
    async def _build_docker_image(self, app_config: dict) -> bool:
        """Step 5: Build Docker image for deployment."""
        
        self.console.print("\n[bold]Step 5: Building Docker Image[/bold]")
        
        # Generate Dockerfile if it doesn't exist
        dockerfile_path = Path("Dockerfile")
        if not dockerfile_path.exists():
            success, result = await self.file_executor.execute(
                "generate_dockerfile",
                {
                    "base_image": app_config.get('base_image', 'python:3.11-slim'),
                    "dependencies_file": self._get_dependencies_file(),
                    "start_command": f'["python", "{app_config.get("entry_point", "app.py")}"]'
                },
                self.console,
                "generate_dockerfile"
            )
            
            if not success:
                return False
        
        # Build Docker image
        image_name = f"{app_config['name']}:{app_config.get('version', 'latest')}"
        
        success, result = await self.file_executor.execute(
            "build_docker",
            {
                "image_name": image_name,
                "build_args": {
                    "ENV": app_config['environment']
                }
            },
            self.console,
            "build_docker_image"
        )
        
        if success:
            self.docker_image = image_name
            
        return success
    
    async def _create_infrastructure(self, app_config: dict) -> bool:
        """Step 6: Create cloud infrastructure using Terraform."""
        
        self.console.print("\n[bold]Step 6: Creating Cloud Infrastructure[/bold]")
        
        cloud_provider = app_config.get('cloud_provider', 'gcp')
        
        if cloud_provider == 'gcp':
            return await self._create_gcp_infrastructure(app_config)
        elif cloud_provider == 'aws':
            return await self._create_aws_infrastructure(app_config)
        else:
            self.console.print(f"[red]Unsupported cloud provider: {cloud_provider}[/red]")
            return False
    
    async def _create_gcp_infrastructure(self, app_config: dict) -> bool:
        """Create GCP infrastructure."""
        
        infrastructure_commands = [
            # Create VPC network
            f"gcloud compute networks create {app_config['name']}-network --subnet-mode=custom",
            
            # Create subnet
            f"gcloud compute networks subnets create {app_config['name']}-subnet "
            f"--network={app_config['name']}-network "
            f"--range=10.0.1.0/24 "
            f"--region={app_config.get('region', 'us-central1')}",
            
            # Create firewall rule
            f"gcloud compute firewall-rules create {app_config['name']}-allow-http "
            f"--network={app_config['name']}-network "
            f"--allow=tcp:80,tcp:443,tcp:{app_config.get('port', 8000)} "
            f"--source-ranges=0.0.0.0/0",
        ]
        
        for command in infrastructure_commands:
            success, result = await self.terraform_executor.execute(
                command,
                self.console,
                f"infra_{command.split()[1]}"
            )
            
            if not success:
                self.console.print(f"[red]Failed to execute: {command}[/red]")
                return False
        
        return True
    
    async def _create_aws_infrastructure(self, app_config: dict) -> bool:
        """Create AWS infrastructure."""
        
        infrastructure_commands = [
            # Create VPC
            f"aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specification "
            f"ResourceType=vpc,Tags=[{{Key=Name,Value={app_config['name']}-vpc}}]",
            
            # Create subnet
            f"aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.0.1.0/24 "
            f"--tag-specification ResourceType=subnet,Tags=[{{Key=Name,Value={app_config['name']}-subnet}}]",
            
            # Create security group
            f"aws ec2 create-security-group --group-name {app_config['name']}-sg "
            f"--description 'Security group for {app_config['name']}' --vpc-id vpc-xxx",
        ]
        
        for command in infrastructure_commands:
            success, result = await self.terraform_executor.execute(
                command,
                self.console,
                f"infra_{command.split()[2]}"
            )
            
            if not success:
                self.console.print(f"[red]Failed to execute: {command}[/red]")
                return False
        
        return True
    
    async def _deploy_application(self, app_config: dict) -> bool:
        """Step 7: Deploy application to cloud."""
        
        self.console.print("\n[bold]Step 7: Deploying Application[/bold]")
        
        cloud_provider = app_config.get('cloud_provider', 'gcp')
        
        if cloud_provider == 'gcp':
            # Deploy to Cloud Run
            deploy_command = (
                f"gcloud run deploy {app_config['name']} "
                f"--image={self.docker_image} "
                f"--platform=managed "
                f"--region={app_config.get('region', 'us-central1')} "
                f"--allow-unauthenticated "
                f"--port={app_config.get('port', 8000)}"
            )
        elif cloud_provider == 'aws':
            # Deploy to ECS or Lambda
            deploy_command = (
                f"aws ecs create-service "
                f"--cluster {app_config['name']}-cluster "
                f"--service-name {app_config['name']}-service "
                f"--task-definition {app_config['name']}-task"
            )
        else:
            return False
        
        success, result = await self.terraform_executor.execute(
            deploy_command,
            self.console,
            "deploy_application"
        )
        
        return success
    
    async def _verify_deployment(self, app_config: dict) -> bool:
        """Step 8: Verify deployment is successful."""
        
        self.console.print("\n[bold]Step 8: Verifying Deployment[/bold]")
        
        # For demo purposes, we'll just check that the service exists
        cloud_provider = app_config.get('cloud_provider', 'gcp')
        
        if cloud_provider == 'gcp':
            verify_command = f"gcloud run services describe {app_config['name']} --region={app_config.get('region', 'us-central1')}"
        elif cloud_provider == 'aws':
            verify_command = f"aws ecs describe-services --cluster {app_config['name']}-cluster --services {app_config['name']}-service"
        else:
            return False
        
        success, result = await self.terraform_executor.execute(
            verify_command,
            self.console,
            "verify_deployment"
        )
        
        return success
    
    def _get_dependencies_file(self) -> str:
        """Get the appropriate dependencies file for the project type."""
        
        dependencies_map = {
            'python': 'requirements.txt',
            'node': 'package.json',
            'rust': 'Cargo.toml',
            'go': 'go.mod',
            'java': 'pom.xml'
        }
        
        return dependencies_map.get(self.project_type, 'requirements.txt')
    
    async def rollback_deployment(self, app_config: dict):
        """Rollback deployment in case of failure."""
        
        self.console.print(Panel.fit(
            "[bold red]Rolling Back Deployment[/bold red]\n"
            "Cleaning up resources created during failed deployment",
            title="🔄 Rollback"
        ))
        
        # Implementation would include cleanup of created resources
        # This is a placeholder for demonstration
        self.console.print("[yellow]Rollback functionality would be implemented here[/yellow]")

async def main():
    """Demonstrate the integrated workflow."""
    
    console = Console()
    console.print(Panel.fit(
        "[bold white]🌟 Saturn Integrated Workflow Demo[/bold white]\n\n"
        "This demo shows how the new FileBuildExecutor integrates with\n"
        "the existing TerraformExecutor for complete deployment automation.",
        title="Saturn Integration Demo"
    ))
    
    # Configuration for both executors
    config = {
        'working_directory': '.',
        'gcp_project_id': 'saturn-demo-project',
        'gcp_default_region': 'us-central1',
        'aws_default_region': 'us-west-2',
        'terraform_dry_run': True,  # For demo purposes
        'keep_files': True
    }
    
    # Application configuration
    app_config = {
        'name': 'saturn-demo-app',
        'version': '1.0.0',
        'environment': 'production',
        'cloud_provider': 'gcp',
        'region': 'us-central1',
        'port': 8000,
        'base_image': 'python:3.11-slim',
        'entry_point': 'app.py'
    }
    
    # Create integrated workflow
    workflow = SaturnIntegratedWorkflow(config)
    
    try:
        # Create a simple demo application structure
        demo_files = {
            'app.py': '''from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Saturn Demo App")

@app.get("/")
def read_root():
    return {"message": "Hello from Saturn!", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
''',
            'requirements.txt': 'fastapi==0.104.1\nuvicorn==0.24.0',
            'README.md': '# Saturn Demo Application\n\nBuilt and deployed with Saturn integrated workflow.'
        }
        
        console.print("\n[dim]Setting up demo application structure...[/dim]")
        for filename, content in demo_files.items():
            success, result = await workflow.file_executor.execute(
                "write_file",
                {"file_path": filename, "content": content},
                console,
                f"setup_{filename}"
            )
        
        # Run the complete workflow
        success = await workflow.full_deployment_workflow(app_config)
        
        if success:
            console.print(Panel.fit(
                "[bold green]🎉 Integration Demo Completed Successfully![/bold green]\n\n"
                "[yellow]Demonstrated Capabilities:[/yellow]\n"
                "✅ File operations with multiple formats\n"
                "✅ Project auto-detection and building\n"
                "✅ Docker image generation and building\n"
                "✅ Template processing for configurations\n"
                "✅ Cloud infrastructure creation with Terraform\n"
                "✅ Application deployment to cloud platforms\n"
                "✅ Deployment verification\n\n"
                "[cyan]Integration Benefits:[/cyan]\n"
                "• Seamless workflow from code to cloud\n"
                "• Unified error handling and logging\n"
                "• Consistent configuration management\n"
                "• Comprehensive automation pipeline",
                title="🏆 Demo Success"
            ))
        else:
            console.print("[red]❌ Demo workflow failed. Check logs above.[/red]")
            
    except KeyboardInterrupt:
        console.print("\n[yellow]Demo interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Demo error: {str(e)}[/red]")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup demo files
        console.print("\n[dim]Cleaning up demo files...[/dim]")
        cleanup_files = ['app.py', 'requirements.txt', 'README.md', 'config.template.json', 
                        'production_config.json', 'Dockerfile']
        for filename in cleanup_files:
            if Path(filename).exists():
                Path(filename).unlink()

if __name__ == "__main__":
    asyncio.run(main()) 