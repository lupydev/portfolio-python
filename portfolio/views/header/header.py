import reflex as rx
from portfolio.components.social_media.social_media import social_media
from portfolio.style.colors import Color, TextColor
import portfolio.style.styles as styles


def header() -> rx.Component:
    return rx.vstack(
        rx.desktop_only(
            rx.hstack(
                rx.image(
                    src="https://i.postimg.cc/VkHYXNX7/profile.png",
                    alt="Profile picture",
                    margin_left=styles.Size.DEFAULT.value,
                    margin_top=styles.Size.DEFAULT.value,
                    border_top_left_radius=styles.Size.SMALL.value,
                    border_bottom_left_radius=styles.Size.SMALL.value,
                    border_bottom_right_radius=styles.Size.SMALL.value,
                    style=styles.border,
                    bg=Color.BACKGROUND_CONTAINER.value,
                    z_index="10",
                    box_shadow=f"-{styles.Size.DEFAULT.value} -{styles.Size.DEFAULT.value} {Color.PRIMARY.value}",
                    height="19em",
                    width="19em",
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
                    width="100%",
                    margin_left=styles.Size.ZERO.value,
                    align_items="start",
                    gap=styles.Size.SMALL.value,
                ),
                margin_top=styles.Size.EXTREME_BIG.value,
                gap=styles.Size.BIG.value,
            ),
        ),
        rx.tablet_only(
            rx.vstack(
                rx.image(
                    src="https://i.postimg.cc/VkHYXNX7/profile.png",
                    alt="Profile picture",
                    margin_left=styles.Size.DEFAULT.value,
                    margin_top=styles.Size.DEFAULT.value,
                    border_top_left_radius=styles.Size.SMALL.value,
                    border_bottom_left_radius=styles.Size.SMALL.value,
                    border_bottom_right_radius=styles.Size.SMALL.value,
                    style=styles.border,
                    bg=Color.BACKGROUND_CONTAINER.value,
                    box_shadow=f"-{styles.Size.DEFAULT.value} -{styles.Size.DEFAULT.value} {Color.PRIMARY.value}",
                    height="20em",
                    width="20em",
                ),
                rx.vstack(
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
                        align_self="center",
                        margin_top=styles.Size.SMALL.value,
                    ),
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
                    width="19em",
                    align_items="start",
                    gap=styles.Size.SMALL.value,
                ),
                margin_top=styles.Size.EXTREME_BIG.value,
                gap=styles.Size.DEFAULT.value,
            ),
        ),
        rx.mobile_only(
            rx.vstack(
                rx.image(
                    src="https://i.postimg.cc/VkHYXNX7/profile.png",
                    alt="Profile picture",
                    margin_left=styles.Size.DEFAULT.value,
                    margin_top=styles.Size.DEFAULT.value,
                    border_top_left_radius=styles.Size.SMALL.value,
                    border_bottom_left_radius=styles.Size.SMALL.value,
                    border_bottom_right_radius=styles.Size.SMALL.value,
                    style=styles.border,
                    bg=Color.BACKGROUND_CONTAINER.value,
                    box_shadow=f"-{styles.Size.DEFAULT.value} -{styles.Size.DEFAULT.value} {Color.PRIMARY.value}",
                    height="14em",
                    width="14em",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.tooltip(
                            social_media(
                                "icons/github.svg",
                                styles.Size.LARGE.value,
                                "https://github.com/lupydev",
                            ),
                            label="GitHub",
                        ),
                        rx.tooltip(
                            social_media(
                                "icons/linkedin.svg",
                                styles.Size.LARGE.value,
                                "https://www.linkedin.com/in/lupydev/",
                            ),
                            label="LinkedIn",
                        ),
                        rx.tooltip(
                            social_media(
                                "icons/floppy.svg",
                                styles.Size.LARGE.value,
                                "",
                            ),
                            label="Curriculum Vitae",
                        ),
                        align_self="center",
                        margin_top=styles.Size.SMALL.value,
                    ),
                    rx.heading(
                        "Backend Developer",
                        font_size=styles.Size.LARGE.value,
                        color=TextColor.TITLE.value,
                        font_weight="bold",
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
                    width="15em",
                    align_items="start",
                    gap=styles.Size.SMALL.value,
                ),
                margin_top=styles.Size.VERY_BIG.value,
                margin_x=styles.Size.DEFAULT.value,
                gap=styles.Size.DEFAULT.value,
            ),
        ),
        rx.tablet_and_desktop(
            rx.text(
                "Transformo ideas en funcionalidades, sueños en interactividad. Soy el desarrollador que convierte desafíos en soluciones, y códigos en experiencias memorables. ",
                rx.link(
                    "¿Te unes a la aventura?",
                    color=Color.SECUNDARY.value,
                    text_decoration="underline",
                    href="#contacto",
                ),
                margin_x=styles.Size.BIG.value,
                font_size=styles.Size.LARGE.value,
            ),
        ),
        max_width="42em",
        gap=styles.Size.XL.value,
    )
