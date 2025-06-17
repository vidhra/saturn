import asyncio
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Footer, Input, Static, Markdown, Label, ListView, ListItem
from textual.widget import Widget
from textual.reactive import reactive
from saturn.orchestrator import run_chat_conversational
from .config import load_config
from saturn.prompts import CHAT_HEADER_PROMPT
import sys
import io
from textual.scroll_view import ScrollView
import re

APP_CONFIG = load_config()
USER_ICON = "👤"
ASSISTANT_ICON = "🤖"

MAX_CHAT_LINES = 15

ANSI_ESCAPE_RE = re.compile(r'\x1b\[[0-9;]*[mGKHF]')
def strip_ansi(text):
    return ANSI_ESCAPE_RE.sub('', text)

class ChatMessageItem(ListItem):
    def __init__(self, text: str, role: str = "user"):
        super().__init__()
        self.text = strip_ansi(text)
        self.role = role

    def compose(self) -> ComposeResult:
        if self.role == "assistant":
            bubble = Markdown(self.text, id="assistant-bubble")
            icon = Label(ASSISTANT_ICON, id="assistant-icon")
            yield Horizontal(icon, bubble, id="assistant-row")
        elif self.role == "thinking":
            yield Static("[italic]Thinking…[/italic]", id="thinking-indicator")
        else:
            bubble = Static(self.text, id="user-bubble")
            icon = Label(USER_ICON, id="user-icon")
            yield Horizontal(bubble, icon, id="user-row")

class StdoutCatcher(io.StringIO):
    def __init__(self, app):
        super().__init__()
        self.app = app
    def write(self, s):
        if s.strip():
            self.app.add_message(s.rstrip(), "system")
        return super().write(s)
    def flush(self):
        pass

class SaturnChatApp(App):
    CSS_PATH = None
    BINDINGS = [("ctrl+c", "quit", "Quit")]
    chat_history = reactive([])
    thinking_item = None

    def compose(self) -> ComposeResult:
        yield Static(CHAT_HEADER_PROMPT, id="chat-header")
        yield ScrollView(Vertical(id="chat_transcript"), id="chat_scroll")
        yield Input(placeholder="Type your cloud query here...", id="chat_input")
        yield Footer()

    async def on_mount(self) -> None:
        self.query_one("#chat_input", Input).focus()
        self.transcript_vertical = self.query_one("#chat_transcript", Vertical)
        self.scroll_view = self.query_one("#chat_scroll", ScrollView)
        self.add_message("Welcome to Saturn Cloud Chat! Ask me anything about your cloud.", "assistant")
        self.user_input_queue = asyncio.Queue()
        self.config_for_chat = APP_CONFIG.copy()
        self.config_for_chat.setdefault("vector_store_choice", "default")
        self.config_for_chat.setdefault("db_config", {})
        self.config_for_chat.setdefault("rag_embedding_model", "local:BAAI/bge-small-en-v1.5")
        self.config_for_chat.setdefault("rag_build_on_init", False)
        self.config_for_chat.setdefault("rag_docs_path_for_init", None)
        # Redirect stdout/stderr
        sys.stdout = StdoutCatcher(self)
        sys.stderr = StdoutCatcher(self)
        self.background_task = asyncio.create_task(self.conversation_loop())

    def add_message(self, text, role):
        item = ChatMessageItem(text, role)
        self.transcript_vertical.mount(item)
        self.chat_history.append({"text": text, "role": role})
        self.scroll_view.scroll_end(animate=False)

    def add_thinking(self):
        if not self.thinking_item:
            self.thinking_item = ChatMessageItem("[italic]Thinking…[/italic]", "thinking")
            self.transcript_vertical.mount(self.thinking_item)
            self.scroll_view.scroll_end(animate=False)

    def remove_thinking(self):
        if self.thinking_item and self.thinking_item in self.transcript_vertical.children:
            self.transcript_vertical.remove(self.thinking_item)
        self.thinking_item = None

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        user_text = event.value.strip()
        if not user_text:
            return
        self.add_message(user_text, "user")
        event.input.value = ""
        self.add_thinking()
        await asyncio.sleep(0)  # Yield to event loop so UI updates
        await self.user_input_queue.put(user_text)

    async def conversation_loop(self):
        async def user_input_stream():
            while True:
                user_input = await self.user_input_queue.get()
                yield user_input
        try:
            async for role, message in run_chat_conversational(
                self.config_for_chat, user_input_stream()
            ):
                self.remove_thinking()
                self.add_message(message, role)
        except Exception as e:
            self.remove_thinking()
            self.add_message(f"[red]Error: {e}[/red]", "assistant")

    CSS = '''
#chat-header {
    background: #181825;
    color: #00ff99;
    padding: 1 2;
    text-align: center;
    height: 2;
    content-align: center middle;
    border-bottom: solid #333333;
}
#assistant-row {
    align-horizontal: left;
    margin: 1 0 0 0;
    padding: 1 0 1 0;
}
#assistant-icon {
    color: #00ff99;
    padding-right: 1;
}
#assistant-bubble {
    background: #222222;
    color: #00ff99;
    border: round #00ff99;
    padding: 1 2;
    max-width: 80%;
}
#user-row {
    align-horizontal: right;
    margin: 1 0 0 0;
    padding: 1 0 1 0;
}
#user-icon {
    color: #1e90ff;
    padding-left: 1;
}
#user-bubble {
    background: #1e90ff;
    color: white;
    border: round #1e90ff;
    padding: 1 2;
    max-width: 80%;
}
#thinking-indicator {
    color: #888888;
    text-style: italic;
    padding: 1 2;
    text-align: left;
}
#chat_transcript {
    padding: 1 0 1 0;
    min-height: 10;
    height: 15;
    max-height: 15;
    overflow: hidden;
}
'''

if __name__ == "__main__":
    SaturnChatApp().run()
