import reflex as rx 



def conv_menu():
    return rx.menu.root(
        rx.menu.trigger(rx.icon("grip-vertical",size=20)),
        rx.menu.content(
            rx.menu.item("Save"),
            rx.menu.item("Download as pdf")
        )
    )   
