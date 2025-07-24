import reflex as rx
from portfolio.components.projects_cards import projects_cards
from portfolio.components.title import title
from portfolio.styles.styles import Size as Size


def projects() -> rx.Component:
    return rx.vstack(
        rx.box(
            title("Projects"),
            width="80%",
        ),
        rx.grid(
            projects_cards(
                img="images/magnum.png",
                title="Magnum Construcciones",
                text="Landing page as a web site for a store of constructions materials",
                tools=[
                    ("html.svg", "HTML"),
                    ("css.svg", "CSS"),
                    ("js.svg", "JavaScript")
                ],
                code_link="https://github.com/lucasspino/Magnum",
                view_demo="https://lucasspino.github.io/Magnum/",
            ),
            columns={
                "base": "1",   # 1 columna en pantallas pequeñas
                "sm": "2",     # 2 columnas en pantallas un poco más grandes
                "md": "3",     # 3 columnas en pantallas medianas para arriba
            },
            width=rx.breakpoints(
                initial="100%",
                sm="100%",
                lg="80%",
            ),
            spacing="4",
            padding_x=Size.SMALL,
            margin_bottom=Size.SMALL,

        ),
        width="100%",
        padding_x=Size.SMALL,
        align_items="center"
    )
