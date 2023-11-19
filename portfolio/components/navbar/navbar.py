import reflex as rx
from portfolio.style.styles import Size
import portfolio.style.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.image(
                    src="lupy.png",
                    height=styles.Size.XL.value,
                ),
                rx.heading(
                    "Lupy",
                    style=styles.navbar_title_style,
                ),
            ),
            href="",
        ),
        rx.hstack(
            rx.link(
                "Portafolio",
                margin_left=Size.ZERO.value,
                padding_x=Size.SMALL.value,
                style=styles.border_right,
                href="#portafolio",
            ),
            rx.link(
                "Experiencia",
                margin_left=Size.ZERO.value,
                padding_x=Size.SMALL.value,
                style=styles.border_right,
                href="#experiencia",
            ),
            rx.link(
                "Contacto",
                margin_left=Size.ZERO.value,
                padding_x=Size.SMALL.value,
                href="#contacto",
            ),
            # rx.button(
            #     rx.icon(tag="sun"),
            #     on_click=rx.toggle_color_mode,
            # ),
        ),
        style=styles.navbar,
        justify="space-between",
    )
