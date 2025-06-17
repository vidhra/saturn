import asyncio
import sys
from typing import AsyncGenerator, Tuple
import os
import shutil

from .config import load_config
from .orchestrator import run_chat_conversational
from .prompts import SYSTEM_CHAT_PROMPT

APP_CONFIG = load_config()

# ANSI color codes for terminal output
COLORS = {
    'blue': '\033[94m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}

# Terminal control sequences
CLEAR_SCREEN = '\033[2J'
CLEAR_LINE = '\033[K'
SAVE_CURSOR = '\033[s'
RESTORE_CURSOR = '\033[u'
MOVE_TO_BOTTOM = '\033[{};0H'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'
MOVE_UP = '\033[A'

class Message:
    def __init__(self, text: str, role: str, color: str = 'white', bold: bool = False):
        self.text = text
        self.role = role
        self.color = color
        self.bold = bold
        
    def format(self) -> str:
        color_code = COLORS.get(self.color, '')
        bold_code = COLORS['bold'] if self.bold else ''
        return f"{color_code}{bold_code}{self.text}{COLORS['reset']}"

class TerminalManager:
    """Manages terminal display and cursor positioning."""
    
    def __init__(self):
        self.terminal_height, self.terminal_width = shutil.get_terminal_size()
        self.content_height = self.terminal_height - 2  # Reserve 2 lines for input
        self.messages: list[Message] = []
        self.input_line = ""
        self.input_prefix = "👤 You: "
        
    def clear_screen(self):
        """Clear the entire screen."""
        print(CLEAR_SCREEN, end='')
        sys.stdout.flush()
        
    def update_dimensions(self):
        """Update terminal dimensions."""
        self.terminal_height, self.terminal_width = shutil.get_terminal_size()
        self.content_height = self.terminal_height - 2
        
    def add_message(self, text: str, role: str, color: str = 'white', bold: bool = False):
        """Add a message to the history."""
        # Split multi-line messages and preserve formatting
        lines = text.split('\n')
        for line in lines:
            if line.strip():  # Only add non-empty lines
                self.messages.append(Message(line, role, color, bold))
        self._redraw()
        
    def _redraw(self):
        """Redraw the entire screen."""
        print(HIDE_CURSOR, end='')  # Hide cursor during redraw
        self.clear_screen()
        
        # Calculate how many messages we can show
        visible_messages = self.messages[-self.content_height:] if len(self.messages) > self.content_height else self.messages
        
        # Print messages
        for msg in visible_messages:
            print(msg.format())
        
        # Move to input line and show cursor
        print(MOVE_TO_BOTTOM.format(self.terminal_height - 1), end='')
        print(CLEAR_LINE, end='')
        print(f"{COLORS['blue']}{COLORS['bold']}{self.input_prefix}{COLORS['reset']}", end='', flush=True)
        print(SHOW_CURSOR, end='')  # Show cursor after positioning
        sys.stdout.flush()

terminal = TerminalManager()

def print_header() -> None:
    """Print the Saturn chat header."""
    terminal.add_message("=" * shutil.get_terminal_size().columns, "system", 'cyan')
    terminal.add_message("Welcome to Saturn!", "system", 'cyan', bold=True)
    terminal.add_message("Ask, act, plan, search, or chat with your cloud.", "system", 'cyan')
    terminal.add_message("=" * shutil.get_terminal_size().columns, "system", 'cyan')
    terminal.add_message("", "system")  # Empty line after header

def print_assistant_message(message: str) -> None:
    """Print an assistant message with proper formatting."""
    terminal.add_message("\n🤖 Assistant:", "assistant", 'green', bold=True)
    # Handle markdown-style formatting
    for line in message.split('\n'):
        if line.startswith('**') and line.endswith('**'):
            terminal.add_message(line.strip('*'), "assistant", 'green', bold=True)
        elif line.startswith('[') and ']' in line:
            color = line[1:line.index(']')].lower()
            text = line[line.index(']')+1:].strip()
            terminal.add_message(text, "assistant", color)
        else:
            terminal.add_message(line, "assistant", 'green')

def print_user_message(message: str) -> None:
    """Print a user message with proper formatting."""
    terminal.add_message(f"{terminal.input_prefix}{message}", "user", 'white')

def print_thinking() -> None:
    """Print a thinking indicator."""
    terminal.add_message("\n🤔 Thinking...", "system", 'magenta')

def clear_thinking() -> None:
    """Clear the thinking indicator."""
    # Remove the last message if it's the thinking indicator
    if terminal.messages and "🤔 Thinking..." in terminal.messages[-1].text:
        terminal.messages.pop()
        terminal._redraw()

async def get_user_input() -> AsyncGenerator[str, None]:
    """Asynchronously get user input."""
    while True:
        try:
            # Position cursor and show input prefix
            print(MOVE_TO_BOTTOM.format(terminal.terminal_height - 1), end='')
            print(CLEAR_LINE, end='')
            print(f"{COLORS['blue']}{COLORS['bold']}{terminal.input_prefix}{COLORS['reset']}", end='', flush=True)
            print(SHOW_CURSOR, end='')  # Ensure cursor is visible
            sys.stdout.flush()
            
            user_input = input()
            print(HIDE_CURSOR, end='')  # Hide cursor during processing
            
            if user_input.strip().lower() in {'exit', 'quit', 'bye'}:
                terminal.add_message("\n👋 Goodbye!", "system", 'cyan', bold=True)
                break
            if user_input.strip():
                terminal.add_message(f"{terminal.input_prefix}{user_input.strip()}", "user", 'white')
                yield user_input.strip()
        except (KeyboardInterrupt, EOFError):
            print(HIDE_CURSOR, end='')
            terminal.add_message("\n\n👋 Goodbye!", "system", 'cyan', bold=True)
            break
        except Exception as e:
            print(HIDE_CURSOR, end='')
            terminal.add_message(f"\nError reading input: {str(e)}", "system", 'red', bold=True)
        finally:
            sys.stdout.flush()

class SaturnChatApp:
    """A simple but elegant command-line chat interface for Saturn."""
    
    def __init__(self):
        self.config = APP_CONFIG.copy()
        self.config.setdefault("vector_store_choice", "default")
        self.config.setdefault("db_config", {})
        self.config.setdefault("rag_embedding_model", "local:BAAI/bge-small-en-v1.5")
        self.config.setdefault("rag_build_on_init", False)
        self.config.setdefault("rag_docs_path_for_init", None)

    async def run(self) -> None:
        """Run the chat application."""
        try:
            # Initial setup
            print(HIDE_CURSOR, end='')
            terminal.clear_screen()
            print_header()
            
            async for role, message in run_chat_conversational(
                self.config, get_user_input()
            ):
                if role == "user":
                    print_user_message(message)
                    print_thinking()
                else:
                    clear_thinking()
                    print_assistant_message(message)
                    
        except Exception as e:
            terminal.add_message(f"\n❌ Error: {str(e)}", "system", 'red', bold=True)
        finally:
            # Always ensure cursor is visible when exiting
            print(SHOW_CURSOR, end='')
            sys.stdout.flush()

def run():
    """Entry point for the chat application."""
    app = SaturnChatApp()
    asyncio.run(app.run())

if __name__ == "__main__":
    run()
