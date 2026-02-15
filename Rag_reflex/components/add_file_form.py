import reflex as rx
from Rag_reflex.states.FileState import FileState

def add_file_form():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Upload Documents", variant="surface")
        ),
        rx.dialog.content(
            rx.dialog.title("Upload Document", margin_top="0.5em"),
            rx.vstack(
                rx.input(
                    placeholder="Doc Name",
                    size="2",
                    width="45%",
                    value=FileState.doc_name,
                    on_change=FileState.set_doc_name,
                ),
                rx.input(
                    placeholder="Details",
                    size="2",
                    width="100%",
                    value=FileState.details,
                    on_change=FileState.set_details,
                ),
                rx.upload(
                    rx.text("Drop file here (pdf, word, markdown, latex..)"),
                    id="file_upload",          # ✅ id is required!
                    border_radius="8px",
                    border="1px dashed gray",
                    bg=rx.color("gray", 3),
                    margin_top="1em",
                    width="100%",
                    accept={
                        "application/pdf": [".pdf"],
                        "application/msword": [".doc", ".docx"],
                        "text/markdown": [".md"],
                        "text/plain": [".tex"],
                    },
                ),              # ✅ rx.upload closes HERE
                rx.hstack(      # ✅ rx.hstack is OUTSIDE rx.upload
                    rx.dialog.close(
                        rx.button("Cancel", color_scheme="red", variant="soft"),
                    ),
                    rx.dialog.close(
                        rx.button(
                            "Upload",
                            color_scheme="blue",  # ✅ color_scheme not color_schema
                            variant="soft",
                            on_click=FileState.handle_upload(
                                rx.upload_files(upload_id="file_upload")
                            ),
                        ),
                    ),
                    justify="end",
                    width="100%",
                    margin_top="1em",
                ),
                width="100%",
                padding="1em",
                spacing="3",
            ),
        ),
    )