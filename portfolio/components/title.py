import reflex as rx
import portfolio.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style,
        font_family=styles.Fonts.SECONDARY
    )
