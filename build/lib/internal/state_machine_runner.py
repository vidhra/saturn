import asyncio
from typing import Any, Dict, Optional

# Import state components
from .states.base_state import StateMachineContext
from .states.start_state import StartState
from .states.completed_state import CompletedState
from .states.failed_state import FailedState

# Import types for context initialization (replace Any with actual types)
# from saturn.knowledge_base import KnowledgeBase
# from saturn.gcp_executor import GcpExecutor
# from model.llm.base_interface import BaseLLMInterface

class StateMachineRunner:
    """Runs the state machine, managing context and transitions."""

    def __init__(self,
                 llm_interface: Any, # BaseLLMInterface,
                 gcp_executor: Any,  # GcpExecutor,
                 knowledge_base: Any, # KnowledgeBase,
                 system_prompt: str,
                 config: Optional[Dict[str, Any]] = None):
        """Initializes the runner with necessary components."""
        self.llm_interface = llm_interface
        self.gcp_executor = gcp_executor
        self.knowledge_base = knowledge_base
        self.system_prompt = system_prompt
        self.config = config or {}
        self.max_retries = self.config.get('max_retries', 5)

    async def process_query(self, query: str) -> StateMachineContext:
        """
        Processes a given query through the state machine.

        Args:
            query: The user's natural language query.

        Returns:
            The final StateMachineContext after reaching a terminal state.
        """
        print(f"\n=== Starting State Machine for Query ===\nQuery: {query}\n")

        # Initialize the context for this run
        context = StateMachineContext(
            original_query=query,
            llm_interface=self.llm_interface,
            gcp_executor=self.gcp_executor,
            knowledge_base=self.knowledge_base,
            system_prompt=self.system_prompt,
            max_retries=self.max_retries
        )

        current_state_class = StartState

        # Main loop: run until a terminal state is reached
        while current_state_class not in [CompletedState, FailedState]:
            current_state_instance = current_state_class() # Instantiate the state
            
            # Debug: Print state transition
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
                # Optionally update context with this severe error
                context.current_errors.append({
                    "method": f"RUNNER ({current_state_instance!r})",
                    "error": f"Unhandled state execution error: {e}",
                    "arguments": {}
                })

        # Reached a terminal state, run it once for final output/logging
        terminal_state_instance = current_state_class()
        print(f"\n==> Entering Terminal State: {terminal_state_instance!r}")
        # The run method of terminal states should just print/log and return itself
        _, context = await terminal_state_instance.run(context)

        print("\n=== State Machine Finished ===")
        return context

# Example Usage (Illustrative - adapt to your application entry point)
# async def main():
#     # Load config, initialize components (LLM, Executor, KB)
#     config = { 'max_retries': 3, ... }
#     llm = ...
#     executor = ...
#     kb = ...
#     system_prompt = ...

#     runner = StateMachineRunner(llm, executor, kb, system_prompt, config)
#     final_context = await runner.process_query("Your user query here")

#     # Inspect final_context.current_errors or final_context.node_outputs

# if __name__ == '__main__':
#     asyncio.run(main()) 