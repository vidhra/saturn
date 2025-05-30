import asyncio
from typing import Any, Dict, Optional

from .states.base_state import StateMachineContext
from .states.start_state import StartState
from .states.completed_state import CompletedState
from .states.failed_state import FailedState


class StateMachineRunner:
    """Runs the state machine, managing context and transitions."""

    def __init__(self,
                 llm_interface: Any,
                 gcp_executor: Any,
                 aws_executor: Any,
                 knowledge_base: Any,
                 system_prompt: str,
                 config: Optional[Dict[str, Any]] = None,
                 console: Optional[Any] = None,
                 rag_engine: Optional[Any] = None):
        """Initializes the runner with necessary components."""
        self.llm_interface = llm_interface
        self.gcp_executor = gcp_executor
        self.aws_executor = aws_executor
        self.knowledge_base = knowledge_base
        self.system_prompt = system_prompt
        self.config = config or {}
        self.max_retries = self.config.get('max_retries', 5)
        self.console = console
        self.rag_engine = rag_engine

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
        file_build_executor = FileBuildExecutor({
            'working_directory': self.config.get('working_directory', '.')
        })

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
            file_build_executor=file_build_executor
        )

        current_state_class = StartState

        while current_state_class not in [CompletedState, FailedState]:
            current_state_instance = current_state_class() # Instantiate the state
            
            print(f"\n==> Entering State: {current_state_instance!r}")

            try:
                next_state_class, context = await current_state_instance.run(context)
                current_state_class = next_state_class
            except Exception as e:
                print(f"\n--- UNHANDLED EXCEPTION in state {current_state_instance!r} --- ")
                print(f"Error: {e}")
                import traceback
                traceback.print_exc()
                print("Transitioning directly to FailedState due to unhandled exception.")
                current_state_class = FailedState
                context.current_errors.append({
                    "method": f"RUNNER ({current_state_instance!r})",
                    "error": f"Unhandled state execution error: {e}",
                    "arguments": {}
                })

        terminal_state_instance = current_state_class()
        print(f"\n==> Entering Terminal State: {terminal_state_instance!r}")
        _, context = await terminal_state_instance.run(context)

        print("\n=== State Machine Finished ===")
        
        if context.state_recorder:
            if context.current_errors:
                context.state_recorder.set_final_run_status("FAILED", context.current_errors)
            else:
                context.state_recorder.set_final_run_status("COMPLETED", [])
            context.state_recorder.save_state()
            
        return context

