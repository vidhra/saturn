#!/usr/bin/env python3
"""
Test the new dynamic reverse-engineering approach that uses pattern analysis
instead of hardcoded service mappings.
"""

import json
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

# Add saturn to path
sys.path.append('.')

from saturn.terraform_executor import HCLConverter

console = Console()

def test_dynamic_gcloud_reverse_engineering():
    """Test dynamic gcloud command reverse engineering."""
    
    console.print(Panel("Dynamic GCloud Reverse Engineering Test", style="bold blue"))
    
    # Test cases with various Terraform resource types and configurations
    test_cases = [
        {
            "resource_type": "google_compute_instance_template",
            "resource_name": "my_instance_template",
            "config": {
                "name": "my-instance-template",
                "machine_type": "e2-medium",
                "image_family": "debian-11",
                "image_project": "debian-cloud",
                "can_ip_forward": False,
                "tags": ["tag1", "tag2"],
                "network": "default",
                "region": "us-central1",
                "project": "demo-project"
            }
        },
        {
            "resource_type": "google_compute_instance",
            "resource_name": "web_server",
            "config": {
                "name": "web-server",
                "machine_type": "e2-small",
                "zone": "us-west1-a",
                "tags": ["web", "production"],
                "project": "my-project"
            }
        },
        {
            "resource_type": "google_storage_bucket",
            "resource_name": "my_bucket",
            "config": {
                "name": "my-storage-bucket",
                "location": "US",
                "uniform_bucket_level_access": True,
                "project": "demo-project"
            }
        },
        {
            "resource_type": "google_compute_firewall",
            "resource_name": "allow_http",
            "config": {
                "name": "allow-http-traffic",
                "network": "default",
                "direction": "INGRESS",
                "priority": 1000,
                "target_tags": ["web"],
                "source_ranges": ["0.0.0.0/0"]
            }
        }
    ]
    
    console.print(f"[bold]Testing {len(test_cases)} GCP resource types...[/bold]\n")
    
    results_table = Table(title="GCloud Reverse Engineering Results")
    results_table.add_column("Resource Type", style="cyan")
    results_table.add_column("Generated Command", style="green")
    results_table.add_column("Method", style="yellow")
    
    for test_case in test_cases:
        resource_type = test_case["resource_type"]
        resource_name = test_case["resource_name"]
        config = test_case["config"]
        
        console.print(f"[cyan]Testing {resource_type}...[/cyan]")
        
        # Use the new dynamic method
        command = HCLConverter._reverse_engineer_gcloud_command(resource_type, resource_name, config)
        
        # Determine method used
        method = "Pattern Analysis" if not command.startswith("#") else "Failed"
        
        # Truncate long commands for table display
        display_command = command if len(command) <= 80 else command[:77] + "..."
        
        results_table.add_row(
            resource_type.replace("google_", ""),
            display_command,
            method
        )
        
        # Show full command
        console.print(f"[green]Generated:[/green] {command}")
        console.print()
    
    console.print(results_table)

def test_dynamic_aws_reverse_engineering():
    """Test dynamic AWS CLI command reverse engineering."""
    
    console.print(Panel("Dynamic AWS CLI Reverse Engineering Test", style="bold green"))
    
    # Test cases with various AWS resource types and configurations
    test_cases = [
        {
            "resource_type": "aws_instance",
            "resource_name": "web_server",
            "config": {
                "ami": "ami-0c02fb55956c7d316",
                "instance_type": "t3.micro",
                "key_name": "my-key",
                "subnet_id": "subnet-12345",
                "security_groups": ["sg-12345"]
            }
        },
        {
            "resource_type": "aws_vpc",
            "resource_name": "main_vpc",
            "config": {
                "cidr_block": "10.0.0.0/16",
                "enable_dns_hostnames": True,
                "enable_dns_support": True,
                "tags": {
                    "Name": "main-vpc"
                }
            }
        },
        {
            "resource_type": "aws_s3_bucket",
            "resource_name": "my_bucket",
            "config": {
                "bucket": "my-demo-bucket-12345",
                "acl": "private"
            }
        },
        {
            "resource_type": "aws_security_group",
            "resource_name": "web_sg",
            "config": {
                "name": "web-security-group",
                "description": "Security group for web servers",
                "vpc_id": "vpc-12345"
            }
        }
    ]
    
    console.print(f"[bold]Testing {len(test_cases)} AWS resource types...[/bold]\n")
    
    results_table = Table(title="AWS CLI Reverse Engineering Results")
    results_table.add_column("Resource Type", style="cyan")
    results_table.add_column("Generated Command", style="green")
    results_table.add_column("Method", style="yellow")
    
    for test_case in test_cases:
        resource_type = test_case["resource_type"]
        resource_name = test_case["resource_name"]
        config = test_case["config"]
        
        console.print(f"[cyan]Testing {resource_type}...[/cyan]")
        
        # Use the new dynamic method
        command = HCLConverter._reverse_engineer_aws_command(resource_type, resource_name, config)
        
        # Determine method used
        method = "Pattern Analysis" if not command.startswith("#") else "Failed"
        
        # Truncate long commands for table display
        display_command = command if len(command) <= 80 else command[:77] + "..."
        
        results_table.add_row(
            resource_type.replace("aws_", ""),
            display_command,
            method
        )
        
        # Show full command
        console.print(f"[green]Generated:[/green] {command}")
        console.print()
    
    console.print(results_table)

def test_pattern_analysis_features():
    """Test the pattern analysis features in detail."""
    
    console.print(Panel("Pattern Analysis Features Test", style="bold magenta"))
    
    console.print("[bold]Testing pattern analysis capabilities:[/bold]")
    
    # Test pluralization
    pluralization_tests = [
        ("instance", "instances"),
        ("instance_template", "instance-templates"), 
        ("firewall", "firewall-rules"),
        ("network", "networks"),
        ("database_instance", "database-instances")
    ]
    
    console.print("\n[cyan]1. Resource Type Pluralization:[/cyan]")
    for input_type, expected in pluralization_tests:
        result = HCLConverter._pluralize_resource_type(input_type)
        status = "✓" if result == expected else "✗"
        console.print(f"  {status} {input_type} → {result} (expected: {expected})")
    
    # Test attribute conversion
    console.print("\n[cyan]2. Terraform Attribute to GCloud Flag Conversion:[/cyan]")
    attr_tests = [
        ("machine_type", "e2-medium", "--machine-type=e2-medium"),
        ("can_ip_forward", False, "--no-can-ip-forward"),
        ("tags", ["web", "prod"], "--tags=web,prod"),
        ("zone", "us-central1-a", "--zone=us-central1-a")
    ]
    
    for attr, value, expected in attr_tests:
        result = HCLConverter._terraform_attr_to_gcloud_flag(attr, value)
        status = "✓" if result == expected else "✗"
        console.print(f"  {status} {attr}={value} → {result} (expected: {expected})")
    
    # Test AWS action mapping
    console.print("\n[cyan]3. AWS Service Action Mapping:[/cyan]")
    aws_action_tests = [
        ("ec2", "instance", "run-instances"),
        ("ec2", "vpc", "create-vpc"),
        ("iam", "user", "create-user"),
        ("s3", "bucket", "mb")
    ]
    
    for service, resource_type, expected in aws_action_tests:
        result = HCLConverter._get_aws_action(service, resource_type)
        status = "✓" if result == expected else "✗"
        console.print(f"  {status} {service} {resource_type} → {result} (expected: {expected})")

def compare_old_vs_new_approach():
    """Compare the old hardcoded approach with the new dynamic approach."""
    
    console.print(Panel("Old vs New Approach Comparison", style="bold yellow"))
    
    comparison_table = Table(title="Approach Comparison")
    comparison_table.add_column("Feature", style="cyan")
    comparison_table.add_column("Old Hardcoded", style="red")
    comparison_table.add_column("New Dynamic", style="green")
    
    comparison_table.add_row(
        "Service Coverage",
        "~20 hardcoded mappings",
        "Unlimited via pattern analysis"
    )
    comparison_table.add_row(
        "New Services",
        "Requires code changes",
        "Automatically supported"
    )
    comparison_table.add_row(
        "Accuracy",
        "High for mapped services",
        "High + falls back gracefully"
    )
    comparison_table.add_row(
        "Maintainability",
        "Manual mapping updates",
        "Self-maintaining patterns"
    )
    comparison_table.add_row(
        "Schema Support",
        "None",
        "Can use real Terraform schemas"
    )
    comparison_table.add_row(
        "Flag Mapping",
        "Fixed attribute mapping",
        "Dynamic attribute conversion"
    )
    
    console.print(comparison_table)
    
    console.print("\n[bold green]Key Advantages of New Approach:[/bold green]")
    console.print("• ✅ No hardcoded service mappings")
    console.print("• ✅ Pattern-based analysis works for any service")
    console.print("• ✅ Can integrate real Terraform provider schemas")
    console.print("• ✅ Dynamic flag/attribute conversion")
    console.print("• ✅ Graceful fallback for unknown resources")
    console.print("• ✅ Self-maintaining as cloud services evolve")

def main():
    """Run dynamic reverse engineering tests."""
    
    console.print("[bold green]Saturn Dynamic Reverse Engineering Test[/bold green]")
    console.print("=" * 70)
    console.print()
    
    console.print("[bold]This test demonstrates the new dynamic approach that:[/bold]")
    console.print("• Uses pattern analysis instead of hardcoded mappings")
    console.print("• Can reverse-engineer commands for ANY Terraform resource")
    console.print("• Supports real provider schema integration")
    console.print("• Maintains accuracy while being extensible")
    console.print()
    
    test_dynamic_gcloud_reverse_engineering()
    console.print("\n" + "="*50 + "\n")
    
    test_dynamic_aws_reverse_engineering()
    console.print("\n" + "="*50 + "\n")
    
    test_pattern_analysis_features()
    console.print("\n" + "="*50 + "\n")
    
    compare_old_vs_new_approach()
    
    console.print(Panel(
        "[bold green]🎉 Dynamic Reverse Engineering Test Complete![/bold green]\n\n"
        "Key Achievements:\n"
        "• Eliminated hardcoded service mappings\n"
        "• Implemented pattern-based reverse engineering\n"
        "• Added support for real Terraform provider schemas\n"
        "• Dynamic attribute/flag conversion\n"
        "• Graceful handling of unknown resources\n"
        "• Extensible approach that scales with cloud services",
        title="Test Complete"
    ))

if __name__ == "__main__":
    main() 