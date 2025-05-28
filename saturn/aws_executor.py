import asyncio
import json
from typing import Dict, Any, Tuple

from rich.console import Console

class AWSExecutor:
    def __init__(self, config: Dict[str, Any]):
        """Initializes the AWS Executor."""
        self.config = config
        self.aws_region = config.get('aws_region', 'us-east-1')
        self.aws_profile = config.get('aws_profile')
        print(f"AWS Executor initialized for region: {self.aws_region}" + 
              (f" using profile: {self.aws_profile}" if self.aws_profile else ""))

    async def execute(
        self,
        command: str,
        console: Console,
        step_id: str
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
        
        env_vars = os.environ.copy()
        if self.aws_profile:
            env_vars["AWS_PROFILE"] = self.aws_profile
        if self.aws_region and not any(flag in command for flag in ["--region", "AWS_REGION"]):
            env_vars["AWS_DEFAULT_REGION"] = self.aws_region

        try:
            with console.status(f"[bold yellow]Executing: [cyan]{step_id}[/cyan]...[/bold yellow]", spinner="dots") as status:
                process = await asyncio.create_subprocess_shell(
                    command,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    env=env_vars 
                )
                
                stdout, stderr = await process.communicate()
                
                if process.returncode == 0:
                    result_str = stdout.decode().strip()
                    console.print(f"[green]  Command executed successfully: [bold cyan]{command}[/bold cyan][/green]")
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

async def main_example():
    console_instance = Console()
    aws_config = {
        'aws_region': 'us-west-2', 
        'aws_profile': 'my-dev-profile'
    }
    executor = AWSExecutor(aws_config)

    success, result = await executor.execute("aws s3 ls", console_instance)
    if success:
        console_instance.print("S3 LS Result:", result)
    else:
        console_instance.print("S3 LS Error:", result)

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

    import os 
    asyncio.run(main_example()) 