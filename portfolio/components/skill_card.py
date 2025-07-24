import reflex as rx
from portfolio.styles.styles import Size as Size
from portfolio.styles.styles import Fonts as Fonts


def skill_card(icon: str, name: str) -> rx.Component:
    return rx.card(
        rx.center(
            rx.image(
                src=f'/icons/{icon}',
                max_width=Size.LARGE,
                height=Size.MEDIUM,
                padding_x=Size.XX_SMALL,
            ),
            rx.text(name, font_size=Size.X_SMALL,
                    font_weight="medium",
                    font_family=Fonts.SECONDARY,
                    align_items="center",
                    ),
            spacing='1'
        ),
        display="flex",
        padding=Size.XX_SMALL,

    )
