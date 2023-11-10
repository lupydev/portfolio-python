import reflex as rx
from enum import Enum

"""
Convencion de estilos
    1. Position
    2. Box model
    3. Typographic
    4. Visuals
    5. Miscelaneos
"""

MAX_WIDTH = "1440px"


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


BASE_STYLE = {
    rx.Link: {
        "_hover": {},
    },
    rx.Button: {},
}

navbar_title_style = dict(font_size=Size.LARGE.value)
