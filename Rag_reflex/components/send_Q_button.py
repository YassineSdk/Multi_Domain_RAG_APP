import reflex as rx 
from Rag_reflex.states.RAGState import RAGState



def send_Question_button():
    return  rx.button(
    rx.icon("send-horizontal"),
    variant="ghost",  
    border_radius="25%",
    on_click= RAGState.handle_question
)