import reflex as rx


def list_icon_right(icon: str, color_icon: str, text: str, **kwargs) -> rx.Component:
    return rx.hstack(
        rx.icon(
            tag=icon,
            color=color_icon,
        ),
        rx.text(
            text,
        ),
        **kwargs,
    )
