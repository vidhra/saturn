# Hybrid orchestrator that provides interoperability between Terraform and gcloud execution
import asyncio
import json
from typing import Dict, Any, Optional, List, Tuple
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .gcp_executor import GcloudExecutor
from .terraform_executor import TerraformExecutor
from .orchestrator import (
    get_llm_interface,
    _generate_plan_dag,
    console
)
from internal.state_recorder import RunStateLogger
from internal.dag.dag import AcyclicGraph
from .rag_engine import RAGEngine

class HybridOrchestrator:
    """
    Hybrid orchestrator that can execute plans using either Terraform or gcloud,
    providing seamless interoperability between both execution methods.
    """
    
    def __init__(self, config: Dict[str, Any], rag_engine: RAGEngine):
        """Initialize the hybrid orchestrator."""
        self.config = config
        self.rag_engine = rag_engine
        self.llm_interface = get_llm_interface(config)
        
        # Initialize both executors
        self.gcloud_executor = GcloudExecutor(config)
        self.terraform_executor = TerraformExecutor(config)
        
        # Execution preferences
        self.default_executor = config.get('default_executor', 'gcloud')  # 'gcloud', 'terraform', or 'hybrid'
        self.terraform_preferred_resources = config.get('terraform_preferred_resources', [
            'compute_instance_template',
            'compute_network',
            'compute_firewall',
            'sql_database_instance',
            'container_cluster'
        ])
        
        console.print(f"[green]Hybrid Orchestrator initialized[/green]")
        console.print(f"Default executor: {self.default_executor}")
        console.print(f"Terraform preferred for: {', '.join(self.terraform_preferred_resources)}")

    async def process_query_hybrid(
        self,
        query: str,
        execution_mode: str = "auto",
        verbose: bool = False
    ) -> Dict[str, Any]:
        """
        Process a query using hybrid execution.
        
        Args:
            query: The natural language query
            execution_mode: 'auto', 'terraform', 'gcloud', or 'dual'
            verbose: Enable verbose output
            
        Returns:
            Dictionary containing execution results
        """
        console.print(Panel(
            f"Processing query with hybrid orchestrator\n"
            f"Query: [cyan]{query}[/cyan]\n"
            f"Execution mode: [yellow]{execution_mode}[/yellow]",
            title="[bold blue]Hybrid Orchestration[/bold blue]"
        ))
        
        state_logger = RunStateLogger()
        
        try:
            # Generate execution plan
            dag, step_details_map = await _generate_plan_dag(
                query, self.llm_interface, state_logger
            )
            
            if not dag or not step_details_map:
                console.print("[red]Failed to generate execution plan[/red]")
                return {"status": "failed", "error": "Plan generation failed"}
            
            # Analyze plan and determine optimal execution strategy
            execution_strategy = self._determine_execution_strategy(
                step_details_map, execution_mode
            )
            
            # Display execution strategy
            self._display_execution_strategy(execution_strategy)
            
            # Execute based on strategy
            if execution_mode == "dual":
                return await self._execute_dual_mode(dag, step_details_map, state_logger, verbose)
            else:
                return await self._execute_single_mode(dag, step_details_map, execution_strategy, state_logger, verbose)
                
        except Exception as e:
            console.print(f"[bold red]Error in hybrid orchestration: {e}[/bold red]")
            if verbose:
                import traceback
                traceback.print_exc()
            return {"status": "failed", "error": str(e)}

    def _determine_execution_strategy(
        self,
        step_details_map: Dict[str, Any],
        execution_mode: str
    ) -> Dict[str, str]:
        """
        Determine the optimal execution strategy for each step.
        
        Args:
            step_details_map: Dictionary of step details
            execution_mode: Requested execution mode
            
        Returns:
            Dictionary mapping step IDs to executor types ('gcloud' or 'terraform')
        """
        strategy = {}
        
        for step_id, step_details in step_details_map.items():
            if execution_mode == "terraform":
                strategy[step_id] = "terraform"
            elif execution_mode == "gcloud":
                strategy[step_id] = "gcloud"
            elif execution_mode == "auto":
                # Auto-determine based on resource type and preferences
                strategy[step_id] = self._auto_select_executor(step_details)
            else:  # dual mode handled separately
                strategy[step_id] = self.default_executor
                
        return strategy

    def _auto_select_executor(self, step_details: Dict[str, Any]) -> str:
        """
        Automatically select the best executor for a step.
        
        Args:
            step_details: Details of the step
            
        Returns:
            'gcloud' or 'terraform'
        """
        description = step_details.get('description', '').lower()
        
        # Check if this is a resource type that benefits from Terraform
        for tf_resource in self.terraform_preferred_resources:
            if tf_resource.replace('_', ' ') in description or tf_resource.replace('_', '-') in description:
                return "terraform"
        
        # Check for infrastructure-as-code keywords
        iac_keywords = ['template', 'infrastructure', 'deployment', 'stack', 'provisioning']
        if any(keyword in description for keyword in iac_keywords):
            return "terraform"
        
        # Check for one-off or imperative operations
        imperative_keywords = ['list', 'describe', 'get', 'delete', 'stop', 'start']
        if any(keyword in description for keyword in imperative_keywords):
            return "gcloud"
        
        # Default to configured preference
        return self.default_executor

    def _display_execution_strategy(self, strategy: Dict[str, str]) -> None:
        """Display the execution strategy in a table."""
        
        strategy_table = Table(title="Execution Strategy", show_header=True, header_style="bold blue")
        strategy_table.add_column("Step ID", style="cyan", no_wrap=True)
        strategy_table.add_column("Executor", style="green")
        strategy_table.add_column("Reason", style="yellow")
        
        for step_id, executor in strategy.items():
            reason = "User specified" if executor != self.default_executor else "Auto-selected"
            color = "green" if executor == "terraform" else "blue"
            strategy_table.add_row(step_id, f"[{color}]{executor}[/{color}]", reason)
        
        console.print(strategy_table)

    async def _execute_single_mode(
        self,
        dag: AcyclicGraph,
        step_details_map: Dict[str, Any],
        strategy: Dict[str, str],
        state_logger: RunStateLogger,
        verbose: bool
    ) -> Dict[str, Any]:
        """Execute the plan using a single execution strategy."""
        
        results = {}
        execution_order = list(dag.topological_sort())
        
        console.print(f"\n[bold cyan]Executing {len(execution_order)} steps[/bold cyan]")
        
        for step_id in execution_order:
            step_details = step_details_map[step_id]
            executor_type = strategy[step_id]
            
            console.print(f"\n[bold]Step {step_id}[/bold] ({executor_type})")
            console.print(f"Description: {step_details.get('description', 'No description')}")
            
            try:
                if executor_type == "terraform":
                    success, result = await self._execute_terraform_step(step_id, step_details, verbose)
                else:
                    success, result = await self._execute_gcloud_step(step_id, step_details, verbose)
                
                results[step_id] = {
                    "success": success,
                    "result": result,
                    "executor": executor_type
                }
                
                if success:
                    console.print(f"[green]✓ Step {step_id} completed successfully[/green]")
                else:
                    console.print(f"[red]✗ Step {step_id} failed: {result}[/red]")
                    
            except Exception as e:
                console.print(f"[red]✗ Step {step_id} failed with exception: {e}[/red]")
                results[step_id] = {
                    "success": False,
                    "result": str(e),
                    "executor": executor_type
                }
        
        return {
            "status": "completed",
            "results": results,
            "execution_strategy": strategy
        }

    async def _execute_dual_mode(
        self,
        dag: AcyclicGraph,
        step_details_map: Dict[str, Any],
        state_logger: RunStateLogger,
        verbose: bool
    ) -> Dict[str, Any]:
        """Execute the plan using both executors and compare results."""
        
        console.print(f"\n[bold yellow]Dual execution mode - running with both executors[/bold yellow]")
        
        results = {}
        execution_order = list(dag.topological_sort())
        
        for step_id in execution_order:
            step_details = step_details_map[step_id]
            
            console.print(f"\n[bold]Step {step_id}[/bold] (dual execution)")
            console.print(f"Description: {step_details.get('description', 'No description')}")
            
            # Execute with both executors
            terraform_result = await self._execute_terraform_step(step_id, step_details, verbose)
            gcloud_result = await self._execute_gcloud_step(step_id, step_details, verbose)
            
            # Compare results
            comparison = self._compare_execution_results(terraform_result, gcloud_result)
            
            results[step_id] = {
                "terraform": {
                    "success": terraform_result[0],
                    "result": terraform_result[1]
                },
                "gcloud": {
                    "success": gcloud_result[0],
                    "result": gcloud_result[1]
                },
                "comparison": comparison
            }
            
            # Display comparison
            self._display_dual_execution_result(step_id, results[step_id])
        
        return {
            "status": "completed",
            "results": results,
            "execution_mode": "dual"
        }

    async def _execute_terraform_step(
        self,
        step_id: str,
        step_details: Dict[str, Any],
        verbose: bool
    ) -> Tuple[bool, Any]:
        """Execute a step using Terraform."""
        
        # Extract command from step details
        command = step_details.get('command', '')
        if not command:
            return False, "No command found in step details"
        
        try:
            # Determine execution mode based on command type
            execution_mode = "convert" if command.startswith('gcloud') else "terraform"
            
            return await self.terraform_executor.execute(
                command, console, step_id, execution_mode
            )
        except Exception as e:
            return False, f"Terraform execution failed: {e}"

    async def _execute_gcloud_step(
        self,
        step_id: str,
        step_details: Dict[str, Any],
        verbose: bool
    ) -> Tuple[bool, Any]:
        """Execute a step using gcloud."""
        
        # Extract command from step details
        command = step_details.get('command', '')
        if not command:
            return False, "No command found in step details"
        
        try:
            return await self.gcloud_executor.execute(command, console, step_id)
        except Exception as e:
            return False, f"Gcloud execution failed: {e}"

    def _compare_execution_results(
        self,
        terraform_result: Tuple[bool, Any],
        gcloud_result: Tuple[bool, Any]
    ) -> Dict[str, Any]:
        """Compare results from both executors."""
        
        comparison = {
            "both_succeeded": terraform_result[0] and gcloud_result[0],
            "both_failed": not terraform_result[0] and not gcloud_result[0],
            "terraform_only": terraform_result[0] and not gcloud_result[0],
            "gcloud_only": not terraform_result[0] and gcloud_result[0],
            "results_differ": terraform_result[1] != gcloud_result[1]
        }
        
        # Determine recommendation
        if comparison["both_succeeded"]:
            if comparison["results_differ"]:
                comparison["recommendation"] = "Both succeeded but results differ - manual review needed"
            else:
                comparison["recommendation"] = "Both succeeded with same result - either can be used"
        elif comparison["terraform_only"]:
            comparison["recommendation"] = "Use Terraform - gcloud failed"
        elif comparison["gcloud_only"]:
            comparison["recommendation"] = "Use gcloud - Terraform failed"
        else:
            comparison["recommendation"] = "Both failed - manual intervention required"
        
        return comparison

    def _display_dual_execution_result(self, step_id: str, result: Dict[str, Any]) -> None:
        """Display the results of dual execution."""
        
        terraform_status = "✓" if result["terraform"]["success"] else "✗"
        gcloud_status = "✓" if result["gcloud"]["success"] else "✗"
        
        console.print(f"  Terraform: [{terraform_status}] {terraform_status}")
        console.print(f"  Gcloud:    [{gcloud_status}] {gcloud_status}")
        console.print(f"  Recommendation: {result['comparison']['recommendation']}")

    async def generate_terraform_from_gcloud_history(
        self,
        log_file_path: str
    ) -> Dict[str, Any]:
        """
        Generate Terraform configuration from gcloud command history.
        
        Args:
            log_file_path: Path to log file containing gcloud commands
            
        Returns:
            Dictionary containing Terraform configurations
        """
        console.print(Panel(
            f"Generating Terraform from gcloud history: {log_file_path}",
            title="[bold blue]History Conversion[/bold blue]"
        ))
        
        try:
            # Read the log file (assuming it's the JSON format like the attached file)
            with open(log_file_path, 'r') as f:
                log_data = json.load(f)
            
            terraform_configs = {}
            
            # Extract commands from the log
            if 'nodes' in log_data:
                for node_id, node_data in log_data['nodes'].items():
                    if 'output' in node_data and 'executed_command_str' in node_data['output']:
                        command = node_data['output']['executed_command_str']
                        
                        # Convert to Terraform
                        tf_config = self.terraform_executor._convert_gcloud_to_terraform(command)
                        
                        if tf_config and tf_config.get('type') != 'unsupported_conversion':
                            terraform_configs[node_id] = tf_config
                            console.print(f"[green]✓ Converted {node_id}: {command}[/green]")
                        else:
                            console.print(f"[yellow]⚠ Could not convert {node_id}: {command}[/yellow]")
            
            # Generate combined Terraform file
            if terraform_configs:
                combined_config = self._combine_terraform_configs(terraform_configs)
                
                # Write to file
                output_file = "generated_terraform.tf"
                with open(output_file, 'w') as f:
                    f.write(combined_config)
                
                console.print(f"[green]Generated Terraform configuration: {output_file}[/green]")
                
                return {
                    "status": "success",
                    "configs": terraform_configs,
                    "combined_file": output_file,
                    "combined_config": combined_config
                }
            else:
                return {
                    "status": "no_conversions",
                    "message": "No commands could be converted to Terraform"
                }
                
        except Exception as e:
            console.print(f"[red]Error generating Terraform from history: {e}[/red]")
            return {"status": "error", "error": str(e)}

    def _combine_terraform_configs(self, configs: Dict[str, Any]) -> str:
        """Combine multiple Terraform configurations into a single file."""
        
        combined = {
            "terraform": {
                "required_providers": {
                    "google": {
                        "source": "hashicorp/google",
                        "version": "~> 4.0"
                    }
                }
            },
            "provider": {
                "google": {
                    "project": self.config.get('gcp_project_id'),
                    "region": "us-central1"
                }
            },
            "resource": {}
        }
        
        # Merge all resources
        for config_name, config in configs.items():
            if config.get('type') == 'terraform_config' and 'config' in config:
                tf_config = config['config']
                if 'resource' in tf_config:
                    for resource_type, resources in tf_config['resource'].items():
                        if resource_type not in combined['resource']:
                            combined['resource'][resource_type] = {}
                        combined['resource'][resource_type].update(resources)
        
        return self.terraform_executor._json_to_hcl(combined)

# Convenience function for hybrid execution
async def run_query_hybrid(
    query: str,
    config: Dict[str, Any],
    rag_engine: RAGEngine,
    execution_mode: str = "auto",
    verbose: bool = False
) -> Dict[str, Any]:
    """
    Run a query using the hybrid orchestrator.
    
    Args:
        query: Natural language query
        config: Configuration dictionary
        rag_engine: RAG engine instance
        execution_mode: 'auto', 'terraform', 'gcloud', or 'dual'
        verbose: Enable verbose output
        
    Returns:
        Dictionary containing execution results
    """
    orchestrator = HybridOrchestrator(config, rag_engine)
    return await orchestrator.process_query_hybrid(query, execution_mode, verbose) 