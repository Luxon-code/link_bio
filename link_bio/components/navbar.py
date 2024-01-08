import reflex as rx
from link_bio.styles import styles
from link_bio.styles.colors import TextColor,Color
def navbar() -> rx.component:
    return rx.hstack(
        rx.box(
            rx.span(
                "Luxon",
                color = Color.PRIMARY.value
            ),
            rx.span(
                "-",
                color = "white"
            ),
            rx.span(
                "code",
                color = Color.SECONDARY.value
            ),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index="999",
        top="0",
    )