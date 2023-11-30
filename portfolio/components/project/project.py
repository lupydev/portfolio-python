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
        rx.desktop_only(
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
                    ),
                ),
                template_columns="repeat(2, 1fr)",
                max_width="40em",
                height="100%",
                style=styles.container_project,
                margin_x=styles.Size.VERY_BIG.value,
                border=f"0.2em solid {Color.SECUNDARY.value}",
            ),
        ),
        rx.tablet_only(
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
                        border_top_left_radius=styles.Size.SMALL.value,
                        opacity="0.7",
                        bg=Color.PRIMARY.value,
                    ),
                    border_top_left_radius=styles.Size.SMALL.value,
                ),
                template_columns="repeat(2, 1fr)",
                # max_width="22em",
                height="100%",
                style=styles.container_project,
                border=f"0.2em solid {Color.SECUNDARY.value}",
                margin_x=styles.Size.VERY_BIG.value,
            ),
        ),
        rx.mobile_only(
            rx.grid(
                rx.grid_item(
                    img(
                        img_url,
                        img_alt,
                        border_top_left_radius=styles.Size.SMALL.value,
                        opacity="0.7",
                        bg=Color.PRIMARY.value,
                    ),
                    border_top_left_radius=styles.Size.SMALL.value,
                ),
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
                template_rows="repeat(2,1fr)",
                height="100%",
                style=styles.container_project,
                border=f"0.2em solid {Color.SECUNDARY.value}",
                margin=f"0 {styles.Size.DEFAULT.value} 0 {styles.Size.BIG.value}",
            ),
            width="100%",
        ),
    )
