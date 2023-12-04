import reflex as rx
from portfolio.components.form.form import contac_form
from portfolio.components.form.mobile_form import contac_form_mobile
from portfolio.style.colors import Color
import portfolio.style.styles as styles


def contact() -> rx.Component:
    return rx.vstack(
        rx.tablet_and_desktop(
            rx.heading(
                "Contacto",
                text_align="end",
                margin_bottom=styles.Size.SMALL.value,
                style=styles.header_title_style,
                padding_top=styles.Size.VERY_BIG.value,
            ),
            rx.grid(
                rx.grid_item(
                    bg=Color.BACKGROUND_CONTAINER.value,
                ),
                rx.grid_item(
                    contac_form(),
                    bg=Color.BACKGROUND.value,
                ),
                template_columns="repeat(2, 1fr)",
                width="100%",
                height="100%",
                gap=styles.Size.DEFAULT.value,
            ),
            width="42em",
        ),
        rx.mobile_only(
            rx.vstack(
                rx.heading(
                    "Contacto",
                    align_self="start",
                    margin_bottom=styles.Size.SMALL.value,
                    style=styles.header_title_style,
                    padding_top=styles.Size.XL.value,
                ),
                contac_form_mobile(),
                margin_x=styles.Size.DEFAULT.value,
            ),
            width="100%",
        ),
        width="100%",
        id="contacto",
    )
