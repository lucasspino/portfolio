import reflex as rx
from portfolio.components.skill_card import skill_card
from portfolio.components.link_button import link_button
from portfolio.styles.styles import Size as Size
import portfolio.styles.styles as styles
from portfolio.styles.styles import Fonts as Fonts


def projects_cards(img: str, title: str, text: str, tools: list[tuple[str, str]], code_link: str, view_demo: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.image(
                src=img,
                width="100%",
                height='auto',
                border_radius=Size.XX_SMALL
            ),
            rx.heading(
                title,
                text_align="center",
                font_family=Fonts.SECONDARY
            ),
            rx.text(
                text,
                text_align="center"
            ),
            rx.flex(
                *[skill_card(icon, name) for icon, name in tools],
                direction="row",               # fila horizontal
                flex_wrap="wrap",              # permite saltar de línea si hay muchos elementos
                justify_content="center",      # centra horizontalmente
                align_items="center",          # centra verticalmente
                width="100%",                  # asegura que el contenedor ocupe todo el ancho
                gap=Size.XX_SMALL,                   # espacio entre tarjetas
                padding_y=Size.XX_SMALL,
            ),
            rx.hstack(
                link_button(
                    "Code",
                    code_link
                ),
                link_button(
                    "View Demo",
                    view_demo
                ),
                width='100%',
                align_items='center',
                justify_content='center'
            ),
            align_items='center',
        ),
    )
