import os
import asyncio
import json
from typing import Dict, Any, Tuple

from rich.console import Console
from rich.prompt import Confirm

class AWSExecutor:
    def __init__(self, config: Dict[str, Any]):
        """Initializes the AWS Executor."""
        self.config = config
        self.aws_region = config.get('aws_region', config.get('aws_default_region', 'us-west-2'))
        self.aws_profile = config.get('aws_profile')
        self.execution_mode = config.get('execution_mode', 'auto')
        print(f"AWS Executor initialized for region: {self.aws_region}")
        print(f"Execution mode: {self.execution_mode}")

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
        if self.aws_region:
            env_vars['AWS_DEFAULT_REGION'] = self.aws_region
        if self.aws_profile:
            env_vars['AWS_PROFILE'] = self.aws_profile
        
        for aws_env_var in ['aws_access_key_id', 'aws_secret_access_key', 'aws_session_token']:
            config_value = self.config.get(aws_env_var)
            if config_value:
                env_vars[aws_env_var.upper()] = config_value

        try:
            if self.execution_mode == 'manual':
                if self._is_destructive_operation(command):
                    console.print(f"\n[bold yellow]Step {step_id}:[/bold yellow]")
                    console.print(f"[cyan]Command to execute:[/cyan] {command}")
                    
                    if not Confirm.ask("Execute this command?", default=True):
                        console.print("[yellow]Command execution skipped by user[/yellow]")
                        return False, "Execution skipped by user"
                else:
                    console.print(f"[dim][READ-ONLY][/dim] Auto-executing: [cyan]{command}[/cyan]")
            
            elif self.execution_mode == 'yolo':
                console.print(f"[bold green][YOLO MODE][/bold green] Auto-executing: [cyan]{command}[/cyan]")

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

    def _is_destructive_operation(self, command: str) -> bool:
        """Check if an AWS CLI command is a destructive operation that requires confirmation."""
        command_lower = command.lower()
        
        destructive_keywords = [
            'create', 'delete', 'remove', 'destroy', 'terminate', 'stop', 'start', 'restart',
            'update', 'modify', 'put', 'post', 'patch', 'add', 'attach', 'detach', 'enable', 'disable',
            'deploy', 'apply', 'import', 'export', 'copy', 'move', 'resize', 'reset',
            'restore', 'backup', 'migrate', 'promote', 'demote', 'replace', 'run-instances',
            'allocate', 'associate', 'authorize', 'deauthorize', 'register', 'deregister',
            'launch', 'reboot', 'release', 'revoke', 'cancel', 'invoke'
        ]
        
        read_only_keywords = [
            'describe', 'list', 'get', 'show', 'print', 'cat', 'tail', 'head',
            'search', 'find', 'check', 'test', 'validate', 'verify', 'status',
            'info', 'help', 'version', 'configure list', 'sts get-caller-identity',
            'wait', 'monitor'
        ]
        
        for read_keyword in read_only_keywords:
            if read_keyword in command_lower:
                return False
        
        for destructive_keyword in destructive_keywords:
            if destructive_keyword in command_lower:
                return True
        
        return False

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
                
                success, result = await self.execute(node["command"], console, step_id)
                results[step_id] = (success, result)
                
                if not success:
                    console.print(f"[bold red]AWS Step {step_id} failed:[/bold red] {result}")
                else:
                    console.print(f"[bold green]AWS Step {step_id} completed successfully[/bold green]")
            
            return results
            
        except Exception as e:
            console.print(f"[bold red]Error executing AWS DAG:[/bold red] {str(e)}")
            results["dag_execution_error"] = (False, str(e))
            return results
