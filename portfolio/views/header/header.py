import reflex as rx
from portfolio.components.link_button import link_button
import portfolio.styles.styles as styles
from portfolio.styles.styles import Size as Size
import portfolio.constants as Constants


def header() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.grid(
                rx.center(
                    rx.avatar(
                        src="images/IMG_8271.jpeg",
                        fallback="LP",
                        size="9",
                        radius="full",
                        border_color=styles.Colours.SECOND_COLOUR,
                        border_width="4px",
                        border_style="solid",
                    ),
                ),
                rx.center(
                    rx.vstack(
                        rx.text(
                            "Lucas Walter Pino",
                            font_size=rx.breakpoints(
                                initial=Size.DEFAULT,
                                sm=Size.DEFAULT,
                                lg=Size.LARGE
                            ),
                            margin_y=rx.breakpoints(
                                initial=Size.X_SMALL,
                                sm=Size.X_SMALL,
                                lg="0px"
                            )
                        ),
                        rx.text(
                            "Full Stack Developer",
                            font_size=rx.breakpoints(
                                initial=Size.SMALL,
                                sm=Size.SMALL,
                                lg=Size.DEFAULT
                            ),
                            margin_bottom=rx.breakpoints(
                                initial=Size.X_SMALL,
                                sm=Size.X_SMALL,
                                lg="0px"
                            )
                        ),
                        rx.text(
                            "Learning, Building, and improving every day.",
                            font_size=Size.X_SMALL,
                            text_align="center",
                        ),
                        align="center",
                        spacing="0",
                    ),
                ),
                columns={
                    "base": "1",   # 1 columna en pantallas pequeñas
                    "sm": "2",     # 2 columnas en pantallas un poco más grandes
                    "md": "2",     # 3 columnas en pantallas medianas para arriba
                },
            ),
            width="100%",
            padding_y=Size.X_LARGE,
        ),
        rx.center(
            rx.text(
                """I'm a Computer Science student with a solid foundation in Python and full-stack knowledge. I'm looking for my first opportunity as a junior developer in a remote position, as my traveling lifestyle and distance studies have helped me develop strong autonomy and adaptability traits, that drive my continuous and efficient learning.""",
                align="center",
            ),
            width=rx.breakpoints(
                initial="100%",
                sm="100%",
                lg="80%",
            ),
            padding=Size.SMALL,
        ),
        rx.flex(
            link_button("Download CV", "/resume/resume.docx.pdf",
                        download=True),
            link_button("Go to GitHub", Constants.GIT_HUB_URL),
            padding=Size.SMALL,
            spacing="3"
        ),
        width="100%",
        align_items="center",
        padding=Size.SMALL,
    )
