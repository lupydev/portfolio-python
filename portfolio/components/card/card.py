import reflex as rx
import portfolio.style.styles as styles


def card(header: str, *args, **kwargs) -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading(
                header,
                style=styles.heading_title_style,
            ),
            rx.vstack(
                *args,
            ),
        ),
        **kwargs,
    )
