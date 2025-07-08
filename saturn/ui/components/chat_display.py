"""
Enhanced chat display component with native text selection support and context engine integration.

This component replaces the message node system with a single TextArea that
supports native text selection, copy operations, and automatic context tracking.
"""

import platform
import subprocess
import re
from typing import List, Tuple, Optional
from datetime import datetime

from textual.binding import Binding
from textual.widgets import TextArea
from textual.message import Message

# Import the context engine
from ..context_engine import ContextEngine


class ChatDisplay(TextArea):
    """
    A specialized TextArea for displaying chat messages with full native text selection support
    and intelligent context tracking.
    
    Features:
    - Native text selection across all messages
    - Standard copy shortcuts (Ctrl+C, Cmd+C, Ctrl+A, Cmd+A)
    - Cross-platform clipboard support
    - Message formatting with role indicators
    - Automatic scrolling to new messages
    - Intelligent context tracking and compression
    - Conversation persistence
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
    
    def __init__(self, context_engine: Optional[ContextEngine] = None, **kwargs):
        super().__init__(
            read_only=True,  # Make it read-only to prevent editing
            show_line_numbers=False,
            **kwargs
        )
        self.messages: List[Tuple[str, str, str]] = []  # (role, content, timestamp)
        self.auto_scroll = True
        
        # Context engine integration
        self.context_engine = context_engine
        self.context_enabled = context_engine is not None
        
        # Enhanced message tracking
        self.message_history: List[dict] = []  # More detailed message tracking
        
    def set_context_engine(self, context_engine: ContextEngine):
        """Set the context engine for this chat display"""
        self.context_engine = context_engine
        self.context_enabled = True
        
        # Load any existing messages from context engine
        if hasattr(context_engine, 'messages') and context_engine.messages:
            self.clear_messages()
            for msg in context_engine.messages:
                self._add_message_to_display(msg.content, msg.role, load_from_context=True)
        
    def add_message(self, content: str, role: str = "user") -> None:
        """Add a new message to the chat display with context tracking."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Strip Rich markup from content before storing
        clean_content = self._strip_rich_markup(content)
        
        # Store in local message list
        self.messages.append((role, clean_content, timestamp))
        
        # Add to context engine if available
        if self.context_enabled and self.context_engine:
            # Extract context tags for better categorization
            context_tags = self._extract_context_tags(clean_content, role)
            self.context_engine.add_message(role, clean_content, context_tags)
        
        # Add to detailed message history
        self.message_history.append({
            'role': role,
            'content': clean_content,
            'timestamp': timestamp,
            'raw_content': content,  # Keep original with markup for reference
            'tokens': len(clean_content) // 4  # Rough token estimate
        })
        
        self._rebuild_content()
        
        if self.auto_scroll:
            # Scroll to bottom after adding message
            self.cursor_location = self.document.end
    
    def _add_message_to_display(self, content: str, role: str, load_from_context: bool = False):
        """Internal method to add message to display without re-adding to context engine"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        clean_content = self._strip_rich_markup(content)
        
        self.messages.append((role, clean_content, timestamp))
        
        if not load_from_context:
            self.message_history.append({
                'role': role,
                'content': clean_content,
                'timestamp': timestamp,
                'raw_content': content,
                'tokens': len(clean_content) // 4
            })
        
        self._rebuild_content()
        
        if self.auto_scroll:
            self.cursor_location = self.document.end
    
    def _extract_context_tags(self, content: str, role: str) -> List[str]:
        """Extract context tags from message content for better categorization"""
        tags = []
        content_lower = content.lower()
        
        # Role-based tags
        tags.append(f"role:{role}")
        
        # Content-based tags
        if any(word in content_lower for word in ['error', 'failed', 'exception']):
            tags.append('type:error')
        elif any(word in content_lower for word in ['success', 'completed', 'done']):
            tags.append('type:success')
        elif any(word in content_lower for word in ['help', 'how', 'what', 'why']):
            tags.append('type:question')
        
        # Cloud provider tags
        if 'gcp' in content_lower or 'google cloud' in content_lower:
            tags.append('provider:gcp')
        elif 'aws' in content_lower:
            tags.append('provider:aws')
        elif 'azure' in content_lower:
            tags.append('provider:azure')
        
        # Operation tags
        operations = ['create', 'delete', 'update', 'list', 'get', 'set', 'deploy', 'build']
        for op in operations:
            if op in content_lower:
                tags.append(f'operation:{op}')
                break
        
        return tags
            
    def clear_messages(self) -> None:
        """Clear all messages from the chat display and optionally start new conversation"""
        self.messages.clear()
        self.message_history.clear()
        self.text = ""
        
        # Start new conversation in context engine
        if self.context_enabled and self.context_engine:
            self.context_engine.start_new_conversation()
        
    async def get_context_for_query(self, query: str) -> List[dict]:
        """Get relevant context for a new query using the context engine"""
        if not self.context_enabled or not self.context_engine:
            return []
        
        try:
            result = await self.context_engine.get_context_for_llm(query)
            
            if not isinstance(result, list):
                print(f"ERROR: context engine returned {type(result)}, expected list")
                return []
            
            valid_messages = []
            for item in result:
                if isinstance(item, dict) and 'role' in item and 'content' in item:
                    valid_messages.append(item)
                else:
                    print(f"WARNING: Invalid context message format: {item}")
            
            return valid_messages
            
        except Exception as e:
            print(f"Error getting context for query: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def get_conversation_summary(self) -> dict:
        """Get a summary of the current conversation"""
        if not self.context_enabled or not self.context_engine:
            return {
                'total_messages': len(self.messages),
                'context_available': False
            }
        
        try:
            stats = self.context_engine.get_context_stats()
            return {
                'conversation_id': stats['conversation_id'],
                'total_messages': stats['total_messages'],
                'context_available': True,
                'compression_ratio': stats['compression_ratio'],
                'total_tokens': stats['total_tokens'],
                'recent_messages': stats['recent_messages']
            }
        except Exception as e:
            print(f"Error getting conversation summary: {e}")
            return {'total_messages': len(self.messages), 'context_available': False}
    
    def load_conversation(self, conversation_id: str) -> bool:
        """Load a specific conversation by ID"""
        if not self.context_enabled or not self.context_engine:
            return False
        
        try:
            success = self.context_engine.load_conversation(conversation_id)
            if success:
                # Reload messages from context engine
                self.clear_messages()
                for msg in self.context_engine.messages:
                    self._add_message_to_display(msg.content, msg.role, load_from_context=True)
                return True
            return False
        except Exception as e:
            print(f"Error loading conversation {conversation_id}: {e}")
            return False
    
    def get_conversation_list(self) -> List[dict]:
        """Get list of available conversations"""
        if not self.context_enabled or not self.context_engine:
            return []
        
        try:
            return self.context_engine.get_conversation_list()
        except Exception as e:
            print(f"Error getting conversation list: {e}")
            return []
        
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
            if i > 0:
                lines.append("")
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