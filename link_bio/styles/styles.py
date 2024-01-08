from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
import reflex as rx

#contantes
MAX_WIDTH ="600px"

#espacios

class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    
#styles base

BASE_STYLE = {
    "font_family":Font.DEFAULT.value,
    "background_color" : Color.BACKGROUND.value,
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color" : Color.CONTENT.value,
        "_hover": {
            "background_color" : Color.SECONDARY.value
        }
    },
    rx.Link:{
        "text_decoration":"none",
        "_hover":{}
    }
}

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color = TextColor.HEADER.value,
    font_family=Font.DEFAULT.value,
    font_weight="bold",
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color = TextColor.BODY.value,
    font_family=Font.DEFAULT.value,
)

title_style = dict(
    width="100%",
    font_family=Font.DEFAULT.value,
    font_weight="bold",
    padding_top=Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

navbar_title_style  = dict(
    font_family=Font.LOGO.value,
    font_size = Size.LARGE.value
)