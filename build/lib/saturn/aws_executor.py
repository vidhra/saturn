import asyncio
import json
from typing import Dict, Any, Tuple

from rich.console import Console

class AWSExecutor:
    def __init__(self, config: Dict[str, Any]):
        """Initializes the AWS Executor."""
        self.config = config
        self.aws_region = config.get('aws_region', 'us-east-1') # Default region
        self.aws_profile = config.get('aws_profile') # Optional AWS CLI profile
        # Add other AWS specific configurations if needed, e.g., credentials path
        print(f"AWS Executor initialized for region: {self.aws_region}" + 
              (f" using profile: {self.aws_profile}" if self.aws_profile else ""))

    async def execute(
        self,
        command: str,
        console: Console
    ) -> Tuple[bool, Any]:
        """
        Executes an AWS CLI command and returns the result.
        
        Args:
            command: The AWS CLI command to execute (should start with 'aws')
            console: Console for logging and status updates
            
        Returns:
            Tuple of (success, result)
        """
        if not command.strip().startswith("aws"):
            error_msg = "Command does not start with 'aws'. AWS Executor can only run AWS CLI commands."
            console.print(f"[bold red]  {error_msg}[/bold red]")
            return False, error_msg

        # If an AWS profile is specified, prepend it to the command
        # This assumes the AWS CLI is configured to use this profile
        # e.g., aws --profile <profile_name> <service> <operation> ...
        # However, it might be better to set AWS_PROFILE environment variable for the subprocess
        # For simplicity, this example does not modify the command string for profile yet,
        # assuming the environment is pre-configured or the command includes --profile.
        # A more robust way is to set environment variables for the subprocess.
        
        env_vars = os.environ.copy()
        if self.aws_profile:
            env_vars["AWS_PROFILE"] = self.aws_profile
        if self.aws_region and not any(flag in command for flag in ["--region", "AWS_REGION"]):
            # Only set AWS_DEFAULT_REGION if --region is not in command and AWS_REGION not in env
            # to avoid overriding more specific settings.
            env_vars["AWS_DEFAULT_REGION"] = self.aws_region

        try:
            with console.status(f"[bold yellow]Executing: [cyan]{command}[/cyan]...[/bold yellow]", spinner="dots") as status:
                process = await asyncio.create_subprocess_shell(
                    command,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    env=env_vars # Pass modified environment variables
                )
                
                stdout, stderr = await process.communicate()
                
                if process.returncode == 0:
                    result_str = stdout.decode().strip()
                    console.print(f"[green]  Command executed successfully: [bold cyan]{command}[/bold cyan][/green]")
                    # Try to parse JSON, otherwise return raw string
                    try:
                        result_json = json.loads(result_str)
                        return True, result_json
                    except json.JSONDecodeError:
                        return True, result_str
                else:
                    error = stderr.decode().strip()
                    console.print(f"[red]  Command failed: [bold cyan]{command}[/bold cyan][/red]\n  Error: {error}")
                    return False, error
                    
        except Exception as e:
            error_msg = f"Exception during AWS command execution: {str(e)}"
            console.print(f"[bold red]  {error_msg}[/bold red]")
            return False, error_msg

    async def execute_dag(
        self,
        dag_definition: Dict[str, Any],
        console: Console
    ) -> Dict[str, Tuple[bool, Any]]:
        """
        Execute a DAG of AWS commands.
        
        Args:
            dag_definition: Dictionary containing nodes, edges, and execution order
            console: Console for logging
            
        Returns:
            Dictionary mapping step IDs to their (success, result) tuples
        """
        results = {}
        execution_order = dag_definition.get("execution_order", [])
        
        if not execution_order:
            console.print("[bold red]Error: No execution order defined in AWS DAG[/bold red]")
            return {"error": (False, "No execution order defined in DAG")}

        try:
            for step_id in execution_order:
                node = dag_definition["nodes"].get(step_id)
                if not node or "command" not in node:
                    console.print(f"[bold red]Error: Invalid node or missing command for step {step_id} in AWS DAG[/bold red]")
                    results[step_id] = (False, f"Invalid node or missing command for step {step_id}")
                    continue
                
                console.print(f"\n[bold cyan]Executing AWS step {step_id}[/bold cyan]")
                console.print(f"Description: {node.get('description', 'No description')}")
                
                if node.get("dependencies"):
                    console.print(f"Dependencies: {', '.join(node['dependencies'])}")
                
                success, result = await self.execute(node["command"], console)
                results[step_id] = (success, result)
                
                if not success:
                    console.print(f"[bold red]AWS Step {step_id} failed:[/bold red] {result}")
                else:
                    console.print(f"[bold green]AWS Step {step_id} completed successfully[/bold green]")
            
            return results
            
        except Exception as e:
            console.print(f"[bold red]Error executing AWS DAG:[/bold red] {str(e)}")
            # Include any partial results if an error occurs mid-DAG
            results["dag_execution_error"] = (False, str(e))
            return results

# Example of how it might be used (for testing, not part of the class itself)
async def main_example():
    console_instance = Console()
    aws_config = {
        'aws_region': 'us-west-2', # Example region
        'aws_profile': 'my-dev-profile' # Example profile, ensure it's configured in ~/.aws/credentials or config
    }
    executor = AWSExecutor(aws_config)
    
    # Example 1: Simple command
    success, result = await executor.execute("aws s3 ls", console_instance)
    if success:
        console_instance.print("S3 LS Result:", result)
    else:
        console_instance.print("S3 LS Error:", result)

    # Example 2: DAG execution
    dag_example = {
        "nodes": {
            "step1_list_buckets": {
                "command": "aws s3api list-buckets --query \"Buckets[].Name\"",
                "description": "List all S3 bucket names.",
                "dependencies": []
            },
            "step2_check_identity": {
                "command": "aws sts get-caller-identity",
                "description": "Check current AWS caller identity.",
                "dependencies": [] # Can run in parallel or before/after step1
            }
        },
        "execution_order": ["step1_list_buckets", "step2_check_identity"]
    }
    dag_results = await executor.execute_dag(dag_example, console_instance)
    console_instance.print("\nAWS DAG Execution Results:", dag_results)

if __name__ == '__main__':
    # Add os import for environment variable setting in the executor
    import os 
    # This example main will only run if you execute this file directly.
    # Ensure your AWS CLI is configured and the profile (if used) exists.
    asyncio.run(main_example()) 