import reflex as rx
def link_button(text:str,url:str) -> rx.component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="calendar"
                ),
                rx.vstack(
                    rx.text(text),
                    rx.text(text)
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )