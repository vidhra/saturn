from textual import on
from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.message import Message
from textual.widgets import Button, OptionList, Static
from textual.widget import Widget


class ModeSelector(Widget):
    """A button that shows a dropdown for mode selection"""
    
    DEFAULT_CSS = """
    ModeSelector {
        dock: top;
        width: 20;
        align: right top;
        margin: 1;
        height: auto;
    }
    
    #mode-container {
        height: auto;
        width: 1fr;
    }
    
    #mode-button {
        width: 1fr;
        height: 3;
        background: #000000;
        border: solid #ffffff;
        text-align: left;
        padding: 0 1;
        color: #ffffff;
    }
    
    #mode-button:hover {
        border: solid #ffffff;
    }
    
    #mode-button.active {
        border: solid #ffffff;
        background: #000000;
    }
    
    #mode-dropdown {
        width: 1fr;
        height: 5;
        background: #000000;
        border: solid #ffffff;
        display: none;
        color: #ffffff;
    }
    
    #mode-dropdown:focus {
        border: solid #ffffff;
    }
    """
    
    def __init__(self, current_mode: str = "auto"):
        super().__init__()
        self.current_mode = current_mode
        self.dropdown_visible = False
        # Make the widget not focusable to avoid interfering with tab navigation
        self.can_focus = False
        # Ensure we don't capture tab events
        self.capture_tab = False
    
    class ModeChanged(Message):
        """Message sent when mode changes"""
        def __init__(self, mode: str) -> None:
            self.mode = mode
            super().__init__()
    
    def compose(self) -> ComposeResult:
        with Vertical(id="mode-container"):
            # Button that looks like input
            mode_icons = {"auto": "🤖 Auto", "agent": "🧠 Agent", "command": "⚡ Command"}
            button_text = mode_icons.get(self.current_mode, "🤖 Auto")
            yield Button(button_text, id="mode-button")
            
            # Dropdown
            options = [
                "🤖 Auto",
                "🧠 Agent", 
                "⚡ Command",
            ]
            yield OptionList(*options, id="mode-dropdown")
    
    def on_mount(self) -> None:
        """Initialize dropdown state on mount"""
        def setup_dropdown():
            try:
                dropdown = self.query_one("#mode-dropdown", OptionList)
                # Use styles.display as shown in Context7 docs
                dropdown.styles.display = "none"
                print("DEBUG: Dropdown hidden on mount using styles.display")
                
                # Pre-select current mode
                modes = ["auto", "agent", "command"]
                if self.current_mode in modes:
                    dropdown.highlighted = modes.index(self.current_mode)
                    print(f"DEBUG: Pre-selected mode {self.current_mode} at index {modes.index(self.current_mode)}")
            except Exception as e:
                print(f"DEBUG: Error in setup_dropdown: {e}")
        
        # Use call_later to ensure the widget is fully mounted
        self.call_later(setup_dropdown)
    
    @on(Button.Pressed, "#mode-button")
    def on_button_pressed(self) -> None:
        """Show dropdown for selection"""
        print(f"DEBUG: Button pressed, showing dropdown")
        try:
            dropdown = self.query_one("#mode-dropdown", OptionList)
            button = self.query_one("#mode-button", Button)
            
            print(f"DEBUG: Current dropdown.styles.display = {dropdown.styles.display}")
            print(f"DEBUG: Current dropdown_visible = {self.dropdown_visible}")
            
            # Always show dropdown when button is pressed (no toggle)
            dropdown.styles.display = "block"
            button.add_class("active")
            self.dropdown_visible = True
            print(f"DEBUG: Set dropdown.styles.display = {dropdown.styles.display}")
            
            # Focus the dropdown and pre-select current mode
            dropdown.focus()
            modes = ["auto", "agent", "command"]
            if self.current_mode in modes:
                dropdown.highlighted = modes.index(self.current_mode)
                print(f"DEBUG: Highlighted mode {self.current_mode}")
        except Exception as e:
            print(f"DEBUG: Error in button pressed: {e}")
    
    @on(OptionList.OptionSelected, "#mode-dropdown")
    def on_option_selected(self, event: OptionList.OptionSelected) -> None:
        """Handle mode selection and close dropdown"""
        print(f"DEBUG: Option selected, index={event.option_index}")
        try:
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
                
                # Always hide dropdown after selection
                dropdown = self.query_one("#mode-dropdown", OptionList)
                dropdown.styles.display = "none"
                button.remove_class("active")
                self.dropdown_visible = False
                print("DEBUG: Hiding dropdown after selection")
                
                # Send message
                self.post_message(self.ModeChanged(selected_mode))
        except Exception as e:
            print(f"DEBUG: Error in option selected: {e}")
    
    def on_key(self, event) -> None:
        """Handle escape and tab keys to close dropdown"""
        if (event.key == "escape" or event.key == "tab") and self.dropdown_visible:
            try:
                dropdown = self.query_one("#mode-dropdown", OptionList)
                button = self.query_one("#mode-button", Button)
                dropdown.styles.display = "none"
                button.remove_class("active")
                self.dropdown_visible = False
                print("DEBUG: Hiding dropdown on escape/tab")
                if event.key == "escape":
                    # Focus back to the button on escape
                    self.query_one("#mode-button").focus()
                    event.stop()
                elif event.key == "tab":
                    # Let tab continue its normal behavior (focus prompt input)
                    pass
            except Exception as e:
                print(f"DEBUG: Error in key handler: {e}") 