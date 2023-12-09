import reflex as rx
from portfolio.components.list.list_left import list_icon_left
from portfolio.components.list.list_right import list_icon_right
from portfolio.state.form_data import FormState
from portfolio.style.colors import Color
from portfolio.style.styles import Size
import portfolio.style.styles as styles


class DrawerState(FormState):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.image(
                            src="favicon.ico",
                            height=styles.Size.LARGE.value,
                            width=styles.Size.LARGE.value,
                        ),
                        rx.heading(
                            "Lupy",
                            style=styles.navbar_title_style,
                        ),
                    ),
                    href="",
                ),
                rx.hstack(
                    rx.link(
                        "Portafolio",
                        margin_left=Size.ZERO.value,
                        padding_x=Size.SMALL.value,
                        style=styles.border_right,
                        href="#portafolio",
                    ),
                    rx.link(
                        "Experiencia",
                        margin_left=Size.ZERO.value,
                        padding_x=Size.SMALL.value,
                        style=styles.border_right,
                        href="#experiencia",
                    ),
                    rx.link(
                        "Contacto",
                        margin_left=Size.ZERO.value,
                        padding_x=Size.SMALL.value,
                        href="#contacto",
                    ),
                ),
                justify="space-between",
                padding_x=Size.EXTREME_BIG.value,
                padding_y=Size.DEFAULT.value,
            ),
        ),
        rx.tablet_only(
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.image(
                            src="favicon.ico",
                            height=styles.Size.LARGE.value,
                            width=styles.Size.LARGE.value,
                        ),
                        rx.heading(
                            "Lupy",
                            style=styles.navbar_title_style,
                        ),
                    ),
                    href="",
                ),
                rx.hstack(
                    rx.link(
                        "Portafolio",
                        margin_left=Size.ZERO.value,
                        padding_x=Size.SMALL.value,
                        style=styles.border_right,
                        href="#portafolio",
                    ),
                    rx.link(
                        "Experiencia",
                        margin_left=Size.ZERO.value,
                        padding_x=Size.SMALL.value,
                        style=styles.border_right,
                        href="#experiencia",
                    ),
                    rx.link(
                        "Contacto",
                        margin_left=Size.ZERO.value,
                        padding_x=Size.SMALL.value,
                        href="#contacto",
                    ),
                ),
                justify="space-between",
                padding_x=Size.LARGE.value,
                padding_y=Size.DEFAULT.value,
            ),
        ),
        rx.mobile_only(
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.image(
                            src="favicon.ico",
                            height=styles.Size.LARGE.value,
                            width=styles.Size.LARGE.value,
                        ),
                        rx.heading(
                            "Lupy",
                            style=styles.navbar_title_style,
                        ),
                    ),
                    href="",
                ),
                rx.box(
                    rx.button(
                        rx.icon(
                            tag="hamburger",
                        ),
                        on_click=DrawerState.right,
                    ),
                    rx.drawer(
                        rx.drawer_overlay(
                            rx.drawer_content(
                                rx.drawer_header(
                                    rx.button(
                                        rx.icon(
                                            tag="close",
                                        ),
                                        on_click=DrawerState.right,
                                    ),
                                    text_align="end",
                                ),
                                rx.drawer_body(
                                    rx.link(
                                        list_icon_right(
                                            "arrow_right",
                                            Color.SECUNDARY_LIGHT.value,
                                            "Portafolio",
                                        ),
                                        on_click=DrawerState.right,
                                        href="#portafolio",
                                    ),
                                    rx.divider(
                                        border_color=Color.PRIMARY_LIGHT.value,
                                        margin_bottom=Size.DEFAULT.value,
                                    ),
                                    rx.link(
                                        list_icon_right(
                                            "arrow_right",
                                            Color.SECUNDARY_LIGHT.value,
                                            "Experiencia",
                                        ),
                                        on_click=DrawerState.right,
                                        href="#experiencia",
                                    ),
                                    rx.divider(
                                        margin_bottom=Size.DEFAULT.value,
                                        border_color=Color.PRIMARY_LIGHT.value,
                                    ),
                                    rx.link(
                                        list_icon_right(
                                            "arrow_right",
                                            Color.SECUNDARY_LIGHT.value,
                                            "Contacto",
                                        ),
                                        on_click=DrawerState.right,
                                        href="#contacto",
                                    ),
                                    rx.divider(
                                        border_color=Color.PRIMARY_LIGHT.value,
                                        margin_bottom=Size.DEFAULT.value,
                                    ),
                                ),
                                # bg="rgba(0, 0, 0, 0.3)",
                                bg=Color.BACKGROUND.value,
                            )
                        ),
                        is_open=DrawerState.show_right,
                        close_on_esc=True,
                        close_on_overlay_click=True,
                    ),
                ),
                justify="space-between",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            ),
        ),
        style=styles.navbar,
        box_shadow=f"1px 0 4px {Color.PRIMARY_LIGHT.value}",
    )
