import reflex as rx
from portfolio.components.navbar.navbar import navbar


def header() -> rx.Component:
    return rx.hstack(
        navbar(),
    )
