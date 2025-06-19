import asyncio
import shutil
import sys
from typing import AsyncGenerator

from .config import load_config
from .orchestrator import run_chat_conversational

APP_CONFIG = load_config()

COLORS = {
    "blue": "\033[94m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "bold": "\033[1m",
    "reset": "\033[0m",
}

# Terminal control sequences
CLEAR_SCREEN = "\033[2J"
CLEAR_LINE = "\033[K"
SAVE_CURSOR = "\033[s"
RESTORE_CURSOR = "\033[u"
MOVE_TO_BOTTOM = "\033[{};0H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
MOVE_UP = "\033[A"


class Message:
    def __init__(self, text: str, role: str, color: str = "white", bold: bool = False):
        self.text = text
        self.role = role
        self.color = color
        self.bold = bold

    def format(self) -> str:
        color_code = COLORS.get(self.color, "")
        bold_code = COLORS["bold"] if self.bold else ""
        return f"{color_code}{bold_code}{self.text}{COLORS['reset']}"


class TerminalManager:
    """Manages terminal display and cursor positioning."""

    def __init__(self):
        self.terminal_height, self.terminal_width = shutil.get_terminal_size()
        self.content_height = self.terminal_height - 2
        self.messages: list[Message] = []
        self.input_line = ""
        self.input_prefix = "👤 You: "
        self.thinking_task = None
        self._thinking_active = False

    def clear_screen(self):
        """Clear the entire screen."""
        print(CLEAR_SCREEN, end="")
        sys.stdout.flush()

    def update_dimensions(self):
        """Update terminal dimensions."""
        self.terminal_height, self.terminal_width = shutil.get_terminal_size()
        self.content_height = self.terminal_height - 2

    def add_message(
        self, text: str, role: str, color: str = "white", bold: bool = False
    ):
        """Add a message to the history."""
        lines = text.split("\n")
        for line in lines:
            if line.strip():
                self.messages.append(Message(line, role, color, bold))
        self._redraw()

    def _redraw(self):
        """Redraw the entire screen."""
        print(HIDE_CURSOR, end="")
        self.clear_screen()

        visible_messages = (
            self.messages[-self.content_height :]
            if len(self.messages) > self.content_height
            else self.messages
        )
        for msg in visible_messages:
            print(msg.format())

        print(MOVE_TO_BOTTOM.format(self.terminal_height - 1), end="")
        print(CLEAR_LINE, end="")
        print(
            f"{COLORS['blue']}{COLORS['bold']}{self.input_prefix}{COLORS['reset']}",
            end="",
            flush=True,
        )
        print(SHOW_CURSOR, end="")
        sys.stdout.flush()

    async def start_thinking(self):
        self._thinking_active = True
        base = "\n🤔 Thinking"
        dots = [".", "..", "..."]
        idx = 0
        while self._thinking_active:
            if self.messages and "🤔 Thinking" in self.messages[-1].text:
                self.messages[-1] = Message(base + dots[idx], "system", "magenta")
            else:
                self.add_message(base + dots[idx], "system", "magenta")
            self._redraw()
            idx = (idx + 1) % 3
            await asyncio.sleep(0.5)

    def stop_thinking(self):
        self._thinking_active = False
        if self.messages and "🤔 Thinking" in self.messages[-1].text:
            self.messages.pop()
            self._redraw()


terminal = TerminalManager()


def print_header() -> None:
    """Print the Saturn chat header."""
    terminal.add_message("=" * shutil.get_terminal_size().columns, "system", "cyan")
    terminal.add_message("Welcome to Saturn!", "system", "cyan", bold=True)
    terminal.add_message(
        "Ask, act, plan, search, or chat with your cloud.", "system", "cyan"
    )
    terminal.add_message("=" * shutil.get_terminal_size().columns, "system", "cyan")


def print_assistant_message(message: str) -> None:
    """Print an assistant message with proper formatting."""
    terminal.add_message("\n🤖 Assistant:", "assistant", "green", bold=True)
    for line in message.split("\n"):
        if "[" in line and "]" in line:
            while "[" in line and "]" in line:
                start = line.find("[")
                end = line.find("]")
                if start > -1 and end > -1:
                    format_tag = line[start + 1 : end]
                    if format_tag.startswith("/"):
                        line = line[:start] + line[end + 1 :]
                    else:
                        parts = format_tag.split()
                        color = parts[0].lower() if parts else "white"
                        is_bold = "bold" in format_tag.lower()
                        text = line[end + 1 :]
                        next_tag = text.find("[")
                        if next_tag > -1:
                            text = text[:next_tag]
                            line = line[:start] + text + line[start + next_tag :]
                        else:
                            line = line[:start] + text
                        if text.strip():
                            terminal.add_message(
                                text.strip(), "assistant", color, is_bold
                            )
                        break
        else:
            if line.strip():
                terminal.add_message(line, "assistant", "green")


def print_user_message(message: str) -> None:
    """Print a user message with proper formatting."""
    terminal.add_message(f"{terminal.input_prefix}{message}", "user", "white")


async def get_user_input() -> AsyncGenerator[str, None]:
    """Asynchronously get user input."""
    while True:
        try:
            print(MOVE_TO_BOTTOM.format(terminal.terminal_height - 1), end="")
            print(CLEAR_LINE, end="")
            print(
                f"{COLORS['blue']}{COLORS['bold']}{terminal.input_prefix}{COLORS['reset']}",
                end="",
                flush=True,
            )
            print(SHOW_CURSOR, end="")
            sys.stdout.flush()

            user_input = input()
            print(HIDE_CURSOR, end="")
            if user_input.strip().lower() in {"exit", "quit", "bye"}:
                terminal.add_message("\n👋 Goodbye!", "system", "cyan", bold=True)
                break
            if user_input.strip():
                terminal.add_message(
                    f"{terminal.input_prefix}{user_input.strip()}", "user", "white"
                )
                yield user_input.strip()
        except (KeyboardInterrupt, EOFError):
            print(HIDE_CURSOR, end="")
            terminal.add_message("\n\n👋 Goodbye!", "system", "cyan", bold=True)
            break
        except Exception as e:
            print(HIDE_CURSOR, end="")
            terminal.add_message(
                f"\nError reading input: {str(e)}", "system", "red", bold=True
            )
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
        self.thinking_task = None

    async def run(self) -> None:
        """Run the chat application."""
        try:
            print(HIDE_CURSOR, end="")
            terminal.clear_screen()
            print_header()

            async for role, message in run_chat_conversational(
                self.config, get_user_input()
            ):
                if role == "user":
                    print_user_message(message)
                    # Cancel any existing thinking task
                    if self.thinking_task and not self.thinking_task.done():
                        self.thinking_task.cancel()
                        try:
                            await self.thinking_task
                        except asyncio.CancelledError:
                            pass
                    # Start new thinking task
                    self.thinking_task = asyncio.create_task(terminal.start_thinking())
                else:
                    # Stop thinking animation
                    if self.thinking_task and not self.thinking_task.done():
                        self.thinking_task.cancel()
                        try:
                            await self.thinking_task
                        except asyncio.CancelledError:
                            pass
                    terminal.stop_thinking()
                    print_assistant_message(message)
                    await asyncio.sleep(0.1)

        except Exception as e:
            terminal.add_message(f"\n❌ Error: {str(e)}", "system", "red", bold=True)
        finally:
            if self.thinking_task and not self.thinking_task.done():
                self.thinking_task.cancel()
                try:
                    await self.thinking_task
                except asyncio.CancelledError:
                    pass
            print(SHOW_CURSOR, end="")
            sys.stdout.flush()


def run():
    """Entry point for the chat application."""
    app = SaturnChatApp()
    asyncio.run(app.run())


if __name__ == "__main__":
    run()
