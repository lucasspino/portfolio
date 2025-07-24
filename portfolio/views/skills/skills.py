import reflex as rx
from portfolio.components.skill_card import skill_card
from portfolio.components.title import title
import portfolio.styles.styles as styles
from portfolio.styles.styles import Size as Size

skill_list = [
    {"icon": "html.svg", "name": "HTML"},
    {"icon": "css.svg", "name": "CSS"},
    {"icon": "js.svg", "name": "JavaScript"},
    {"icon": "python.svg", "name": "Python"},
    {"icon": "database.svg", "name": "SQL"},
    {"icon": "git.svg", "name": "GIT"},
]


def skills() -> rx.Component:
    return rx.vstack(
        rx.box(
            title("Skills"),
            width="80%",
        ),
        rx.grid(
            *[skill_card(skill["icon"], skill["name"])
              for skill in skill_list],
            columns={
                "base": "1",   # 1 columna en pantallas pequeñas
                "sm": "4",     # 2 columnas en pantallas un poco más grandes
                "md": "6",     # 3 columnas en pantallas medianas para arriba
            },
            width="80%",
            spacing="4",
            padding_x=Size.SMALL,
            margin_bottom=Size.SMALL,
        ),
        width="100%",
        padding_x=Size.SMALL,
        align_items="center"
    )
