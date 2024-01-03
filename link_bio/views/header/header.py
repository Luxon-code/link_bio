import reflex as rx

def header() -> rx.component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Joseph Trujillo",size="xl"),
            rx.vstack(
                rx.heading("LUXON-CODE",size="lg"),
                rx.text("@luxon-code",
                        margin_top="0px"),
                align_items="start"
            )
        ),
        rx.text("""Soy ingeniero de software desde hace más de 12 años.
                Actualmente trabajo como freelance full-stack developer i0S y Android.
                Además creo contenido formativo sobre programación y tecnología en redes.
                Aqui podrás encontrar todos mis enlaces de interés. ¡Bienvenida!"""),
        align_items="start"
    )