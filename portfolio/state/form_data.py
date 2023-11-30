import reflex as rx
import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from portfolio.state.base import State
from decouple import config


class FormState(State):
    email: str
    message: str
    modal_message: str
    show_modal: bool = False

    @rx.var
    def is_name_error(self) -> bool:
        if self.name == "":
            return False
        else:
            return len(self.name) < 2

    @rx.var
    def is_email_error(self) -> bool:
        if self.email == "":
            return False
        return len(self.email) < 6

    @rx.var
    def is_message_error(self) -> bool:
        if self.message == "":
            return False
        else:
            return len(self.message) < 10

    def handle_submit(self, form_data: dict):
        """Handle the data sending to API."""
        self.form_data = form_data
        self.modal_message = "Gracias por comunicarte conmigo, te estaré respondiendo a la brevedad posible"
        self.show_modal = not self.show_modal
        yield FormState.send_email(form_data)
        yield FormState.toggle_modal
        return [rx.set_value(field_id, "") for field_id in form_data]

    # @rx.background
    def send_email(self, form_data: dict):
        # async with self:
        self.mensaje = ""
        try:
            # Configuración del servidor de email
            server = smtplib.SMTP(
                config("EMAIL_HOST"),
                config("EMAIL_PORT"),
            )
            server.starttls()
            server.login(
                config("EMAIL_HOST_USER"),
                config("EMAIL_HOST_PASSWORD"),
            )
            name = form_data.get("name")
            email = form_data.get("email")
            message = form_data.get("message")
            divider = "-" * 40

            # Construir el message de email
            msg = MIMEMultipart()
            msg["From"] = email
            msg["To"] = config("EMAIL_TO")
            msg["Subject"] = f"LupyDev -> {name}"

            cuerpo_mensaje = f"Alguien acaba de enviarte un correro desde: https://lupy.dev\n\nNombre:\n{name}\n{divider}\nCorreo:\n{email}\n{divider}\n\nMensaje:\n{message}\n{divider}"
            msg.attach(MIMEText(cuerpo_mensaje, "plain"))

            # Enviar el message
            server.sendmail(email, config("EMAIL_HOST_USER"), msg.as_string())
            server.quit()

        except Exception as e:
            self.mensaje = f"Error al enviar el correo: {e}"

        # finally:
        #     return [rx.set_value(field_id, "") for field_id in form_data]

    # @rx.background
    def toggle_modal(self):
        # async with self:
        asyncio.sleep(2)
        self.show_modal = False

    async def close_modal(self):
        async with self:
            self.show_modal = False
