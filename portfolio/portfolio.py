import reflex as rx
from portfolio.components.navbar import navbar
from portfolio.views.header.header import header
from portfolio.views.projects.projects import projects
from portfolio.views.skills.skills import skills
from portfolio.components.footer import footer
import portfolio.styles.styles as styles
from portfolio.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    skills(),
                    projects(),
                ),
            ),
            footer(),
            bg=styles.Colours.FIRST_COLOUR,
            border_radius=Size.SMALL,
            height="auto",
            spacing="0"
        ),
        width="100%",
        height="auto",
        bg=styles.Colours.SECOND_COLOUR,
        padding=Size.MEDIUM,
    )


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
    ],
)
app.add_page(index)
