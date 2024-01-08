import reflex as rx
from link_bio.styles import styles
def link_button(title:str,body:str,url:str,icon:str) -> rx.component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=icon,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=styles.Size.MEDIUM.value,
                ),
                rx.vstack(
                    rx.text(title,style=styles.button_title_style),
                    rx.text(body,style=styles.button_body_style),
                    spacing="0px",
                    align_items="start",
                    margin="0px"
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )