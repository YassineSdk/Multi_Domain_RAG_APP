import reflex as rx

def file_card(title, details):
    return rx.card(
        rx.hstack(
            # ── Box 1 : Icon ──────────────────────────────
            rx.box(
                rx.icon("file-text", size=30, color="#3B6EE8"),
                width="20%",
                height="100%",          
                display="flex",
                align_items="center",
                justify_content="center",
            ),

            # ── Box 2 : Text (variable height content) ────
            rx.box(
                rx.heading(title, size="1"),
                rx.text(details, size="1"),
                width="60%",
                height="100%",          # stretch to full card height
                display="flex",
                flex_direction="column",
                justify_content="center",  # centers text block vs THIS box
                align_items="flex_start",
                overflow="hidden",
            ),

            # ── Box 3 : Checkbox ──────────────────────────
            rx.box(
                rx.checkbox(),
                width="20%",
                height="100%",          # stretch to full card height
                display="flex",
                align_items="center",   # centers checkbox vs THIS box only
                justify_content="center",
            ),

            width="100%",
            height="100%",   # hstack fills the card
            align_items="stretch",  # makes all 3 boxes stretch to same height
            spacing="0",
        ),
        width="49%",
        height="70px",
        padding="0",
    )