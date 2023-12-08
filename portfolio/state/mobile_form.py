from portfolio.state.form_data import FormState
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config


class MobileState(FormState):
    def mobile_handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.modal_message = "Gracias por comunicarte conmigo, te estaré respondiendo a la brevedad posible"
        self.show_modal = not self.show_modal
        yield MobileState.mobile_send_email(form_data)
        yield FormState.toggle_modal

    def mobile_send_email(self, form_data: dict):
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
            name = form_data.get("mobile_name")
            email = form_data.get("mobile_email")
            message = form_data.get("mobile_message")
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
