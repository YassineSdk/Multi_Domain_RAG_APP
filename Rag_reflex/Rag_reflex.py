import reflex as rx
from rxconfig import config
from Rag_reflex.views.main_view import main_view
from Rag_reflex.components.header import header
from Rag_reflex.states.FileState import FileState

class State(rx.State):
    """The app state."""

@rx.page(route="/",on_load=FileState.load_files)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.vstack(
            header(),
            main_view(),
            width="100%"

    ),
        width="100%"

    )


app = rx.App(
    style={
        "font_family": "DM Sans, sans-serif",
    }
)
app.add_page(index)
