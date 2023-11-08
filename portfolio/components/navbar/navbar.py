import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="favicon.ico"),
            rx.heading("My App"),
        ),
        rx.spacer(),
        rx.hstack(
            rx.image(src="favicon.ico"),
            rx.heading("My App"),
        ),
        position="sticky",
        width="100%",
        top="0px",
        z_index="999",
    )
