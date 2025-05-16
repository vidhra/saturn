from typing import Dict, Any, Type, Tuple, List, Optional
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor
from .base_state import BaseState, StateMachineContext
from .planning_state import PlanningState
from .error_handling_state import ErrorHandlingState
from ..dag.dag import AcyclicGraph, Edge
import re
import jsonschema

class ToolValidationError(Exception):
    """Raised when tool parameters are invalid."""
    pass

class DependencyError(Exception):
    """Raised when there are issues with step dependencies."""
    pass

class ReasoningState(BaseState):
    """State responsible for processing user queries and generating tool-callable steps."""

    # Define valid tools and their required parameters
    VALID_TOOLS = {
        # Local tools
        "codebase_search": {"query": str, "target_directories": list},
        "read_file": {"target_file": str, "should_read_entire_file": bool},
        "edit_file": {"target_file": str, "instructions": str, "code_edit": str},
        "run_terminal_cmd": {"command": str, "is_background": bool},
        "grep_search": {"query": str, "case_sensitive": bool},
        "list_dir": {"relative_workspace_path": str}
    }

    # Map of GCP service prefixes to their full names
    GCP_SERVICE_MAP = {
        "vpcaccess": "vpcaccess_v1",
        "compute": "compute_v1",
        "storage": "storage_v1",
        "run": "run_v2"
    }

    # Cache for validated parameter sets
    _parameter_cache = {}
    
    # Common parameter patterns
    COMMON_PARAMETERS = {
        'project_id': {
            'type': 'string',
            'pattern': r'^[a-z][a-z0-9-]{4,28}[a-z0-9]$',
            'description': 'The GCP project ID'
        },
        'location': {
            'type': 'string',
            'pattern': r'^[a-z]+-[a-z]+[0-9]$',
            'description': 'The GCP region/location'
        },
        'parent': {
            'type': 'string',
            'pattern': r'^projects/[^/]+/locations/[^/]+$',
            'description': 'The parent resource path'
        }
    }

    def __init__(self):
        super().__init__()
        self.executor = ThreadPoolExecutor(max_workers=4)  # For parallel execution
        self._parameter_cache = {}
        self._validation_errors = []

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        """
        Process the user query and generate a DAG of tool-callable steps.
        
        Args:
            context: The current state machine context
            
        Returns:
            Tuple containing next state and updated context
        """
        try:
            # Use the LLM interface to generate a step-by-step plan
            reasoning_prompt = f"""
            Given the user query: {context.original_query}
            
            Break down the task into individual steps that can be executed as tool calls.
            For each step, specify:
            1. The tool to call (e.g., codebase_search, read_file, edit_file, run_terminal_cmd)
            2. Required parameters for the tool
            3. Dependencies on previous steps (if any)
            4. Expected output and how it will be used
            
            Format each step as a JSON object with:
            {{
                "step_id": "unique_id",
                "tool": "tool_name",
                "parameters": {{
                    "param1": "value1",
                    ...
                }},
                "dependencies": ["step_id1", "step_id2"],
                "description": "What this step does",
                "expected_output": "What we expect to get from this step"
            }}
            
            Return a list of these steps in execution order.
            """
            
            # Get reasoning from LLM with retry logic
            reasoning_response = await self._get_llm_response_with_retry(context, reasoning_prompt)
            context.llm_text_response = reasoning_response
            
            # Parse the reasoning into a DAG definition
            dag_definition = await self._parse_reasoning_to_dag(reasoning_response)
            context.dag_definition = dag_definition
            
            # Initialize node states
            context.node_states = {
                node_id: "PENDING" 
                for node_id in dag_definition["nodes"]
            }

            # Log the DAG structure
            self._log_dag_structure(dag_definition, context)
            
            # Move to planning state
            return PlanningState, context
            
        except Exception as e:
            context.current_errors.append({
                "state": "reasoning",
                "error": str(e),
                "details": "Failed to process query and generate DAG"
            })
            return ErrorHandlingState, context

    def _log_dag_structure(self, dag_definition: Dict[str, Any], context: StateMachineContext) -> None:
        """Log the DAG structure in a tree-like format."""
        if not hasattr(context, 'console'):
            return

        console = context.console
        nodes = dag_definition["nodes"]
        edges = dag_definition["edges"]
        execution_order = dag_definition["execution_order"]

        # Create a mapping of node to its children
        children_map = {}
        for edge in edges:
            source, target = edge.split(" -> ")
            if source not in children_map:
                children_map[source] = []
            children_map[source].append(target)

        # Find root nodes (nodes with no incoming edges)
        root_nodes = set(nodes.keys())
        for edge in edges:
            _, target = edge.split(" -> ")
            root_nodes.discard(target)

        console.print("\n[bold cyan]DAG Structure:[/bold cyan]")
        
        def print_node(node_id: str, level: int = 0, prefix: str = "") -> None:
            """Recursively print a node and its children."""
            node = nodes[node_id]
            indent = "    " * level
            arrow = "└── " if level > 0 else ""
            
            # Print node info
            console.print(f"{indent}{arrow}[bold]{node_id}[/bold]")
            console.print(f"{indent}    Tool: [yellow]{node['tool']}[/yellow]")
            console.print(f"{indent}    Description: {node['description']}")
            
            # Print children
            for child in children_map.get(node_id, []):
                print_node(child, level + 1)

        # Print each root node and its subtree
        for root in sorted(root_nodes):
            print_node(root)

        # Print execution order
        console.print("\n[bold cyan]Execution Order:[/bold cyan]")
        for i, node_id in enumerate(execution_order, 1):
            node = nodes[node_id]
            console.print(f"{i}. [bold]{node_id}[/bold] - {node['tool']}")

    async def _get_llm_response_with_retry(self, context: StateMachineContext, prompt: str, max_retries: int = 3) -> str:
        """Get LLM response with retry logic."""
        for attempt in range(max_retries):
            try:
                response = await context.llm_interface.generate(prompt)
                if self._validate_llm_response(response):
                    return response
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                await asyncio.sleep(1 * (attempt + 1))  # Exponential backoff
        raise Exception("Failed to get valid LLM response after retries")

    def _validate_llm_response(self, response: str) -> bool:
        """Validate that the LLM response is properly formatted JSON."""
        try:
            steps = json.loads(response)
            if not isinstance(steps, list):
                return False
            for step in steps:
                if not all(k in step for k in ["step_id", "tool", "parameters", "dependencies", "description", "expected_output"]):
                    return False
            return True
        except json.JSONDecodeError:
            return False

    async def _parse_reasoning_to_dag(self, reasoning_response: str) -> Dict[str, Any]:
        """
        Parse the LLM's reasoning response into a DAG definition with tool-callable steps.
        
        Args:
            reasoning_response: The LLM's response containing the reasoning
            
        Returns:
            Dict containing the DAG definition
        """
        try:
            # Parse the JSON response from LLM
            steps = json.loads(reasoning_response)
            
            # Validate steps
            self._validate_steps(steps)
            
            # Create DAG
            dag = AcyclicGraph()
            nodes = {}
            
            # Add nodes and edges
            for step in steps:
                node_id = step["step_id"]
                dag.add(node_id)
                nodes[node_id] = {
                    "type": "tool_call",
                    "tool": step["tool"],
                    "parameters": step["parameters"],
                    "description": step["description"],
                    "expected_output": step["expected_output"],
                    "dependencies": step["dependencies"]
                }
                
                # Add edges for dependencies
                for dep in step["dependencies"]:
                    dag.connect(Edge(dep, node_id))
            
            # Validate DAG
            dag.validate()
            
            # Get execution order
            execution_order = dag.topo_order(ORDER_DOWN)
            
            return {
                "nodes": nodes,
                "edges": [str(edge) for edge in dag.edges],
                "execution_order": execution_order
            }
            
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid JSON in LLM response: {str(e)}")
        except Exception as e:
            # If parsing fails, return a basic DAG with error handling
            return {
                "nodes": {
                    "error_node": {
                        "type": "error_handling",
                        "parameters": {"error": str(e)},
                        "dependencies": []
                    }
                },
                "edges": [],
                "execution_order": ["error_node"]
            }

    def _validate_steps(self, steps: List[Dict[str, Any]]) -> None:
        """
        Validate the steps for correctness and completeness.
        
        Args:
            steps: List of step definitions
            
        Raises:
            ToolValidationError: If tool parameters are invalid
            DependencyError: If there are issues with dependencies
        """
        step_ids = set()
        
        for step in steps:
            # Validate step_id uniqueness
            if step["step_id"] in step_ids:
                raise DependencyError(f"Duplicate step_id: {step['step_id']}")
            step_ids.add(step["step_id"])
            
            # Validate tool
            if step["tool"] not in self.VALID_TOOLS:
                raise ToolValidationError(f"Invalid tool: {step['tool']}")
            
            # Validate parameters
            required_params = self.VALID_TOOLS[step["tool"]]
            for param, param_type in required_params.items():
                if param not in step["parameters"]:
                    raise ToolValidationError(f"Missing required parameter '{param}' for tool {step['tool']}")
                if not isinstance(step["parameters"][param], param_type):
                    raise ToolValidationError(
                        f"Invalid type for parameter '{param}' in tool {step['tool']}. "
                        f"Expected {param_type.__name__}, got {type(step['parameters'][param]).__name__}"
                    )
            
            # Validate dependencies
            for dep in step["dependencies"]:
                if dep not in step_ids:
                    raise DependencyError(f"Dependency '{dep}' not found for step {step['step_id']}")

    async def _validate_parameters(self, tool: str, parameters: Dict[str, Any], context: StateMachineContext) -> Tuple[bool, List[str]]:
        """
        Enhanced parameter validation that reduces round trips by:
        1. Checking parameter cache first
        2. Validating common parameters upfront
        3. Providing detailed error messages for all issues at once
        """
        # Check cache first
        cache_key = f"{tool}:{json.dumps(parameters, sort_keys=True)}"
        if cache_key in self._parameter_cache:
            return self._parameter_cache[cache_key]
            
        errors = []
        
        # Get schema from knowledge base
        param_schema = context.knowledge_base.get_tool_parameter_json_schema(tool)
        if not param_schema:
            return True, []  # No schema means no validation needed
            
        # 1. Validate common parameters first
        for param_name, param_spec in self.COMMON_PARAMETERS.items():
            if param_name in parameters:
                value = parameters[param_name]
                if not isinstance(value, str):
                    errors.append(f"Parameter '{param_name}' must be a string")
                elif not re.match(param_spec['pattern'], value):
                    errors.append(f"Parameter '{param_name}' has invalid format: {param_spec['description']}")
                    
        # 2. Validate against schema
        try:
            jsonschema.validate(instance=parameters, schema=param_schema)
        except jsonschema.exceptions.ValidationError as e:
            # Collect all validation errors
            for error in e.context:
                errors.append(f"Parameter '{error.path[0]}': {error.message}")
                
        # 3. Special handling for GCP tools
        if '_' in tool:  # Likely a GCP tool
            # Ensure project_id is available
            if 'project_id' not in parameters and hasattr(context, 'gcp_executor'):
                if context.gcp_executor.gcp_project_id:
                    parameters['project_id'] = context.gcp_executor.gcp_project_id
                else:
                    errors.append("project_id is required but not provided")
                    
            # Construct parent if needed
            if 'parent' not in parameters and ('project_id' in parameters or hasattr(context, 'gcp_executor')):
                project = parameters.get('project_id') or getattr(context.gcp_executor, 'gcp_project_id', None)
                location = parameters.get('location')
                if project and location:
                    parameters['parent'] = f"projects/{project}/locations/{location}"
                    
        # Cache the result
        is_valid = len(errors) == 0
        self._parameter_cache[cache_key] = (is_valid, errors)
        
        return is_valid, errors

    async def _execute_step(self, step: Dict[str, Any], context: StateMachineContext) -> Any:
        """
        Execute a single step with retry logic.
        
        Args:
            step: Step definition
            context: Current context
            
        Returns:
            Step execution result
        """
        max_retries = 3
        last_error = None
        
        # Log step execution start
        if hasattr(context, 'console'):
            context.console.print(f"\n[bold cyan]Executing Step: {step['step_id']}[/bold cyan]")
            context.console.print(f"Tool: [yellow]{step['tool']}[/yellow]")
            context.console.print(f"Description: {step['description']}")
            context.console.print(f"Dependencies: {', '.join(step['dependencies']) if step['dependencies'] else 'None'}")
        
        for attempt in range(max_retries):
            try:
                # Execute step
                result = await self._execute_tool(
                    step["tool"],
                    step["parameters"],
                    context
                )
                
                # Log successful execution
                if hasattr(context, 'console'):
                    context.console.print(f"[green]✓ Step {step['step_id']} completed successfully[/green]")
                    if step.get('expected_output'):
                        context.console.print(f"Expected output: {step['expected_output']}")
                
                return result
                
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    # Log retry attempt
                    if hasattr(context, 'console'):
                        context.console.print(f"[yellow]Retry {attempt + 1}/{max_retries} for {step['tool']} due to: {str(e)}[/yellow]")
                    await asyncio.sleep(1 * (attempt + 1))  # Exponential backoff
                else:
                    # Log final failure
                    if hasattr(context, 'console'):
                        context.console.print(f"[red]Failed to execute {step['tool']} after {max_retries} attempts[/red]")
                    raise Exception(f"Failed after {max_retries} attempts. Last error: {str(last_error)}")

    async def _execute_tool(self, tool: str, parameters: Dict[str, Any], context: StateMachineContext) -> Any:
        """Execute a tool with enhanced parameter validation."""
        # Validate parameters first
        is_valid, errors = await self._validate_parameters(tool, parameters, context)
        if not is_valid:
            error_msg = "\n".join(errors)
            raise ValueError(f"Parameter validation failed for {tool}:\n{error_msg}")
            
        try:
            # Check if this is a GCP tool call
            is_gcp_tool = False
            service_prefix = None
            
            # Check for GCP service prefixes
            for prefix, full_service in self.GCP_SERVICE_MAP.items():
                if tool.startswith(f"{prefix}_"):
                    is_gcp_tool = True
                    service_prefix = full_service
                    break
            
            if is_gcp_tool:
                # Validate GCP context requirements
                if not hasattr(context, 'gcp_executor'):
                    raise ValueError("GCP tool called but no GcpExecutor available in context")
                if not hasattr(context, 'knowledge_base'):
                    raise ValueError("GCP tool called but no KnowledgeBase available in context")
                if not hasattr(context, 'console'):
                    raise ValueError("GCP tool called but no Console available in context")
                
                # Ensure project_id is available
                if not context.gcp_executor.gcp_project_id:
                    raise ValueError("GCP tool called but no project_id configured in GcpExecutor")
                
                # Execute using GcpExecutor
                try:
                    success, result = await context.gcp_executor.execute(
                        service_method_name=tool,
                        llm_args=parameters,
                        knowledge_base=context.knowledge_base,
                        console=context.console
                    )
                    
                    if not success:
                        # Format error message for better debugging
                        error_msg = f"GCP execution failed for {tool}: {result}"
                        if isinstance(result, dict) and 'error' in result:
                            error_msg = f"GCP execution failed for {tool}: {result['error']}"
                        raise Exception(error_msg)
                    
                    # Log successful execution
                    context.console.print(f"[green]Successfully executed GCP tool: {tool}[/green]")
                    return result
                    
                except Exception as gcp_err:
                    # Enhanced error handling for GCP-specific errors
                    error_msg = f"GCP execution error for {tool}: {str(gcp_err)}"
                    if hasattr(gcp_err, 'response'):
                        error_msg += f"\nResponse: {gcp_err.response}"
                    raise Exception(error_msg)
            
            # For non-GCP tools, use the local executors
            if tool not in self.VALID_TOOLS:
                raise ValueError(f"Unknown tool: {tool}")
            
            # Execute the tool in thread pool
            executor = getattr(self, f"_execute_{tool}")
            return await asyncio.get_event_loop().run_in_executor(
                self.executor,
                executor,
                parameters,
                context
            )
            
        except Exception as e:
            # Enhanced error reporting
            error_msg = f"Error executing tool {tool}: {str(e)}"
            if hasattr(context, 'console'):
                context.console.print(f"[red]{error_msg}[/red]")
            raise Exception(error_msg)

    def _execute_codebase_search(self, parameters: Dict[str, Any], context: StateMachineContext) -> Any:
        """Execute codebase search tool."""
        query = parameters["query"]
        target_dirs = parameters["target_directories"]
        
        # Use the context's knowledge base or search functionality
        if hasattr(context, 'knowledge_base'):
            return context.knowledge_base.search(query, target_dirs)
        else:
            # Fallback to basic file search
            import os
            results = []
            for root, _, files in os.walk(os.getcwd()):
                if any(root.startswith(d) for d in target_dirs):
                    for file in files:
                        if file.endswith(('.py', '.js', '.ts', '.java')):
                            results.append(os.path.join(root, file))
            return results

    def _execute_read_file(self, parameters: Dict[str, Any], context: StateMachineContext) -> Any:
        """Execute read file tool."""
        target_file = parameters["target_file"]
        should_read_entire_file = parameters["should_read_entire_file"]
        
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                if should_read_entire_file:
                    return f.read()
                else:
                    # Read first 1000 characters as preview
                    return f.read(1000)
        except Exception as e:
            raise Exception(f"Error reading file {target_file}: {str(e)}")

    def _execute_edit_file(self, parameters: Dict[str, Any], context: StateMachineContext) -> Any:
        """Execute edit file tool."""
        target_file = parameters["target_file"]
        instructions = parameters["instructions"]
        code_edit = parameters["code_edit"]
        
        try:
            # Read current content
            with open(target_file, 'r', encoding='utf-8') as f:
                current_content = f.read()
            
            # Apply edit
            # This is a simple implementation - you might want to use a proper diff/patch library
            if code_edit in current_content:
                return "No changes needed - code already exists"
            
            # Write new content
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(current_content + "\n" + code_edit)
            
            return "File edited successfully"
            
        except Exception as e:
            raise Exception(f"Error editing file {target_file}: {str(e)}")

    def _execute_terminal_cmd(self, parameters: Dict[str, Any], context: StateMachineContext) -> Any:
        """Execute terminal command tool."""
        command = parameters["command"]
        is_background = parameters["is_background"]
        
        try:
            import subprocess
            if is_background:
                # Start process in background
                process = subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                return f"Started background process with PID: {process.pid}"
            else:
                # Run command and wait for completion
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    return result.stdout
                else:
                    raise Exception(f"Command failed: {result.stderr}")
                    
        except Exception as e:
            raise Exception(f"Error executing command: {str(e)}")

    def _execute_grep_search(self, parameters: Dict[str, Any], context: StateMachineContext) -> Any:
        """Execute grep search tool."""
        query = parameters["query"]
        case_sensitive = parameters["case_sensitive"]
        
        try:
            import subprocess
            flags = "" if case_sensitive else "-i"
            result = subprocess.run(
                f"grep {flags} -r '{query}' .",
                shell=True,
                capture_output=True,
                text=True
            )
            if result.returncode in (0, 1):  # grep returns 1 if no matches found
                return result.stdout
            else:
                raise Exception(f"Grep failed: {result.stderr}")
                
        except Exception as e:
            raise Exception(f"Error executing grep: {str(e)}")

    def _execute_list_dir(self, parameters: Dict[str, Any], context: StateMachineContext) -> Any:
        """Execute list directory tool."""
        relative_path = parameters["relative_workspace_path"]
        
        try:
            import os
            path = os.path.join(os.getcwd(), relative_path)
            if not os.path.exists(path):
                raise Exception(f"Directory does not exist: {relative_path}")
            
            items = os.listdir(path)
            return {
                "path": relative_path,
                "items": items,
                "is_directory": [os.path.isdir(os.path.join(path, item)) for item in items]
            }
            
        except Exception as e:
            raise Exception(f"Error listing directory {relative_path}: {str(e)}") 