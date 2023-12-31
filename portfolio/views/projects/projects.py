import reflex as rx

from portfolio.components.image.image import img
from portfolio.components.project.project import project
from portfolio.components.social_media.social_media import social_media
from portfolio.style.colors import Color
import portfolio.style.styles as styles


def projects() -> rx.Component:
    return rx.vstack(
        rx.tablet_and_desktop(
            rx.heading(
                "Portafolio",
                style=styles.header_title_style,
                align_self="start",
                margin_bottom=styles.Size.SMALL.value,
                padding_top=styles.Size.VERY_BIG.value,
            ),
            margin_x=styles.Size.VERY_BIG.value,
        ),
        rx.mobile_only(
            rx.heading(
                "Portafolio",
                style=styles.header_title_style,
                align_self="start",
                margin_x=styles.Size.DEFAULT.value,
                margin_bottom=styles.Size.SMALL.value,
                padding_top=styles.Size.XL.value,
            ),
        ),
        rx.vstack(
            project(
                "El Buen Conejo",
                "https://res.cloudinary.com/dzc8agefr/image/upload/v1699939914/1_vdi3km.png",
                "conejon",
                rx.text(
                    "Plataforma web que reune al gremio de cunicultores para impulsar el sector, las granjas de criaderos y el consumo de carne de conejo como alternativa a otras proteinas animales, además de dar visibilidad a los productores y crear comunidad."
                ),
                rx.hstack(
                    social_media(
                        "icons/external_link.svg",
                        styles.Size.DEFAULT.value,
                        "https://el-buen-conejo-p77dvghrt-jaardila-3.vercel.app/",
                    ),
                    social_media(
                        "icons/github.svg",
                        styles.Size.DEFAULT.value,
                        "https://github.com/lupydev/el-buen-conejo",
                    ),
                    position="absolute",
                    bottom=styles.Size.MEDIUM.value,
                    right=styles.Size.MEDIUM.value,
                ),
            ),
            gap=styles.Size.BIG.value,
            border=styles.border,
        ),
        align_items="start",
        gap=styles.Size.DEFAULT.value,
        id="portafolio",
    )
