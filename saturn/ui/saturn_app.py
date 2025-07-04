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

from .state_tracker import SaturnStateTracker, create_ui_aware_runner

from .components import (
    HelpScreen,
    ModelSelectorScreen,
    ModeSelector,
    SaturnPromptInput,
)
from .components.chat_display import ChatDisplay


class SaturnApp(App):
    """Saturn Chat Application with native text selection support"""

    CSS = """
    Screen {
        background: #000000;
        color: #ffffff;
    }
    
    #chat-display {
        height: 1fr;
        background: #000000;
        border: none;
        margin: 0;
        padding: 1;
        color: #ffffff;
    }
    
    #chat-display:focus {
        border: none;
        background: #000000;
    }
    
    /* Ensure text selection is visible against black background */
    #chat-display .text-area--selection {
        background: #333333;
        color: #ffffff;
    }
    
    /* Remove any other TextArea styling that might interfere */
    TextArea {
        background: #000000;
        color: #ffffff;
    }
    
    SaturnPromptInput {
        dock: bottom;
        height: auto;
        max-height: 30%;
        background: #000000;
        border: solid #ffffff;
        margin: 0 1 1 1;
    }
    
    SaturnPromptInput:focus {
        border: solid #ffffff;
    }
    
    /* Model Selector Modal Styles */
    .model-selector-modal {
        width: 80;
        height: 25;
        background: #000000;
        border: solid #ffffff;
        padding: 1;
    }
    
    .modal-title {
        text-align: center;
        text-style: bold;
        color: #ffffff;
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
        color: #ffffff;
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
        color: #888888;
        text-style: italic;
        margin: 1 0;
    }
    
    OptionList {
        border: solid #ffffff;
        background: #000000;
    }
    
    OptionList:focus {
        border: solid #ffffff;
    }
    
    Footer {
        background: #000000;
        color: #888888;
    }
    """

    TITLE = "Saturn"
    SUB_TITLE = "AI Assistant"

    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
        Binding("ctrl+c", "copy_selection", "Copy", show=True),
        Binding("ctrl+shift+c", "copy_last_message", "Copy Last", show=False),
        Binding("ctrl+a", "select_all", "Select All", show=True),
        Binding("ctrl+l", "clear_chat", "Clear"),
        Binding("ctrl+m", "show_model_selector", "Models", show=True),
        Binding("f1", "help", "Help"),
        Binding("escape", "clear_selection", "Clear Selection", show=False),
        Binding("tab", "focus_input", "Focus input", show=False),
        Binding("shift+tab", "focus_chat", "Focus chat", show=False),
    ]

    def __init__(self):
        super().__init__()
        self.config = load_config()
        self._setup_config()
        self.conversation_active = False
        self.current_provider = self.config.get("llm_provider", "gemini")
        self.current_model = self._get_current_model_name()
        self.app_mode = "auto"

    def _get_current_model_name(self) -> str:
        """Get the current model name based on provider"""
        provider = self.current_provider
        if provider == "openai":
            return self.config.get('openai_model', 'gpt-4.1')
        elif provider == "gemini":
            return self.config.get('gemini_model', 'gemini-2.5-pro')
        elif provider == "claude":
            return self.config.get('claude_model', 'claude-sonnet-4-20250514')
        elif provider == "mistral":
            return self.config.get('mistral_model', 'mistral-medium-2506')
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

        vector_store = self.config.get("vector_store", "chroma")
        self.config["vector_store_choice"] = vector_store.lower()
        self.config["rag_build_on_init"] = (
            self.config["vector_store_choice"] in ["default", "chroma", "duckdb"]
        )

        from saturn.rag_engine import build_provider_db_config

        cloud_provider = "gcp"  

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

        if "working_directory" not in self.config:
            self.config["working_directory"] = os.getcwd()

        if "api_defs_dir" not in self.config:
            self.config["api_defs_dir"] = os.path.join(
                os.path.dirname(__file__), "..", "..", "internal", "knowledge_base"
            )

    def compose(self) -> ComposeResult:

        yield ModeSelector(current_mode=self.app_mode)

        yield ChatDisplay(id="chat-display")

        yield SaturnPromptInput(id="prompt")

        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app"""
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        model_info = f"{self.current_provider.title()}: {self.current_model}"
        mode_info = f"Mode: {self.app_mode.title()}"
        self.add_system_message(f"Saturn AI Assistant ready ({model_info}, {mode_info}) - {self.timestamp}")

        self.query_one("#prompt").focus()

    @property
    def chat_display(self) -> ChatDisplay:
        """Get the chat display widget"""
        return self.query_one("#chat-display", ChatDisplay)

    def on_saturn_prompt_input_prompt_submitted(
        self, event: SaturnPromptInput.PromptSubmitted
    ) -> None:
        """Handle user message submission immediately (synchronous)"""
        user_message = event.text

        self.add_user_message(user_message)

        event.prompt_input.submit_ready = False

        if not self.conversation_active:
            self.conversation_active = True
            self.call_later(self.stream_agent_response, user_message)

    @work(thread=False)
    async def stream_agent_response(self, user_query: str) -> None:
        """Stream response from Saturn orchestrator with real-time state tracking"""

        try:
            state_tracker = SaturnStateTracker(self)

            try:

                runtime_config = self.config.copy()
                if hasattr(self, 'app_mode'):
                    mode_mapping = {
                        "auto": "auto",   
                        "agent": "yolo",    
                        "command": "manual"  
                    }
                    execution_mode = mode_mapping.get(self.app_mode, "auto")
                    runtime_config["execution_mode"] = execution_mode

                from model.llm.base_interface import get_llm_interface
                from saturn.aws_executor import AWSExecutor
                from saturn.gcp_executor import GcloudExecutor
                from saturn.knowledge_base import KnowledgeBase
                from saturn.mcp_integration import MCPToolIntegrator
                from saturn.prompts import SYSTEM_CHAT_PROMPT
                from saturn.rag_engine import RAGEngine

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
                    # Get the docs path for building the index
                    docs_path = runtime_config.get(
                        "rag_docs_path_for_init",
                        os.path.join(
                            os.path.dirname(__file__),
                            "..",
                            "..",
                            "internal",
                            "tools", 
                            "gcloud_online_docs_markdown",
                        ),
                    )
                    
                    rag_engine = RAGEngine(
                        config=runtime_config,
                        vector_store_choice=runtime_config.get("vector_store_choice", "chroma"),
                        db_config=runtime_config.get("db_config"),
                        documents_path_for_init=docs_path,
                        build_index_on_init=False,  # Try to load existing index first
                        verbose=True,
                    )

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
                    question_handler=self.ui_question_handler,
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
                self.add_assistant_message(full_response)

            except Exception as init_error:
                # Use the original orchestrator as fallback
                import traceback

                error_details = traceback.format_exc()
                self.add_system_message(f"⚠ Using fallback orchestrator: {str(init_error)}")

                async def simple_generator():
                    yield user_query

                full_response = ""
                await state_tracker._add_state_message("🔄 Running fallback orchestrator...")
                
                async for role, message in run_chat_conversational(
                    runtime_config, simple_generator()
                ):
                    if role == "assistant":
                        # Show assistant response in chunks for real-time feel
                        full_response += message
                        if len(message) > 100:  # Show chunks for long responses
                            chunk_preview = message[:100] + "..."
                            await state_tracker._add_state_message(f"💬 {chunk_preview}")

                self.add_assistant_message(full_response)

        except Exception as e:
            # Show error state
            state_tracker = SaturnStateTracker(self)
            await state_tracker.on_error(str(e))
            self.add_system_message(f"Error: {str(e)}")
        finally:
            # Ensure prompt is re-enabled
            prompt = self.query_one("#prompt", SaturnPromptInput)
            prompt.submit_ready = True
            self.conversation_active = False

    def add_user_message(self, content: str) -> None:
        """Add a user message to the chat"""
        self.chat_display.add_message(content, "user")

    def add_assistant_message(self, content: str) -> None:
        """Add an assistant message to the chat"""
        self.chat_display.add_message(content, "assistant")

    def add_system_message(self, content: str) -> None:
        """Add a system message to the chat"""
        self.chat_display.add_message(content, "system")

    def action_clear_chat(self) -> None:
        """Clear the chat conversation"""
        self.chat_display.clear_messages()
        self.notify("Chat cleared")
        
    def action_clear_selection(self) -> None:
        """Clear the current text selection"""
        self.clear_selection()
        self.notify("Selection cleared")

    def action_copy_selection(self) -> None:
        """Copy the current selection to clipboard"""
        chat_display = self.chat_display
        if chat_display.selected_text.strip():
            chat_display.action_copy_selection()
        else:
            self.notify("No text selected", severity="warning")

    def action_copy_last_message(self) -> None:
        """Copy the last assistant message to clipboard"""
        chat_display = self.chat_display
        last_message = chat_display.get_last_assistant_message()
        
        if last_message.strip():
            chat_display._copy_to_clipboard(last_message, "last assistant message")
        else:
            self.notify("No assistant messages found", severity="warning")

    def action_select_all(self) -> None:
        """Select all text in the chat"""
        self.chat_display.action_select_all()

    def action_help(self) -> None:
        """Show help information"""
        self.push_screen(HelpScreen())

    def action_focus_input(self) -> None:
        """Focus the input field"""
        self.query_one("#prompt").focus()

    def action_focus_chat(self) -> None:
        """Focus the chat display"""
        self.query_one("#chat-display").focus()

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

    async def ui_question_handler(self, formatted_question: str, suggested_answers: list = None) -> str:
        """Handle questions in UI mode by creating an interactive dialog."""
        import asyncio
        from textual.widgets import Input, Button, Vertical, Label
        from textual.containers import Container
        from textual.screen import ModalScreen
        
        class QuestionScreen(ModalScreen):
            def __init__(self, question: str, suggested_answers: list = None):
                super().__init__()
                self.question = question
                self.suggested_answers = suggested_answers or []
                self.user_response = None
                self.response_event = asyncio.Event()
            
            def compose(self):
                with Container():
                    yield Label(self.question, id="question-label")
                    if self.suggested_answers:
                        yield Label("Suggested options:", id="options-label")
                        for i, answer in enumerate(self.suggested_answers, 1):
                            yield Label(f"{i}. {answer}", classes="option-item")
                    yield Input(placeholder="Your answer...", id="answer-input")
                    with Vertical():
                        yield Button("Submit", variant="primary", id="submit-btn")
                        yield Button("Skip", variant="default", id="skip-btn")
            
            def on_button_pressed(self, event: Button.Pressed) -> None:
                if event.button.id == "submit-btn":
                    input_widget = self.query_one("#answer-input", Input)
                    answer = input_widget.value.strip()
                    
                    # Check if it's a number for suggested answers
                    if self.suggested_answers and answer.isdigit():
                        index = int(answer) - 1
                        if 0 <= index < len(self.suggested_answers):
                            self.user_response = self.suggested_answers[index]
                        else:
                            self.user_response = answer
                    else:
                        self.user_response = answer if answer else "NO_ANSWER"
                    
                    self.response_event.set()
                    self.dismiss()
                elif event.button.id == "skip-btn":
                    self.user_response = "SKIPPED_BY_USER"
                    self.response_event.set()
                    self.dismiss()
        
        # Create and push the question screen
        question_screen = QuestionScreen(formatted_question, suggested_answers)
        self.push_screen(question_screen)
        
        # Wait for user response
        await question_screen.response_event.wait()
        
        return question_screen.user_response or "NO_ANSWER"


def run():
    """Entry point for the Saturn TUI"""
    app = SaturnApp()
    app.run()


if __name__ == "__main__":
    run()
