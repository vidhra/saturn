from textual import on
from textual.app import ComposeResult
from textual.containers import Container
from textual.message import Message
from textual.widgets import Button, OptionList, Static
from textual.widget import Widget


class ModeSelector(Widget):
    """A button that looks like the prompt input but shows a dropdown for mode selection"""
    
    DEFAULT_CSS = """
    ModeSelector {
        dock: top;
        height: 8;
        width: 20;
        align: right top;
        margin: 1;
    }
    
    #mode-button {
        width: 1fr;
        height: 3;
        background: #000000;
        border: solid #21262d;
        text-align: left;
        padding: 0 1;
    }
    
    #mode-button:hover {
        border: solid #58a6ff;
    }
    
    #mode-dropdown {
        width: 1fr;
        height: 0;
        background: #0d1117;
        border: solid #58a6ff;
    }
    
    #mode-dropdown.visible {
        height: 5;
    }
    
    #mode-dropdown:focus {
        border: solid #ffffff;
    }
    """
    
    def __init__(self, current_mode: str = "auto"):
        super().__init__()
        self.current_mode = current_mode
        self.dropdown_visible = False
    
    class ModeChanged(Message):
        """Message sent when mode changes"""
        def __init__(self, mode: str) -> None:
            self.mode = mode
            super().__init__()
    
    def compose(self) -> ComposeResult:
        # Button that looks like input
        mode_icons = {"auto": "🤖 Auto", "agent": "🧠 Agent", "command": "⚡ Command"}
        button_text = mode_icons.get(self.current_mode, "🤖 Auto")
        yield Button(button_text, id="mode-button")
        
        # Hidden dropdown - using OptionList directly instead of Container
        options = [
            "🤖 Auto",
            "🧠 Agent", 
            "⚡ Command",
        ]
        yield OptionList(*options, id="mode-dropdown")
    
    @on(Button.Pressed, "#mode-button")
    def on_button_pressed(self) -> None:
        """Toggle dropdown visibility"""
        dropdown = self.query_one("#mode-dropdown")
        if self.dropdown_visible:
            dropdown.remove_class("visible")
            self.dropdown_visible = False
        else:
            dropdown.add_class("visible")
            self.dropdown_visible = True
            # Focus the dropdown
            dropdown.focus()
    
    @on(OptionList.OptionSelected, "#mode-dropdown")
    def on_option_selected(self, event: OptionList.OptionSelected) -> None:
        """Handle mode selection"""
        if event.option_index is not None:
            modes = ["auto", "agent", "command"]
            selected_mode = modes[event.option_index]
            
            # Update current mode
            self.current_mode = selected_mode
            
            # Update button text
            mode_icons = {"auto": "🤖 Auto", "agent": "🧠 Agent", "command": "⚡ Command"}
            button_text = mode_icons.get(selected_mode, "🤖 Auto")
            button = self.query_one("#mode-button", Button)
            button.label = button_text
            
            # Hide dropdown after selection
            dropdown = self.query_one("#mode-dropdown")
            dropdown.remove_class("visible")
            self.dropdown_visible = False
            
            # Send message
            self.post_message(self.ModeChanged(selected_mode))
    
    def on_key(self, event) -> None:
        """Handle escape key to close dropdown"""
        if event.key == "escape" and self.dropdown_visible:
            dropdown = self.query_one("#mode-dropdown")
            dropdown.remove_class("visible")
            self.dropdown_visible = False
            # Focus back to the button
            self.query_one("#mode-button").focus()
            event.stop() 