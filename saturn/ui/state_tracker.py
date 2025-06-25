"""
Saturn State Machine Tracker for UI Integration

This module provides real-time state tracking for Saturn's state machine,
integrating with the actual state classes to provide meaningful progress updates.
"""

import asyncio
from typing import Optional, Callable, Any, Dict
import re

# Import actual state classes to get their descriptions
from internal.states.start_state import StartState
from internal.states.reasoning_state import ReasoningState
from internal.states.planning_state import PlanningState
from internal.states.executing_state import ExecutingState
from internal.states.processing_results_state import ProcessingResultsState
from internal.states.completed_state import CompletedState
from internal.states.failed_state import FailedState
from internal.states.terraform_state import TerraformState
from internal.states.error_handling_state import ErrorHandlingState

# Import the actual StateMachineRunner
from internal.state_machine_runner import StateMachineRunner


class SaturnStateTracker:
    """State machine tracker that loads descriptions from actual Saturn state classes"""
    
    def __init__(self, chat_app):
        self.chat_app = chat_app
        self.current_state = None
        
        # Load state descriptions from actual classes
        self.state_classes = {
            "StartState": StartState,
            "ReasoningState": ReasoningState, 
            "PlanningState": PlanningState,
            "ExecutingState": ExecutingState,
            "ProcessingResultsState": ProcessingResultsState,
            "CompletedState": CompletedState,
            "FailedState": FailedState,
            "TerraformState": TerraformState,
            "ErrorHandlingState": ErrorHandlingState,
        }
        
        # Curated descriptions for UI display
        self.state_descriptions = {
            "StartState": "Initializing Saturn AI Assistant",
            "ReasoningState": "Analyzing request and understanding intent", 
            "PlanningState": "Creating execution plan and selecting tools",
            "ExecutingState": "Executing operations on cloud infrastructure",
            "ProcessingResultsState": "Processing results and validating operations",
            "TerraformState": "Managing infrastructure with Terraform",
            "CompletedState": "Operations completed successfully",
            "FailedState": "Operations failed",
            "ErrorHandlingState": "Handling errors and retrying operations",
        }
        
        # Sub-operations for detailed progress
        self.sub_operations = {
            "ReasoningState": [
                "Parsing user query and extracting intent",
                "Analyzing context and requirements", 
                "Determining required cloud operations"
            ],
            "PlanningState": [
                "Discovering available tools and services",
                "Building execution DAG", 
                "Optimizing execution plan"
            ],
            "ExecutingState": [
                "Authenticating with cloud providers",
                "Checking current infrastructure state",
                "Executing planned operations"
            ],
            "ProcessingResultsState": [
                "Collecting operation results",
                "Validating success criteria",
                "Preparing response"
            ]
        }
    
    async def on_state_enter(self, state_name: str, context=None):
        """Called when entering a new state"""
        self.current_state = state_name
        description = self.state_descriptions.get(state_name, f"Processing {state_name}")
        await self._add_state_message(f"➤ {description}")
        
        # Show sub-operations for detailed states
        if state_name in self.sub_operations:
            for sub_op in self.sub_operations[state_name]:
                await asyncio.sleep(0.8)  # Realistic timing
                await self._add_state_message(f"  └─ {sub_op}")
    
    async def on_operation(self, operation: str, context=None):
        """Called for specific operations within states"""
        await self._add_state_message(f"  └─ {operation}")
    
    async def on_error(self, error: str, context=None):
        """Called when an error occurs"""
        await self._add_state_message(f"⚠ Error: {error}")
    
    async def on_checkpoint_saved(self, checkpoint_id: str):
        """Called when a checkpoint is saved"""
        await self._add_state_message(f"💾 Checkpoint saved: {checkpoint_id}")
    
    async def on_cache_operation(self, operation: str, details: str = ""):
        """Called for cache operations"""
        if details:
            await self._add_state_message(f"🗃️ {operation}: {details}")
        else:
            await self._add_state_message(f"🗃️ {operation}")
    
    async def _add_state_message(self, text: str):
        """Add a state update message to the chat"""
        # Use the chat_app's method to avoid circular imports
        self.chat_app.add_system_message(text)


class UIAwareStateMachineRunner(StateMachineRunner):
    """Extended StateMachineRunner that provides UI callbacks for real-time tracking"""
    
    def __init__(self, state_tracker: SaturnStateTracker, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_tracker = state_tracker
        self.original_print = print
        
    async def process_query(self, query: str):
        """Override process_query to provide real-time UI updates"""
        await self.state_tracker._add_state_message(f"🚀 Starting Saturn for: {query}")
        
        # Call the original process_query but with UI callbacks
        return await self._process_query_with_ui_callbacks(query)
    
    async def _process_query_with_ui_callbacks(self, query: str):
        """Process query with UI state callbacks"""
        try:
            # Import required modules
            from internal.state_recorder import RunStateLogger
            from saturn.file_executor import FileBuildExecutor
            from internal.states.base_state import StateMachineContext
            
            # Initialize components
            state_recorder = RunStateLogger(query)
            file_build_executor = FileBuildExecutor(
                {"working_directory": self.config.get("working_directory", ".")}
            )
            
            # Create context
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
            
            # Pass runner instance to context
            context._state_machine_runner = self
            
            current_state_class = StartState
            
            # Main state machine loop with UI callbacks
            while current_state_class not in [CompletedState, FailedState]:
                current_state_instance = current_state_class()
                state_name = current_state_instance.__class__.__name__
                
                # Notify UI of state entry
                await self.state_tracker.on_state_enter(state_name, context)
                
                # Handle checkpointing
                enable_checkpoints = self.config.get("enable_checkpoints", False)
                if enable_checkpoints:
                    checkpoint_id = await self._save_checkpoint(context, current_state_class)
                    await self.state_tracker.on_checkpoint_saved(checkpoint_id)
                
                try:
                    # Execute state
                    next_state_class, context = await current_state_instance.run(context)
                    current_state_class = next_state_class
                    
                except Exception as e:
                    await self.state_tracker.on_error(f"Unhandled exception in {state_name}: {str(e)}")
                    current_state_class = FailedState
                    context.current_errors.append({
                        "method": f"RUNNER ({current_state_instance!r})",
                        "error": f"Unhandled state execution error: {e}",
                        "arguments": {},
                    })
            
            # Execute terminal state
            terminal_state_instance = current_state_class()
            terminal_state_name = terminal_state_instance.__class__.__name__
            await self.state_tracker.on_state_enter(terminal_state_name, context)
            
            _, context = await terminal_state_instance.run(context)
            
            # Finalize state recorder
            if context.state_recorder:
                if context.current_errors:
                    context.state_recorder.set_final_run_status("FAILED", context.current_errors)
                else:
                    context.state_recorder.set_final_run_status("COMPLETED", [])
                context.state_recorder.save_state()
            
            # Show cache statistics
            cache_stats = self.tool_cache.get_cache_stats()
            await self.state_tracker.on_cache_operation(
                "Cache Statistics",
                f"{cache_stats['file_tools_cached']} file tools, {cache_stats['mcp_tools_cached']} MCP tools cached"
            )
            
            # Cleanup checkpoints
            enable_checkpoints = self.config.get("enable_checkpoints", False)
            if enable_checkpoints:
                await self._cleanup_checkpoints(context.state_recorder.run_start_time)
            
            return context
            
        except Exception as e:
            await self.state_tracker.on_error(f"Critical error in state machine: {str(e)}")
            raise


class MockStateRunner:
    """Mock state runner for demonstration purposes until real integration"""
    
    def __init__(self, state_tracker: SaturnStateTracker):
        self.tracker = state_tracker
    
    async def run_demo_progression(self):
        """Run a demonstration of state progression"""
        # Start state
        await self.tracker.on_state_enter("StartState")
        await asyncio.sleep(1.0)
        
        # Reasoning state with sub-operations
        await self.tracker.on_state_enter("ReasoningState")
        await asyncio.sleep(1.5)
        
        # Planning state with sub-operations  
        await self.tracker.on_state_enter("PlanningState")
        await asyncio.sleep(1.5)
        
        # Executing state with sub-operations
        await self.tracker.on_state_enter("ExecutingState")
        await asyncio.sleep(1.5)
        
        # Processing results
        await self.tracker.on_state_enter("ProcessingResultsState")
        await asyncio.sleep(1.0)
        
        # Complete
        await self.tracker.on_state_enter("CompletedState")


async def create_ui_aware_runner(
    state_tracker: SaturnStateTracker,
    llm_interface: Any,
    gcp_executor: Any,
    aws_executor: Any,
    knowledge_base: Any,
    system_prompt: str,
    config: Dict[str, Any],
    console: Any = None,
    rag_engine: Any = None,
    mcp_integrator: Any = None,
) -> UIAwareStateMachineRunner:
    """Factory function to create a UI-aware state machine runner"""
    return UIAwareStateMachineRunner(
        state_tracker=state_tracker,
        llm_interface=llm_interface,
        gcp_executor=gcp_executor,
        aws_executor=aws_executor,
        knowledge_base=knowledge_base,
        system_prompt=system_prompt,
        config=config,
        console=console,
        rag_engine=rag_engine,
        mcp_integrator=mcp_integrator,
    )


def get_state_class_info(state_name: str) -> dict:
    """Get information about a specific state class"""
    state_classes = {
        "StartState": StartState,
        "ReasoningState": ReasoningState, 
        "PlanningState": PlanningState,
        "ExecutingState": ExecutingState,
        "ProcessingResultsState": ProcessingResultsState,
        "CompletedState": CompletedState,
        "FailedState": FailedState,
        "TerraformState": TerraformState,
        "ErrorHandlingState": ErrorHandlingState,
    }
    
    state_class = state_classes.get(state_name)
    if not state_class:
        return {"name": state_name, "docstring": "Unknown state"}
    
    return {
        "name": state_name,
        "class": state_class,
        "docstring": state_class.__doc__ or "No documentation available",
        "module": state_class.__module__,
    } 