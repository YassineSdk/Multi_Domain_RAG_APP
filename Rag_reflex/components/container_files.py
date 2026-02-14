import reflex as rx 
from .add_file_form import add_file_form

def container_files():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon('folder-kanban',size=20 , color= rx.color_mode_cond(light="#059669",dark="#10B981")),
                rx.heading('Files and Folder',size="3",weight="medium",color_schema="gray"),
                align_items="center"),
            rx.divider(),
            add_file_form(),
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
        width="30%",
        display="flex"
    )