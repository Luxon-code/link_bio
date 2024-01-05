import reflex as rx
from link_bio.styles import styles
def info_text(title:str,body:str) -> rx.component:
    return rx.box(
        rx.span(title,font_weight="bold",color="blue"),
        F" {body}",font_size=styles.Size.MEDIUM.value
    )