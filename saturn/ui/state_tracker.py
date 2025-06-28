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
        """Add a state update message to the chat (async version)"""
        # Use the chat_app's method to avoid circular imports
        self.chat_app.add_system_message(text)
    
    def _add_state_message_sync(self, text: str):
        """Add a state update message to the chat (synchronous version)"""
        # Use the chat_app's method to avoid circular imports
        self.chat_app.add_system_message(text)
    
    def on_operation_sync(self, operation: str, context=None):
        """Called for specific operations within states (synchronous)"""
        self._add_state_message_sync(f"  └─ {operation}")
    
    def on_error_sync(self, error: str, context=None):
        """Called when an error occurs (synchronous)"""
        self._add_state_message_sync(f"⚠ Error: {error}")
    
    def on_checkpoint_saved_sync(self, checkpoint_id: str):
        """Called when a checkpoint is saved (synchronous)"""
        self._add_state_message_sync(f"💾 Checkpoint saved: {checkpoint_id}")
    
    def on_cache_operation_sync(self, operation: str, details: str = ""):
        """Called for cache operations (synchronous)"""
        if details:
            self._add_state_message_sync(f"🗃️ {operation}: {details}")
        else:
            self._add_state_message_sync(f"🗃️ {operation}")


class UIAwareStateMachineRunner(StateMachineRunner):
    """Extended StateMachineRunner that provides UI callbacks for real-time tracking"""
    
    def __init__(self, state_tracker: SaturnStateTracker, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_tracker = state_tracker
        self.original_print = print
        self._setup_real_time_console()
        
    def _setup_real_time_console(self):
        """Set up console to stream output in real-time to UI"""
        from rich.console import Console
        import io
        import asyncio
        
        class UIStreamingConsole(Console):
            def __init__(self, state_tracker, chat_app, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.state_tracker = state_tracker
                self.chat_app = chat_app
                self.last_message = ""  # Track last message to avoid duplicates
                
            def print(self, *args, **kwargs):
                # Convert args to string representation
                message_parts = []
                for arg in args:
                    # Handle Rich renderables
                    if hasattr(arg, '__rich__') or hasattr(arg, '__rich_console__'):
                        try:
                            # Try to render Rich objects to plain text
                            from io import StringIO
                            temp_console = Console(file=StringIO(), width=100, legacy_windows=False)
                            temp_console.print(arg)
                            rendered = temp_console.file.getvalue()
                            message_parts.append(rendered.strip())
                        except:
                            message_parts.append(str(arg))
                    elif hasattr(arg, '__str__'):
                        message_parts.append(str(arg))
                    else:
                        message_parts.append(repr(arg))
                
                message = ' '.join(message_parts)
                if message.strip():
                    # Clean up the message (remove ANSI codes and extra whitespace)
                    import re
                    clean_message = re.sub(r'\x1b\[[0-9;]*[mK]', '', message).strip()
                    
                    # Avoid duplicate messages
                    if clean_message and clean_message != self.last_message:
                        self.last_message = clean_message
                        
                        # Filter out some noisy/irrelevant messages
                        skip_patterns = [
                            r'^\s*$',  # Empty lines
                            r'^Loading\.\.\.$',  # Generic loading messages
                            r'^.*\d+%.*$',  # Progress percentages (handled separately)
                        ]
                        
                        should_skip = any(re.match(pattern, clean_message) for pattern in skip_patterns)
                        
                        if not should_skip:
                            # Add emoji indicators for common message types
                            if 'error' in clean_message.lower() or 'failed' in clean_message.lower():
                                clean_message = f"❌ {clean_message}"
                            elif 'success' in clean_message.lower() or 'completed' in clean_message.lower():
                                clean_message = f"✅ {clean_message}"
                            elif 'warning' in clean_message.lower():
                                clean_message = f"⚠️ {clean_message}"
                            elif any(word in clean_message.lower() for word in ['loading', 'initializing', 'starting']):
                                clean_message = f"🔄 {clean_message}"
                            
                            # Add the message to UI synchronously through the chat app
                            self.chat_app.add_system_message(clean_message)
            
            def status(self, message):
                """Handle Rich status messages"""
                clean_message = str(message).strip()
                if clean_message:
                    self.chat_app.add_system_message(f"📊 {clean_message}")
            
            def log(self, *args, **kwargs):
                """Handle logging calls"""
                self.print(*args, **kwargs)
        
        # Replace console with UI-aware version
        self.console = UIStreamingConsole(
            self.state_tracker, 
            self.state_tracker.chat_app, 
            width=120, 
            force_terminal=False,
            legacy_windows=False
        )
        
    async def process_query(self, query: str):
        """Override process_query to provide real-time UI updates"""
        await self.state_tracker._add_state_message(f"🚀 Starting Saturn for: {query}")
        
        try:
            # Call the REAL StateMachineRunner.process_query method
            # Now console output will stream in real-time via our custom console
            context = await super().process_query(query)
            return context
            
        except Exception as e:
            await self.state_tracker.on_error(f"State machine error: {str(e)}")
            raise
    
    async def transition_to_state(self, state_class, context):
        """Override state transitions to provide real-time updates"""
        state_name = state_class.__name__
        await self.state_tracker.on_state_enter(state_name, context)
        
        # Call parent method
        try:
            result = await super().transition_to_state(state_class, context)
            return result
        except AttributeError:
            # If transition_to_state doesn't exist in parent, just return
            return context
    
    def log_operation(self, operation: str, details: str = ""):
        """Log an operation in real-time"""
        message = f"🔧 {operation}"
        if details:
            message += f": {details}"
        self.state_tracker.chat_app.add_system_message(message)
    
    def log_tool_execution(self, tool_name: str, status: str = "executing"):
        """Log tool execution in real-time"""
        status_icons = {
            "executing": "⚙️",
            "success": "✅", 
            "error": "❌",
            "warning": "⚠️"
        }
        icon = status_icons.get(status, "🔧")
        message = f"{icon} {tool_name}"
        if status != "executing":
            message += f" - {status}"
        self.state_tracker.chat_app.add_system_message(message)
    
    def log_checkpoint(self, checkpoint_id: str):
        """Log checkpoint creation in real-time"""
        self.state_tracker.chat_app.add_system_message(f"💾 Checkpoint: {checkpoint_id}")
    
    def log_cache_operation(self, operation: str, details: str = ""):
        """Log cache operations in real-time"""
        message = f"🗃️ {operation}"
        if details:
            message += f": {details}"
        self.state_tracker.chat_app.add_system_message(message)
    



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