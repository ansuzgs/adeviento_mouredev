import reflex as rx

import adeviento_web.styles.styles as styles
from adeviento_web.components.header_text import header_text
from adeviento_web.styles.colors import Color
from adeviento_web.styles.styles import Size


def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text("star", "Patrocinado por", dark=False),
            rx.text(
                "Con el apoyo de la comunidad y de los patrocinadores constearé los 24 regalos."
            ),
            rx.span(
                "¿Quieres apoyar esta iniciativa? Escribeme a braismoure@mouredev.com"
            ),
            padding_y=Size.VERY_BIG.value,
            style=styles.max_width_style,
        ),
        bg=Color.ACCENT.value,
        width="100%",
    )
