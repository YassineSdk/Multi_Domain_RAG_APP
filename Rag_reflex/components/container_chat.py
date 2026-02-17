import reflex as rx 
from .chat_block import chat_block
from .chat_field import chat_field
#from Rag_reflex.states.ChatState import ChatState


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
            chat_block("testttt","test"),
            width="800px",
            height="550px",
            overflow="auto",
            margin='1em'
            )),
            chat_field(),
            width="100%"

        ),




        border_radius="12px",
        background_color=rx.color_mode_cond(
        light="#F1F3F4",
        dark="#1E1E1E",
    ),
        padding="2em",
        height="800px",
        margin="4px",
        width="50%",
        display="flex"
    )