import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font

MAX_WIDTH = "1000px"


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    BUTTON = "3em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.Heading: {"font_family": Font.DEFAULT.value, "color": TextColor.ACCENT.value},
    rx.Link: {
        "text_decoration": "none",
        "_hover": {"text_decoration": "none", "color": TextColor.ACCENT.value},
    },
    rx.Span: {
        "font_size": Size.MEDIUM.value,
    },
    rx.Button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "_hover": {"color": f"{TextColor.PRIMARY.value} !important"},
    },
}

max_width_style = dict(
    align_items="start", padding_x=Size.BIG.value, width="100%", max_width=MAX_WIDTH
)
