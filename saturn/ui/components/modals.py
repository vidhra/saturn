"""
Modal screens for the Saturn TUI application.
"""

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label, OptionList, Static
from textual.widgets.option_list import Option


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
• Ctrl+N: Start new conversation
• Ctrl+M: Select AI model
• Ctrl+I: Show context info
• Tab: Focus input • Shift+Tab: Focus chat
• Ctrl+C: Copy selected text
• Ctrl+Shift+C: Copy last assistant message
• Ctrl+A / Cmd+A: Select all chat text
• Esc: Clear text selection
• F1: Help • Ctrl+Q: Quit

Text Selection (Native Support):
• Click & drag to select text naturally
• Shift+Arrow keys for precise selection
• Double-click to select words
• Triple-click to select lines
• Selection works across all messages seamlessly
• Standard copy/paste shortcuts work
• Full keyboard navigation support

Modes:
• 🤖 Auto: Intelligent mode selection
• 🧠 Agent: AI assistant mode  
• ⚡ Command: Direct command execution

Context Engine (Cursor-style):
• 🧠 Intelligent conversation compression
• 🎯 Relevance-based context selection
• 📊 Technical context extraction
• 💾 Persistent conversation storage
• 🗜️ Automatic message summarization
• ⚡ Real-time context injection to LLM

Features:
• Native text selection with standard shortcuts
• Multi-model support (OpenAI, Gemini, Claude, Mistral)
• Multi-line input support
• Cross-platform clipboard (Windows/Mac/Linux)
• Real-time execution feedback
• Full keyboard navigation

Cloud Operations:
• AWS, GCP, Azure automation
• Infrastructure as Code
• Terraform, CloudFormation
• Monitoring & troubleshooting

Press ESC to close
            """,
                classes="help-content",
            )


class ModelSelectorScreen(ModalScreen):
    """Model selection modal similar to Elia's interface"""

    BINDINGS = [
        Binding("escape", "dismiss", "Close"),
        Binding("q", "dismiss", "Close"),
        Binding("enter", "select_model", "Select"),
        Binding("left", "focus_provider", "Focus Provider", show=False),
        Binding("right", "focus_model", "Focus Model", show=False),
        Binding("tab", "focus_next", "Next Panel", show=False),
    ]

    def __init__(self, current_provider: str, current_model: str, **kwargs):
        super().__init__(**kwargs)
        self.current_provider = current_provider
        self.current_model = current_model
        self.selected_provider = current_provider
        self.selected_model = current_model

        # Define available models for each provider
        self.models_by_provider = {
            "openai": [
                ("gpt-4o", "GPT-4o (Latest)"),
                ("gpt-4.1", "GPT-4.1"),
                ("o3-mini", "o3-mini"),
                ("o3","o3")
            ],
            "gemini": [
                ("gemini-2.5-pro", "Gemini 2.5 Pro"),
                ("gemini-2.5-flash", "Gemini 2.5 Flash"),
            ],
            "claude": [
                ("claude-opus-4-20250514", "Claude 4 Opus"),
                ("claude-sonnet-4-20250514", "Claude 4 Sonnet"),
                ("claude-3-7-sonnet-20250219", "Claude 3.7 Sonnet (Latest)"),
                ("claude-3-5-haiku-20241022", "Claude 3.5 Haiku"),

            ],
            "mistral": [
                ("mistral-large-2411", "Mistral Large (Latest)"),
                ("mistral-medium-2505", "Mistral Medium"),
                ("codestral-2501", "Codestral (Code-focused)"),
            ],
        }

    def compose(self) -> ComposeResult:
        with Container(classes="model-selector-modal"):
            yield Static("🤖 Select AI Model", classes="modal-title")
            
            with Horizontal(classes="model-content"):
                # Provider selection on the left
                with Vertical(classes="provider-panel"):
                    yield Label("Provider", classes="panel-label")
                    provider_options = [
                        Option(f"🔸 OpenAI", id="openai"),
                        Option(f"🔹 Google Gemini", id="gemini"), 
                        Option(f"🔸 Anthropic Claude", id="claude"),
                        Option(f"🔹 Mistral AI", id="mistral"),
                    ]
                    yield OptionList(*provider_options, id="provider-list")
                
                # Model selection on the right
                with Vertical(classes="model-panel"):
                    yield Label("Available Models", classes="panel-label")
                    yield OptionList(id="model-list")
            
            yield Static("Navigate: ←→ or Tab | Select: Enter | Close: Esc", classes="help-text")
            
            with Horizontal(classes="button-bar"):
                yield Button("Cancel", variant="default", id="cancel-btn")
                yield Button("Select Model", variant="primary", id="select-btn")

    def on_mount(self) -> None:
        """Initialize the modal with current selections"""
        # Set current provider
        provider_list = self.query_one("#provider-list", OptionList)
        provider_index = list(self.models_by_provider.keys()).index(self.current_provider)
        provider_list.highlighted = provider_index
        
        # Load models for current provider
        self._update_model_list(self.current_provider)
        
        # Focus the provider list initially
        provider_list.focus()

    @on(OptionList.OptionSelected, "#provider-list")
    def on_provider_selected(self, event: OptionList.OptionSelected) -> None:
        """Handle provider selection"""
        if event.option and event.option.id:
            self.selected_provider = event.option.id
            self._update_model_list(self.selected_provider)
            # Focus the model list after provider selection
            self.query_one("#model-list", OptionList).focus()

    @on(OptionList.OptionSelected, "#model-list") 
    def on_model_selected(self, event: OptionList.OptionSelected) -> None:
        """Handle model selection"""
        if event.option and event.option.id:
            self.selected_model = event.option.id

    @on(Button.Pressed, "#cancel-btn")
    def on_cancel(self) -> None:
        """Cancel selection"""
        self.dismiss()

    @on(Button.Pressed, "#select-btn")
    def on_select(self) -> None:
        """Confirm model selection"""
        self.action_select_model()

    def action_select_model(self) -> None:
        """Select the highlighted model"""
        model_list = self.query_one("#model-list", OptionList)
        if model_list.highlighted is not None:
            model_option = model_list.get_option_at_index(model_list.highlighted)
            if model_option and model_option.id:
                self.selected_model = model_option.id
        
        # Ensure we have valid selections
        if not self.selected_model and self.selected_provider in self.models_by_provider:
            # Default to first model if none selected
            first_model = self.models_by_provider[self.selected_provider][0][0]
            self.selected_model = first_model
                
        # Return the selection to the parent app
        self.dismiss((self.selected_provider, self.selected_model))

    def action_focus_provider(self) -> None:
        """Focus the provider list"""
        self.query_one("#provider-list", OptionList).focus()

    def action_focus_model(self) -> None:
        """Focus the model list"""
        self.query_one("#model-list", OptionList).focus()

    def action_focus_next(self) -> None:
        """Focus next panel (tab between provider and model lists)"""
        provider_list = self.query_one("#provider-list", OptionList)
        model_list = self.query_one("#model-list", OptionList)
        
        if provider_list.has_focus:
            model_list.focus()
        else:
            provider_list.focus()

    def _update_model_list(self, provider: str) -> None:
        """Update the model list for the selected provider"""
        model_list = self.query_one("#model-list", OptionList)
        model_list.clear_options()
        
        if provider in self.models_by_provider:
            model_options = []
            for model_id, display_name in self.models_by_provider[provider]:
                # Mark current model with a checkmark
                prefix = "✅ " if (provider == self.current_provider and model_id == self.current_model) else "   "
                model_options.append(Option(f"{prefix}{display_name}", id=model_id))
            
            model_list.add_options(model_options)
            
            # If we're switching to a different provider, reset the selected model to the first one
            if provider != self.current_provider:
                self.selected_model = self.models_by_provider[provider][0][0]
                model_list.highlighted = 0
            else:
                # Highlight the current model for the current provider
                self._highlight_current_model()

    def _highlight_current_model(self) -> None:
        """Highlight the current model in the list"""
        model_list = self.query_one("#model-list", OptionList)
        models = self.models_by_provider.get(self.selected_provider, [])
        
        target_model = self.current_model if self.selected_provider == self.current_provider else self.selected_model
        
        for i, (model_id, _) in enumerate(models):
            if model_id == target_model:
                model_list.highlighted = i
                break


class ModeSelectorScreen(ModalScreen):
    """Simple mode selector modal"""

    BINDINGS = [
        Binding("escape", "dismiss", "Close"),
        Binding("q", "dismiss", "Close"),
        Binding("enter", "select_mode", "Select"),
    ]

    def __init__(self, current_mode: str = "auto", **kwargs):
        super().__init__(**kwargs)
        self.current_mode = current_mode
        self.selected_mode = current_mode

    def compose(self) -> ComposeResult:
        with Container(classes="mode-selector-modal"):
            yield Static("🔧 Select Mode", classes="mode-title")
            
            mode_options = [
                Option(f"🤖 Auto {'✓' if self.current_mode == 'auto' else ''}", id="auto"),
                Option(f"🧠 Agent {'✓' if self.current_mode == 'agent' else ''}", id="agent"),
                Option(f"⚡ Command {'✓' if self.current_mode == 'command' else ''}", id="command"),
            ]
            yield OptionList(*mode_options, id="mode-list", classes="mode-list")
            
            yield Static("Navigate: ↑↓ | Select: Enter | Close: Esc", classes="help-text")

    def on_mount(self) -> None:
        """Initialize the modal with current selection"""
        mode_list = self.query_one("#mode-list", OptionList)
        modes = ["auto", "agent", "command"]
        if self.current_mode in modes:
            mode_list.highlighted = modes.index(self.current_mode)
        mode_list.focus()

    @on(OptionList.OptionSelected, "#mode-list")
    def on_mode_selected(self, event: OptionList.OptionSelected) -> None:
        """Handle mode selection"""
        if event.option and event.option.id:
            self.selected_mode = event.option.id
            self.action_select_mode()

    def action_select_mode(self) -> None:
        """Select the highlighted mode"""
        mode_list = self.query_one("#mode-list", OptionList)
        if mode_list.highlighted is not None:
            mode_option = mode_list.get_option_at_index(mode_list.highlighted)
            if mode_option and mode_option.id:
                self.selected_mode = mode_option.id
        
        # Return the selection to the parent app
        self.dismiss(self.selected_mode)
