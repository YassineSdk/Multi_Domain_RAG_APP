import reflex as rx 
from .chat_block import chat_block
from .chat_field import chat_field
from Rag_reflex.states.RAGState import RAGState


def container_chat():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon('bot-message-square',size=20 , color= rx.color_mode_cond(light="#4361EE",dark="#7B2FBE")),
                rx.heading('Chat section',size="3",weight="medium",color_schema="gray"),
                align_items="center"
            ),
            rx.divider(),
            rx.box(
            rx.auto_scroll(
                rx.foreach(
                RAGState.current_pairs,
            lambda pair: chat_block(pair["answer"],pair["question"])),
            width="850px",
            height="600px",
            overflow="auto",
            margin_bottom='0.4em'
            )),

            rx.cond(
                RAGState.is_loading,
                    rx.box(
                    rx.image(src="loading.gif",width="200px",height="200px"),
                    width="100%",display="reflex",align_items="center",justify_content="center"),
                    chat_field()

            ),
            width="100%"

        ),

        border_radius="12px",
        background_color=rx.color_mode_cond(
        light="#F1F3F4",
        dark="#1E1E1E",
    ),
        padding="2em",
        height="840px",
        margin="4px",
        width="50%",
        display="flex"
    )