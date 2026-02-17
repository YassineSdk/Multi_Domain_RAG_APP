import reflex as rx 


def chat_block(response,Question):
    return rx.flex(
        rx.flex(
            rx.box(
                response,
                bg=rx.color("gray",4),
                border_radius="6px",
                max_width="50%",
                padding="0.5em",
                margin="1em",
                
            ),
            width="100%",
            justify_content="flex-start"
        ),

        rx.flex(
            rx.box(
                Question,
                bg=rx.color_mode_cond(light="#BBE0EF",dark="#0992C2"),
                variant="soft",
                border_radius="6px",
                padding="0.5em",
                margin="1em",
                max_width="50%",
            ),
            width="100%",
            justify_content="flex-end"
    
        ),
        display="flex",
        width="100%",
        flex_direction="column",
        gap="1px",
        
    )