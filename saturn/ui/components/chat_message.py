"""
Chat message components for the Saturn TUI application.
"""

from datetime import datetime
from typing import Optional

from textual.app import ComposeResult
from textual.binding import Binding
from textual.widgets import Static

from .input_widgets import SaturnTextArea


class ChatMessage(Static):
    """Individual chat message like Chatbox"""

    BINDINGS = [
        Binding("ctrl+c,y", "copy_message", "Copy message", show=False),
    ]

    def __init__(
        self, content: str, role: str, timestamp: Optional[str] = None, **kwargs
    ):
        super().__init__(**kwargs)
        self.content = content
        self.role = role
        self.timestamp = timestamp or datetime.now().strftime("%H:%M:%S")
        # Make messages focusable
        self.can_focus = True

    def compose(self) -> ComposeResult:
        # Header with role and timestamp

        if self.role == "user":
            yield SaturnTextArea(
                text=self.content,
                read_only=True,
                classes="user-content",
                id="message-content",
            )
        elif self.role == "assistant":
            yield Static(
                f"[bold green]⟨saturn⟩[/bold green] [dim]{self.timestamp}[/dim]"
            )
            yield SaturnTextArea(
                text=self.content,
                read_only=True,
                classes="assistant-content",
                id="message-content",
            )
        else:
            yield SaturnTextArea(
                text=self.content,
                read_only=True,
                classes="system-content",
                id="message-content",
            )

    def action_copy_message(self) -> None:
        """Copy this message's content using the existing SaturnTextArea copy functionality"""
        try:
            # Get the SaturnTextArea that contains the message content
            content_area = self.query_one("#message-content", SaturnTextArea)
            # Use the existing copy functionality
            content_area.action_copy_to_clipboard()
        except Exception as e:
            self.notify(f"❌ Copy failed: {str(e)}", severity="error")

    def on_focus(self) -> None:
        """Visual feedback when message is focused"""
        self.add_class("focused-message")

    def on_blur(self) -> None:
        """Remove visual feedback when message loses focus"""
        self.remove_class("focused-message") 