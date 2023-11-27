import reflex as rx
from datetime import date
from portfolio.components.image.image import img
from portfolio.style.colors import Color
import portfolio.style.styles as styles


def footer() -> rx.Component:
    return rx.vstack(
        rx.divider(),
        rx.text(
            "Esta web fue creada en ",
            rx.span(
                "Python puro ",
                font_weight="bold",
                color=Color.SECUNDARY.value,
            ),
            "con el framework: ",
            rx.link(
                "Reflex",
                rx.icon(
                    tag="external_link",
                ),
                href="https://reflex.dev/",
                font_weight="bold",
                color=Color.SECUNDARY.value,
                text_decoration="underline",
            ),
            margin_y=styles.Size.ZERO.value,
        ),
        rx.text(
            f"© {date.today().year} hecho con ",
            rx.span(
                "❤",
                color=Color.PRIMARY.value,
            ),
            " por: ",
            rx.span(
                "Lupy, ",
                font_weight="bold",
                color=Color.SECUNDARY.value,
            ),
            rx.span(
                "de Colombia para el 🌎",
            ),
            margin_y=styles.Size.ZERO.value,
        ),
        style=styles.footer,
        id="footer",
    )
