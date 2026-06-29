import reflex as rx 
from .save_dialog import save_dialog
from Rag_reflex.states.QAPairItem import QAPairItem



def conv_menu(pair: QAPairItem):
    return rx.menu.root(
        rx.menu.trigger(rx.icon("grip-vertical",size=20)),
        rx.menu.content(
            rx.menu.item(save_dialog(pair)),
            rx.menu.item("Download as pdf")
        )
    )   
