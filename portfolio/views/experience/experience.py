from datetime import date
import reflex as rx
from portfolio.components.experience.left import experience_left
from portfolio.components.list.list_left import list_icon_left
from portfolio.components.list.list_right import list_icon_right
from portfolio.style.colors import Color
import portfolio.style.styles as styles
from portfolio.components.experience.right import experience_right


def experience() -> rx.Component:
    return rx.vstack(
        rx.tablet_and_desktop(
            rx.vstack(
                rx.heading(
                    "Experiencia",
                    text_align="center",
                    margin_bottom=styles.Size.SMALL.value,
                    style=styles.header_title_style,
                    padding_top=styles.Size.VERY_BIG.value,
                ),
                rx.grid(
                    rx.grid_item(
                        experience_left(
                            "Backend Developer Trainee",
                            "NoCountry",
                            f"Oct 2023 - {date.today().strftime('%b')} {date.today().year}",
                            list_icon_left(
                                "arrow_left",
                                Color.SECUNDARY.value,
                                "Colaboré activamente en la creación y desarrollo integral de un MVP desde sus etapas iniciales, contribuyendo al diseño y ejecución desde cero.",
                            ),
                            rx.divider(
                                border_color=Color.PRIMARY.value,
                            ),
                            list_icon_left(
                                "arrow_left",
                                Color.SECUNDARY.value,
                                "Desempeñé un papel fundamental en la elaboración del modelo entidad-relación de la base de datos.",
                            ),
                            rx.divider(
                                border_color=Color.PRIMARY.value,
                            ),
                            list_icon_left(
                                "arrow_left",
                                Color.SECUNDARY.value,
                                "Diseñé y llevé a cabo la implementación de una de las RESTful APIs esenciales para el éxito del MVP.",
                            ),
                            rx.divider(
                                border_color=Color.PRIMARY.value,
                            ),
                            list_icon_left(
                                "arrow_left",
                                Color.SECUNDARY.value,
                                "Apliqué metodología SCRUM de manera efectiva en la planificación y ejecución de mis tareas.",
                            ),
                        ),
                        height="fit-content",
                        border_bottom_right_radius=styles.Size.DEFAULT.value,
                    ),
                    rx.grid_item(
                        rx.box(
                            width="100%",
                            height="100%",
                            bg=Color.BACKGROUND.value,
                        ),
                    ),
                    # rx.grid_item(
                    #     rx.box(
                    #         width="100%",
                    #         height="100%",
                    #         bg=Color.BACKGROUND.value,
                    #     ),
                    # ),
                    # rx.grid_item(
                    #     experience_right(
                    #         "Backend Developer Trainee",
                    #         "NoCountry",
                    #         f"Oct 2023 - {date.today().strftime('%b')} {date.today().year}",
                    #         list_icon_right(
                    #             "arrow_right",
                    #             Color.SECUNDARY.value,
                    #             "Participé en la creación de un MVP desde cero.",
                    #         ),
                    #         list_icon_right(
                    #             "arrow_right",
                    #             Color.SECUNDARY.value,
                    #             "Apoyé en la creación del modelo entidad-relación de la base de datos.",
                    #         ),
                    #         list_icon_right(
                    #             "arrow_right",
                    #             Color.SECUNDARY.value,
                    #             "Desarrollé e implementé una de las RESTful APIs del MVP.",
                    #         ),
                    #     ),
                    #     border_bottom_left_radius=styles.Size.DEFAULT.value,
                    # ),
                    template_columns="repeat(2, 1fr)",
                    width="100%",
                    height="auto",
                ),
                gap=styles.Size.DEFAULT.value,
            ),
            max_width="42em",
        ),
        rx.mobile_only(
            rx.box(
                rx.heading(
                    "Experiencia",
                    justify_item="start",
                    margin_bottom=styles.Size.SMALL.value,
                    style=styles.header_title_style,
                    padding_top=styles.Size.XL.value,
                ),
                experience_right(
                    "Backend Developer Trainee",
                    "NoCountry",
                    f"Oct 2023 - {date.today().strftime('%b')} {date.today().year}",
                    list_icon_right(
                        "arrow_right",
                        Color.SECUNDARY.value,
                        "Colaboré activamente en la creación y desarrollo integral de un MVP desde sus etapas iniciales, contribuyendo al diseño y ejecución desde cero.",
                    ),
                    rx.divider(
                        border_color=Color.PRIMARY.value,
                    ),
                    list_icon_right(
                        "arrow_right",
                        Color.SECUNDARY.value,
                        "Desempeñé un papel fundamental en la elaboración del modelo entidad-relación de la base de datos.",
                    ),
                    rx.divider(
                        border_color=Color.PRIMARY.value,
                    ),
                    list_icon_right(
                        "arrow_right",
                        Color.SECUNDARY.value,
                        "Diseñé y llevé a cabo la implementación de una de las RESTful APIs esenciales para el éxito del MVP.",
                    ),
                    rx.divider(
                        border_color=Color.PRIMARY.value,
                    ),
                    list_icon_right(
                        "arrow_right",
                        Color.SECUNDARY.value,
                        "Apliqué metodología SCRUM de manera efectiva en la planificación y ejecución de mis tareas.",
                    ),
                ),
                margin_x=styles.Size.DEFAULT.value,
            ),
        ),
        id="experiencia",
    )
