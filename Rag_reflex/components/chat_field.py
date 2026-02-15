import reflex as rx 


def chat_field():
    return rx.box(
        rx.input(placeholder='select a file and ask ur question ....',height="80px",align_items="start",padding="0.5"),
        height="50px",
        border_radius="8px",
        width="90%",
        padding="1em",
        align="end"

    
    )