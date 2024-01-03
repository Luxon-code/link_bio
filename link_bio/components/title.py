import reflex as rx
from link_bio.styles import styles
def title(title:str) -> rx.component:
    return rx.heading(
        title,
        size="lg",
        style=styles.title_style
    )