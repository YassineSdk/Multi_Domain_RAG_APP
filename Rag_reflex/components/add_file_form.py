import reflex as rx 
from Rag_reflex.states.UploadState import UploadState




def add_file_form():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button('appload documents',variant="surface")

        ),
        rx.dialog.content(
            rx.dialog.title("Upload Document",margin_top="0.5em"),
            rx.vstack(
                rx.input(placeholder="Doc Name",size="2",width="45%"),
                rx.input(placeholder="Details",size="2",width="100%"),
            ),

            rx.upload(
                rx.text("Drop file here (pdf , word , markdown , latex ..)"),
                border_radius="8px",
                border="1px dashed gray",
                bg=rx.color("gray",3),
                margin_top="1em",
                accept={
                        "application/pdf": [".pdf"],
                        "application/msword": [".doc", ".docx"],
                        "text/markdown": [".md"],
                        "text/plain": [".tex"] }

            ),
            rx.hstack(
                rx.dialog.close(
                rx.button("Cancel",color_scheme="red",variant='soft'),
                margin_top="1em"
                ),  
                rx.dialog.close(
                rx.button("Upload",color_schema="blue",variant='soft',on_click=UploadState.upload_file),
                margin_top="1em"
                ),

            ),
            width="100%",
            padding="1em",
            spacing="3"
        ),
        width="100%"

    )

