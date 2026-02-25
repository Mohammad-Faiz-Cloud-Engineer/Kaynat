"""Kaynat GUI Window - Stub implementation."""


class Window:
    """Represents a GUI window."""
    
    def __init__(self, title="Window", width=800, height=600):
        self.title = title
        self.width = width
        self.height = height
        self.widgets = []
        self.visible = False
    
    def show(self):
        """Show the window."""
        self.visible = True
    
    def hide(self):
        """Hide the window."""
        self.visible = False
    
    def close(self):
        """Close the window."""
        self.visible = False
    
    def add_widget(self, widget):
        """Add a widget to the window."""
        self.widgets.append(widget)
