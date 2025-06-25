import asyncio
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, VerticalScroll
from textual.message import Message
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual.widgets import Footer, Static, TextArea

try:
    import pyperclip

    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

from saturn.config import load_config
from saturn.orchestrator import run_chat_conversational


class SaturnPromptInput(TextArea):
    """Saturn's input widget based on Elia's PromptInput"""

    @dataclass
    class PromptSubmitted(Message):
        text: str
        prompt_input: "SaturnPromptInput"

    BINDINGS = [
        Binding(
            "ctrl+j,alt+enter,ctrl+enter",
            "submit_prompt",
            "Send message",
            key_display="^j",
        )
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
            text_area.border_subtitle = "[white]^j[/white] Send message"
        else:
            text_area.border_subtitle = None

        text_area.set_class(text_area.wrapped_document.height > 1, "multiline")

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


class SaturnTextArea(TextArea):
    """Enhanced TextArea with copy functionality like Elia's"""

    BINDINGS = [
        Binding("ctrl+c,y", "copy_to_clipboard", "Copy", show=False),
    ]

    def action_copy_to_clipboard(self) -> None:
        """Copy selected text or all text to clipboard"""
        if not CLIPBOARD_AVAILABLE:
            self.notify("Clipboard not available", severity="warning")
            return

        text_to_copy = self.selected_text if self.selected_text else self.text

        try:
            pyperclip.copy(text_to_copy)
            self.notify(f"Copied {len(text_to_copy)} characters", title="Copied!")
        except Exception as e:
            self.notify(f"Copy failed: {str(e)}", severity="error")


class ChatMessage(Static):
    """Individual chat message like Elia's Chatbox"""

    def __init__(
        self, content: str, role: str, timestamp: Optional[str] = None, **kwargs
    ):
        super().__init__(**kwargs)
        self.content = content
        self.role = role
        self.timestamp = timestamp or datetime.now().strftime("%H:%M:%S")

    def compose(self) -> ComposeResult:
        # Header with role and timestamp
        if self.role == "user":
            yield Static(f"[bold white]❯[/bold white] [dim]{self.timestamp}[/dim]")
            yield Static(self.content, classes="user-content")
        elif self.role == "assistant":
            yield Static(
                f"[bold green]⟨saturn⟩[/bold green] [dim]{self.timestamp}[/dim]"
            )
            yield SaturnTextArea(
                text=self.content, read_only=True, classes="assistant-content"
            )
        else:
            yield Static(f"[dim yellow]⚠[/dim yellow] [dim]{self.timestamp}[/dim]")
            yield Static(self.content, classes="system-content")


class ThinkingIndicator(Static):
    """Real-time thinking display like Elia's ResponseStatus"""

    def __init__(self, **kwargs):
        super().__init__("", **kwargs)
        self.visible = False
        self.thinking_states = [
            "⠋ Analyzing query...",
            "⠙ Planning approach...",
            "⠹ Executing operations...",
            "⠸ Processing results...",
            "⠼ Finalizing response...",
        ]
        self.current_state = 0

    def start_thinking(self, message: str = ""):
        """Start the thinking animation"""
        self.visible = True
        self.display = True
        if message:
            self.update(f"[dim yellow]{message}[/dim yellow]")
        else:
            self._animate_thinking()

    def _animate_thinking(self):
        """Animate the thinking display"""
        if not self.visible:
            return

        state = self.thinking_states[self.current_state % len(self.thinking_states)]
        self.update(f"[dim yellow]{state}[/dim yellow]")
        self.current_state += 1

        # Schedule next animation
        self.set_timer(0.1, self._animate_thinking)

    def stop_thinking(self):
        """Stop thinking and hide"""
        self.visible = False
        self.display = False
        self.update("")


class HelpScreen(ModalScreen):
    """Professional help modal like Elia's"""

    BINDINGS = [
        Binding("escape", "dismiss", "Close"),
        Binding("q", "dismiss", "Close"),
    ]

    def compose(self) -> ComposeResult:
        with Container(classes="help-modal"):
            yield Static("Saturn AI Assistant", classes="help-title")
            yield Static(
                """Commands:
• Ctrl+J / Alt+Enter: Send message
• Ctrl+L: Clear conversation  
• F1: Help • Ctrl+C: Quit

Features:
• Real-time execution feedback
• Multi-line input support
• Copy/paste support
• Markdown rendering

Cloud Operations:
• AWS, GCP, Azure automation
• Infrastructure as Code
• Terraform, CloudFormation
• Monitoring & troubleshooting

Press ESC to close
            """,
                classes="help-content",
            )


class SaturnApp(App):
    """Saturn Chat Application based on Elia's proven architecture"""

    CSS = """
    Screen {
        background: #0d1117;
        color: #f0f6fc;
    }
    
    #chat-container {
        height: 1fr;
        background: #0d1117;
        padding: 0 1;
        margin-bottom: 1;
    }
    
    #thinking {
        dock: top;
        height: 1;
        background: #161b22;
        padding: 0 1;
        margin: 0;
    }
    
    .user-content {
        color: #ffffff;
        background: #0969da;
        margin: 0 0 1 2;
        padding: 1;
    }
    
    .assistant-content {
        background: #161b22;
        border: solid #21262d;
        margin: 0 0 1 2;
        padding: 1;
        min-height: 3;
    }
    
    .system-content {
        color: #888888;
        background: #0f0f0f;
        margin: 0 0 1 2;
        padding: 0 1;
        text-style: italic;
    }
    
    SaturnPromptInput {
        dock: bottom;
        height: auto;
        max-height: 30%;
        background: #161b22;
        border: solid #21262d;
        margin: 1;
    }
    
    SaturnPromptInput:focus {
        border: solid #58a6ff;
    }
    
    .help-modal {
        width: 50;
        height: 20;
        background: #161b22;
        border: solid #21262d;
        padding: 2;
    }
    
    .help-title {
        text-align: center;
        text-style: bold;
        color: #58a6ff;
        margin-bottom: 1;
    }
    
    .help-content {
        color: #f0f6fc;
    }
    
    Footer {
        background: #161b22;
        color: #7d8590;
    }
    """

    TITLE = "Saturn"
    SUB_TITLE = "AI Assistant"

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit"),
        Binding("ctrl+l", "clear_chat", "Clear"),
        Binding("f1", "help", "Help"),
    ]

    def __init__(self):
        super().__init__()
        self.config = load_config()
        self._setup_config()
        self.conversation_active = False

    def _setup_config(self):
        """Setup configuration similar to CLI preprocessing"""
        import os

        # Convert vector_store to vector_store_choice (like CLI does)
        vector_store = self.config.get("vector_store", "chroma")
        self.config["vector_store_choice"] = vector_store.lower()

        # Set up other required config keys
        self.config["rag_build_on_init"] = (
            True if self.config["vector_store_choice"] == "default" else False
        )

        # Set up database configuration
        from saturn.rag_engine import build_provider_db_config

        cloud_provider = "gcp"  # Default for TUI

        if self.config["vector_store_choice"] == "chroma":
            db_configuration = build_provider_db_config(
                self.config, cloud_provider.lower(), "chroma"
            )
        elif self.config["vector_store_choice"] == "duckdb":
            db_configuration = build_provider_db_config(
                self.config, cloud_provider.lower(), "duckdb"
            )
        else:
            db_configuration = None

        self.config["db_config"] = db_configuration

        # Set up RAG docs path for init
        self.config["rag_docs_path_for_init"] = self.config.get(
            "rag_docs_path",
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "internal",
                "tools",
                "gcloud_online_docs_markdown",
            ),
        )

    def compose(self) -> ComposeResult:
        # Thinking indicator (hidden by default)
        yield ThinkingIndicator(id="thinking")

        # Main chat area
        with VerticalScroll(id="chat-container") as container:
            container.can_focus = False

        # Input area (like Elia's PromptInput)
        yield SaturnPromptInput(id="prompt")

        # Footer
        yield Footer()

    async def on_mount(self) -> None:
        """Initialize the app like Elia's chat screen"""
        # Welcome message
        await self.add_system_message("Saturn AI Assistant ready")

        # Focus input (Elia's AUTO_FOCUS pattern)
        self.query_one("#prompt").focus()

    @property
    def chat_container(self) -> VerticalScroll:
        """Get chat container like Elia"""
        return self.query_one("#chat-container", VerticalScroll)

    def scroll_to_latest_message(self):
        """Scroll to latest message like Elia"""
        container = self.chat_container
        container.refresh()
        container.scroll_end(animate=False, force=True)

    @on(SaturnPromptInput.PromptSubmitted)
    async def user_message_submitted(
        self, event: SaturnPromptInput.PromptSubmitted
    ) -> None:
        """Handle user message submission like Elia's pattern"""
        user_message = event.text

        # Add user message
        await self.add_user_message(user_message)

        # Start thinking indicator
        thinking = self.query_one("#thinking", ThinkingIndicator)
        thinking.start_thinking("Analyzing DevOps requirements...")

        # Disable further input
        event.prompt_input.submit_ready = False

        # Start conversation
        if not self.conversation_active:
            self.conversation_active = True
            self.stream_agent_response(user_message)

    @work(thread=False)
    async def stream_agent_response(self, user_query: str) -> None:
        """Stream agent response like Elia's pattern"""
        try:
            thinking = self.query_one("#thinking", ThinkingIndicator)

            # Show different thinking states
            thinking.start_thinking("Planning infrastructure operations...")
            await asyncio.sleep(0.3)

            thinking.start_thinking("Executing cloud automation...")

            # Create async generator for orchestrator
            async def simple_generator():
                yield user_query

            # Run the orchestrator
            async for role, message in run_chat_conversational(
                self.config, simple_generator()
            ):
                if role == "assistant":
                    thinking.stop_thinking()
                    await self.add_assistant_message(message)
                    break

        except Exception as e:
            thinking = self.query_one("#thinking", ThinkingIndicator)
            thinking.stop_thinking()
            await self.add_system_message(f"Error: {str(e)}")
        finally:
            # Re-enable input like Elia
            prompt = self.query_one("#prompt", SaturnPromptInput)
            prompt.submit_ready = True
            self.conversation_active = False

    async def add_user_message(self, content: str) -> None:
        """Add user message like Elia's pattern"""
        message = ChatMessage(content, "user")
        await self.chat_container.mount(message)
        self.scroll_to_latest_message()

    async def add_assistant_message(self, content: str) -> None:
        """Add assistant message like Elia's pattern"""
        message = ChatMessage(content, "assistant")
        await self.chat_container.mount(message)
        self.scroll_to_latest_message()

    async def add_system_message(self, content: str) -> None:
        """Add system message like Elia's pattern"""
        message = ChatMessage(content, "system")
        await self.chat_container.mount(message)
        self.scroll_to_latest_message()

    def action_clear_chat(self) -> None:
        """Clear the chat conversation"""
        self.chat_container.remove_children()
        self.notify("Chat cleared")

    def action_help(self) -> None:
        """Show help information"""
        self.push_screen(HelpScreen())


def run():
    """Entry point for the Saturn TUI"""
    app = SaturnApp()
    app.run()


if __name__ == "__main__":
    run()
