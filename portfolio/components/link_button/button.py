import reflex as rx

from portfolio.style.styles import Size


def link_button(text: str, img: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.text(text),
                rx.image(
                    src=img,
                ),
            )
        ),
        href=url,
        # padding=Size.SMALL.value,
        is_external=True,
    )
