import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles import styles,fonts
from link_bio.styles.colors import TextColor,Color
def header() -> rx.component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Joseph Trujillo",
                size="xl",
                color=TextColor.BODY.value,
                bg = Color.CONTENT.value,
                src="avatar.png",
                padding = "2px",
                border = "4px",
                border_color = Color.PRIMARY.value  
            ),
            rx.vstack(
                rx.heading(
                    "LUXON-CODE",
                    size="lg",
                    color = TextColor.HEADER.value,
                    font_family = fonts.Font.DEFAULT.value
                ),
                rx.text(
                    "@luxon-code",
                    margin_top="0px",
                    color = TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("https://facebok.com","icons/facebook.svg"),
                    link_icon("https://twitter.com","icons/twitter.svg"),
                    link_icon("https://instagram.com","icons/instagram.svg"),
                ),
                align_items="start"
            ),
            spacing=styles.Size.DEFAULT.value,
        ),
        rx.flex(
            info_text("+13","años de experencia"),
            rx.spacer(),
            info_text("+20","Proyectos terminados"),
            rx.spacer(),
            info_text("+30","Aplicaciones terminadas"),
            width="100%",
        ),
        rx.text("""Soy ingeniero de software desde hace más de 12 años.
                Actualmente trabajo como freelance full-stack developer i0S y Android.
                Además creo contenido formativo sobre programación y tecnología en redes.
                Aqui podrás encontrar todos mis enlaces de interés. ¡Bienvenidos!""",
                color = TextColor.BODY.value
                ),
        spacing=styles.Size.BIG.value,
        align_items="start"
    )