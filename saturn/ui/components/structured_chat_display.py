"""
Structured Chat Display Component

This component replaces the regex-based text stripping approach with native 
structured content rendering using the content dispatcher system.
"""

import platform
import subprocess
from typing import List, Optional, Union
from datetime import datetime

from textual.binding import Binding
from textual.containers import VerticalScroll, Vertical
from textual.widgets import Static, RichLog
from textual.widget import Widget
from textual.message import Message
from textual import work

from ..context_engine import ContextEngine
from saturn.content_types import ContentItem, TextContent, ContentBuilder
from ..content_dispatcher import ContentDispatcher, dispatch_content


class StructuredChatDisplay(VerticalScroll):
    """
    A chat display that handles structured content types from the state machine.
    
    Features:
    - Native rendering of structured content (tables, code, panels, etc.)
    - No regex stripping - content is properly typed from source
    - Copy operations work on individual content items
    - Context engine integration for conversation management
    - Automatic scrolling and message grouping
    """
    
    BINDINGS = [
        Binding("ctrl+c,cmd+c", "copy_selection", "Copy", show=True),
        Binding("ctrl+a,cmd+a", "select_all", "Select All", show=True),
        Binding("ctrl+shift+c", "copy_last_message", "Copy Last", show=False),
    ]
    
    def __init__(self, context_engine: Optional[ContextEngine] = None, **kwargs):
        super().__init__(**kwargs)
        self.messages: List[tuple] = []  # (role, content, timestamp, is_structured)
        self.content_widgets: List[Widget] = []
        self.auto_scroll = True
        
        # Context engine integration
        self.context_engine = context_engine
        self.context_enabled = context_engine is not None
        
        # Content tracking
        self.message_history: List[dict] = []
        self.current_message_group: Optional[str] = None
    
    def set_context_engine(self, context_engine: ContextEngine):
        """Set the context engine for this chat display"""
        self.context_engine = context_engine
        self.context_enabled = True
    
    def add_message(self, content: Union[str, ContentItem], role: str = "user") -> None:
        """Add a message to the chat display - can be text or structured content"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if isinstance(content, ContentItem):
            # Structured content
            self._add_structured_content(content, role, timestamp)
        else:
            # Plain text content - convert to TextContent
            text_content = ContentBuilder(source_state=f"{role}_message").text(
                str(content),
                tags=[role]
            )
            self._add_structured_content(text_content, role, timestamp)
    
    def add_structured_content(self, content_item: ContentItem) -> None:
        """Add structured content directly (from state machine)"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        role = content_item.metadata.source_state or "system"
        self._add_structured_content(content_item, role, timestamp)
    
    def _add_structured_content(self, content_item: ContentItem, role: str, timestamp: str):
        """Internal method to add structured content"""
        # Store message
        self.messages.append((role, content_item, timestamp, True))
        
        # Add to context engine if available
        if self.context_enabled and self.context_engine:
            # Convert structured content to text for context tracking
            content_text = self._extract_text_from_content(content_item)
            context_tags = self._extract_context_tags(content_text, role, content_item)
            self.context_engine.add_message(role, content_text, context_tags)
        
        # Add to detailed message history
        self.message_history.append({
            'role': role,
            'content_item': content_item,
            'timestamp': timestamp,
            'content_type': content_item.metadata.content_type.value,
            'source_state': content_item.metadata.source_state,
            'step_id': content_item.metadata.step_id,
            'tokens': self._estimate_tokens(content_item)
        })
        
        # Create and add widget
        self._add_content_widget(content_item, role, timestamp)
        
        if self.auto_scroll:
            self.scroll_end()
    
    def _add_content_widget(self, content_item: ContentItem, role: str, timestamp: str):
        """Create and add widget for content item"""
        # Create role header
        role_icons = {
            "user": "👤",
            "assistant": "🤖", 
            "system": "⚙️",
            "ExecutingState": "⚡",
            "PlanningState": "📋",
            "ReasoningState": "🧠"
        }
        
        icon = role_icons.get(role, "📄")
        header_text = f"{icon} {role.title()}"
        if content_item.metadata.step_id:
            header_text += f" - {content_item.metadata.step_id}"
        header_text += f" ({timestamp})"
        
        # Add message header
        header = Static(header_text, classes=f"message-header {role}-header")
        self.mount(header)
        self.content_widgets.append(header)
        
        # Create content widget using dispatcher
        content_widget = dispatch_content(content_item)
        content_widget.add_class(f"message-content")
        content_widget.add_class(f"{role}-content")
        
        # Add CSS classes from dispatcher
        css_classes = ContentDispatcher.get_widget_css_classes(content_item)
        for css_class in css_classes:
            content_widget.add_class(css_class)
        
        # Mount the content widget
        self.mount(content_widget)
        self.content_widgets.append(content_widget)
        
        # Add spacing
        spacer = Static("", classes="message-spacer")
        self.mount(spacer)
        self.content_widgets.append(spacer)
    
    def _extract_text_from_content(self, content_item: ContentItem) -> str:
        """Extract text representation from structured content for context engine"""
        from saturn.content_types import (
            TextContent, CodeContent, TableContent, PanelContent,
            ErrorContent, SuccessContent, WarningContent, ProgressContent,
            CommandResultContent, StateUpdateContent, JsonContent
        )
        
        if isinstance(content_item, TextContent):
            return content_item.text
        elif isinstance(content_item, CodeContent):
            return f"Code ({content_item.language}):\n{content_item.code}"
        elif isinstance(content_item, TableContent):
            # Convert table to text representation
            headers = [col.header for col in content_item.columns]
            table_text = f"Table: {content_item.title or 'Untitled'}\n"
            table_text += " | ".join(headers) + "\n"
            table_text += "-" * (len(table_text.split('\n')[-2])) + "\n"
            for row in content_item.rows:
                table_text += " | ".join(row) + "\n"
            return table_text
        elif isinstance(content_item, PanelContent):
            return f"Panel ({content_item.title}): {content_item.content}"
        elif isinstance(content_item, ErrorContent):
            return f"Error: {content_item.message}"
        elif isinstance(content_item, SuccessContent):
            return f"Success: {content_item.message}"
        elif isinstance(content_item, WarningContent):
            return f"Warning: {content_item.message}"
        elif isinstance(content_item, ProgressContent):
            return f"Progress: {content_item.message}"
        elif isinstance(content_item, CommandResultContent):
            return f"Command '{content_item.command}' -> {content_item.stdout or 'No output'}"
        elif isinstance(content_item, StateUpdateContent):
            return f"State {content_item.state_name}: {content_item.message}"
        elif isinstance(content_item, JsonContent):
            return f"JSON Data: {str(content_item.data)[:200]}..."
        else:
            return str(content_item)
    
    def _extract_context_tags(self, content_text: str, role: str, content_item: ContentItem) -> List[str]:
        """Extract context tags from content for context engine"""
        tags = [f"role:{role}"]
        tags.append(f"type:{content_item.metadata.content_type.value}")
        
        if content_item.metadata.source_state:
            tags.append(f"state:{content_item.metadata.source_state}")
        
        if content_item.metadata.step_id:
            tags.append(f"step:{content_item.metadata.step_id}")
        
        # Add content-specific tags
        content_lower = content_text.lower()
        if any(word in content_lower for word in ['error', 'failed', 'exception']):
            tags.append('outcome:error')
        elif any(word in content_lower for word in ['success', 'completed', 'done']):
            tags.append('outcome:success')
        
        # Add existing metadata tags
        tags.extend(content_item.metadata.tags)
        
        return tags
    
    def _estimate_tokens(self, content_item: ContentItem) -> int:
        """Rough token estimation for content items"""
        text = self._extract_text_from_content(content_item)
        return len(text) // 4  # Rough estimate
    
    def clear_messages(self) -> None:
        """Clear all messages and widgets"""
        self.messages.clear()
        self.message_history.clear()
        
        # Remove all content widgets
        for widget in self.content_widgets:
            if widget.parent:
                widget.remove()
        self.content_widgets.clear()
        
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
                self.clear_messages()
                # Convert stored messages back to structured content
                for msg in self.context_engine.messages:
                    # Create text content for loaded messages
                    text_content = ContentBuilder().text(msg.content, tags=msg.tags or [])
                    self._add_structured_content(text_content, msg.role, msg.timestamp)
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
    
    def action_copy_selection(self) -> None:
        """Copy selected text to clipboard - implementation depends on focused widget"""
        # Find the currently focused widget and attempt to copy from it
        focused = self.app.focused
        if hasattr(focused, 'selected_text') and focused.selected_text:
            self._copy_to_clipboard(focused.selected_text, "selection")
        else:
            self.notify("No text selected", severity="warning")
    
    def action_select_all(self) -> None:
        """Select all in the focused widget"""
        focused = self.app.focused
        if hasattr(focused, 'select_all'):
            focused.select_all()
            self.notify("All text selected")
        else:
            self.notify("Select all not available", severity="warning")
    
    def action_copy_last_message(self) -> None:
        """Copy the last assistant message to clipboard"""
        for role, content_item, _, _ in reversed(self.messages):
            if role == "assistant":
                text = self._extract_text_from_content(content_item)
                self._copy_to_clipboard(text, "last assistant message")
                return
        
        self.notify("No assistant messages found", severity="warning")
    
    def _copy_to_clipboard(self, text: str, description: str) -> None:
        """Copy text to clipboard using platform-specific commands"""
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
    
    def get_message_count(self) -> int:
        """Get the total number of messages"""
        return len(self.messages)
    
    def get_messages_by_role(self, role: str) -> List[tuple]:
        """Get all messages by a specific role"""
        return [(content_item, timestamp) for r, content_item, timestamp, _ in self.messages if r == role] 