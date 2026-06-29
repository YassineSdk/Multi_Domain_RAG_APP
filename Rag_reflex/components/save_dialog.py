import reflex as rx 
from Rag_reflex.states.RAGState import RAGState 
from Rag_reflex.states.QAPairItem import QAPairItem


def save_dialog(pair: QAPairItem)-> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("save", on_click=RAGState.select_qa(pair["id"]))
        ),
        rx.dialog.content(
            rx.input(
                placeholder="title",
                value=RAGState.save_title,
                on_change=RAGState.set_save_title,
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancel", variant="soft", color_scheme="gray"),
                ),
                rx.dialog.close(
                    rx.button("Save", on_click=RAGState.confirm_save),
                ),
                gap="1em",
                justify="end",
                margin_top="1em",
        ),
    ),
)
