import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("BTS", color=Color.PRIMARY.value),
            rx.span(".", color=TextColor.BODY.value),
            rx.span("SW", color=Color.PRIMARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
