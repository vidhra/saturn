import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
from pathlib import Path

from rich.console import Console

console = Console()


class SaturnWorkflow:
    """
    Handles Saturn workflow (.sat) files for saving and loading DAG execution flows.
    
    .sat files contain the complete execution plan including:
    - DAG structure (nodes, edges, execution order)
    - Step details with tool information and arguments
    - Metadata about the original query and creation time
    """
    
    SAT_VERSION = "1.0"
    
    def __init__(self):
        self.console = console
    
    def save_workflow(
        self,
        dag: Any,
        step_details_map: Dict[str, Any],
        execution_order: List[str],
        original_query: str,
        filename: Optional[str] = None,
        output_dir: str = "."
    ) -> str:
        """
        Save a DAG execution flow to a .sat file.
        
        Args:
            dag: The AcyclicGraph instance
            step_details_map: Dictionary mapping step IDs to their details
            execution_order: List of step IDs in execution order
            original_query: The original user query that generated this workflow
            filename: Optional filename (without extension). If None, auto-generates
            output_dir: Directory to save the file in
            
        Returns:
            Path to the saved .sat file
        """
        if filename is None:
            # Generate filename from query and timestamp
            safe_query = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in original_query)
            safe_query = safe_query.replace(' ', '_').strip('_')[:10]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{safe_query}_{timestamp}"
        
        # Ensure .sat extension
        if not filename.endswith('.sat'):
            filename += '.sat'
        
        filepath = os.path.join(output_dir, filename)
        
        # Prepare workflow data
        workflow_data = {
            "saturn_workflow": {
                "version": self.SAT_VERSION,
                "created_at": datetime.now().isoformat(),
                "original_query": original_query,
                "description": f"Saturn workflow generated from: {original_query[:100]}..."
            },
            "dag": {
                "nodes": list(dag.vertices) if dag else [],
                "edges": [{"source": str(e.source), "target": str(e.target)} for e in dag.edges] if dag else [],
                "execution_order": execution_order
            },
            "steps": {}
        }
        
        # Add step details
        for step_id, details in step_details_map.items():
            step_data = {
                "id": details.get("id", step_id),
                "description": details.get("description", ""),
                "tool_to_use": details.get("tool_to_use", "cli_command_generation"),
                "tool_args": details.get("tool_args", {}),
                "cloud_provider": details.get("cloud_provider"),
                "dependencies": details.get("dependencies", []),
                "pass_output_to_next": details.get("pass_output_to_next", True)
            }
            
            # Include executed command if available (for reproducible execution)
            if details.get("executed_command"):
                step_data["executed_command"] = details["executed_command"]
                step_data["execution_successful"] = details.get("execution_successful", False)
                
                # Include tool-specific data for proper re-execution
                if details.get("mcp_tool_name"):
                    step_data["mcp_tool_name"] = details["mcp_tool_name"]
                    step_data["mcp_tool_args"] = details.get("mcp_tool_args", {})
                elif details.get("file_tool_name"):
                    step_data["file_tool_name"] = details["file_tool_name"]
                    step_data["file_tool_args"] = details.get("file_tool_args", {})
            
            workflow_data["steps"][step_id] = step_data
        
        # Save to file
        try:
            os.makedirs(output_dir, exist_ok=True)
            with open(filepath, 'w') as f:
                json.dump(workflow_data, f, indent=2)
            
            self.console.print(f"[green]✓ Saturn workflow saved to: [bold]{filepath}[/bold][/green]")
            self.console.print(f"[dim]Steps: {len(step_details_map)}, Dependencies: {len(workflow_data['dag']['edges'])}[/dim]")
            
            return filepath
            
        except Exception as e:
            self.console.print(f"[bold red]Error saving workflow file: {e}[/bold red]")
            raise
    
    def load_workflow(self, filepath: str) -> Tuple[Any, Dict[str, Any], List[str], str]:
        """
        Load a DAG execution flow from a .sat file.
        
        Args:
            filepath: Path to the .sat file
            
        Returns:
            Tuple of (dag, step_details_map, execution_order, original_query)
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Saturn workflow file not found: {filepath}")
        
        if not filepath.endswith('.sat'):
            raise ValueError(f"File must have .sat extension: {filepath}")
        
        try:
            with open(filepath, 'r') as f:
                workflow_data = json.load(f)
            
            # Validate format
            if "saturn_workflow" not in workflow_data:
                raise ValueError("Invalid .sat file format: missing saturn_workflow section")
            
            if "dag" not in workflow_data or "steps" not in workflow_data:
                raise ValueError("Invalid .sat file format: missing dag or steps section")
            
            # Extract metadata
            workflow_info = workflow_data["saturn_workflow"]
            original_query = workflow_info.get("original_query", "Loaded from .sat file")
            created_at = workflow_info.get("created_at", "Unknown")
            version = workflow_info.get("version", "Unknown")
            
            self.console.print(f"[cyan]Loading Saturn workflow from: [bold]{filepath}[/bold][/cyan]")
            self.console.print(f"[dim]Created: {created_at}, Version: {version}[/dim]")
            self.console.print(f"[dim]Original query: {original_query}[/dim]")
            
            # Reconstruct DAG
            from internal.dag.dag import AcyclicGraph, Edge
            
            dag = AcyclicGraph()
            dag_data = workflow_data["dag"]
            
            # Add vertices
            for node_id in dag_data.get("nodes", []):
                dag.add(node_id)
            
            # Add edges
            for edge_data in dag_data.get("edges", []):
                source = edge_data["source"]
                target = edge_data["target"]
                dag.connect(Edge(source, target))
            
            # Get execution order
            execution_order = dag_data.get("execution_order", [])
            
            # Reconstruct step details map
            step_details_map = {}
            for step_id, step_data in workflow_data["steps"].items():
                step_details_map[step_id] = {
                    "id": step_data.get("id", step_id),
                    "description": step_data.get("description", ""),
                    "tool_to_use": step_data.get("tool_to_use", "cli_command_generation"),
                    "tool_args": step_data.get("tool_args", {}),
                    "cloud_provider": step_data.get("cloud_provider"),
                    "dependencies": step_data.get("dependencies", []),
                    "pass_output_to_next": step_data.get("pass_output_to_next", True)
                }
            
            self.console.print(f"[green]✓ Workflow loaded: {len(step_details_map)} steps, {len(dag_data.get('edges', []))} dependencies[/green]")
            
            return dag, step_details_map, execution_order, original_query
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in .sat file: {e}")
        except Exception as e:
            self.console.print(f"[bold red]Error loading workflow file: {e}[/bold red]")
            raise
    
    def validate_workflow(self, filepath: str) -> bool:
        """
        Validate that a .sat file is properly formatted.
        
        Args:
            filepath: Path to the .sat file
            
        Returns:
            True if valid, False otherwise
        """
        try:
            dag, step_details_map, execution_order, _ = self.load_workflow(filepath)
            
            # Basic validation
            if not step_details_map:
                self.console.print("[yellow]Warning: No steps found in workflow[/yellow]")
                return False
            
            # Validate that all steps in execution order exist in step details
            for step_id in execution_order:
                if step_id not in step_details_map:
                    self.console.print(f"[red]Error: Step '{step_id}' in execution order not found in step details[/red]")
                    return False
            
            # Validate dependencies
            for step_id, details in step_details_map.items():
                for dep in details.get("dependencies", []):
                    if dep not in step_details_map:
                        self.console.print(f"[red]Error: Dependency '{dep}' for step '{step_id}' not found[/red]")
                        return False
            
            self.console.print("[green]✓ Workflow validation passed[/green]")
            return True
            
        except Exception as e:
            self.console.print(f"[red]Validation failed: {e}[/red]")
            return False
    
    def list_workflows(self, directory: str = ".") -> List[Dict[str, Any]]:
        """
        List all .sat files in a directory with their metadata.
        
        Args:
            directory: Directory to search for .sat files
            
        Returns:
            List of workflow metadata dictionaries
        """
        workflows = []
        
        try:
            for file_path in Path(directory).glob("*.sat"):
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    
                    workflow_info = data.get("saturn_workflow", {})
                    dag_info = data.get("dag", {})
                    steps_info = data.get("steps", {})
                    
                    workflows.append({
                        "filename": file_path.name,
                        "filepath": str(file_path),
                        "created_at": workflow_info.get("created_at", "Unknown"),
                        "original_query": workflow_info.get("original_query", "Unknown"),
                        "description": workflow_info.get("description", ""),
                        "version": workflow_info.get("version", "Unknown"),
                        "step_count": len(steps_info),
                        "edge_count": len(dag_info.get("edges", [])),
                        "file_size": file_path.stat().st_size
                    })
                except Exception as e:
                    # Skip invalid files
                    self.console.print(f"[dim yellow]Skipping invalid .sat file {file_path.name}: {e}[/dim yellow]")
                    continue
        
        except Exception as e:
            self.console.print(f"[red]Error listing workflows: {e}[/red]")
        
        return sorted(workflows, key=lambda x: x["created_at"], reverse=True) 