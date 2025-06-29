"""
Enhanced chat display component with native text selection support.

This component replaces the message node system with a single TextArea that
supports native text selection, copy operations, and standard shortcuts.
"""

import platform
import subprocess
import re
from typing import List, Tuple
from datetime import datetime

from textual.binding import Binding
from textual.widgets import TextArea
from textual.message import Message


class ChatDisplay(TextArea):
    """
    A specialized TextArea for displaying chat messages with full native text selection support.
    
    Features:
    - Native text selection across all messages
    - Standard copy shortcuts (Ctrl+C, Cmd+C, Ctrl+A, Cmd+A)
    - Cross-platform clipboard support
    - Message formatting with role indicators
    - Automatic scrolling to new messages
    """
    
    BINDINGS = [
        Binding("ctrl+c,cmd+c", "copy_selection", "Copy", show=True),
        Binding("ctrl+a,cmd+a", "select_all", "Select All", show=True),
        Binding("ctrl+shift+c", "copy_all", "Copy All", show=False),
        # Override TextArea's default edit bindings to prevent editing
        Binding("enter", "ignore", "", show=False),
        Binding("backspace", "ignore", "", show=False),
        Binding("delete", "ignore", "", show=False),
    ]
    
    def __init__(self, **kwargs):
        super().__init__(
            read_only=True,  # Make it read-only to prevent editing
            show_line_numbers=False,
            **kwargs
        )
        self.messages: List[Tuple[str, str, str]] = []  # (role, content, timestamp)
        self.auto_scroll = True
        
    def add_message(self, content: str, role: str = "user") -> None:
        """Add a new message to the chat display."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        # Strip Rich markup from content before storing
        clean_content = self._strip_rich_markup(content)
        self.messages.append((role, clean_content, timestamp))
        self._rebuild_content()
        
        if self.auto_scroll:
            # Scroll to bottom after adding message
            self.cursor_location = self.document.end
            
    def clear_messages(self) -> None:
        """Clear all messages from the chat display."""
        self.messages.clear()
        self.text = ""
        
    # Pre-compiled regex patterns for better performance
    _markup_pattern = re.compile(r'\[/?[^\]]*\]')
    _box_chars_pattern = re.compile(r'[─━│┃┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╌╍╎╏═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╭╮╯╰╱╲╳╴╵╶╷╸╹╺╻╼╽╾╿]+')
    _empty_line_pattern = re.compile(r'^\s*$')
    
    def _strip_rich_markup(self, text: str) -> str:
        """Strip Rich markup tags and box drawing characters from text to display clean content."""
        # Single regex operation to remove Rich markup tags
        clean_text = self._markup_pattern.sub('', text)
        
        # Single regex operation to remove all box drawing characters at once
        clean_text = self._box_chars_pattern.sub('', clean_text)
        
        # Filter out empty lines efficiently
        lines = clean_text.split('\n')
        filtered_lines = [line.rstrip() for line in lines if line.strip()]
        
        return '\n'.join(filtered_lines)
        
    def _rebuild_content(self) -> None:
        """Rebuild the entire text content from messages."""
        lines = []
        
        for i, (role, content, timestamp) in enumerate(self.messages):
            # Add spacing between messages (except first)
            if i > 0:
                lines.append("")
                
            # Just add the content without headers or separators
            lines.extend(content.split('\n'))
                
        self.text = '\n'.join(lines)
        
    def action_ignore(self) -> None:
        """Ignore action - prevents editing."""
        pass
        
    def action_copy_selection(self) -> None:
        """Copy selected text to clipboard."""
        text_to_copy = self.selected_text
        
        if not text_to_copy.strip():
            self.notify("No text selected", severity="warning")
            return
            
        self._copy_to_clipboard(text_to_copy, "selection")
        
    def action_copy_all(self) -> None:
        """Copy all chat content to clipboard."""
        if not self.text.strip():
            self.notify("No messages to copy", severity="warning")
            return
            
        self._copy_to_clipboard(self.text, "all messages")
        
    def action_select_all(self) -> None:
        """Select all text in the chat display."""
        super().select_all()
        self.notify("All text selected")
        
    def _copy_to_clipboard(self, text: str, description: str) -> None:
        """Copy text to clipboard using platform-specific commands."""
        try:
            system = platform.system().lower()
            if system == "darwin":  # macOS
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "windows":  # Windows
                subprocess.run(
                    ["clip"], input=text.encode(), shell=True, check=True
                )
            elif system == "linux":  # Linux
                try:
                    subprocess.run(
                        ["xclip", "-selection", "clipboard"],
                        input=text.encode(),
                        check=True,
                    )
                except FileNotFoundError:
                    subprocess.run(
                        ["xsel", "--clipboard", "--input"],
                        input=text.encode(),
                        check=True,
                    )
                    
            self.notify(f"📋 Copied {description} ({len(text)} characters)")
            
        except Exception as e:
            self.notify(f"❌ Copy failed: {str(e)}", severity="error")
            
    def get_last_assistant_message(self) -> str:
        """Get the content of the last assistant message."""
        for role, content, _ in reversed(self.messages):
            if role == "assistant":
                return content
        return ""
        
    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the chat."""
        self.cursor_location = self.document.end
        
    def get_message_count(self) -> int:
        """Get the total number of messages."""
        return len(self.messages)
        
    def get_messages_by_role(self, role: str) -> List[Tuple[str, str]]:
        """Get all messages by a specific role."""
        return [(content, timestamp) for r, content, timestamp in self.messages if r == role] 