import reflex as rx 




def send_Question_button():
    return  rx.button(
    rx.icon("send-horizontal"),
    variant="ghost",  
    border_radius="25%",
)