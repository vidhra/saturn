"""
Input widgets for the Saturn TUI application.
"""

import platform
import subprocess
from dataclasses import dataclass
from typing import TYPE_CHECKING

from textual import on
from textual.binding import Binding
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import TextArea

if TYPE_CHECKING:
    pass

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


class SaturnTextArea(TextArea):
    """Enhanced TextArea with copy functionality"""

    BINDINGS = [
        Binding("ctrl+c,y", "copy_to_clipboard", "Copy", show=False),
    ]

    def action_copy_to_clipboard(self) -> None:
        """Copy selected text or all text to clipboard - works on Windows/Mac/Linux"""
        text_to_copy = self.selected_text if self.selected_text else self.text

        if not text_to_copy.strip():
            self.notify("No text to copy", severity="warning")
            return

        try:
            if CLIPBOARD_AVAILABLE:
                # Use pyperclip if available
                pyperclip.copy(text_to_copy)
                self.notify(f"📋 Copied {len(text_to_copy)} characters")
            else:
                # Fallback to platform-specific clipboard commands
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


class SaturnPromptInput(TextArea):
    """Saturn's input widget based on PromptInput"""

    @dataclass
    class PromptSubmitted(Message):
        text: str
        prompt_input: "SaturnPromptInput"

    BINDINGS = [
        Binding("enter", "submit_prompt", "Send message", key_display="⏎"),
    ]

    submit_ready = reactive(True)

    def __init__(self, **kwargs):
        super().__init__(text="", language=None, **kwargs)

    def on_mount(self):
        self.border_title = "Enter your message..."

    @on(TextArea.Changed)
    async def prompt_changed(self, event: TextArea.Changed) -> None:
        text_area = event.text_area
        if text_area.text.strip() != "":
            text_area.border_subtitle = "[white]⏎[/white] Send message"
        else:
            text_area.border_subtitle = None

        text_area.set_class(text_area.wrapped_document.height > 1, "multiline")

    async def on_key(self, event) -> None:
        """Handle key events for submit shortcuts."""
        if event.key == "enter":
            # Enter: Submit message
            event.stop()
            self.action_submit_prompt()
            return

    def action_submit_prompt(self) -> None:
        if self.text.strip() == "":
            self.notify("Cannot send empty message!")
            return

        if self.submit_ready:
            message = self.PromptSubmitted(self.text, prompt_input=self)
            self.clear()
            self.post_message(message)
        else:
            self.app.bell()
            self.notify("Please wait for response to complete.") 