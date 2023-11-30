import reflex as rx
import portfolio.style.styles as styles
from portfolio.components.navbar.navbar import navbar
from portfolio.components.footer.footer import footer
from portfolio.views.experience.experience import experience
from portfolio.views.header.header import header
from portfolio.views.projects.projects import projects


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                projects(),
                experience(),
                width="100%",
            ),
        ),
        footer(),
        width="100%",
    )


app = rx.App(
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="Lupy | Backend Developer",
    description="Hola, mi nombre es: Luis aka Lupy. Soy desarrollador de software especializado en el backend",
    image="favicon.ico",
)
app.compile()
