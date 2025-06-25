#!/usr/bin/env python3
"""
Shared UI Components for Saturn TUI
Modern, reusable components for the terminal interface
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from rich.syntax import Syntax
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal
from textual.reactive import reactive
from textual.widgets import Label, ProgressBar, Static, TextArea

try:
    import pyperclip

    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


class StatusIndicator(Static):
    """Animated status indicator for operations"""

    status = reactive("idle")
    message = reactive("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.animation_index = 0

    def compose(self) -> ComposeResult:
        yield Label("", id="status-icon")
        yield Label("", id="status-text")

    def watch_status(self, status: str) -> None:
        """Update status display"""
        icon_label = self.query_one("#status-icon", Label)

        if status == "idle":
            icon_label.update("⚪")
        elif status == "processing":
            icon_label.update(self.animation_chars[self.animation_index])
            self.animation_index = (self.animation_index + 1) % len(
                self.animation_chars
            )
        elif status == "success":
            icon_label.update("✅")
        elif status == "error":
            icon_label.update("❌")
        elif status == "warning":
            icon_label.update("⚠️")

    def watch_message(self, message: str) -> None:
        """Update status message"""
        text_label = self.query_one("#status-text", Label)
        text_label.update(f"[dim]{message}[/dim]")


class ExecutionProgress(Container):
    """Progress display for execution steps"""

    current_step = reactive(0)
    total_steps = reactive(0)
    step_name = reactive("")

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label("Progress:", classes="progress-label")
            yield ProgressBar(id="main-progress")
        yield Label("", id="step-info")

    def watch_current_step(self, step: int) -> None:
        """Update current step"""
        self.update_progress()

    def watch_total_steps(self, total: int) -> None:
        """Update total steps"""
        self.update_progress()

    def watch_step_name(self, name: str) -> None:
        """Update step name"""
        step_label = self.query_one("#step-info", Label)
        if name:
            step_label.update(f"[dim]{name}[/dim]")
        else:
            step_label.update("")

    def update_progress(self):
        """Update the progress bar"""
        progress_bar = self.query_one("#main-progress", ProgressBar)
        if self.total_steps > 0:
            progress = self.current_step / self.total_steps
            progress_bar.progress = min(progress * 100, 100)


class CodeBlock(Static):
    """Syntax-highlighted code block"""

    def __init__(self, code: str, language: str = "bash", **kwargs):
        super().__init__(**kwargs)
        self.code = code
        self.language = language

    def render(self) -> Syntax:
        """Render syntax-highlighted code"""
        return Syntax(
            self.code,
            self.language,
            theme="monokai",
            line_numbers=True,
            background_color="default",
        )


class LogEntry(Static):
    """Individual log entry with timestamp"""

    def __init__(self, message: str, level: str = "info", **kwargs):
        super().__init__(**kwargs)
        self.message = message
        self.level = level
        self.timestamp = datetime.now().strftime("%H:%M:%S")

    def compose(self) -> ComposeResult:
        timestamp_color = "dim"
        message_color = "white"
        icon = "ℹ️"

        if self.level == "error":
            message_color = "red"
            icon = "❌"
        elif self.level == "warning":
            message_color = "yellow"
            icon = "⚠️"
        elif self.level == "success":
            message_color = "green"
            icon = "✅"
        elif self.level == "debug":
            message_color = "dim"
            icon = "🐛"

        yield Static(
            f"[{timestamp_color}]{self.timestamp}[/{timestamp_color}] "
            f"{icon} [{message_color}]{self.message}[/{message_color}]"
        )


class StateTransition(Static):
    """Display state transitions with visual feedback"""

    current_state = reactive("StartState")
    previous_state = reactive("")
    transition_time = reactive("")

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label("", id="prev-state")
            yield Label("→", classes="arrow")
            yield Label("", id="current-state")
            yield Label("", id="transition-time")

    def watch_current_state(self, state: str) -> None:
        """Update current state display"""
        current_label = self.query_one("#current-state", Label)
        current_label.update(f"[bold cyan]{state}[/bold cyan]")

        prev_label = self.query_one("#prev-state", Label)
        if self.previous_state:
            prev_label.update(f"[dim]{self.previous_state}[/dim]")

    def watch_transition_time(self, time: str) -> None:
        """Update transition timestamp"""
        time_label = self.query_one("#transition-time", Label)
        if time:
            time_label.update(f"[dim]({time})[/dim]")


class MetricsPanel(Container):
    """Display execution metrics and statistics"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metrics: Dict[str, Any] = {}

    def compose(self) -> ComposeResult:
        yield Label("📊 Execution Metrics", classes="panel-title")
        yield Container(id="metrics-content")

    def update_metric(self, key: str, value: Any, unit: str = ""):
        """Update a specific metric"""
        self.metrics[key] = {"value": value, "unit": unit}
        self.refresh_display()

    def refresh_display(self):
        """Refresh the metrics display"""
        content = self.query_one("#metrics-content", Container)
        content.remove_children()

        for key, data in self.metrics.items():
            value = data["value"]
            unit = data["unit"]
            content.mount(
                Static(f"[cyan]{key}:[/cyan] [white]{value}[/white] [dim]{unit}[/dim]")
            )


class CommandHistory(Container):
    """Command history with search and navigation"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history: List[str] = []
        self.current_index = -1

    def add_command(self, command: str):
        """Add a command to history"""
        if command and (not self.history or self.history[-1] != command):
            self.history.append(command)
        self.current_index = -1

    def get_previous(self) -> Optional[str]:
        """Get previous command in history"""
        if self.history and self.current_index < len(self.history) - 1:
            self.current_index += 1
            return self.history[-(self.current_index + 1)]
        return None

    def get_next(self) -> Optional[str]:
        """Get next command in history"""
        if self.current_index > 0:
            self.current_index -= 1
            return self.history[-(self.current_index + 1)]
        elif self.current_index == 0:
            self.current_index = -1
            return ""
        return None

    def clear_history(self):
        """Clear command history"""
        self.history.clear()
        self.current_index = -1


class CopyableTextArea(TextArea):
    """TextArea with copy functionality"""

    BINDINGS = [
        Binding("ctrl+c", "copy_content", "Copy", show=False),
    ]

    def action_copy_content(self) -> None:
        """Copy text content to clipboard"""
        if not CLIPBOARD_AVAILABLE:
            self.notify("Clipboard not available", severity="warning")
            return

        text_to_copy = self.selected_text if self.selected_text else self.text

        try:
            pyperclip.copy(text_to_copy)
            length = len(text_to_copy)
            self.notify(f"Copied {length} characters", title="Copied!")
        except Exception as e:
            self.notify(f"Copy failed: {str(e)}", severity="error")


class MessageWidget(Static):
    """A styled message widget for chat"""

    def __init__(
        self, content: str, role: str, timestamp: Optional[str] = None, **kwargs
    ):
        super().__init__(**kwargs)
        self.content = content
        self.role = role
        self.timestamp = timestamp or datetime.now().strftime("%H:%M:%S")
        self.classes = f"message message-{role}"


class StatusBar(Static):
    """Status bar for showing application state"""

    def __init__(self, **kwargs):
        super().__init__("", classes="status-bar", **kwargs)
        self.current_status = "Ready"

    def set_status(self, status: str, color: str = "white"):
        """Update status with optional color"""
        self.current_status = status
        self.update(f"[{color}]{status}[/{color}]")

    def clear_status(self):
        """Clear the status"""
        self.update("")
        self.current_status = "Ready"


# Export all components
__all__ = [
    "StatusIndicator",
    "ExecutionProgress",
    "CodeBlock",
    "LogEntry",
    "StateTransition",
    "MetricsPanel",
    "CommandHistory",
    "CopyableTextArea",
    "MessageWidget",
    "StatusBar",
]
