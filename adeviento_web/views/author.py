import reflex as rx

import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.components.button import button
from adeviento_web.components.header_text import header_text
from adeviento_web.styles.colors import Color, TextColor
from adeviento_web.styles.styles import Size


def author() -> rx.Component:
    return rx.vstack(
        header_text("like", "Hola, mi nombre es Brais Moure"),
        rx.flex(
            rx.avatar(
                name="Brais Moure",
                size="2xl",
                src="avatar.jpg",
                bg=Color.PRIMARY.value,
                padding="2px",
                border="4px",
                border_color=Color.SECONDARY.value,
                margin_right=Size.SMALL.value,
                margin_bottom=Size.SMALL.value,
            ),
            rx.vstack(
                rx.span("Soy ingeniero de software desde hace mas de 13 años."),
                rx.span(
                    "En 2018 comence a divulgar contenido sobre programacion y desarrollo de software en redes sociales como ",
                    rx.span(
                        "@mouredev",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value,
                    ),
                    ".",
                ),
                author_buttons(),
                width="100%",
                align_items="start",
            ),
            width="100%",
            spacing=Size.BIG.value,
            flex_direction=["column", "column", "column", "row", "row"],
        ),
        style=styles.max_width_style,
    )


def author_buttons() -> rx.Component:
    return rx.box(
        button("YouTube", constants.YOUTUBE_URL),
        button("Twitch", constants.TWITCH_URL),
        button("Twitter", constants.TWITTER_URL),
    )
