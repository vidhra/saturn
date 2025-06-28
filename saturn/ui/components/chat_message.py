"""
Chat message components for the Saturn TUI application.
"""

from datetime import datetime
from typing import Optional, List, Tuple, Any
import re

from textual import events
from textual.app import ComposeResult
from textual.binding import Binding
from textual.geometry import Offset
from textual.widgets import Static
from textual.message import Message

from .input_widgets import SaturnTextArea


class SelectionManager:
    """Manages multi-node text selection across chat messages"""
    
    def __init__(self, chat_container):
        self.chat_container = chat_container
        self.selection_active = False
        self.selection_start_message = None
        self.selection_end_message = None
        self.selection_start_offset = None
        self.selection_end_offset = None
        self.selected_messages = []
        
    def start_selection(self, message: 'ChatMessage', offset: Offset):
        """Start a new selection"""
        self.clear_selection()
        self.selection_active = True
        self.selection_start_message = message
        self.selection_end_message = message
        self.selection_start_offset = offset
        self.selection_end_offset = offset
        self.update_selection()
        
    def update_selection(self, end_message: 'ChatMessage' = None, end_offset: Offset = None):
        """Update the current selection"""
        if not self.selection_active:
            return
            
        if end_message:
            self.selection_end_message = end_message
        if end_offset is not None:
            self.selection_end_offset = end_offset
        elif end_message and not self.selection_end_offset:
            # If no offset provided but we have a new message, use a default offset
            self.selection_end_offset = Offset(0, 0)
            
        # Get all chat messages and find the selection range
        all_messages = list(self.chat_container.query(ChatMessage))
        
        if not self.selection_start_message or not self.selection_end_message:
            return
            
        try:
            start_idx = all_messages.index(self.selection_start_message)
            end_idx = all_messages.index(self.selection_end_message)
            
            # Ensure proper order
            if start_idx > end_idx:
                start_idx, end_idx = end_idx, start_idx
                self.selection_start_message, self.selection_end_message = self.selection_end_message, self.selection_start_message
                self.selection_start_offset, self.selection_end_offset = self.selection_end_offset, self.selection_start_offset
            
            # Update selected messages
            self.selected_messages = all_messages[start_idx:end_idx + 1]
            
            # Apply visual selection
            for i, message in enumerate(all_messages):
                if i < start_idx or i > end_idx:
                    message.set_selection_state(None)
                elif i == start_idx and i == end_idx:
                    # Single message selection
                    message.set_selection_state("partial", self.selection_start_offset, self.selection_end_offset)
                elif i == start_idx:
                    # First message in multi-message selection
                    message.set_selection_state("start", self.selection_start_offset)
                elif i == end_idx:
                    # Last message in multi-message selection
                    message.set_selection_state("end", None, self.selection_end_offset)
                else:
                    # Fully selected message in between
                    message.set_selection_state("full")
                    
        except ValueError:
            # Message not found in list
            pass
    
    def end_selection(self):
        """End the current selection"""
        self.selection_active = False
        
    def clear_selection(self):
        """Clear all selection"""
        self.selection_active = False
        for message in self.selected_messages:
            message.set_selection_state(None)
        self.selected_messages = []
        self.selection_start_message = None
        self.selection_end_message = None
        
    def get_selected_text(self) -> str:
        """Get the currently selected text across all messages"""
        if not self.selected_messages:
            return ""
            
        selected_text_parts = []
        
        for i, message in enumerate(self.selected_messages):
            text = message.content
            
            if len(self.selected_messages) == 1:
                # Single message selection - get partial text
                if self.selection_start_offset and self.selection_end_offset:
                    # For single message, estimate text positions based on character position
                    # This is simplified - could be improved with actual text layout
                    start_char = max(0, min(len(text), self.selection_start_offset.x * 2))  # Rough estimate
                    end_char = max(start_char, min(len(text), self.selection_end_offset.x * 2))
                    text = text[start_char:end_char]
            elif i == 0:
                # First message - from start offset to end
                if self.selection_start_offset:
                    start_char = max(0, min(len(text), self.selection_start_offset.x * 2))
                    text = text[start_char:]
            elif i == len(self.selected_messages) - 1:
                # Last message - from start to end offset  
                if self.selection_end_offset:
                    end_char = max(0, min(len(text), self.selection_end_offset.x * 2))
                    text = text[:end_char]
            # For middle messages, use full text
            
            if text.strip():
                # Add role prefix for context
                role_prefix = ""
                if message.role == "assistant":
                    role_prefix = "[assistant] "
                elif message.role == "system":
                    role_prefix = "[system] "
                # No prefix for user messages
                selected_text_parts.append(f"{role_prefix}{text}")
        
        return "\n\n".join(selected_text_parts)


class ChatMessage(Static):
    """Individual chat message with multi-node selection support"""

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
        
        # Selection state
        self.selection_state = None  # None, "full", "start", "end", "partial"
        self.selection_start_offset = None
        self.selection_end_offset = None
        
        # Enable focus and mouse events for selection
        self.can_focus = True

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

    def on_mount(self) -> None:
        """Setup selection manager reference"""
        # Get the selection manager from the app
        app = self.app
        if hasattr(app, 'selection_manager'):
            self.selection_manager = app.selection_manager
        else:
            # Create selection manager if it doesn't exist
            chat_container = self.parent
            if chat_container:
                app.selection_manager = SelectionManager(chat_container)
                self.selection_manager = app.selection_manager

    def on_mouse_down(self, event: events.MouseDown) -> None:
        """Start selection on mouse down"""
        if hasattr(self, 'selection_manager'):
            try:
                # Capture mouse to receive all mouse events
                self.capture_mouse()
                self.selection_manager.start_selection(self, event.offset)
                event.stop()
            except Exception:
                # If capture fails, still try to start selection
                self.selection_manager.start_selection(self, event.offset)
                event.stop()

    def on_mouse_move(self, event: events.MouseMove) -> None:
        """Update selection on mouse move (when mouse is captured)"""
        if hasattr(self, 'selection_manager') and self.selection_manager.selection_active:
            try:
                # Find which message the mouse is currently over
                chat_container = self.selection_manager.chat_container
                screen_offset = event.screen_offset
                
                # Find the message under the mouse cursor
                for message in chat_container.query(ChatMessage):
                    if hasattr(message, 'region') and message.region.contains(screen_offset):
                        # Convert screen offset to message-relative offset
                        relative_offset = screen_offset - message.region.offset
                        self.selection_manager.update_selection(message, relative_offset)
                        return
                
                # If no message found under cursor, update with current message and event offset
                self.selection_manager.update_selection(self, event.offset)
                
            except Exception:
                # Fallback to simple update if region calculations fail
                self.selection_manager.update_selection(self, event.offset)

    def on_mouse_up(self, event: events.MouseUp) -> None:
        """End selection on mouse up"""
        if hasattr(self, 'selection_manager') and self.selection_manager.selection_active:
            self.selection_manager.end_selection()
            try:
                # Release mouse capture
                self.release_mouse()
            except Exception:
                # Ignore release errors
                pass
            event.stop()

    def on_enter(self, event: events.Enter) -> None:
        """Handle mouse entering the message during selection"""
        if hasattr(self, 'selection_manager') and self.selection_manager.selection_active:
            # Enter event doesn't have offset, so we'll update without specific offset
            # The selection manager will use the last known mouse position
            self.selection_manager.update_selection(self)

    def set_selection_state(self, state: Optional[str], start_offset: Optional[Offset] = None, end_offset: Optional[Offset] = None):
        """Set the visual selection state of this message"""
        self.selection_state = state
        self.selection_start_offset = start_offset
        self.selection_end_offset = end_offset
        
        # Update visual styling based on selection state
        if state == "full":
            self.add_class("fully-selected")
            self.remove_class("partially-selected")
        elif state in ["start", "end", "partial"]:
            self.add_class("partially-selected")
            self.remove_class("fully-selected")
        else:
            self.remove_class("fully-selected")
            self.remove_class("partially-selected")

    def action_copy_message(self) -> None:
        """Copy this message's content or current selection"""
        try:
            # Import here to avoid circular imports
            import platform
            import subprocess
            
            # If there's an active selection, copy that instead
            if (hasattr(self, 'selection_manager') and 
                self.selection_manager.selected_messages):
                text_to_copy = self.selection_manager.get_selected_text()
                copy_type = "selection"
            else:
                text_to_copy = self.content
                copy_type = "message"
            
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

            self.notify(f"📋 Copied {copy_type} ({len(text_to_copy)} characters)")

        except Exception as e:
            self.notify(f"❌ Copy failed: {str(e)}", severity="error")

 