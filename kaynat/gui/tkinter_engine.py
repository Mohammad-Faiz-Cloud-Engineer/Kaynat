"""
Kaynat GUI Engine - Tkinter Implementation

Provides a working GUI system for Kaynat applications.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import Dict, Callable, Any


class KaynatWindow:
    """A GUI window."""
    
    def __init__(self, title="Kaynat App", width=800, height=600):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.widgets = {}
        self.callbacks = {}
        
    def add_label(self, name, text, row=0, column=0, font=None):
        """Add a label widget."""
        label = tk.Label(self.root, text=text, font=font or ("Arial", 12))
        label.grid(row=row, column=column, padx=5, pady=5, sticky="w")
        self.widgets[name] = label
        return label
    
    def add_button(self, name, text, row=0, column=0, callback=None, width=None):
        """Add a button widget."""
        button = tk.Button(
            self.root, 
            text=text,
            command=lambda: self._handle_callback(name),
            width=width or 10
        )
        button.grid(row=row, column=column, padx=5, pady=5)
        self.widgets[name] = button
        if callback:
            self.callbacks[name] = callback
        return button
    
    def add_entry(self, name, row=0, column=0, width=None):
        """Add a text entry widget."""
        entry = tk.Entry(self.root, width=width or 20)
        entry.grid(row=row, column=column, padx=5, pady=5)
        self.widgets[name] = entry
        return entry
    
    def get_text(self, name):
        """Get text from a widget."""
        widget = self.widgets.get(name)
        if isinstance(widget, tk.Entry):
            return widget.get()
        elif isinstance(widget, tk.Label):
            return widget.cget("text")
        return ""
    
    def set_text(self, name, text):
        """Set text on a widget."""
        widget = self.widgets.get(name)
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
            widget.insert(0, str(text))
        elif isinstance(widget, tk.Label):
            widget.config(text=str(text))
    
    def _handle_callback(self, name):
        """Handle button callback."""
        if name in self.callbacks:
            self.callbacks[name]()
    
    def show(self):
        """Show the window and start event loop."""
        self.root.mainloop()
    
    def close(self):
        """Close the window."""
        self.root.destroy()


class GUIEngine:
    """Main GUI engine."""
    
    def __init__(self):
        self.windows = []
        self.current_window = None
    
    def create_window(self, title="Kaynat App", width=800, height=600):
        """Create a new window."""
        window = KaynatWindow(title, width, height)
        self.windows.append(window)
        self.current_window = window
        return window
    
    def run(self):
        """Start the GUI (windows handle their own event loops)."""
        if self.current_window:
            self.current_window.show()

