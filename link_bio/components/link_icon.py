import reflex as rx
from link_bio.styles import styles
def link_icon(url:str) -> rx.component:
    return rx.link(
        rx.icon(
            tag="link"
        ),
        href=url,
        is_external=True
    )