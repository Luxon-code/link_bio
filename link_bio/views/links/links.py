import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
def links() -> rx.component:
    return rx.vstack(
        rx.center(
            title("Comunidad"),
        ),
        link_button(
            "Tiwtch",
            "Directos todos los dias",
            "https://www.twitch.tv"
        ),
        link_button(
            "Facebook",
            "Conoce mas sobre mi",
            "https://www.facebook.com"
        ),
        link_button(
            "Twitter",
            "Novedades sobre la insdustria",
            "https://twitter.com"
        ),
        link_button(
            "YouTube",
            "Tuturiales semanales",
            "https://www.youtube.com"
        ),
        width="100%",
    )