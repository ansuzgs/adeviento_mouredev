import reflex as rx

import adeviento_web.styles.styles as styles
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


def calendar() -> rx.Component:
    return rx.vstack(
        header_text("heart", "Calendario de adviento"),
        rx.vstack(
            rx.hstack(
                rx.text("El evento comienza en"),
                rx.text(id="countdown"),
                align_items="start",
            ),
            button("Recordar", constants.DISCORD_EVENT_URL),
            rx.span(
                "· Los regalos son sorpresa, no olvides pasarte por aqui cada dia para descubrirlos."
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%",
        ),
        rx.responsive_grid(
            rx.foreach(
                list(range(1, 25)),
                lambda number: day(
                    number,
                ),
            ),
            columns=[3, 3, 4, 5, 6],
            width="100%",
            padding_top=Size.BIG.value,
        ),
        rx.script(src="/js/countdown.js"),
        style=styles.max_width_style,
    )
