import reflex as rx
import portfolio.styles.styles as styles


def link_button(name: str, link: str, download: bool = False) -> rx.Component:
    return rx.button(
        rx.link(name,
                href=link,
                is_external=not download,  # Si es descarga, no se abre en nueva pestaña
                download=download
                ),
        bg=styles.Colours.SECOND_COLOUR,
    ),

# def link_button(name: str, link: str, download: bool = False) -> rx.Component:
#     return rx.link(
#         rx.button(name, bg=styles.Colours.SECOND_COLOUR),
#         href=link,
#         is_external=not download,  # Si es descarga, no se abre en nueva pestaña
#         download=download
#     )
