from link_bio.styles import styles
import reflex as rx
import datetime
def footer() -> rx.component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link(f" ⛓ 2019-{datetime.date.today().year} LUXON-CODE V1 ⛓ ",
                font_size=styles.Size.MEDIUM.value),
        rx.text("BUILDING SOFTWARE WITH FROM COLOMBIA TO THE WORLD",
                font_size=styles.Size.MEDIUM.value, margin_top="0px"),
        margin_bottom=styles.Size.LARGE.value
    )