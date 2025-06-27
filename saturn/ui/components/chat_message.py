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
        # Disable focus for messages to prevent tab navigation
        self.can_focus = False

    def compose(self) -> ComposeResult:
        # Header with role and timestamp

        if self.role == "user":
            text_area = SaturnTextArea(
                text=self.content,
                read_only=True,
                classes="user-content",
                id="message-content",
            )
            text_area.can_focus = False  # Disable tab focus for message content
            yield text_area
        elif self.role == "assistant":
            yield Static(
                f"[bold green]⟨saturn⟩[/bold green] [dim]{self.timestamp}[/dim]"
            )
            text_area = SaturnTextArea(
                text=self.content,
                read_only=True,
                classes="assistant-content",
                id="message-content",
            )
            text_area.can_focus = False  # Disable tab focus for message content
            yield text_area
        else:
            text_area = SaturnTextArea(
                text=self.content,
                read_only=True,
                classes="system-content",
                id="message-content",
            )
            text_area.can_focus = False  # Disable tab focus for message content
            yield text_area

    def action_copy_message(self) -> None:
        """Copy this message's content directly"""
        try:
            # Import here to avoid circular imports
            import platform
            import subprocess
            
            text_to_copy = self.content
            
            if not text_to_copy.strip():
                self.notify("No text to copy", severity="warning")
                return

            # Use platform-specific clipboard commands
            system = platform.system().lower()
            if system == "darwin":  # macOS
                subprocess.run(["pbcopy"], input=text_to_copy.encode(), check=True)
            elif system == "windows":  # Windows
                subprocess.run(
                    ["clip"], input=text_to_copy.encode(), shell=True, check=True
                )
            elif system == "linux":  # Linux
                try:
                    subprocess.run(
                        ["xclip", "-selection", "clipboard"],
                        input=text_to_copy.encode(),
                        check=True,
                    )
                except FileNotFoundError:
                    subprocess.run(
                        ["xsel", "--clipboard", "--input"],
                        input=text_to_copy.encode(),
                        check=True,
                    )

            self.notify(f"📋 Copied {len(text_to_copy)} characters")

        except Exception as e:
            self.notify(f"❌ Copy failed: {str(e)}", severity="error")

 