import reflex as rx 
from Rag_reflex.states.FileState import FileState


def delete_file_dialog():
    return rx.dialog.root(
        rx.dialog.trigger(
                rx.button(
                "Delete Documents",
                color_scheme="red",
                variant="surface",
                display="flex",
                disabled=FileState.checked_files.length() == 0),
        ),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title('Delete file confirmation'),

                rx.foreach(
                FileState.checked_files,
                lambda title: rx.text(f"• {title}", size="2",color_scheme="red"),
                ),
                rx.dialog.description(
                "Are you sure want to delete this file ?"),

                rx.hstack(
                    rx.dialog.close(
                        rx.button('Cancel',color_scheme="yellow",variant="surface",on_click=FileState.clear_cheked_files)
                    ),

                    rx.dialog.close(
                        rx.button('Delete',color_scheme="red",variant="surface",on_click=FileState.delete_files)
                    ),
                    spacing="2",
                    justify_content="end"
                ),

                direction="column",
                spacing="2"
            ),

        ),
    width="100%",
    height="100%",
    padding="2em"
        
    )