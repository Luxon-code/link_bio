from link_bio.styles import styles
import reflex as rx
import datetime
from link_bio.styles.colors import TextColor,Color
def footer() -> rx.component:
    return rx.vstack(
        rx.image(src="code.gif",
                 height="4em",
                 padding="2px",
                 border="2px",
                 border_color=Color.PRIMARY.value),
        rx.link(f" ⛓ 2019-{datetime.date.today().year} LUXON-CODE V1 ⛓ ",
                href="https://github.com/Luxon-code",
                font_size=styles.Size.MEDIUM.value,
                ),
        rx.text("BUILDING SOFTWARE WITH FROM COLOMBIA TO THE WORLD",
                font_size=styles.Size.MEDIUM.value, margin_top="0px"),
        margin_bottom=styles.Size.BIG.value,
        padding_bottom=styles.Size.BIG.value,
        padding_x=styles.Size.BIG.value,
        color = TextColor.FOOTER.value,
        align_items="center"
    )