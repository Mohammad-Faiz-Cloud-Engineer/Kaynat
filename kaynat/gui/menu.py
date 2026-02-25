"""Kaynat GUI Menu - Stub implementation."""


class MenuItem:
    """Menu item."""
    def __init__(self, label, action=None):
        self.label = label
        self.action = action


class Menu:
    """Menu container."""
    def __init__(self, label):
        self.label = label
        self.items = []
    
    def add_item(self, item):
        """Add menu item."""
        self.items.append(item)


class MenuBar:
    """Menu bar."""
    def __init__(self):
        self.menus = []
    
    def add_menu(self, menu):
        """Add menu to menu bar."""
        self.menus.append(menu)
