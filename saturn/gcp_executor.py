# Contains logic refactored from call.py for executing GCP API calls
import importlib
import json
import google.api_core.exceptions
import google.oauth2.service_account # Needed for credentials file
from typing import Dict, Any, Tuple, Optional, List
import asyncio
import traceback
# import re # No longer needed
from google.api_core.operation import Operation # Import Operation for type checking
from google.api_core.operation_async import AsyncOperation # Import AsyncOperation
from google.protobuf.json_format import MessageToDict # For result conversion
from rich.console import Console # Added console for rich printing
import subprocess

# Import necessary components from the package
from .knowledge_base import KnowledgeBase

# Mapping from service name prefix (used in tool names) to the actual google-cloud library package
# This needs to be maintained or generated dynamically.
# Example:
SERVICE_TO_LIBRARY_MAP = {
    "vpcaccess_v1": "google.cloud.vpcaccess_v1",
    "compute_v1": "google.cloud.compute_v1",
    "storage_v1": "google.cloud.storage_v1",
    "run_v2": "google.cloud.run_v2",
    # Add more services as needed
}

# Mapping from service name prefix to the Async Client class name within that library
# Example:
SERVICE_TO_CLIENT_CLASS_MAP = {
    "vpcaccess_v1": "VpcAccessServiceAsyncClient",
    "compute_v1": "InstancesAsyncClient", # Or other specific clients like NetworksAsyncClient etc.
    "storage_v1": "StorageAsyncClient",
    "run_v2": "JobsAsyncClient",
    # Add more services as needed
}

class GcloudExecutor:
    def __init__(self, config: Dict[str, Any]):
        """Initializes the Gcloud Executor."""
        self.config = config
        self.gcp_project_id = config.get('gcp_project_id')
        self.credentials_path = config.get('gcp_credentials_path')
        print(f"Gcloud Executor initialized for project: {self.gcp_project_id}")

    async def execute(
        self,
        command: str,
        console: Console
    ) -> Tuple[bool, Any]:
        """
        Executes a gcloud CLI command and returns the result.
        
        Args:
            command: The gcloud CLI command to execute
            console: Console for logging
            
        Returns:
            Tuple of (success, result)
        """
        console.print(f"  Executing command: [bold cyan]{command}[/bold cyan]")
        
        try:
            # Run the command and capture output
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0:
                # Command succeeded
                result = stdout.decode().strip()
                console.print("[green]Command executed successfully[/green]")
                return True, result
            else:
                # Command failed
                error = stderr.decode().strip()
                console.print(f"[red]Command failed: {error}[/red]")
                return False, error
                
        except Exception as e:
            error_msg = f"Error executing command: {str(e)}"
            console.print(f"[bold red]{error_msg}[/bold red]")
            return False, error_msg

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
            # Get execution order
            execution_order = dag_definition.get("execution_order", [])
            if not execution_order:
                raise ValueError("No execution order defined in DAG")
            
            # Execute steps in order
            for step_id in execution_order:
                node = dag_definition["nodes"][step_id]
                
                console.print(f"\n[bold cyan]Executing step {step_id}[/bold cyan]")
                console.print(f"Description: {node.get('description', 'No description')}")
                
                if node.get("dependencies"):
                    console.print(f"Dependencies: {', '.join(node['dependencies'])}")
                
                # Execute the command
                success, result = await self.execute(node["command"], console)
                results[step_id] = (success, result)
                
                if not success:
                    console.print(f"[bold red]Step {step_id} failed:[/bold red] {result}")
                else:
                    console.print(f"[bold green]Step {step_id} completed successfully[/bold green]")
            
            return results
            
        except Exception as e:
            console.print(f"[bold red]Error executing DAG:[/bold red] {str(e)}")
            return results

# Helper (if needed, from call.py)
# def convert_strings_to_json(data: dict) -> dict:
#     """Recursively attempt to parse any string fields as JSON objects."""
#     # ... implementation ... 