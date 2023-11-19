import reflex as rx
import portfolio.style.styles as styles


def card(header: str, *content: rx, **css_style) -> rx.Component:
    return rx.vstack(
        rx.heading(
            header,
            style=styles.heading_title_style,
        ),
        rx.divider(),
        rx.vstack(
            *content,
        ),
        align_items="start",
        **css_style,
    )
