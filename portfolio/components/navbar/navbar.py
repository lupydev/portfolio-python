import reflex as rx

from portfolio.style.styles import Size
import portfolio.style.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.image(src="favicon.ico"),
                rx.heading(
                    "LuPy",
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
                border_right="1px solid #000",
                href="#portafolio",
            ),
            rx.link(
                "Experiencia",
                margin_left=Size.ZERO.value,
                padding_x=Size.SMALL.value,
                border_right="1px solid #000",
                href="#experiencia",
            ),
            rx.link(
                "Contacto",
                margin_left=Size.ZERO.value,
                padding_x=Size.SMALL.value,
                border_right="1px solid #000",
                href="#contacto",
            ),
            rx.link(
                rx.image(
                    src="assets/icons/dark_mode.svg",
                ),
                margin_left=Size.ZERO.value,
                padding_x=Size.SMALL.value,
            ),
        ),
        position="sticky",
        justify="space-between",
        padding_x=Size.EXTREME_BIG.value,
        padding_y=Size.DEFAULT.value,
        top="0",
        z_index="999",
        id="home",
    )
