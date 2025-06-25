import json
import os
from typing import Any, Dict, Optional, List

from .states.base_state import StateMachineContext
from .states.completed_state import CompletedState
from .states.failed_state import FailedState
from .states.start_state import StartState


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
        

        self.checkpoint_dir = self.config.get("checkpoint_dir", "./checkpoints")
        os.makedirs(self.checkpoint_dir, exist_ok=True)

    async def process_query(self, query: str) -> StateMachineContext:
        """
        Processes a given query through the state machine.

        Args:
            query: The user's natural language query.

        Returns:
            The final StateMachineContext after reaching a terminal state.
        """
        print(f"\n=== Starting State Machine for Query ===\nQuery: {query}\n")

        from internal.state_recorder import RunStateLogger

        state_recorder = RunStateLogger(query)

        from saturn.file_executor import FileBuildExecutor

        file_build_executor = FileBuildExecutor(
            {"working_directory": self.config.get("working_directory", ".")}
        )

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
            config=self.config,
        )

        current_state_class = StartState

        while current_state_class not in [CompletedState, FailedState]:
            current_state_instance = current_state_class()

            print(f"\n==> Entering State: {current_state_instance!r}")


            checkpoint_id = await self._save_checkpoint(context, current_state_class)
            
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

        with open(checkpoint_path, 'r') as f:
            checkpoint_data = json.load(f)

        # Reconstruct context from checkpoint
        context = await self._deserialize_context(checkpoint_data['context'])
        state_class_name = checkpoint_data['current_state']
        
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
                print(f"\n--- EXCEPTION in resumed state {current_state_instance!r} ---")
                print(f"Error: {e}")
                current_state_class = FailedState
                context.current_errors.append({
                    "method": f"RESUMED_RUNNER ({current_state_instance!r})",
                    "error": f"Resumed state execution error: {e}",
                    "arguments": {},
                })

        terminal_state_instance = current_state_class()
        print(f"\n==> Entering Terminal State: {terminal_state_instance!r}")
        _, context = await terminal_state_instance.run(context)

        return context

    async def _save_checkpoint(self, context: StateMachineContext, state_class: type) -> str:
        """Save current context and state as a checkpoint."""
        timestamp = context.state_recorder.run_start_time.replace(":", "-").replace(".", "-")
        checkpoint_id = f"{timestamp}_{state_class.__name__}"
        checkpoint_path = os.path.join(self.checkpoint_dir, f"{checkpoint_id}.json")

        checkpoint_data = {
            "checkpoint_id": checkpoint_id,
            "timestamp": context.state_recorder.run_start_time,
            "current_state": state_class.__name__,
            "context": await self._serialize_context(context)
        }

        with open(checkpoint_path, 'w') as f:
            json.dump(checkpoint_data, f, indent=2)

        if self.console:
            self.console.print(f"[dim]Checkpoint saved: {checkpoint_id}[/dim]")

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
            "dag_edges": [(str(e.source), str(e.target)) for e in context.dag.edges] if context.dag else [],
        }

    async def _deserialize_context(self, context_data: Dict[str, Any]) -> StateMachineContext:
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
            from .states.processing_results_state import ProcessingResultsState
            state_mapping["ProcessingResultsState"] = ProcessingResultsState
        except ImportError:
            pass

        try:
            from .states.terraform_state import TerraformState, TerraformPlanningState
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
                        self.console.print(f"[dim]Cleaned up checkpoint: {filename}[/dim]")
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
                    with open(checkpoint_path, 'r') as f:
                        data = json.load(f)
                        checkpoints.append({
                            "id": data["checkpoint_id"],
                            "timestamp": data["timestamp"],
                            "state": data["current_state"]
                        })
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid checkpoint files
                    
        return sorted(checkpoints, key=lambda x: x["timestamp"], reverse=True)
