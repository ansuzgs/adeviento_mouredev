import reflex as rx
import adeviento_web.styles.styles as styles
import adeviento_web.constants as constants

from adeviento_web.components.button import button
from adeviento_web.styles.colors import TextColor


def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Cómo funciona el evento?",
                class_name="title",
                color=TextColor.ACCENT.value,
            ),
            rx.span(
                "· Del 1 al 24 de dicimebre descubriré cada día un nuevo regalo en el calendario"
            ),
            rx.span("· Puedes participar desde cualquier parte del mundo."),
            rx.span(
                "· Solo tendras que hacer retweet a la publicacion que enlazare desde esta cuenta de X"
            ),
            button("Twitter", constants.TWITTER_URL),
            rx.span(
                "· Al dia siguiente realizare el sorteo de forma publica y compartire el ganador en la web y en X"
            ),
            button("Twitch", constants.TWITCH_URL),
            rx.span(
                "· ¡Vuelta a empezar! Publicare un nuevo regalo y comenzara de nuevo el proceso."
            ),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width="100%",
        ),
        style=styles.max_width_style,
    )
