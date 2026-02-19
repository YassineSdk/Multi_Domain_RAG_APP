import reflex as rx 
from Rag_reflex.states.RAGState import RAGState

def chat_block(response,Question):
    return rx.flex(
            rx.flex(
            rx.box(
                Question,
                bg=rx.color("gray",4),
                border_radius="6px",
                max_width="50%",
                padding="0.5em",
                margin="1em",
            ),
            width="100%",
            justify_content="flex-end"
    
        ),
        rx.flex(
            rx.hstack(
                
            rx.box(rx.icon("bot", size=20), width="20px", height="20px"),
            rx.box(
                rx.box(
                rx.markdown(response),
                bg=rx.color_mode_cond(light="#BBE0EF",dark="#0992C2"),
                variant="soft",
                border_radius="6px",
                padding="0.5em",
                # margin="1em",
                max_width="70%",
            )),
            align="baseline",
            width="100%"
            ),

            width="100%",
            justify_content="flex-start",
        ),

        display="flex",
        width="100%",
        flex_direction="column",
        gap="1px",
        
    )