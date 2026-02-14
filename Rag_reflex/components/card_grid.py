import reflex as rx 
import random 
import random 




def domain_card(icon_url):
    return rx.card(
        rx.link(
            rx.flex(
                rx.avatar(src=icon_url),
                rx.box(
                rx.heading('Audit Repports',size="1"),
                rx.text('Audit report related to the mission',size="1",color=rx.color_mode_cond(dark="white",light="black"))                
            ),
            spacing="2"
            ),

        )

    )


def card_grid():
    avatar_icon = ["/stamp.png","/accounting.png","/logistics.png","/finance"]
    return rx.grid(
        rx.foreach(
            rx.Var.range(12),
             lambda i: domain_card(random.choice(avatar_icon))
            
        ),
        columns="2",
        rows="4",
        spacing="4",
        width="100%",
        direction=["column", "column", "row"]
    )
