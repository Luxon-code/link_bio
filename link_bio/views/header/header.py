import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles import styles
def header() -> rx.component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Joseph Trujillo",size="xl"),
            rx.vstack(
                rx.heading("LUXON-CODE",size="lg"),
                rx.text("@luxon-code",
                        margin_top="0px"),
                rx.hstack(
                    link_icon("https://facebok.com"),
                    link_icon("https://facebok.com"),
                    link_icon("https://facebok.com"),
                ),
                align_items="start"
            ),
            spacing=styles.Size.DEFAULT.value,
        ),
        rx.flex(
            info_text("+13","años de experencia"),
            rx.spacer(),
            info_text("+13","años de experencia"),
            rx.spacer(),
            info_text("+13","años de experencia"),
            width="100%",
        ),
        rx.text("""Soy ingeniero de software desde hace más de 12 años.
                Actualmente trabajo como freelance full-stack developer i0S y Android.
                Además creo contenido formativo sobre programación y tecnología en redes.
                Aqui podrás encontrar todos mis enlaces de interés. ¡Bienvenida!"""),
        spacing=styles.Size.LARGE.value,
        align_items="start"
    )