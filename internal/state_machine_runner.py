import json
import os
import time
from typing import Any, Dict, List, Optional

from saturn.config import vprint

from .states.base_state import StateMachineContext
from .states.completed_state import CompletedState
from .states.failed_state import FailedState
from .states.start_state import StartState


class ToolCache:
    """Cache for expensive tool discovery operations."""

    def __init__(self, cache_ttl: int = 300):  # 5 minutes default TTL
        self.cache_ttl = cache_ttl
        self._file_tools_cache = {}
        self._mcp_tools_cache = {}
        self._project_type_cache = {}

    def _is_cache_valid(self, cache_entry: Dict) -> bool:
        """Check if cache entry is still valid based on TTL."""
        return time.time() - cache_entry.get("timestamp", 0) < self.cache_ttl

    def get_file_tools(self, working_directory: str) -> Optional[List[Dict[str, Any]]]:
        """Get cached file tools for a working directory."""
        cache_key = working_directory
        if cache_key in self._file_tools_cache:
            entry = self._file_tools_cache[cache_key]
            if self._is_cache_valid(entry):
                return entry["tools"]
        return None

    def set_file_tools(self, working_directory: str, tools: List[Dict[str, Any]]):
        """Cache file tools for a working directory."""
        self._file_tools_cache[working_directory] = {
            "tools": tools,
            "timestamp": time.time(),
        }

    def get_mcp_tools(self, mcp_config_hash: str) -> Optional[List[Dict[str, Any]]]:
        """Get cached MCP tools based on configuration hash."""
        if mcp_config_hash in self._mcp_tools_cache:
            entry = self._mcp_tools_cache[mcp_config_hash]
            if self._is_cache_valid(entry):
                return entry["tools"]
        return None

    def set_mcp_tools(self, mcp_config_hash: str, tools: List[Dict[str, Any]]):
        """Cache MCP tools."""
        self._mcp_tools_cache[mcp_config_hash] = {
            "tools": tools,
            "timestamp": time.time(),
        }

    def get_project_type(self, working_directory: str) -> Optional[str]:
        """Get cached project type detection."""
        cache_key = working_directory
        if cache_key in self._project_type_cache:
            entry = self._project_type_cache[cache_key]
            if self._is_cache_valid(entry):
                return entry["project_type"]
        return None

    def set_project_type(self, working_directory: str, project_type: str):
        """Cache project type detection."""
        self._project_type_cache[working_directory] = {
            "project_type": project_type,
            "timestamp": time.time(),
        }

    def clear_cache(self):
        """Clear all cached data."""
        self._file_tools_cache.clear()
        self._mcp_tools_cache.clear()
        self._project_type_cache.clear()

    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics for debugging."""
        return {
            "file_tools_cached": len(self._file_tools_cache),
            "mcp_tools_cached": len(self._mcp_tools_cache),
            "project_types_cached": len(self._project_type_cache),
            "cache_ttl": self.cache_ttl,
        }


class StateMachineRunner:
    """Runs the state machine, managing context and transitions."""

    def __init__(
        self,
        llm_interface: Any,
        gcp_executor: Any,
        aws_executor: Any,
        knowledge_base: Any,
        system_prompt: str,
        config: Optional[Dict[str, Any]] = None,
        console: Optional[Any] = None,
        rag_engine: Optional[Any] = None,
        mcp_integrator: Optional[Any] = None,
    ):
        """Initializes the runner with necessary components."""
        self.llm_interface = llm_interface
        self.gcp_executor = gcp_executor
        self.aws_executor = aws_executor
        self.knowledge_base = knowledge_base
        self.system_prompt = system_prompt
        self.config = config or {}
        self.max_retries = self.config.get("max_retries", 5)
        self.console = console
        self.rag_engine = rag_engine
        self.mcp_integrator = mcp_integrator

        # Initialize tool cache
        cache_ttl = self.config.get("tool_cache_ttl", 300)  # 5 minutes default
        self.tool_cache = ToolCache(cache_ttl)

        # Cache for expensive one-time operations
        self._cached_file_tool_caller = None
        self._cached_working_directory = None

        self.checkpoint_dir = self.config.get("checkpoint_dir", "./checkpoints")
        os.makedirs(self.checkpoint_dir, exist_ok=True)

    def set_question_handler(self, question_handler):
        """Set a question handler for interactive questions during execution."""
        self._question_handler = question_handler

    def _setup_file_tools_with_question_handler(self, working_directory: str):
        """Set up file tools with the question handler if available."""
        if hasattr(self, '_question_handler') and self._question_handler:
            # Initialize file tool caller if not already done
            if (
                self._cached_file_tool_caller is None
                or self._cached_working_directory != working_directory
            ):
                from saturn.file_build_tools import FileBuildToolCaller
                self._cached_file_tool_caller = FileBuildToolCaller(working_directory)
                self._cached_working_directory = working_directory
            
            # Set the question handler on the file tool caller
            self._cached_file_tool_caller.set_question_handler(self._question_handler)

    def get_cached_file_tools(self, working_directory: str) -> List[Dict[str, Any]]:
        """Get file tools with caching to avoid repeated expensive discovery."""
        # Check cache first
        cached_tools = self.tool_cache.get_file_tools(working_directory)
        if cached_tools is not None:
            if self.console:
                self.console.print(
                    f"[dim]Using cached file tools ({len(cached_tools)} tools)[/dim]"
                )
            return cached_tools

        # Cache miss - perform expensive discovery
        if self.console:
            vprint("[dim]Discovering file tools (cache miss)...[/dim]",verbose=self.config.get("verbose", False))

        from saturn.file_build_tools import FileBuildToolCaller

        # Reuse tool caller instance if working directory hasn't changed
        if (
            self._cached_file_tool_caller is None
            or self._cached_working_directory != working_directory
        ):
            self._cached_file_tool_caller = FileBuildToolCaller(working_directory)
            self._cached_working_directory = working_directory

        tools = self._cached_file_tool_caller.get_available_tools()

        # Cache the result
        self.tool_cache.set_file_tools(working_directory, tools)

        if self.console:
            vprint(
                f"[dim]File tools discovered and cached ({len(tools)} tools)[/dim]",verbose=self.config.get("verbose", False)
            )

        return tools

    def get_cached_mcp_tools(self) -> List[Dict[str, Any]]:
        """Get MCP tools with caching."""
        if not hasattr(self, "mcp_integrator") or not self.mcp_integrator:
            return []

        # Create a simple hash of MCP configuration for cache key
        try:
            mcp_config = getattr(self.mcp_integrator, "config", {})
            config_str = str(sorted(mcp_config.items())) if mcp_config else "default"
            mcp_config_hash = str(hash(config_str))
        except:
            mcp_config_hash = "default"

        # Check cache first
        cached_tools = self.tool_cache.get_mcp_tools(mcp_config_hash)
        if cached_tools is not None:
            if self.console:
                self.console.print(
                    f"[dim]Using cached MCP tools ({len(cached_tools)} tools)[/dim]"
                )
            return cached_tools

        # Cache miss - get MCP tools
        if self.console:
            vprint("[dim]Discovering MCP tools (cache miss)...[/dim]",verbose=self.config.get("verbose", False))

        try:
            mcp_schemas = self.mcp_integrator.mcp_manager.get_all_tools_schemas()
            tools = (
                [tool["function"]["name"] for tool in mcp_schemas]
                if mcp_schemas
                else []
            )

            # Cache the result
            self.tool_cache.set_mcp_tools(mcp_config_hash, tools)

            if self.console:
                vprint(
                    f"[dim]MCP tools discovered and cached ({len(tools)} tools)[/dim]",verbose=self.config.get("verbose", False)
                )

            return tools
        except Exception as e:
            if self.console:
                vprint(
                    f"[dim yellow]Warning: Failed to get MCP tools: {e}[/dim yellow]",verbose=self.config.get("verbose", False)
                )
            return []

    def get_cached_project_type(self, working_directory: str) -> Optional[str]:
        """Get project type with caching."""
        cached_type = self.tool_cache.get_project_type(working_directory)
        if cached_type is not None:
            if self.console:
                self.console.print(
                    f"[dim]Using cached project type: {cached_type}[/dim]"
                )
            return cached_type

        # Cache miss - detect project type
        if self.console:
            vprint("[dim]Detecting project type (cache miss)...[/dim]",verbose=self.config.get("verbose", False))

        try:
            if (
                self._cached_file_tool_caller is None
                or self._cached_working_directory != working_directory
            ):
                from saturn.file_build_tools import FileBuildToolCaller

                self._cached_file_tool_caller = FileBuildToolCaller(working_directory)
                self._cached_working_directory = working_directory

            # Use the cached tool caller for project detection
            import asyncio

            result = asyncio.run(self._cached_file_tool_caller.detect_project_type())
            project_type = (
                result.get("project_type", "unknown")
                if result.get("success")
                else "unknown"
            )

            # Cache the result
            self.tool_cache.set_project_type(working_directory, project_type)

            if self.console:
                vprint(
                    f"[dim]Project type detected and cached: {project_type}[/dim]",verbose=self.config.get("verbose", False)
                )

            return project_type
        except Exception as e:
            if self.console:
                vprint(
                    f"[dim yellow]Warning: Failed to detect project type: {e}[/dim yellow]",verbose=self.config.get("verbose", False)
                )
            return "unknown"

    async def process_query(self, query: str) -> StateMachineContext:
        """
        Processes a given query through the state machine.

        Args:
            query: The user's natural language query or path to .sat file.

        Returns:
            The final StateMachineContext after reaching a terminal state.
        """
        # Check if query is a .sat file path
        is_sat_file = query.endswith('.sat') and os.path.exists(query)
        
        if is_sat_file:
            print(f"\n=== Starting State Machine for Saturn Workflow ===\nFile: {query}\n")
            # For .sat files, we'll load the original query from the file for logging
            try:
                from internal.saturn_workflow import SaturnWorkflow
                workflow_handler = SaturnWorkflow()
                _, _, _, original_query = workflow_handler.load_workflow(query)
                display_query = f"[Workflow] {original_query}"
            except:
                display_query = f"[Workflow] {query}"
        else:
            print(f"\n=== Starting State Machine for Query ===\nQuery: {query}\n")
            display_query = query

        from internal.state_recorder import RunStateLogger

        state_recorder = RunStateLogger(display_query)

        from saturn.file_executor import FileBuildExecutor

        file_build_executor = FileBuildExecutor(
            {"working_directory": self.config.get("working_directory", ".")}
        )

        # Set up file tools with question handler if available
        working_directory = self.config.get("working_directory", ".")
        self._setup_file_tools_with_question_handler(working_directory)

        # Prepare config for .sat file handling
        config_for_context = self.config.copy()
        if is_sat_file:
            config_for_context["sat_file_path"] = query

        context = StateMachineContext(
            original_query=query,
            llm_interface=self.llm_interface,
            gcp_executor=self.gcp_executor,
            aws_executor=self.aws_executor,
            knowledge_base=self.knowledge_base,
            system_prompt=self.system_prompt,
            max_retries=self.max_retries,
            console=self.console,
            rag_engine=self.rag_engine,
            state_recorder=state_recorder,
            file_build_executor=file_build_executor,
            mcp_integrator=self.mcp_integrator,
            config=config_for_context,
        )

        # Pass runner instance to context so states can access cached tools
        context._state_machine_runner = self

        # Determine initial state based on input type
        if is_sat_file:
            from internal.states.load_workflow_state import LoadWorkflowState
            current_state_class = LoadWorkflowState
            if self.console:
                vprint("[dim]Starting with LoadWorkflowState for .sat file[/dim]",verbose=self.config.get("verbose", False))
        else:
            current_state_class = StartState

        while current_state_class not in [CompletedState, FailedState]:
            current_state_instance = current_state_class()

            print(f"\n==> Entering State: {current_state_instance!r}")

            # Conditionally save checkpoint based on configuration
            enable_checkpoints = self.config.get("enable_checkpoints", False)
            if enable_checkpoints:
                checkpoint_id = await self._save_checkpoint(
                    context, current_state_class
                )

            try:
                next_state_class, context = await current_state_instance.run(context)
                current_state_class = next_state_class
            except Exception as e:
                print(
                    f"\n--- UNHANDLED EXCEPTION in state {current_state_instance!r} --- "
                )
                print(f"Error: {e}")
                import traceback

                traceback.print_exc()
                print(
                    "Transitioning directly to FailedState due to unhandled exception."
                )
                current_state_class = FailedState
                context.current_errors.append(
                    {
                        "method": f"RUNNER ({current_state_instance!r})",
                        "error": f"Unhandled state execution error: {e}",
                        "arguments": {},
                    }
                )

        terminal_state_instance = current_state_class()
        print(f"\n==> Entering Terminal State: {terminal_state_instance!r}")
        _, context = await terminal_state_instance.run(context)

        print("\n=== State Machine Finished ===")

        if context.state_recorder:
            if context.current_errors:
                context.state_recorder.set_final_run_status(
                    "FAILED", context.current_errors
                )
            else:
                context.state_recorder.set_final_run_status("COMPLETED", [])
            context.state_recorder.save_state()


        # Cleanup checkpoints only if checkpointing was enabled
        enable_checkpoints = self.config.get("enable_checkpoints", False)
        if enable_checkpoints:
            await self._cleanup_checkpoints(context.state_recorder.run_start_time)

        return context

    async def resume_from_checkpoint(self, checkpoint_id: str) -> StateMachineContext:
        """
        Resume execution from a saved checkpoint.

        Args:
            checkpoint_id: The ID of the checkpoint to resume from

        Returns:
            The StateMachineContext to continue execution
        """
        checkpoint_path = os.path.join(self.checkpoint_dir, f"{checkpoint_id}.json")

        if not os.path.exists(checkpoint_path):
            raise FileNotFoundError(f"Checkpoint {checkpoint_id} not found")

        print(f"\n=== Resuming from Checkpoint: {checkpoint_id} ===")

        with open(checkpoint_path, "r") as f:
            checkpoint_data = json.load(f)

        # Reconstruct context from checkpoint
        context = await self._deserialize_context(checkpoint_data["context"])
        state_class_name = checkpoint_data["current_state"]

        # Get the state class from name
        current_state_class = self._get_state_class_by_name(state_class_name)

        print(f"Resuming at state: {state_class_name}")

        # Continue state machine execution from this point
        while current_state_class not in [CompletedState, FailedState]:
            current_state_instance = current_state_class()
            print(f"\n==> Resuming State: {current_state_instance!r}")

            try:
                next_state_class, context = await current_state_instance.run(context)
                current_state_class = next_state_class
            except Exception as e:
                print(
                    f"\n--- EXCEPTION in resumed state {current_state_instance!r} ---"
                )
                print(f"Error: {e}")
                current_state_class = FailedState
                context.current_errors.append(
                    {
                        "method": f"RESUMED_RUNNER ({current_state_instance!r})",
                        "error": f"Resumed state execution error: {e}",
                        "arguments": {},
                    }
                )

        terminal_state_instance = current_state_class()
        print(f"\n==> Entering Terminal State: {terminal_state_instance!r}")
        _, context = await terminal_state_instance.run(context)

        return context

    async def _save_checkpoint(
        self, context: StateMachineContext, state_class: type
    ) -> str:
        """Save current context and state as a checkpoint."""
        timestamp = context.state_recorder.run_start_time.replace(":", "-").replace(
            ".", "-"
        )
        checkpoint_id = f"{timestamp}_{state_class.__name__}"
        checkpoint_path = os.path.join(self.checkpoint_dir, f"{checkpoint_id}.json")

        checkpoint_data = {
            "checkpoint_id": checkpoint_id,
            "timestamp": context.state_recorder.run_start_time,
            "current_state": state_class.__name__,
            "context": await self._serialize_context(context),
        }

        with open(checkpoint_path, "w") as f:
            json.dump(checkpoint_data, f, indent=2)

        if self.console:
            vprint(f"[dim]Checkpoint saved: {checkpoint_id}[/dim]",verbose=self.config.get("verbose", False))

        return checkpoint_id

    async def _serialize_context(self, context: StateMachineContext) -> Dict[str, Any]:
        """Serialize context for checkpoint saving."""
        return {
            "original_query": context.original_query,
            "system_prompt": context.system_prompt,
            "max_retries": context.max_retries,
            "current_attempt": context.current_attempt,
            "execution_order": context.execution_order,
            "step_outputs": context.step_outputs,
            "current_errors": context.current_errors,
            "step_details_map": context.step_details_map,
            "dag_vertices": list(context.dag.vertices) if context.dag else [],
            "dag_edges": (
                [(str(e.source), str(e.target)) for e in context.dag.edges]
                if context.dag
                else []
            ),
        }

    async def _deserialize_context(
        self, context_data: Dict[str, Any]
    ) -> StateMachineContext:
        """Deserialize context from checkpoint data."""
        from internal.state_recorder import RunStateLogger
        from saturn.file_executor import FileBuildExecutor

        # Reconstruct basic context
        context = StateMachineContext(
            original_query=context_data["original_query"],
            llm_interface=self.llm_interface,
            gcp_executor=self.gcp_executor,
            aws_executor=self.aws_executor,
            knowledge_base=self.knowledge_base,
            system_prompt=context_data["system_prompt"],
            max_retries=context_data["max_retries"],
            console=self.console,
            rag_engine=self.rag_engine,
            state_recorder=RunStateLogger(context_data["original_query"]),
            file_build_executor=FileBuildExecutor(
                {"working_directory": self.config.get("working_directory", ".")}
            ),
            mcp_integrator=self.mcp_integrator,
            config=self.config,
        )

        # Restore execution state
        context.current_attempt = context_data["current_attempt"]
        context.execution_order = context_data["execution_order"]
        context.step_outputs = context_data["step_outputs"]
        context.current_errors = context_data["current_errors"]
        context.step_details_map = context_data["step_details_map"]

        # Reconstruct DAG if it existed
        if context_data["dag_vertices"]:
            from internal.dag.dag import AcyclicGraph, Edge

            context.dag = AcyclicGraph()
            for vertex in context_data["dag_vertices"]:
                context.dag.add(vertex)
            for source, target in context_data["dag_edges"]:
                context.dag.connect(Edge(source, target))

        return context

    def _get_state_class_by_name(self, state_name: str):
        """Get state class by name."""
        state_mapping = {
            "StartState": StartState,
            "CompletedState": CompletedState,
            "FailedState": FailedState,
        }

        # Import states dynamically to avoid circular imports
        try:
            from .states.reasoning_state import ReasoningState

            state_mapping["ReasoningState"] = ReasoningState
        except ImportError:
            pass

        try:
            from .states.planning_state import PlanningState

            state_mapping["PlanningState"] = PlanningState
        except ImportError:
            pass

        try:
            from .states.executing_state import ExecutingState

            state_mapping["ExecutingState"] = ExecutingState
        except ImportError:
            pass

        try:
            from .states.load_workflow_state import LoadWorkflowState

            state_mapping["LoadWorkflowState"] = LoadWorkflowState
        except ImportError:
            pass

        try:
            from .states.processing_results_state import ProcessingResultsState

            state_mapping["ProcessingResultsState"] = ProcessingResultsState
        except ImportError:
            pass

        try:
            from .states.terraform_state import (TerraformPlanningState,
                                                 TerraformState)

            state_mapping["TerraformState"] = TerraformState
            state_mapping["TerraformPlanningState"] = TerraformPlanningState
        except ImportError:
            pass

        return state_mapping.get(state_name, StartState)

    async def _cleanup_checkpoints(self, run_start_time: str):
        """Clean up checkpoints for a completed run."""
        timestamp_prefix = run_start_time.replace(":", "-").replace(".", "-")

        for filename in os.listdir(self.checkpoint_dir):
            if filename.startswith(timestamp_prefix) and filename.endswith(".json"):
                checkpoint_path = os.path.join(self.checkpoint_dir, filename)
                try:
                    os.remove(checkpoint_path)
                    if self.console:
                        vprint(
                            f"[dim]Cleaned up checkpoint: {filename}[/dim]",verbose=self.config.get("verbose", False)
                        )
                except OSError:
                    pass  # Ignore cleanup errors

    def list_checkpoints(self) -> List[Dict[str, str]]:
        """List available checkpoints."""
        checkpoints = []

        if not os.path.exists(self.checkpoint_dir):
            return checkpoints

        for filename in os.listdir(self.checkpoint_dir):
            if filename.endswith(".json"):
                checkpoint_path = os.path.join(self.checkpoint_dir, filename)
                try:
                    with open(checkpoint_path, "r") as f:
                        data = json.load(f)
                        checkpoints.append(
                            {
                                "id": data["checkpoint_id"],
                                "timestamp": data["timestamp"],
                                "state": data["current_state"],
                            }
                        )
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid checkpoint files

        return sorted(checkpoints, key=lambda x: x["timestamp"], reverse=True)
