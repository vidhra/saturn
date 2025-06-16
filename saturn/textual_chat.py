import asyncio

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.reactive import reactive
from textual.scroll_view import ScrollView
from textual.widgets import Footer, Input, Static

from saturn.orchestrator import run_chat_conversational

from .config import load_config

# You may want to load config from cli.py or a config file
APP_CONFIG = load_config()


class ChatMessage(Static):
    def __init__(self, text: str, role: str = "user"):
        super().__init__(text)
        self.role = role
        self.update_style()

    def update_style(self):
        if self.role == "user":
            self.styles.background = "#1e90ff"
            self.styles.color = "white"
            self.styles.align_horizontal = "right"
        else:
            self.styles.background = "#222222"
            self.styles.color = "#00ff99"
            self.styles.align_horizontal = "left"


class SaturnChatApp(App):
    CSS_PATH = None
    BINDINGS = [("ctrl+c", "quit", "Quit")]

    chat_history = reactive([])

    def compose(self) -> ComposeResult:
        yield ScrollView(id="chat_transcript")
        yield Input(placeholder="Type your cloud query here...", id="chat_input")
        yield Footer()

    async def on_mount(self) -> None:
        print("on_mount called!")
        self.query_one("#chat_input", Input).focus()
        self.chat_history.append(
            {
                "text": "Welcome to Saturn Cloud Chat! Ask me anything about your cloud.",
                "role": "assistant",
            }
        )
        print("Chat history after welcome:", self.chat_history)
        self.update_transcript()
        self.user_input_queue = asyncio.Queue()
        self.config_for_chat = APP_CONFIG.copy()
        self.config_for_chat.setdefault("vector_store_choice", "default")
        self.config_for_chat.setdefault("db_config", {})
        self.config_for_chat.setdefault(
            "rag_embedding_model", "local:BAAI/bge-small-en-v1.5"
        )
        self.config_for_chat.setdefault("rag_build_on_init", False)
        self.config_for_chat.setdefault("rag_docs_path_for_init", None)
        self.background_task = asyncio.create_task(self.conversation_loop())

    def update_transcript(self):
        print("update_transcript called!")
        transcript = self.query_one("#chat_transcript", ScrollView)
        print("Transcript widget:", transcript)
        print("Current chat history:", self.chat_history)
        # Remove all children manually for compatibility
        transcript.remove(*list(transcript.children))
        transcript.mount(
            Vertical(
                *[ChatMessage(msg["text"], msg["role"]) for msg in self.chat_history]
            )
        )
        transcript.scroll_end(animate=False)

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        user_text = event.value.strip()
        print(f"User submitted: {user_text}")  # Debug print
        if not user_text:
            return
        await self.user_input_queue.put(user_text)
        event.input.value = ""

    async def conversation_loop(self):
        async def user_input_stream():
            while True:
                user_input = await self.user_input_queue.get()
                print(f"conversation_loop got user input: {user_input}")  # Debug print
                yield user_input

        try:
            async for role, message in run_chat_conversational(
                self.config_for_chat, user_input_stream()
            ):
                print(
                    f"Received from run_chat_conversational: role={role}, message={message}"
                )  # Debug print
                self.chat_history.append({"text": message, "role": role})
                self.update_transcript()
        except Exception as e:
            print(f"Exception in conversation_loop: {e}")  # Debug print
            self.chat_history.append(
                {"text": f"[red]Error: {e}[/red]", "role": "assistant"}
            )
            self.update_transcript()


if __name__ == "__main__":
    SaturnChatApp().run()
