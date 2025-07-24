import reflex as rx
import portfolio.styles.styles as styles
from portfolio.styles.styles import Size as Size
import portfolio.constants as Constants


def footer() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Lucas Walter Pino - Full Stack Developer",
            font_size=rx.breakpoints(
                initial=Size.SMALL,
                sm=Size.SMALL,
                lg=Size.DEFAULT,
            ),
            font_family=styles.Fonts.SECONDARY,
            padding_x=Size.SMALL,
            text_align="center"
        ),
        rx.text(
            "Learning, Building, and improving every day.",
            font_size=rx.breakpoints(
                initial=Size.X_SMALL,
                sm=Size.X_SMALL,
                lg=Size.SMALL,
            ),
            padding_x=Size.SMALL,
            text_align="center"
        ),
        rx.hstack(
            rx.link(
                rx.icon("github", size=30),
                href=Constants.GIT_HUB_URL,
                is_external=True,
                color=styles.Colours.THIRD_COLOUR,
            ),
            rx.link(
                rx.icon("linkedin", size=30),
                href=Constants.LINKEDIN_URL,
                is_external=True,
                color=styles.Colours.THIRD_COLOUR,
            ),
            rx.link(
                rx.icon("mail", size=30),
                href="mailto:lucaspino07@gmail.com",
                is_external=True,
                title="lucaspino07@gmail.com",
                color=styles.Colours.THIRD_COLOUR,
            ),
        ),
        rx.text(
            "© 2025 Lucas Walter Pino. All rights reserved.",
            font_size=rx.breakpoints(
                initial=Size.XX_SMALL,
                sm=Size.SMALL,
                lg=Size.X_SMALL,
            ),
        ),
        width="100%",
        align_items="center",
        padding_top="5em",
        margin_bottom="2em"
    )
