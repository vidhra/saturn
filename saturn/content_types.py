"""
Content Types for Saturn UI

This module defines the content types used by the Saturn UI system.
"""

from enum import Enum
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass


class ContentType(Enum):
    """Content type enumeration"""
    TEXT = "text"
    CODE = "code"

    PANEL = "panel"
    ERROR = "error"
    SUCCESS = "success"
    WARNING = "warning"
    PROGRESS = "progress"
    LIST = "list"
    TREE = "tree"
    JSON = "json"
    COMMAND_RESULT = "command_result"
    STATE_UPDATE = "state_update"


@dataclass
class ContentMetadata:
    """Metadata for content items"""
    content_type: ContentType
    source_state: str
    title: Optional[str] = None
    step_id: Optional[str] = None
    timestamp: Optional[str] = None


class ContentItem:
    """Base class for all content items"""
    
    def __init__(self, metadata: ContentMetadata):
        self.metadata = metadata


class ListContent(ContentItem):
    """Content for displaying lists (todo lists, etc.)"""
    
    def __init__(self, items: List[Dict[str, Any]], ordered: bool = False, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.LIST,
                source_state="system"
            )
        super().__init__(metadata)
        self.items = items
        self.ordered = ordered


class TextContent(ContentItem):
    """Content for displaying text"""
    
    def __init__(self, text: str, markdown: bool = False, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.TEXT,
                source_state="system"
            )
        super().__init__(metadata)
        self.text = text
        self.markdown = markdown


class CodeContent(ContentItem):
    """Content for displaying code"""
    
    def __init__(self, code: str, language: str = "python", filename: str = None, 
                 line_numbers: bool = True, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.CODE,
                source_state="system"
            )
        super().__init__(metadata)
        self.code = code
        self.language = language
        self.filename = filename
        self.line_numbers = line_numbers





class PanelContent(ContentItem):
    """Content for displaying panels"""
    
    def __init__(self, content: str, title: str = None, border_style: str = "white",
                 padding: int = 1, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.PANEL,
                source_state="system"
            )
        super().__init__(metadata)
        self.content = content
        self.title = title
        self.border_style = border_style
        self.padding = padding


class ErrorContent(ContentItem):
    """Content for displaying errors"""
    
    def __init__(self, message: str, error_type: str = None, details: str = None,
                 traceback: str = None, step_id: str = None, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.ERROR,
                source_state="system"
            )
        super().__init__(metadata)
        self.message = message
        self.error_type = error_type
        self.details = details
        self.traceback = traceback
        self.step_id = step_id


class SuccessContent(ContentItem):
    """Content for displaying success messages"""
    
    def __init__(self, message: str, result: Any = None, step_id: str = None, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.SUCCESS,
                source_state="system"
            )
        super().__init__(metadata)
        self.message = message
        self.result = result
        self.step_id = step_id


class WarningContent(ContentItem):
    """Content for displaying warnings"""
    
    def __init__(self, message: str, details: str = None, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.WARNING,
                source_state="system"
            )
        super().__init__(metadata)
        self.message = message
        self.details = details


class ProgressContent(ContentItem):
    """Content for displaying progress"""
    
    def __init__(self, message: str, percentage: float = None, current: int = None,
                 total: int = None, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.PROGRESS,
                source_state="system"
            )
        super().__init__(metadata)
        self.message = message
        self.percentage = percentage
        self.current = current
        self.total = total


class TreeNode:
    """Node for tree content"""
    
    def __init__(self, label: str, children: List['TreeNode'] = None, data: Any = None):
        self.label = label
        self.children = children or []
        self.data = data


class TreeContent(ContentItem):
    """Content for displaying trees"""
    
    def __init__(self, root: TreeNode, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.TREE,
                source_state="system"
            )
        super().__init__(metadata)
        self.root = root


class JsonContent(ContentItem):
    """Content for displaying JSON data"""
    
    def __init__(self, data: Any, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.JSON,
                source_state="system"
            )
        super().__init__(metadata)
        self.data = data


class CommandResultContent(ContentItem):
    """Content for displaying command results"""
    
    def __init__(self, command: str, stdout: str = None, stderr: str = None,
                 success: bool = True, exit_code: int = None, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.COMMAND_RESULT,
                source_state="system"
            )
        super().__init__(metadata)
        self.command = command
        self.stdout = stdout
        self.stderr = stderr
        self.success = success
        self.exit_code = exit_code


class StateUpdateContent(ContentItem):
    """Content for displaying state updates"""
    
    def __init__(self, state_name: str, message: str, metadata: ContentMetadata = None):
        if metadata is None:
            metadata = ContentMetadata(
                content_type=ContentType.STATE_UPDATE,
                source_state="system"
            )
        super().__init__(metadata)
        self.state_name = state_name
        self.message = message


class ContentBuilder:
    """Builder for creating content items"""
    
    def __init__(self, source_state: str = "system"):
        self.source_state = source_state
    
    def text(self, text: str, markdown: bool = False, **kwargs) -> TextContent:
        """Create a text content item"""
        metadata = ContentMetadata(
            content_type=ContentType.TEXT,
            source_state=self.source_state,
            **kwargs
        )
        return TextContent(text, markdown, metadata)
    
    def list(self, items: List[Dict[str, Any]], ordered: bool = False, **kwargs) -> ListContent:
        """Create a list content item"""
        metadata = ContentMetadata(
            content_type=ContentType.LIST,
            source_state=self.source_state,
            **kwargs
        )
        return ListContent(items, ordered, metadata) 