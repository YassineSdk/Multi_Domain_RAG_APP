import reflex as rx 

def summary_window(repport, date, content=None):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.icon(tag="eye", size=20, color=rx.color_mode_cond(light="#3B6EE8", dark="#0ABFBC"), cursor="pointer"),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.icon("clipboard-clock", size=22, color=rx.color_mode_cond(light="#3B6EE8", dark="#0ABFBC")),
                rx.heading(repport, size="4", weight="medium"),
                rx.dialog.title(""),
                rx.spacer(),
                rx.badge(date, variant="soft", color_scheme="cyan"),
                align_items="center",
                width="100%",
                spacing="2",
                margin_bottom="5px"
            ),
            rx.divider(),

            rx.scroll_area(
                rx.text(content, size="2", white_space="pre-wrap",margin_top="5px"),
                type="always",
                scrollbars="vertical",
                style={"height": "290px"},
            ),


            rx.hstack(
                rx.button(
                    rx.icon("download", size=16),
                    "Download PDF",
                    color_scheme="blue",
                    variant="surface",
                    on_click=rx.toast.success("Downloaded successfully"),
                ),
                rx.dialog.close(
                    rx.button("Close", variant="surface", color_scheme="red"),
                ),
                justify_content="end",
                align_items="center",
                width="100%",
                padding_top="0.5em",
            ),

            style={
                "width": "600px",
                "width": "100%",
                "padding": "1.8em",
                "max_height":"800px",
                "margin_bottom":"2px"
            },
        ),
    )