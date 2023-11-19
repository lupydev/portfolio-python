import reflex as rx


def img(url: str, alt: str, **css_styles) -> rx.Component:
    return rx.image(
        src=url,
        alt=alt,
        **css_styles,
    )
