from enum import Enum
import reflex as rx

#contantes
MAX_WIDTH ="600px"

#espacios

class Espacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "1em"
    LARGE = "2em"
    
#styles base

BASE_STYLE = {
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding":Espacer.SMALL.value,
        "border_radius":Espacer.MEDIUM.value,
    }
}