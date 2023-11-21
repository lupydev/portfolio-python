import reflex as rx
from portfolio.components.social_media.social_media import social_media
from portfolio.style.colors import Color, TextColor
import portfolio.style.styles as styles


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.image(
                    src="https://i.postimg.cc/VkHYXNX7/profile.png",
                    alt="Profile picture",
                    position="absolute",
                    margin_left=styles.Size.DEFAULT.value,
                    margin_top=styles.Size.DEFAULT.value,
                    border_radius=styles.Size.SMALL.value,
                    style=styles.border,
                    bg=Color.BACKGROUND_CONTAINER.value,
                    z_index="10",
                ),
                style=styles.container_header,
            ),
            rx.vstack(
                rx.heading(
                    "Backend Developer",
                    style=styles.header_title_style,
                ),
                rx.text(
                    "Luis Guzmán",
                    font_size=styles.Size.LARGE.value,
                    font_weight="bold",
                ),
                rx.text(
                    "@lupydev",
                    font_weight="bold",
                    color=Color.SECUNDARY_LIGHT.value,
                ),
                rx.hstack(
                    rx.tooltip(
                        social_media(
                            "icons/github.svg",
                            styles.Size.BIG.value,
                            "https://github.com/lupydev",
                        ),
                        label="GitHub",
                    ),
                    rx.tooltip(
                        social_media(
                            "icons/linkedin.svg",
                            styles.Size.BIG.value,
                            "https://www.linkedin.com/in/lupydev/",
                        ),
                        label="LinkedIn",
                    ),
                    rx.tooltip(
                        social_media(
                            "icons/floppy.svg",
                            styles.Size.BIG.value,
                            "",
                        ),
                        label="Curriculum Vitae",
                    ),
                    margin_top=styles.Size.SMALL.value,
                ),
                width="19em",
                align_items="start",
                gap=styles.Size.SMALL.value,
            ),
            gap=styles.Size.BIG.value,
        ),
        rx.text(
            "Soy un desarrollador python con un año de experiencia. Mi objetivo principal es aprender y crecer constantemente mientras contribuyo al mundo de la tecnología. Durante mi tiempo de aprendizaje he estado enfocándome en adquirir sólidos conocimientos en Django REST framework y FastAPI para desarrollar RESTful APIs de calidad. Estoy emocionado por las oportunidades que estas tecnologías brindan para crear aplicaciones o páginas webs de alto rendimiento y escalabilidad.",
            max_width="40em",
        ),
        gap=styles.Size.XL.value,
        margin_top=styles.Size.EXTREME_BIG.value,
    )
