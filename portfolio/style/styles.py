import reflex as rx
from enum import Enum

from portfolio.style.colors import Color, TextColor
from portfolio.style.fonts import Font

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
    XL = "3em"
    VERY_BIG = "4em"
    HUGE = "6em"
    EXTREME_BIG = "8em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "line_height": Size.LARGE.value,
    "color": TextColor.BODY.value,
    "background_color": Color.BACKGROUND.value,
    rx.Heading: {
        "color": TextColor.TITLE.value,
    },
    rx.Link: {
        "font_weight": "bold",
        "_hover": {
            "color": Color.SECUNDARY_LIGHT.value,
        },
    },
    rx.Divider: {
        "border_color": Color.SECUNDARY_LIGHT.value,
    },
}

navbar = dict(
    position="sticky",
    z_index="999",
    top="0",
    bg=Color.BACKGROUND.value,
)

navbar_title_style = dict(
    font_size=Size.LARGE.value,
)


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

header_title_style = dict(
    color=TextColor.TITLE.value,
    font_size=Size.BIG.value,
    font_weight="bold",
)

heading_title_style = dict(
    font_size=Size.LARGE.value,
)

container_project = dict(
    border_top_left_radius=Size.DEFAULT.value,
    border_bottom_left_radius=Size.DEFAULT.value,
    bg=Color.BACKGROUND_CONTAINER.value,
    box_shadow=f"-{Size.DEFAULT.value} -{Size.DEFAULT.value} {Color.PRIMARY.value}",
)

social_media = dict(
    width="100%",
    height="100%",
    padding=Size.SMALL.value,
    border_radius=Size.SMALL.value,
    bg=Color.PRIMARY.value,
    _hover=dict(
        bg=Color.PRIMARY_LIGHT.value,
    ),
)
