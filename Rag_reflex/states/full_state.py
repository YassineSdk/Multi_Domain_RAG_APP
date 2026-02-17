import reflex as rx
import uuid
from datetime import datetime
from openai import OpenAI
from sqlmodel import Field, select, desc


# ─────────────────────────────────────────────
#  DB MODELS
# ─────────────────────────────────────────────

class Conversation(rx.Model, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)


class Message(rx.Model, table=True):
    id: int | None = Field(default=None, primary_key=True)
    conv_id: str
    role: str        # "user" or "assistant"
    content: str
    created_at: datetime = Field(default_factory=datetime.now)


# ─────────────────────────────────────────────
#  LLM
# ─────────────────────────────────────────────

def llm_response(question: str) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="your-api-key-here",  # 🔑 replace with your key
    )
    response = client.chat.completions.create(
        model="openrouter/aurora-alpha",
        messages=[
            {"role": "user", "content": question}
        ],
        extra_body={"reasoning": {"enabled": True}}
    )
    return response.choices[0].message.content


# ─────────────────────────────────────────────
#  UI MESSAGE MODEL (not stored in DB)
# ─────────────────────────────────────────────

class ChatMessage(rx.Base):
    role: str
    content: str


# ─────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────

class ChatState(rx.State):
    messages: list[ChatMessage] = []
    question: str = ""
    is_loading: bool = False
    conv_id: str = ""

    def set_question(self, value: str):
        self.question = value

    def on_load(self):
        """Loads latest conversation on page load, or creates a fresh one."""
        with rx.session() as session:
            latest_conv = session.exec(
                select(Conversation)
                .order_by(desc(Conversation.created_at))
                .limit(1)
            ).first()

            if latest_conv:
                self.conv_id = latest_conv.id
                messages = session.exec(
                    select(Message)
                    .where(Message.conv_id == self.conv_id)
                    .order_by(Message.created_at)
                ).all()
                self.messages = [
                    ChatMessage(role=m.role, content=m.content)
                    for m in messages
                ]
            else:
                self.conv_id = str(uuid.uuid4())
                self.messages = []
                session.add(Conversation(id=self.conv_id))
                session.commit()

    def new_conversation(self):
        """Creates a fresh conversation — wired to New Chat button."""
        with rx.session() as session:
            self.conv_id = str(uuid.uuid4())
            self.messages = []
            session.add(Conversation(id=self.conv_id))
            session.commit()

    async def send_question(self):
        if not self.question.strip():
            return

        user_content = self.question

        # 1. Show user message + clear input + show spinner
        self.messages.append(ChatMessage(role="user", content=user_content))
        self.question = ""
        self.is_loading = True
        yield  # ← UI updates here

        # 2. Save user message to DB
        with rx.session() as session:
            session.add(Message(
                conv_id=self.conv_id,
                role="user",
                content=user_content,
            ))
            session.commit()

        # 3. Call LLM
        response_text = llm_response(user_content)

        # 4. Show response + stop spinner
        self.messages.append(ChatMessage(role="assistant", content=response_text))
        self.is_loading = False
        yield  # ← UI updates here

        # 5. Save assistant message to DB
        with rx.session() as session:
            session.add(Message(
                conv_id=self.conv_id,
                role="assistant",
                content=response_text,
            ))
            session.commit()


# ─────────────────────────────────────────────
#  COMPONENTS
# ─────────────────────────────────────────────

def chat_bubble(message: ChatMessage) -> rx.Component:
    return rx.box(
        rx.text(message.content),
        align_self=rx.cond(
            message.role == "user",
            "flex-end",
            "flex-start",
        ),
        background_color=rx.cond(
            message.role == "user",
            "#ADD8E6",
            "#F0F0F0",
        ),
        border_radius="10px",
        padding="12px",
        max_width="70%",
        margin_y="5px",
    )


def chat_history() -> rx.Component:
    return rx.vstack(
        rx.foreach(ChatState.messages, chat_bubble),
        rx.cond(
            ChatState.is_loading,
            rx.hstack(
                rx.spinner(size="2"),
                rx.text("Thinking...", color="gray", font_style="italic"),
            ),
            rx.fragment(),
        ),
        width="100%",
        align_items="stretch",
        padding="10px",
        overflow_y="auto",
        flex="1",
    )


def chat_field() -> rx.Component:
    return rx.hstack(
        rx.text_area(
            value=ChatState.question,
            on_change=ChatState.set_question,
            placeholder="Type your question...",
            flex="1",
            disabled=ChatState.is_loading,
        ),
        rx.button(
            rx.cond(
                ChatState.is_loading,
                rx.spinner(size="2"),
                rx.icon("send-horizontal"),
            ),
            #on_click=ChatState.send_question,
            #disabled=ChatState.is_loading,
        ),
        width="100%",
        padding="10px",
    )


def container_chat() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Chat", size="4"),
            rx.spacer(),
            rx.button(
                rx.icon("plus"),
                "New Chat",
                on_click=ChatState.new_conversation,
                variant="soft",
            ),
            width="100%",
            padding="10px",
        ),
        chat_history(),
        chat_field(),
        width="100%",
        height="100vh",
        justify="between",
    )


# ─────────────────────────────────────────────
#  PAGE + APP
# ─────────────────────────────────────────────

@rx.page(route="/", on_load=ChatState.on_load)
def index() -> rx.Component:
    return container_chat()


app = rx.App()