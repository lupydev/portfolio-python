import reflex as rx
from portfolio.components.card.card import card
from portfolio.components.image.image import img
from portfolio.style.colors import Color
import portfolio.style.styles as styles


def project(
    title: str,
    img_url: str,
    img_alt: str,
    *card_body: rx,
) -> rx.Component:
    return rx.box(
        rx.grid(
            rx.grid_item(
                card(
                    title,
                    *card_body,
                ),
                position="relative",
                padding=styles.Size.MEDIUM.value,
                border_top_left_radius=styles.Size.SMALL.value,
                border_bottom_left_radius=styles.Size.SMALL.value,
            ),
            rx.grid_item(
                img(
                    img_url,
                    img_alt,
                    opacity="0.7",
                    bg=Color.PRIMARY.value,
                    border_top_right_radius=styles.Size.SMALL.value,
                    border_bottom_right_radius=styles.Size.SMALL.value,
                ),
                border_top_right_radius=styles.Size.SMALL.value,
                border_bottom_right_radius=styles.Size.SMALL.value,
            ),
            template_columns="repeat(2, 1fr)",
            width="100%",
            height="100%",
            border_radius=styles.Size.SMALL.value,
            margin_top=styles.Size.DEFAULT.value,
            margin_left=styles.Size.DEFAULT.value,
            position="absolute",
            style=styles.border,
            z_index="10",
        ),
        style=styles.container_project,
    )
