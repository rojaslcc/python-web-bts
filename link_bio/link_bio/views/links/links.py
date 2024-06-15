import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Facebook Bruddas Tech&Solutions",
            "Proyecto de amigos para el desarrollo de aplicaciones/juegos/apps interactivas Mobile/Web/Desktop en modalidad freelance.",
            "icons/facebook.svg",
            const.FACEBOOK_BTS_URL
        ),
        link_button(
            "Twitch",
            "Pronto transmisiones sobre temas de programación/tecnología.",
            "icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "YouTube ⓘ canal Bruddas Tech&Solutions",
            "Proyecto de amigos para el generación de tutoriales y contenido de aplicaciones/juegos/apps interactivas Mobile/Web/Desktop y tecnología.",
            "icons/youtube.svg",
            const.YOUTUBE_BTS_URL
        ),

        title("Recursos y más"),
        link_button(
            "Blog",
            "Blog del equipo donde publicamos novedades de nuestros servicios.",
            "icons/wordpress.svg",
            const.WORDPRESS_URL
        ),

        title("Contacto"),
        link_button(
            "e-Mail",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )
