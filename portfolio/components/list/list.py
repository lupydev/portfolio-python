import reflex as rx


def list_icon(icon: str, text: str, **kwargs) -> rx.Component:
    return rx.hstack(
        rx.icon(
            tag=icon,
        ),
        rx.text(
            text,
        ),
        **kwargs,
    )
