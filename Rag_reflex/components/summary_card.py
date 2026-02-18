import reflex as rx
from .summary_window import summary_window

def summary_card(repport, date,content):
    return rx.box(
        rx.card(
        rx.hstack(
            rx.icon("clipboard-clock",size=25,color=rx.color_mode_cond(light="#3B6EE8",dark="#0ABFBC")),
            rx.text(f"{repport}" ,size="1"),
            rx.box(
            rx.badge(date,variant="soft",display="flex",color_scheme="cyan"),
            display="flex",
            justify_content="flex-end",
            flex="1"
            ),
            summary_window(repport, date,content),
            display="flex",
            align_items="center",
            justify_content="space-between",
            spacing="2",
            width="100%"

        ),
        width="95%",
        height="50px",
        display="flex",
        align_items="center",
        outline="blue" ,
        margin_bottom="10px",
    ),
    )