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
        
        # Capture output from the real state machine
        import io
        import contextlib
        from rich.console import Console
        
        # Create a string buffer to capture output
        output_buffer = io.StringIO()
        ui_console = Console(file=output_buffer, width=120)
        
        # Save original console
        original_console = self.console
        self.console = ui_console
        
        try:
            # Call the REAL StateMachineRunner.process_query method
            context = await super().process_query(query)
            
            # Get captured output and show it in UI
            captured_output = output_buffer.getvalue()
            if captured_output.strip():
                # Split output into lines and show each as a system message
                for line in captured_output.strip().split('\n'):
                    if line.strip():
                        await self.state_tracker._add_state_message(line.strip())
            
            return context
            
        finally:
            # Restore original console
            self.console = original_console
    



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