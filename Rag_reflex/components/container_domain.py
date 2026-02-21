import reflex as rx 
import random
from .summary_card import summary_card
from Rag_reflex.utils.text import text

def container_domain():
    summary_list = [{"title":"Financial efficiency", "date":"02/01/05","content":text()},
    {"title":"Customer policy", "date":"02/02/05","content":text()},
    {"title":"ratio analysis", "date":"02/03/05","content":text()}
    ]

    return rx.box(
        rx.vstack(
                rx.hstack( 
                    rx.hstack(
                        rx.icon('book-open-text',size=20 , color= rx.color_mode_cond(light="#3B6EE8",dark="#0ABFBC")),
                        rx.heading('collection',size="3",weight="medium",color_schema="gray"),
                
                    spacing="1",
                    align_items="center"
            ),
            justify="between",
            width="100%"
            ),
            rx.divider(),
            rx.auto_scroll(
                [summary_card(summary['title'],summary['date'],summary['content']) for summary in summary_list],

                width="100%",
                spacing="3"),
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
        width="20%",
        display="flex"
    )