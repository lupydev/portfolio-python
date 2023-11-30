import reflex as rx
from enum import Enum

from portfolio.style.colors import Color

"""
Convencion de estilos
    1. Position
    2. Box model
    3. Typographic
    4. Visuals
    5. Miscelaneos
"""


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    EXTREME_BIG = "8em"


BASE_STYLE = {
    rx.Link: {
        "_hover": {
            "color": Color.SECUNDARY_LIGHT.value,
        },
    },
    rx.Divider: {
        "border_color": Color.SECUNDARY_LIGHT.value,
    },
}


navbar_title_style = dict(font_size=Size.LARGE.value)


border = dict(
    border=f"0.2em solid {Color.SECUNDARY.value}",
)

border_right = dict(
    border_right=f"0.2em solid {Color.SECUNDARY.value}",
)

footer = dict(
    margin_top=Size.VERY_BIG.value,
    margin_bottom=Size.DEFAULT.value,
    margin_x=Size.DEFAULT.value,
    text_align="center",
)
