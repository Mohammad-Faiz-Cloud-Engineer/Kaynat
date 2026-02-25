"""Kaynat GUI Themes - Stub implementation."""


class Theme:
    """GUI theme."""
    def __init__(self, name):
        self.name = name
        self.colors = {}
        self.fonts = {}


class DarkTheme(Theme):
    """Dark theme."""
    def __init__(self):
        super().__init__("dark")
        self.colors = {
            "background": "#2b2b2b",
            "foreground": "#ffffff",
            "accent": "#0078d4"
        }


class LightTheme(Theme):
    """Light theme."""
    def __init__(self):
        super().__init__("light")
        self.colors = {
            "background": "#ffffff",
            "foreground": "#000000",
            "accent": "#0078d4"
        }


def apply_theme(window, theme):
    """Apply theme to window."""
    # Theme application logic would go here
    pass
