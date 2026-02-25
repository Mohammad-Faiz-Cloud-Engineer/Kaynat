"""Kaynat GUI Events - Stub implementation."""


class Event:
    """Base event class."""
    def __init__(self, event_type):
        self.type = event_type


class ClickEvent(Event):
    """Mouse click event."""
    def __init__(self, x, y):
        super().__init__("click")
        self.x = x
        self.y = y


class KeyEvent(Event):
    """Keyboard event."""
    def __init__(self, key):
        super().__init__("key")
        self.key = key


class EventHandler:
    """Handles GUI events."""
    def __init__(self):
        self.handlers = {}
    
    def register(self, event_type, handler):
        """Register an event handler."""
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)
    
    def trigger(self, event):
        """Trigger an event."""
        if event.type in self.handlers:
            for handler in self.handlers[event.type]:
                handler(event)
