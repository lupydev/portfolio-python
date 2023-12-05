import reflex as rx
from portfolio.state.form_data import FormState
from portfolio.style.colors import Color
import portfolio.style.styles as styles


def contac_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                id="tablet_desktop",
                display="none",
            ),
            rx.form_control(
                rx.input(
                    placeholder="Nombre",
                    id="name",
                    on_blur=FormState.set_name,
                    focus_border_color=Color.PRIMARY.value,
                    error_border_color=Color.PRIMARY_LIGHT.value,
                    is_required=True,
                ),
                rx.cond(
                    FormState.is_name_error,
                    rx.form_error_message(
                        "El nombre debe ser mayor de 2 caracteres",
                    ),
                ),
                is_invalid=FormState.is_name_error,
            ),
            rx.form_control(
                rx.input(
                    placeholder="hello@lupy.dev",
                    type_="email",
                    id="email",
                    on_blur=FormState.set_email,
                    focus_border_color=Color.PRIMARY.value,
                    error_border_color=Color.PRIMARY_LIGHT.value,
                    is_required=True,
                ),
                rx.cond(
                    FormState.is_email_error,
                    rx.form_error_message(
                        "El email debe ser mayor de 6 caracteres",
                    ),
                ),
                is_invalid=FormState.is_email_error,
            ),
            rx.form_control(
                rx.text_area(
                    placeholder="Hola Lupy!\n\nMe encantaría que me ayudes a volver realidad este proyecto.",
                    on_blur=FormState.set_message,
                    height="10em",
                    focus_border_color=Color.PRIMARY.value,
                    error_border_color=Color.PRIMARY_LIGHT.value,
                    is_required=True,
                    id="message",
                ),
                rx.cond(
                    FormState.is_message_error,
                    rx.form_error_message(
                        "El mensaje debe ser mayor de 10 caracteres",
                    ),
                ),
                is_invalid=FormState.is_message_error,
            ),
            rx.button(
                "Enviar",
                type_="submit",
                style=styles.button_form,
                is_disabled=FormState.is_button_disable,
            ),
            rx.modal(
                rx.modal_overlay(
                    rx.modal_content(
                        rx.modal_header("Mensaje enviado!"),
                        rx.modal_body(FormState.modal_message),
                    ),
                ),
                is_open=FormState.show_modal,
                close_on_esc=True,
                close_on_overlay_click=True,
                is_centered=True,
            ),
            gap=styles.Size.SMALL.value,
        ),
        width="100%",
        paddin=styles.Size.DEFAULT.value,
        gap=styles.Size.SMALL.value,
        on_submit=FormState.handle_submit,
        reset_on_submit=True,
        handle_submit_unique_name="tablet-desktop",
    )
