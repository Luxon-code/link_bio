from enum import Enum
import reflex as rx

#contantes
MAX_WIDTH ="600px"

#espacios

class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "2em"
    
#styles base

BASE_STYLE = {
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
    },
    rx.Link:{
        "text_decoration":"none",
        "_hover":{}
    }
}

button_title_style = dict(
    font_size=Size.DEFAULT.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value
)