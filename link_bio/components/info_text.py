import reflex as rx
from link_bio.styles import styles
from link_bio.styles.colors import TextColor,Color
def info_text(title:str,body:str) -> rx.component:
    return rx.box(
        rx.span(
                title,
                font_weight="bold",
                color=Color.PRIMARY.value
            ),
        F" {body}",font_size=styles.Size.MEDIUM.value,
        color = TextColor.BODY.value
    )