import importlib
import json
import google.api_core.exceptions
import google.oauth2.service_account 
from typing import Dict, Any, Tuple, Optional, List
import asyncio
import traceback
from google.api_core.operation import Operation 
from google.api_core.operation_async import AsyncOperation
from google.protobuf.json_format import MessageToDict 
from rich.console import Console 
from rich.prompt import Confirm
import subprocess

from .knowledge_base import KnowledgeBase

class GcloudExecutor:
    def __init__(self, config: Dict[str, Any]):
        """Initializes the Gcloud Executor."""
        self.config = config
        self.gcp_project_id = config.get('gcp_project_id')
        self.credentials_path = config.get('gcp_credentials_path')
        self.execution_mode = config.get('execution_mode', 'auto')
        print(f"Gcloud Executor initialized for project: {self.gcp_project_id}")
        print(f"Execution mode: {self.execution_mode}")

    async def execute(
        self,
        command: str,
        console: Console,
        step_id: str
    ) -> Tuple[bool, Any]:
        """
        Executes a gcloud CLI command and returns the result.
        
        Args:
            command: The gcloud CLI command to execute
            console: Console for logging and status updates
            
        Returns:
            Tuple of (success, result)
        """
        
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
                    stderr=asyncio.subprocess.PIPE
                )
                
                stdout, stderr = await process.communicate()
                
                if process.returncode == 0:
                    result = stdout.decode().strip()
                    console.print(f"[green]  Command executed successfully: [bold cyan]{command}[/bold cyan][/green]")
                    return True, result
                else:
                    error = stderr.decode().strip()
                    console.print(f"[red]  Command failed: [bold cyan]{command}[/bold cyan][/red]\n  Error: {error}")
                    return False, error
                    
        except Exception as e:
            error_msg = f"Exception during command execution: {str(e)}"
            console.print(f"[bold red]  {error_msg}[/bold red]")
            return False, error_msg

    def _is_destructive_operation(self, command: str) -> bool:
        """Check if a gcloud command is a destructive operation that requires confirmation."""
        command_lower = command.lower()
        
        destructive_keywords = [
            'create', 'delete', 'remove', 'destroy', 'terminate', 'stop', 'start', 'restart',
            'update', 'modify', 'set', 'add', 'attach', 'detach', 'enable', 'disable',
            'deploy', 'apply', 'import', 'export', 'copy', 'move', 'resize', 'reset',
            'restore', 'backup', 'migrate', 'promote', 'demote', 'patch', 'replace'
        ]
        
        read_only_keywords = [
            'describe', 'list', 'get', 'show', 'print', 'cat', 'tail', 'head',
            'search', 'find', 'check', 'test', 'validate', 'verify', 'status',
            'info', 'help', 'version', 'config list', 'auth list'
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
        Execute a DAG of gcloud commands.
        
        Args:
            dag_definition: Dictionary containing nodes, edges, and execution order
            console: Console for logging
            
        Returns:
            Dictionary mapping step IDs to their (success, result) tuples
        """
        results = {}
        
        try:
            execution_order = dag_definition.get("execution_order", [])
            if not execution_order:
                raise ValueError("No execution order defined in DAG")
            
            for step_id in execution_order:
                node = dag_definition["nodes"][step_id]
                
                console.print(f"\n[bold cyan]Executing step {step_id}[/bold cyan]")
                console.print(f"Description: {node.get('description', 'No description')}")
                
                if node.get("dependencies"):
                    console.print(f"Dependencies: {', '.join(node['dependencies'])}")
                
                success, result = await self.execute(node["command"], console, step_id)
                results[step_id] = (success, result)
                
                if not success:
                    console.print(f"[bold red]Step {step_id} failed:[/bold red] {result}")
                    
                    if self.execution_mode == 'manual' and "skipped by user" not in str(result):
                        if not Confirm.ask("Continue with remaining steps despite this failure?", default=False):
                            console.print("[yellow]DAG execution stopped by user[/yellow]")
                            break
                else:
                    console.print(f"[bold green]Step {step_id} completed successfully[/bold green]")
            
            return results
            
        except Exception as e:
            console.print(f"[bold red]Error executing DAG:[/bold red] {str(e)}")
            return results
