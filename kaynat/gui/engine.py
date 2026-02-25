"""Kaynat GUI Engine - Stub implementation."""


class GUIEngine:
    """Main GUI engine for Kaynat applications."""
    
    def __init__(self):
        self.windows = []
        self.running = False
    
    def create_window(self, title="Kaynat App", width=800, height=600):
        """Create a new window."""
        from kaynat.gui.window import Window
        window = Window(title, width, height)
        self.windows.append(window)
        return window
    
    def run(self):
        """Start the GUI event loop."""
        self.running = True
        # Event loop would go here
        pass
    
    def stop(self):
        """Stop the GUI event loop."""
        self.running = False
