import reflex as rx
from typing import Literal

Theme = Literal["light", "dark"]


class ThemeState(rx.State):
    """Manages the theme of the application."""

    theme: Theme = "light"

    @rx.event
    def toggle_theme(self):
        """Toggle the theme between light and dark."""
        self.theme = "dark" if self.theme == "light" else "light"