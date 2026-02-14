import reflex as rx
from Rag_reflex.components.container_domain import container_domain
from Rag_reflex.components.container_files import container_files
from Rag_reflex.components.container_chat import container_chat

def main_view():
    return   rx.hstack(
            container_files(),
            container_chat(),
            container_domain(),
        width="100%",
        padding="1em"
        )