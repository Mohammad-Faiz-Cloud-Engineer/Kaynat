"""Kaynat GUI Canvas - Stub implementation."""


class Canvas:
    """Canvas for drawing graphics."""
    
    def __init__(self, width=600, height=400):
        self.width = width
        self.height = height
        self.shapes = []
    
    def draw_line(self, x1, y1, x2, y2, color="black"):
        """Draw a line."""
        self.shapes.append(("line", x1, y1, x2, y2, color))
    
    def draw_rectangle(self, x, y, width, height, fill="white"):
        """Draw a rectangle."""
        self.shapes.append(("rectangle", x, y, width, height, fill))
    
    def draw_circle(self, x, y, radius, fill="white"):
        """Draw a circle."""
        self.shapes.append(("circle", x, y, radius, fill))
    
    def draw_text(self, text, x, y, font="Arial 12"):
        """Draw text."""
        self.shapes.append(("text", text, x, y, font))
    
    def clear(self):
        """Clear the canvas."""
        self.shapes.clear()
