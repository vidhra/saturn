import os
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

# Import state tracker
from .state_tracker import SaturnStateTracker, create_ui_aware_runner


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
                import platform
                import subprocess

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


class ThinkingIndicator(Static):
    """Real-time thinking display with state tracking like ResponseStatus"""

    def __init__(self, **kwargs):
        super().__init__("", **kwargs)
        self.visible = False
        self.current_state = ""
        self.current_step = ""
        self.operation_count = 0

        # State descriptions for better UX
        self.state_descriptions = {
            "StartState": "Initializing Saturn AI Assistant...",
            "ReasoningState": "Analyzing your request and understanding intent...",
            "PlanningState": "Creating execution plan and selecting tools...",
            "ExecutingState": "Executing operations on cloud infrastructure...",
            "ProcessingResultsState": "Processing results and validating operations...",
            "TerraformState": "Managing infrastructure with Terraform...",
            "TerraformPlanningState": "Planning Terraform resource configurations...",
            "CompletedState": "Operations completed successfully!",
            "FailedState": "Operations failed - reviewing errors...",
        }

        # Dynamic sub-operations for each state
        self.sub_operations = {
            "ReasoningState": [
                "Parsing natural language query",
                "Identifying cloud services mentioned",
                "Analyzing complexity and scope",
                "Determining execution approach",
            ],
            "PlanningState": [
                "Discovering available tools",
                "Building dependency graph",
                "Optimizing execution order",
                "Validating tool parameters",
            ],
            "ExecutingState": [
                "Authenticating with cloud providers",
                "Executing infrastructure operations",
                "Monitoring operation progress",
                "Collecting execution results",
            ],
            "ProcessingResultsState": [
                "Validating operation results",
                "Checking for errors or warnings",
                "Updating state tracking",
                "Preparing next steps",
            ],
        }

    def start_thinking(self, message: str = ""):
        """Start the thinking animation"""
        self.visible = True
        self.display = True
        # Force immediate refresh
        self.refresh()
        if message:
            self.update(f"[bold yellow]▶[/bold yellow] {message}")
        else:
            self._show_current_state()

    def update_state(self, state_name: str, step: str = ""):
        """Update current state and step information"""
        if state_name != self.current_state:
            self.current_state = state_name
            self.current_step = step
            self.operation_count = 0
            self._show_current_state()
        elif step and step != self.current_step:
            self.current_step = step
            self._show_current_state()

    def _show_current_state(self):
        """Show current state with description and sub-operations"""
        if not self.visible:
            return

        # Main state description
        main_desc = self.state_descriptions.get(
            self.current_state, f"Processing {self.current_state}..."
        )

        # Show sub-operation if available
        sub_ops = self.sub_operations.get(self.current_state, [])
        if sub_ops and self.operation_count < len(sub_ops):
            current_sub_op = sub_ops[self.operation_count % len(sub_ops)]
            display_text = f"[bold yellow]▶[/bold yellow] {main_desc}\n[dim]  └─ {current_sub_op}...[/dim]"
            self.operation_count += 1
        elif self.current_step:
            display_text = f"[bold yellow]▶[/bold yellow] {main_desc}\n[dim]  └─ {self.current_step}[/dim]"
        else:
            display_text = f"[bold yellow]▶[/bold yellow] {main_desc}"

        self.update(display_text)

        # Auto-advance sub-operations for active states
        if sub_ops and self.current_state in [
            "ReasoningState",
            "PlanningState",
            "ExecutingState",
        ]:
            self.set_timer(1.5, self._advance_sub_operation)

    def _advance_sub_operation(self):
        """Advance to next sub-operation for visual progress"""
        if self.visible and self.current_state in self.sub_operations:
            self._show_current_state()

    def stop_thinking(self):
        """Stop thinking and hide"""
        self.visible = False
        self.display = False
        self.update("")
        self.current_state = ""
        self.current_step = ""
        self.operation_count = 0


class HelpScreen(ModalScreen):
    """Professional help modal"""

    BINDINGS = [
        Binding("escape", "dismiss", "Close"),
        Binding("q", "dismiss", "Close"),
    ]

    def compose(self) -> ComposeResult:
        with Container(classes="help-modal"):

            yield Static("Saturn AI Assistant", classes="help-title")
            yield Static(
                """Commands:
• Enter: Send message
• Ctrl+L: Clear conversation  
• ↑/K: Focus previous message
• ↓/J: Focus next message
• Tab: Focus input field
• Ctrl+C or Y: Copy focused message
• F1: Help • Ctrl+C: Quit

Features:
• Real-time execution feedback
• Multi-line input support
• Cross-platform clipboard (Windows/Mac/Linux)
• Message navigation and copying
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
    """Saturn Chat Application based on proven architecture"""

    CSS = """
    Screen {
        background: #000000;
        color: #f0f6fc;
    }
    
    #chat-container {
        height: 1fr;
        background: #000000;
        padding: 0 1;
        margin-bottom: 1;
    }
    
    .user-content {
        color: #ffffff;
        background: #000000;
        margin: 0 0 0 0;
        padding: 1;
        border: none;
        height: auto;
        min-height: 1;
    }
    
    .assistant-content {
        background: #000000;
        border: solid #ffffff;
        margin: 0 0 0 0;
        padding: 1;
        min-height: 1;
    }
    
    .system-content {
        color: #888888;
        background: #000000;
        margin: 0 0 1 1;
        padding: 1;
        border: none;
        height: auto;
        min-height: 1;
        text-style: italic;
    }
    
    /* Focused message styling */
    ChatMessage.focused-message {
        border: solid #ffffff;
        background: #000000;
    }
    
    ChatMessage.focused-message .user-content {
        border: solid #ffffff;
    }
    
    ChatMessage.focused-message .assistant-content {
        border: solid #ffffff;
    }
    
    ChatMessage.focused-message .system-content {
        border: solid #ffffff;
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
        Binding("up,k", "focus_previous_message", "Previous message", show=False),
        Binding("down,j", "focus_next_message", "Next message", show=False),
        Binding("tab", "focus_input", "Focus input", show=False),
    ]

    def __init__(self):
        super().__init__()
        self.config = load_config()
        self._setup_config()
        self.conversation_active = False

    def _setup_config(self):
        """Setup configuration similar to CLI preprocessing"""

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

        # Ensure working directory is set
        if "working_directory" not in self.config:
            self.config["working_directory"] = os.getcwd()

        # Set up API definitions directory
        if "api_defs_dir" not in self.config:
            self.config["api_defs_dir"] = os.path.join(
                os.path.dirname(__file__), "..", "..", "internal", "knowledge_base"
            )

    def compose(self) -> ComposeResult:
        # Main chat area
        with VerticalScroll(id="chat-container") as container:
            container.can_focus = False

        # Input area ( PromptInput)
        yield SaturnPromptInput(id="prompt")

        # Footer
        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app like chat screen"""
        # Welcome message
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.add_system_message("Saturn AI Assistant ready: " + self.timestamp)

        # Focus input
        self.query_one("#prompt").focus()

    @property
    def chat_container(self) -> VerticalScroll:
        """Get chat container"""
        return self.query_one("#chat-container", VerticalScroll)

    def scroll_to_latest_message(self):
        """Scroll to latest message"""
        container = self.chat_container
        container.refresh()
        container.scroll_end(animate=False, force=True)

    def on_saturn_prompt_input_prompt_submitted(
        self, event: SaturnPromptInput.PromptSubmitted
    ) -> None:
        """Handle user message submission immediately (synchronous)"""
        user_message = event.text

        # Add user message immediately
        message = ChatMessage(user_message, "user")
        self.chat_container.mount(message)
        self.scroll_to_latest_message()

        # Add status message to chat
        status_msg = ChatMessage("Processing your request...", "system")
        self.chat_container.mount(status_msg)
        self.scroll_to_latest_message()

        # Disable further input immediately
        event.prompt_input.submit_ready = False

        # Start conversation in background
        if not self.conversation_active:
            self.conversation_active = True
            # Use call_later to avoid blocking
            self.call_later(self.stream_agent_response, user_message)

    @work(thread=False)
    async def stream_agent_response(self, user_query: str) -> None:
        """Stream response from Saturn orchestrator with real-time state tracking"""

        try:
            # Create state tracker using the separate module
            state_tracker = SaturnStateTracker(self)

            try:
                # Debug: Check config paths
                self.add_system_message(
                    f"Working directory: {self.config.get('working_directory', 'None')}"
                )

                # Initialize Saturn components for real state machine
                from model.llm.base_interface import get_llm_interface
                from saturn.aws_executor import AWSExecutor
                from saturn.gcp_executor import GcloudExecutor
                from saturn.knowledge_base import KnowledgeBase
                from saturn.mcp_integration import MCPToolIntegrator
                from saturn.prompts import SYSTEM_CHAT_PROMPT
                from saturn.rag_engine import RAGEngine

                # Load components like the orchestrator does
                llm_interface = get_llm_interface(self.config)

                gcp_executor = GcloudExecutor(self.config)
                aws_executor = AWSExecutor(self.config)
                knowledge_base = KnowledgeBase(
                    api_defs_dir=self.config.get(
                        "api_defs_dir", "./internal/knowledge_base"
                    ),
                    working_directory=self.config.get("working_directory", "."),
                )

                # Initialize RAG engine if configured
                rag_engine = None
                if self.config.get("rag_build_on_init", False):
                    rag_engine = RAGEngine(self.config)
                    await rag_engine.initialize()

                # Initialize MCP integration
                mcp_integrator = MCPToolIntegrator(
                    self.config.get("working_directory", ".")
                )
                await mcp_integrator.initialize()

                # Create UI-aware state machine runner
                runner = await create_ui_aware_runner(
                    state_tracker=state_tracker,
                    llm_interface=llm_interface,
                    gcp_executor=gcp_executor,
                    aws_executor=aws_executor,
                    knowledge_base=knowledge_base,
                    system_prompt=SYSTEM_CHAT_PROMPT,
                    config=self.config,
                    console=None,  # We use state tracker instead of console
                    rag_engine=rag_engine,
                    mcp_integrator=mcp_integrator,
                )

                # Run the real state machine with UI callbacks
                context = await runner.process_query(user_query)

                # Get the LLM response from context
                full_response = ""
                if hasattr(context, "llm_text_response") and context.llm_text_response:
                    full_response = context.llm_text_response
                elif (
                    hasattr(context, "execution_results") and context.execution_results
                ):
                    # If no LLM response, show execution results
                    results = []
                    for tool_name, success, result in context.execution_results:
                        status = "✅" if success else "❌"
                        results.append(f"{status} {tool_name}: {result}")
                    full_response = "\n".join(results)
                else:
                    full_response = "Saturn completed processing your request."

                # Add assistant message
                assistant_message = ChatMessage(full_response, "assistant")
                await self.chat_container.mount(assistant_message)
                self.scroll_to_latest_message()

            except Exception as init_error:
                # Use the original orchestrator as fallback
                import traceback

                error_details = traceback.format_exc()
                self.add_system_message(f"⚠ Error details: {error_details}")
                await state_tracker._add_state_message(
                    f"⚠ Using fallback orchestrator: {str(init_error)}"
                )

                async def simple_generator():
                    yield user_query

                full_response = ""
                async for role, message in run_chat_conversational(
                    self.config, simple_generator()
                ):
                    if role == "assistant":
                        full_response += message

                assistant_message = ChatMessage(full_response, "assistant")
                await self.chat_container.mount(assistant_message)
                self.scroll_to_latest_message()

        except Exception as e:
            # Show error state
            state_tracker = SaturnStateTracker(self)
            await state_tracker.on_error(str(e))

            error_message = ChatMessage(f"Error: {str(e)}", "system")
            await self.chat_container.mount(error_message)
            self.scroll_to_latest_message()
        finally:
            # Ensure prompt is re-enabled
            prompt = self.query_one("#prompt", SaturnPromptInput)
            prompt.submit_ready = True
            self.conversation_active = False

    def add_user_message(self, content: str) -> None:
        message = ChatMessage(content, "user")
        self.chat_container.mount(message)
        self.scroll_to_latest_message()

    def add_assistant_message(self, content: str) -> None:
        message = ChatMessage(content, "assistant")
        self.chat_container.mount(message)
        self.scroll_to_latest_message()

    def add_system_message(self, content: str) -> None:
        message = ChatMessage(content, "system")
        self.chat_container.mount(message)
        self.scroll_to_latest_message()

    def action_clear_chat(self) -> None:
        """Clear the chat conversation"""
        self.chat_container.remove_children()
        self.notify("Chat cleared")

    def action_help(self) -> None:
        """Show help information"""
        self.push_screen(HelpScreen())

    def action_focus_previous_message(self) -> None:
        """Focus the previous chat message"""
        self._navigate_messages(direction="up")

    def action_focus_next_message(self) -> None:
        """Focus the next chat message"""
        self._navigate_messages(direction="down")

    def action_focus_input(self) -> None:
        """Focus the input field"""
        self.query_one("#prompt").focus()

    def _navigate_messages(self, direction: str) -> None:
        """Navigate between chat messages"""
        chat_messages = self.chat_container.query(ChatMessage)
        if not chat_messages:
            return

        focused = self.app.focused
        current_index = None

        # Find currently focused message
        if isinstance(focused, ChatMessage):
            try:
                current_index = list(chat_messages).index(focused)
            except ValueError:
                current_index = None

        # Determine next message to focus
        if current_index is None:
            # No message currently focused, focus first or last based on direction
            target_index = 0 if direction == "down" else len(chat_messages) - 1
        else:
            if direction == "up":
                target_index = max(0, current_index - 1)
            else:  # direction == "down"
                target_index = min(len(chat_messages) - 1, current_index + 1)

        # Focus the target message
        if 0 <= target_index < len(chat_messages):
            target_message = chat_messages[target_index]
            target_message.focus()

            # Scroll to ensure the focused message is visible
            self.chat_container.scroll_to_widget(target_message, animate=True)


def run():
    """Entry point for the Saturn TUI"""
    app = SaturnApp()
    app.run()


if __name__ == "__main__":
    run()
