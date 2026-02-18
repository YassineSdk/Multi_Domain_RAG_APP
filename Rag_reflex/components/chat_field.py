import reflex as rx 
from .send_Q_button import send_Question_button
#from Rag_reflex.states.ChatState import ChatState

def chat_field():
    return rx.box(
                rx.stack(
                rx.text_area(placeholder='select a file and ask ur question ....',align_items="start",padding="1em",width="100%",height="100px"),
                rx.box(
                    send_Question_button(),
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    width="10%",

                    ),
                    display="flex",
                    align_items="center",
                    height="50px",
                    width="100%"
                    ),
            height="100px",
            border_radius="8px",
            width="100%",
            padding="0.1em",
            margin_top="28px"
    )