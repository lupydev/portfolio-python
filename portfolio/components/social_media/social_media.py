import reflex as rx


def social_media() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src="https://i.postimg.cc/9FQcfjfX/signo-de-github.png",
                height="30px",
            ),
            href="https://github.com/lumiguz",
            is_external=True,
        ),
        rx.link(
            rx.image(
                src="https://i.postimg.cc/c4k0g5KR/logotipo-de-linkedin.png",
                height="30px",
            ),
            href="https://www.linkedin.com/in/lupy/",
            is_external=True,
        ),
    )
