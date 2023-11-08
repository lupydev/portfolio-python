import reflex as rx
from datetime import date
from portfolio.components.social_media.social_media import social_media


def footer() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.text("Hecho con ❤ por:"),
                rx.markdown(" `Lupy`"),
            ),
            rx.text("de Colombia para el Mundo"),
            rx.markdown("`Esta web fue creada en Python`"),
            rx.text(f"© 2023 - {date.today().year}"),
        ),
        rx.spacer(),
        social_media(),
    )
    # return rx.vstack(
    #     rx.hstack(
    #         rx.text("Hecho con ❤ por:"),
    #         rx.markdown(" `Lupy`"),
    #         rx.spacer(),
    #         social_media(),
    #     ),
    #     rx.text("de Colombia para el Mundo"),
    #     rx.markdown("`Esta web fue creada en Python`"),
    #     rx.text(f"© 2023 - {date.today().year}"),
    # )
