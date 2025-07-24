from enum import Enum
import reflex as rx

# Colours


class Colours(Enum):
    FIRST_COLOUR = "#1da484"
    SECOND_COLOUR = "#343d54"
    THIRD_COLOUR = "#ebf0ee"

# Size


class Size(Enum):
    XX_SMALL = ".5em"
    X_SMALL = ".8em"
    SMALL = "1em"
    DEFAULT = "1.5em"
    MEDIUM = "2em"
    LARGE = "3em"
    X_LARGE = "4em"

# Fonts


class Fonts(Enum):
    MAIN = "Comfortaa"
    SECONDARY = "Poppins"

# Base Styles


BASE_STYLE = {
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    },
    rx.button: {
        "padding": Size.XX_SMALL,
        "border_radius": Size.XX_SMALL,
        "font_size": Size.X_SMALL
    },
    rx.text: {
        "font_family": Fonts.MAIN
    },
}

title_style = dict(
    size="lg",
    width="100%",
    padding=Size.SMALL,
    margin_y=Size.SMALL
)
