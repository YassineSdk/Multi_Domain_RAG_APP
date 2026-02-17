import reflex as rx

config = rx.Config(
    app_name="Rag_reflex",
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap",
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)