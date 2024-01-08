import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles import styles
def links() -> rx.component:
    return rx.vstack(
        rx.center(
            title("Comunidad"),
        ),
        link_button(
            "Tiwtch",
            "Directos todos los dias",
            "https://www.twitch.tv",
            "icons/twitch.svg"
        ),
        link_button(
            "Facebook",
            "Conoce mas sobre mi",
            "https://www.facebook.com",
            "icons/facebook.svg"
        ),
        link_button(
            "Twitter",
            "Novedades sobre la insdustria",
            "https://twitter.com",
            "icons/twitter.svg"
        ),
        link_button(
            "YouTube",
            "Tuturiales semanales",
            "https://www.youtube.com",
            "icons/youtube.svg"
        ),
        link_button(
            "GitHub",
            "Mis proyectos y mas..",
            "https://github.com/Luxon-code",
            "icons/github.svg"
        ),
        width="100%",
        spacing=styles.Size.MEDIUM.value,
    )