#!/usr/bin/env python3
"""
State Machine Integration for Saturn TUI
Provides real-time feedback from state machine execution to the UI
"""

import sys
from io import StringIO
from typing import Any, Callable, Dict, Optional

from rich.console import Console


class StateMachineUIBridge:
    """
    Bridge between the state machine and the TUI for real-time feedback.
    Captures state transitions and execution progress.
    """

    def __init__(
        self,
        state_callback: Callable[[str, str, str], None],
        status_callback: Callable[[str, Optional[float]], None],
        trace_callback: Callable[[str], None],
    ):
        """
        Initialize the bridge with UI callback functions.

        Args:
            state_callback: Function to update state display (state, progress, step)
            status_callback: Function to update execution status (status, progress)
            trace_callback: Function to add trace entries
        """
        self.state_callback = state_callback
        self.status_callback = status_callback
        self.trace_callback = trace_callback

        self.captured_output = StringIO()
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

        # State tracking
        self.current_state = "Idle"
        self.step_counter = 0
        self.total_steps = 0

    def start_capture(self):
        """Start capturing output for real-time feedback"""
        sys.stdout = self.captured_output
        sys.stderr = self.captured_output

    def stop_capture(self):
        """Stop capturing output and restore original streams"""
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

    def process_output(self, text: str):
        """
        Process captured output and extract state information for UI updates.
        This is where we parse state machine output and convert it to UI updates.
        """
        lines = text.split("\n")

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Add to trace
            self.trace_callback(line)

            # Parse state transitions
            if "==> Entering State:" in line:
                state_name = line.split(":")[-1].strip()
                self.current_state = state_name
                self.state_callback(state_name, "Active", "")

                # Update status based on state
                if "ReasoningState" in state_name:
                    self.status_callback("Analyzing your request...", 0.1)
                elif "PlanningState" in state_name:
                    self.status_callback("Creating execution plan...", 0.3)
                elif "ExecutingState" in state_name:
                    self.status_callback("Executing operations...", 0.5)
                elif "ProcessingResultsState" in state_name:
                    self.status_callback("Processing results...", 0.8)
                elif "CompletedState" in state_name:
                    self.status_callback("Operations completed successfully", 1.0)
                elif "FailedState" in state_name:
                    self.status_callback("❌ Operations failed", 0.0)

            # Parse reasoning steps
            elif "🤔" in line or "🔍" in line or "🎯" in line or "🏗️" in line:
                self.state_callback(self.current_state, line, "")
                self.status_callback(f"💭 {line}", 0.2)

            # Parse planning progress
            elif "Generating execution plan" in line:
                self.status_callback("📝 Generating execution plan...", 0.35)

            elif "plan generated successfully" in line:
                self.status_callback("✅ Execution plan ready", 0.4)

            # Parse execution progress
            elif "Executing step" in line:
                if "step" in line.lower():
                    try:
                        # Extract step info
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if "step" in part.lower() and i + 1 < len(parts):
                                step_info = " ".join(parts[i : i + 3])
                                self.status_callback(f"⚡ {step_info}", 0.6)
                                break
                    except:
                        self.status_callback("⚡ Executing operation...", 0.6)

            # Parse completion indicators
            elif "completed successfully" in line.lower():
                self.status_callback("✅ Operation completed", 0.9)

            elif "failed" in line.lower() and "error" in line.lower():
                self.status_callback("❌ Operation failed", 0.0)

            # Parse step counting
            elif "Step" in line and "/" in line:
                try:
                    # Extract step progress (e.g., "Step 2/5")
                    step_part = [part for part in line.split() if "/" in part][0]
                    current, total = map(int, step_part.split("/"))
                    progress = current / total * 0.8  # Reserve 0.8-1.0 for completion
                    self.status_callback(f"📋 Step {current} of {total}", progress)
                except:
                    pass


class ConsoleCapture:
    """
    Console wrapper that captures output while preserving Rich formatting.
    """

    def __init__(self, bridge: StateMachineUIBridge):
        self.bridge = bridge
        self.console = Console(file=StringIO(), force_terminal=True)

    def print(self, *args, **kwargs):
        """Capture print output and forward to bridge"""
        text = " ".join(str(arg) for arg in args)
        self.bridge.process_output(text)

    def __getattr__(self, name):
        """Delegate other console methods to the internal console"""
        return getattr(self.console, name)


async def run_with_ui_feedback(
    query_processor, bridge: StateMachineUIBridge, *args, **kwargs
):
    """
    Run a query processor with UI feedback integration.

    Args:
        query_processor: Async function that processes the query
        bridge: StateMachineUIBridge instance
        *args, **kwargs: Arguments to pass to query_processor
    """

    # Create console wrapper
    console_wrapper = ConsoleCapture(bridge)

    # Replace console in kwargs if present
    if "console" in kwargs:
        kwargs["console"] = console_wrapper

    try:
        # Start output capture
        bridge.start_capture()

        # Initialize status
        bridge.status_callback("🚀 Initializing Saturn...", 0.05)

        # Run the query processor
        result = await query_processor(*args, **kwargs)

        # Final status update
        bridge.status_callback("✅ Query processed successfully", 1.0)

        return result

    except Exception as e:
        bridge.status_callback(f"❌ Error: {str(e)}", 0.0)
        bridge.trace_callback(f"ERROR: {str(e)}")
        raise

    finally:
        # Stop output capture
        bridge.stop_capture()


class RealTimeStateMachineRunner:
    """
    Enhanced state machine runner that provides real-time UI feedback.
    """

    def __init__(
        self,
        state_callback: Callable[[str, str, str], None],
        status_callback: Callable[[str, Optional[float]], None],
        trace_callback: Callable[[str], None],
    ):

        self.bridge = StateMachineUIBridge(
            state_callback, status_callback, trace_callback
        )

    async def run_query(self, query: str, config: Dict[str, Any], rag_engine: Any):
        """
        Run a query with real-time UI feedback.

        Args:
            query: User query string
            config: Saturn configuration
            rag_engine: RAG engine instance

        Returns:
            Query result
        """
        from saturn.orchestrator import run_query_with_state_machine

        return await run_with_ui_feedback(
            run_query_with_state_machine,
            self.bridge,
            query=query,
            config=config,
            rag_engine=rag_engine,
            max_total_attempts=3,
            verbose=False,
        )

    async def run_chat_query(self, query: str, config: Dict[str, Any]):
        """
        Run a chat query with real-time UI feedback.

        Args:
            query: User query string
            config: Saturn configuration

        Returns:
            Async generator of (role, message) tuples
        """
        from saturn.orchestrator import run_chat_conversational

        async def single_query_generator():
            yield query

        async for role, message in run_chat_conversational(
            config, single_query_generator()
        ):
            yield role, message
