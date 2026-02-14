import reflex as rx 

def header():
    return rx.box(
        rx.hstack(
            rx.hstack(
                # app name and icon 
                rx.image(
                    src= "logo.png",
                    width= "2.5em",
                    height= "auto",
                    border_radius= "25",

                ),
                rx.heading("QueryMind",size="7",weight="medium",color_scheme="sky",),
            align_items="center"
            ),
            rx.color_mode.button(position="top-right"),
            justify="between",
            align_items="center",
            width="100%",
            ),

        height="80px",
        width="100%",
        padding="2rem",
        display="flex",
        align_items="center",
        justify="between"
                )