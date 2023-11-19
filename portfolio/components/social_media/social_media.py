import reflex as rx
import portfolio.style.styles as styles

from portfolio.style.colors import Color
from portfolio.style.styles import Size


def social_media(
    image: str,
    img_size: str,
    url: str,
) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            height=img_size,
        ),
        href=url,
        is_external=True,
        justify_item="center",
        style=styles.social_media,
    )
