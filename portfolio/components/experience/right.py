from datetime import date
import reflex as rx
from portfolio.style.colors import Color
import portfolio.style.styles as styles


def experience_right(
    position: str,
    company: str,
    date: str,
    *list_icon: rx,
) -> rx.Component:
    return rx.vstack(
        rx.heading(
            position,
            style=styles.heading_title_style,
        ),
        rx.text(
            company,
            font_weight="bold",
            font_size=styles.Size.MIDDLE.value,
        ),
        rx.hstack(
            rx.icon(
                tag="calendar",
            ),
            rx.text(
                date,
            ),
            color=Color.SECUNDARY.value,
        ),
        rx.divider(
            border_color=Color.PRIMARY.value,
        ),
        *list_icon,
        padding=styles.Size.MEDIUM.value,
        border_bottom_left_radius=styles.Size.DEFAULT.value,
        border_left=f"0.3em solid {Color.PRIMARY.value}",
        align_items="start",
    )