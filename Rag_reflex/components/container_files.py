import reflex as rx 
from .add_file_form import add_file_form
from .card_grid import file_card
from Rag_reflex.states.FileState import FileState
from .delete_file_dialog import delete_file_dialog

def container_files():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon('folder-kanban',size=20 , color= rx.color_mode_cond(light="#059669",dark="#10B981")),
                rx.heading('Files and Folder',size="3",weight="medium",color_schema="gray"),
                align_items="center"),
            rx.divider(),
            #-- files Operation functions
            rx.stack(
                add_file_form(),
                delete_file_dialog(),
                spacing="3"



            ),
            rx.flex(
                rx.foreach(
                    FileState.files,
                    lambda file: file_card(
                        file['title'],
                        file["details"],
                    ),
                ),
                flex_wrap="wrap",
                spacing="2",
                width="100%"
            ),
            

            width="100%"

        ),

        border_radius="12px",
        background_color=rx.color_mode_cond(
        light="#F1F3F4",
        dark="#1E1E1E",
    ),
        padding="1em",
        height="840px",
        margin="4px",
        width="35%",
        display="flex"
    )