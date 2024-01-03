import reflex as rx
from link_bio.styles import styles
def navbar() -> rx.component:
    return rx.hstack(
        rx.text(
            "Luxon-code",
        ),
        position="sticky",
        bg="lightgray",
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index="999",
        top="0",
    )