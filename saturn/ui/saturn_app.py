"""
Saturn TUI Application - Main Application File

A modern terminal user interface for the Saturn AI Assistant,
featuring real-time chat, model selection, and cloud operations.
"""

import os
from datetime import datetime

from textual import work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, VerticalScroll
from textual.widgets import Footer

from saturn.config import load_config
from saturn.orchestrator import run_chat_conversational

# Import state tracker
from .state_tracker import SaturnStateTracker, create_ui_aware_runner

# Import UI components
from .components import (
    ChatMessage,
    HelpScreen,
    ModelSelectorScreen,
    ModeSelector,
    SaturnPromptInput,
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
        padding: 0 1 0 1;
        margin-bottom: 1;
    }
    
    /* Reduce spacing between chat messages - apply to ChatMessage containers */
    ChatMessage {
        margin: 0;
        padding: 0;
        height: auto;
    }
    
    .user-content {
        color: #ffffff;
        background: #000000;
        margin: 0;
        padding: 1;
        border: none;
        height: auto;
        min-height: 1;
    }
    
    .assistant-content {
        background: #000000;
        border: solid #ffffff;
        margin: 0;
        padding: 1;
        min-height: 1;
    }
    
    .system-content {
        color: #888888;
        background: #000000;
        margin: 0 0 0 1;
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
        background: #000000;
        border: solid #21262d;
        margin: 1 3 1 1;
        
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
    
    /* Model Selector Modal Styles */
    .model-selector-modal {
        width: 80;
        height: 25;
        background: #161b22;
        border: solid #58a6ff;
        padding: 1;
    }
    
    .modal-title {
        text-align: center;
        text-style: bold;
        color: #58a6ff;
        margin-bottom: 1;
    }
    
    .model-content {
        height: 1fr;
        margin-bottom: 1;
    }
    
    .provider-panel {
        width: 1fr;
        margin-right: 1;
    }
    
    .model-panel {
        width: 2fr;
    }
    
    .panel-label {
        text-style: bold;
        color: #f0f6fc;
        margin-bottom: 1;
    }
    
    .button-bar {
        height: 4;
        align: center middle;
    }
    
    .button-bar Button {
        margin: 0 1;
    }
    
    .help-text {
        text-align: center;
        color: #7d8590;
        text-style: italic;
        margin: 1 0;
    }
    
    OptionList {
        border: solid #000000;
        background: #000000;
    }
    
    OptionList:focus {
        border: solid #58a6ff;
    }
    

    

    
    Footer {
        background: #161b22;
        color: #7d8590;
    }
    """

    TITLE = "Saturn"
    SUB_TITLE = "AI Assistant"

    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
        Binding("ctrl+c", "copy_last_message", "Copy", show=True),
        Binding("ctrl+l", "clear_chat", "Clear"),
        Binding("ctrl+m", "show_model_selector", "Models", show=True),
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
        # Track current model settings
        self.current_provider = self.config.get("llm_provider", "gemini")
        self.current_model = self._get_current_model_name()
        # Track current mode
        self.app_mode = "auto"

    def _get_current_model_name(self) -> str:
        """Get the current model name based on provider"""
        provider = self.current_provider
        if provider == "openai":
            return self.config.get('openai_model', 'gpt-4o')
        elif provider == "gemini":
            return self.config.get('gemini_model', 'gemini-1.5-pro')
        elif provider == "claude":
            return self.config.get('claude_model', 'claude-3-5-sonnet-20241022')
        elif provider == "mistral":
            return self.config.get('mistral_model', 'mistral-large-latest')
        else:
            return "unknown"

    def _update_model_config(self, provider: str, model: str) -> None:
        """Update the configuration with new model selection"""
        self.config["llm_provider"] = provider
        self.current_provider = provider
        self.current_model = model
        
        if provider == "openai":
            self.config["openai_model"] = model
        elif provider == "gemini":
            self.config["gemini_model"] = model
        elif provider == "claude":
            self.config["claude_model"] = model
        elif provider == "mistral":
            self.config["mistral_model"] = model

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
        # Mode selector in top right
        yield ModeSelector(current_mode=self.app_mode)
        
        # Main chat area
        with VerticalScroll(id="chat-container") as container:
            container.can_focus = False

        # Input area ( PromptInput)
        yield SaturnPromptInput(id="prompt")

        # Footer
        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app like chat screen"""
        # Welcome message with current model info
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        model_info = f"{self.current_provider.title()}: {self.current_model}"
        mode_info = f"Mode: {self.app_mode.title()}"
        self.add_system_message(f"Saturn AI Assistant ready ({model_info}, {mode_info}) - {self.timestamp}")

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

                # Set up execution mode based on app mode (if mode selector is implemented)
                runtime_config = self.config.copy()
                if hasattr(self, 'app_mode'):
                    mode_mapping = {
                        "auto": "auto",      # Standard execution with progress display
                        "agent": "yolo",     # Auto-execute without prompts (agent mode)
                        "command": "manual"  # Ask for confirmation on destructive operations
                    }
                    execution_mode = mode_mapping.get(self.app_mode, "auto")
                    runtime_config["execution_mode"] = execution_mode
                    self.add_system_message(f"🔧 Execution mode: {execution_mode} (based on {self.app_mode} mode)")

                # Initialize Saturn components for real state machine
                from model.llm.base_interface import get_llm_interface
                from saturn.aws_executor import AWSExecutor
                from saturn.gcp_executor import GcloudExecutor
                from saturn.knowledge_base import KnowledgeBase
                from saturn.mcp_integration import MCPToolIntegrator
                from saturn.prompts import SYSTEM_CHAT_PROMPT
                from saturn.rag_engine import RAGEngine

                # Load components like the orchestrator does
                llm_interface = get_llm_interface(runtime_config)

                gcp_executor = GcloudExecutor(runtime_config)
                aws_executor = AWSExecutor(runtime_config)
                knowledge_base = KnowledgeBase(
                    api_defs_dir=runtime_config.get(
                        "api_defs_dir", "./internal/knowledge_base"
                    ),
                    working_directory=runtime_config.get("working_directory", "."),
                )

                # Initialize RAG engine if configured
                rag_engine = None
                if runtime_config.get("rag_build_on_init", False):
                    rag_engine = RAGEngine(runtime_config)
                    await rag_engine.initialize()

                # Initialize MCP integration
                mcp_integrator = MCPToolIntegrator(
                    runtime_config.get("working_directory", ".")
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
                    config=runtime_config,
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
                    runtime_config, simple_generator()
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

    def action_copy_last_message(self) -> None:
        """Copy the last assistant message to clipboard"""
        chat_messages = self.chat_container.query(ChatMessage)
        if not chat_messages:
            self.notify("No messages to copy", severity="warning")
            return
        
        # Find the last assistant message
        last_assistant_message = None
        for message in reversed(chat_messages):
            if message.role == "assistant":
                last_assistant_message = message
                break
        
        if last_assistant_message:
            # Use the message's copy functionality
            last_assistant_message.action_copy_message()
        else:
            self.notify("No assistant messages found", severity="warning")

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

    def action_show_model_selector(self) -> None:
        """Show the model selector modal"""
        def on_model_selected(selection) -> None:
            if selection:
                provider, model = selection
                old_model = f"{self.current_provider}: {self.current_model}"
                self._update_model_config(provider, model)
                new_model = f"{provider}: {model}"
                self.add_system_message(f"Model changed from {old_model} to {new_model}")
                self.notify(f"Model changed to {provider.title()}: {model}")

        model_selector = ModelSelectorScreen(
            current_provider=self.current_provider,
            current_model=self.current_model
        )
        self.push_screen(model_selector, callback=on_model_selected)

    def on_mode_selector_mode_changed(self, event: ModeSelector.ModeChanged) -> None:
        """Handle mode changes from the mode selector"""
        old_mode = self.app_mode
        self.app_mode = event.mode
        
        mode_icons = {"auto": "🤖", "agent": "🧠", "command": "⚡"}
        icon = mode_icons.get(event.mode, "")
        
        self.add_system_message(f"Mode changed from {old_mode.title()} to {event.mode.title()}")
        self.notify(f"{icon} Switched to {event.mode.title()} mode")


def run():
    """Entry point for the Saturn TUI"""
    app = SaturnApp()
    app.run()


if __name__ == "__main__":
    run()
