import reflex as rx
import portfolio.styles.styles as styles
from portfolio.styles.styles import Size as Size
import portfolio.constants as Constants


def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text(
                "Lucas Walter Pino",
                font_size=Size.SMALL,
            ),
            rx.hstack(
                rx.link(
                    rx.icon("file-user", size=30,),
                    href="/resume/resume.docx.pdf",
                    is_external=True,
                    color=styles.Colours.THIRD_COLOUR,
                ),
                rx.link(
                    rx.icon("github", size=30,),
                    href=Constants.GIT_HUB_URL,
                    is_external=True,
                    color=styles.Colours.THIRD_COLOUR,
                ),
                spacing=rx.breakpoints(
                    initial="2",
                    sm="4",
                    lg="5"
                ),
            ),
            width="100%",
            justify_content="space-between",
            padding_x=Size.MEDIUM,
            padding_y=Size.SMALL,
        ),
        position="sticky",
        top="0",
        width="100%",
        height=Size.LARGE,
        border_radius=Size.SMALL,
        bg=styles.Colours.FIRST_COLOUR,
        z_index=999,
    )
