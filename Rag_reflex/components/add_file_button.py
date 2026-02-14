import reflex as rx 
from Rag_reflex.components.add_file_form import add_file_form



def add_file():
    return  rx.button(
    rx.icon("plus"),
    variant="ghost",  # makes it look like just an icon, no button styling
    border_radius="25%",
)
    