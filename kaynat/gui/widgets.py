"""Kaynat GUI Widgets - Stub implementation."""


class Widget:
    """Base widget class."""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visible = True


class Label(Widget):
    """Label widget."""
    def __init__(self, text=""):
        super().__init__()
        self.text = text


class Button(Widget):
    """Button widget."""
    def __init__(self, text="Button"):
        super().__init__()
        self.text = text
        self.on_click = None


class TextInput(Widget):
    """Text input widget."""
    def __init__(self, placeholder=""):
        super().__init__()
        self.text = ""
        self.placeholder = placeholder


class TextArea(Widget):
    """Multi-line text area widget."""
    def __init__(self):
        super().__init__()
        self.text = ""


class Checkbox(Widget):
    """Checkbox widget."""
    def __init__(self, label=""):
        super().__init__()
        self.label = label
        self.checked = False


class Dropdown(Widget):
    """Dropdown widget."""
    def __init__(self, options=None):
        super().__init__()
        self.options = options or []
        self.selected = None
