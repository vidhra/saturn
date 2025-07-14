"""
Content Dispatcher for Saturn Chat UI

This module handles routing structured content types from the state machine
to appropriate Textual widgets for proper rendering in the chat interface.
"""

import json
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

from textual.widgets import Static, DataTable, Tree, RichLog
from textual.containers import Vertical, Horizontal
from textual.widget import Widget
from rich.syntax import Syntax
from rich.panel import Panel
from rich.text import Text
from rich.json import JSON
from rich.progress import Progress

from saturn.content_types import (
    ContentItem, ContentType, ContentMetadata,
    TextContent, CodeContent, TableContent, PanelContent,
    ErrorContent, SuccessContent, WarningContent, ProgressContent,
    ListContent, TreeContent, JsonContent, CommandResultContent,
    StateUpdateContent, TreeNode
)


class ContentWidget(Vertical):
    """Base widget container for content items with metadata"""
    
    def __init__(self, content_item: ContentItem, **kwargs):
        super().__init__(**kwargs)
        self.content_item = content_item
        self.metadata = content_item.metadata
        self.content_id = f"{self.metadata.content_type.value}_{id(content_item)}"
    
    def compose(self):
        """Override in subclasses to compose the actual content"""
        yield Static("Base content widget - should be overridden")


class TextWidget(ContentWidget):
    """Widget for displaying text content"""
    
    def compose(self):
        content = self.content_item
        if content.markdown:
            # Use RichLog for markdown rendering
            rich_log = RichLog(auto_scroll=False, highlight=True, markup=True)
            rich_log.write(content.text)
            yield rich_log
        else:
            yield Static(content.text)


class CodeWidget(ContentWidget):
    """Widget for displaying code with syntax highlighting"""
    
    def compose(self):
        content = self.content_item
        
        # Create title if filename is provided
        if content.filename:
            yield Static(f"📄 {content.filename}", classes="code-filename")
        
        # Create syntax highlighted code using Rich
        rich_log = RichLog(auto_scroll=False, highlight=True, markup=True)
        syntax = Syntax(
            content.code, 
            content.language,
            line_numbers=content.line_numbers,
            theme="monokai"
        )
        rich_log.write(syntax)
        yield rich_log


class TableWidget(ContentWidget):
    """Widget for displaying structured tables"""
    
    def compose(self):
        content = self.content_item
        
        # Add title if provided
        if content.title:
            yield Static(content.title, classes="table-title")
        
        # Create DataTable
        table = DataTable(show_header=True, zebra_stripes=True)
        
        # Add columns
        for column in content.columns:
            table.add_column(column.header, width=column.width)
        
        # Add rows
        for row in content.rows:
            table.add_row(*row)
        
        yield table
        
        # Add caption if provided
        if content.caption:
            yield Static(content.caption, classes="table-caption")


class PanelWidget(ContentWidget):
    """Widget for displaying panel/box content"""
    
    def compose(self):
        content = self.content_item
        
        # Use RichLog to render a Rich Panel
        rich_log = RichLog(auto_scroll=False, highlight=True, markup=True)
        panel = Panel(
            content.content,
            title=content.title,
            border_style=content.border_style,
            padding=(content.padding, content.padding)
        )
        rich_log.write(panel)
        yield rich_log


class ErrorWidget(ContentWidget):
    """Widget for displaying error content with proper styling"""
    
    def compose(self):
        content = self.content_item
        
        # Error header
        error_header = f"❌ Error"
        if content.step_id:
            error_header += f" in {content.step_id}"
        if content.error_type:
            error_header += f" ({content.error_type})"
        
        yield Static(error_header, classes="error-header")
        
        # Main error message
        yield Static(content.message, classes="error-message")
        
        # Additional details
        if content.details:
            yield Static("Details:", classes="error-details-label")
            yield Static(content.details, classes="error-details")
        
        # Traceback if available
        if content.traceback:
            yield Static("Traceback:", classes="error-traceback-label")
            # Use code widget for traceback formatting
            rich_log = RichLog(auto_scroll=False, highlight=True)
            syntax = Syntax(content.traceback, "python", theme="monokai")
            rich_log.write(syntax)
            yield rich_log


class SuccessWidget(ContentWidget):
    """Widget for displaying success content"""
    
    def compose(self):
        content = self.content_item
        
        # Success header
        success_header = f"✅ Success"
        if content.step_id:
            success_header += f" - {content.step_id}"
        
        yield Static(success_header, classes="success-header")
        yield Static(content.message, classes="success-message")
        
        # Show result if available
        if content.result is not None:
            yield Static("Result:", classes="success-result-label")
            # Format result appropriately
            if isinstance(content.result, (dict, list)):
                rich_log = RichLog(auto_scroll=False, highlight=True)
                rich_log.write(JSON.from_data(content.result))
                yield rich_log
            else:
                yield Static(str(content.result), classes="success-result")


class WarningWidget(ContentWidget):
    """Widget for displaying warning content"""
    
    def compose(self):
        content = self.content_item
        
        yield Static(f"⚠️ Warning", classes="warning-header")
        yield Static(content.message, classes="warning-message")
        
        if content.details:
            yield Static("Details:", classes="warning-details-label")
            yield Static(content.details, classes="warning-details")


class ProgressWidget(ContentWidget):
    """Widget for displaying progress information"""
    
    def compose(self):
        content = self.content_item
        
        # Progress message
        progress_text = f"🔄 {content.message}"
        
        # Add percentage if available
        if content.percentage is not None:
            progress_text += f" ({content.percentage:.1f}%)"
        elif content.current is not None and content.total is not None:
            progress_text += f" ({content.current}/{content.total})"
        
        yield Static(progress_text, classes="progress-message")


class ListWidget(ContentWidget):
    """Widget for displaying list content"""
    
    def compose(self):
        content = self.content_item
        
        if content.title:
            yield Static(content.title, classes="list-title")
        
        # Create list content
        list_text = self._format_list_items(content.items, content.ordered)
        yield Static(list_text, classes="list-content")
    
    def _format_list_items(self, items: List[Union[str, ListContent]], ordered: bool, indent: int = 0) -> str:
        """Format list items recursively"""
        lines = []
        prefix = "  " * indent
        
        for i, item in enumerate(items, 1):
            if isinstance(item, ListContent):
                # Nested list
                lines.append(f"{prefix}{'►' if not ordered else f'{i}.'} {item.title or 'Nested List'}:")
                lines.append(self._format_list_items(item.items, item.ordered, indent + 1))
            else:
                # Simple item
                marker = f"{i}." if ordered else "•"
                lines.append(f"{prefix}{marker} {item}")
        
        return "\n".join(lines)


class TreeWidget(ContentWidget):
    """Widget for displaying tree/hierarchical content"""
    
    def compose(self):
        content = self.content_item
        
        if content.title:
            yield Static(content.title, classes="tree-title")
        
        # Create Textual Tree widget
        tree = Tree(content.root.label)
        self._populate_tree_node(tree.root, content.root)
        yield tree
    
    def _populate_tree_node(self, textual_node, content_node: TreeNode):
        """Recursively populate tree nodes"""
        for child in content_node.children:
            child_node = textual_node.add(child.label)
            if child.children:
                self._populate_tree_node(child_node, child)


class JsonWidget(ContentWidget):
    """Widget for displaying JSON/structured data"""
    
    def compose(self):
        content = self.content_item
        
        if content.title:
            yield Static(content.title, classes="json-title")
        
        # Use RichLog to display formatted JSON
        rich_log = RichLog(auto_scroll=False, highlight=True)
        if content.pretty:
            rich_log.write(JSON.from_data(content.data))
        else:
            rich_log.write(json.dumps(content.data))
        yield rich_log


class CommandResultWidget(ContentWidget):
    """Widget for displaying command execution results"""
    
    def compose(self):
        content = self.content_item
        
        # Command header with status
        status_icon = "✅" if content.success else "❌"
        command_header = f"{status_icon} Command: `{content.command}`"
        
        if content.exit_code is not None:
            command_header += f" (exit code: {content.exit_code})"
        
        if content.execution_time is not None:
            command_header += f" [{content.execution_time:.2f}s]"
        
        yield Static(command_header, classes="command-header")
        
        # Show stdout if available
        if content.stdout:
            yield Static("Output:", classes="command-output-label")
            # Use code widget for output formatting
            rich_log = RichLog(auto_scroll=False, highlight=True)
            syntax = Syntax(content.stdout, "text", theme="monokai")
            rich_log.write(syntax)
            yield rich_log
        
        # Show stderr if available
        if content.stderr:
            yield Static("Error Output:", classes="command-error-label")
            rich_log = RichLog(auto_scroll=False, highlight=True)
            syntax = Syntax(content.stderr, "text", theme="monokai")
            rich_log.write(syntax)
            yield rich_log


class StateUpdateWidget(ContentWidget):
    """Widget for displaying state machine updates"""
    
    def compose(self):
        content = self.content_item
        
        # State update with icon
        state_text = f"🔄 {content.state_name}: {content.message}"
        if content.operation:
            state_text += f" ({content.operation})"
        
        yield Static(state_text, classes="state-update")


class ContentDispatcher:
    """Dispatcher that routes content types to appropriate widgets"""
    
    # Map content types to widget classes
    WIDGET_MAP = {
        ContentType.TEXT: TextWidget,
        ContentType.CODE: CodeWidget,
        ContentType.TABLE: TableWidget,
        ContentType.PANEL: PanelWidget,
        ContentType.ERROR: ErrorWidget,
        ContentType.SUCCESS: SuccessWidget,
        ContentType.WARNING: WarningWidget,
        ContentType.PROGRESS: ProgressWidget,
        ContentType.LIST: ListWidget,
        ContentType.TREE: TreeWidget,
        ContentType.JSON: JsonWidget,
        ContentType.COMMAND_RESULT: CommandResultWidget,
        ContentType.STATE_UPDATE: StateUpdateWidget,
    }
    
    @classmethod
    def create_widget(cls, content_item: ContentItem) -> Widget:
        """Create appropriate widget for content item"""
        content_type = content_item.metadata.content_type
        widget_class = cls.WIDGET_MAP.get(content_type)
        
        if widget_class is None:
            # Fallback to text widget for unknown types
            from .content_types import TextContent, ContentMetadata
            fallback_content = TextContent(
                text=f"Unknown content type: {content_type}",
                metadata=ContentMetadata(ContentType.TEXT)
            )
            return TextWidget(fallback_content)
        
        return widget_class(content_item)
    
    @classmethod
    def get_widget_css_classes(cls, content_item: ContentItem) -> List[str]:
        """Get CSS classes for content item based on metadata"""
        classes = [
            f"content-{content_item.metadata.content_type.value}",
            f"priority-{content_item.metadata.priority}"
        ]
        
        # Add source state class if available
        if content_item.metadata.source_state:
            classes.append(f"from-{content_item.metadata.source_state.lower()}")
        
        # Add tag-based classes
        for tag in content_item.metadata.tags:
            classes.append(f"tag-{tag.replace(':', '-')}")
        
        return classes
    
    @classmethod
    def should_group_content(cls, content1: ContentItem, content2: ContentItem) -> bool:
        """Determine if two content items should be grouped together"""
        # Group items from same source and step
        return (
            content1.metadata.source_state == content2.metadata.source_state and
            content1.metadata.step_id == content2.metadata.step_id and
            content1.metadata.step_id is not None
        )


# Convenience function for dispatching content
def dispatch_content(content_item: ContentItem) -> Widget:
    """Create widget for content item"""
    return ContentDispatcher.create_widget(content_item) 