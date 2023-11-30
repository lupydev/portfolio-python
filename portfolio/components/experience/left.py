import reflex as rx
from portfolio.style.colors import Color
import portfolio.style.styles as styles


def experience_left(
    title_position: str,
    company: str,
    date: str,
    *list_icon: rx,
) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title_position,
            style=styles.heading_title_style,
        ),
        rx.text(
            company,
            font_weight="bold",
            font_size=styles.Size.MIDDLE.value,
        ),
        rx.hstack(
            rx.text(
                date,
            ),
            rx.icon(
                tag="calendar",
            ),
            color=Color.SECUNDARY.value,
        ),
        rx.divider(
            border_color=Color.PRIMARY.value,
        ),
        *list_icon,
        style=styles.experience_left,
    )
