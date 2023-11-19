import reflex as rx


def list_icon_left(icon: str, color_icon: str, text: str, **kwargs) -> rx.Component:
    return rx.hstack(
        rx.text(
            text,
        ),
        rx.icon(
            tag=icon,
            color=color_icon,
        ),
        **kwargs,
    )
