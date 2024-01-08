import reflex as rx
from link_bio.styles import styles
def link_icon(url:str,icon:str) -> rx.component:
    return rx.link(
        rx.image(
            src=icon,
            width=styles.Size.DEFAULT.value
        ),
        href=url,
        is_external=True
    )