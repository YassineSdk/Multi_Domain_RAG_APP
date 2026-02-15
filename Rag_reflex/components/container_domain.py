import reflex as rx 
from Rag_reflex.components.add_file_button import add_file
import random


def container_domain():
    return rx.box(
        rx.vstack(
                rx.hstack( 
                    rx.hstack(
                        rx.icon('book-open-text',size=20 , color= rx.color_mode_cond(light="#3B6EE8",dark="#0ABFBC")),
                        rx.heading('Conversation resume',size="3",weight="medium",color_schema="gray"),
                
                    spacing="1",
                    align_items="center"
            ),
            add_file(),
            justify="between",
            width="100%"
            ),
            rx.divider(),
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
        width="20%",
        display="flex"
    )