import reflex as rx 

def add_file_form():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Upload Document"),
            rx.vstack(
                rx.input("doc name",size="2",weight="bold"),
                rx.input("Description",size="2",weight="bold"),
                padding="1em",
                width="100%"
            ),
            rx.upload(
                rx.text("Drop file here (pdf , word , markdown , latex ..)"),
                padding="2em",
                border_radius="8px"
            ),
        )
    )