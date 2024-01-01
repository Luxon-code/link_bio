import reflex as rx
import datetime
def footer() -> rx.component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link(f" ⛓ 2019-{datetime.date.today().year} LUXON-CODE V1 ⛓ "),
        rx.text("BUILDING SOFTWARE WITH FROM COLOMBIA TO THE WORLD")
    )