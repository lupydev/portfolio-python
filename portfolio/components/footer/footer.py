import reflex as rx
from datetime import date
from portfolio.style.styles import Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Esta web fue creada en ",
            rx.span(
                "Python puro ",
                font_weight="bold",
            ),
            rx.span("con el framework: "),
            rx.link(
                "Reflex",
                href="https://reflex.dev/",
                font_weight="bold",
                text_decoration="underline",
            ),
            margin_y=Size.ZERO.value,
        ),
        rx.text(
            f"© {date.today().year} hecho con ❤ por: ",
            rx.span(
                "Lupy, ",
                font_weight="bold",
            ),
            rx.span(
                "de Colombia para el 🌎",
            ),
            margin_y=Size.ZERO.value,
        ),
        margin_top=Size.VERY_BIG.value,
        margin_bottom=Size.DEFAULT.value,
        width="100%",
        id="footer",
    )
