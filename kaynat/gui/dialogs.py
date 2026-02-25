"""Kaynat GUI Dialogs - Stub implementation."""


def show_message(message):
    """Show a message dialog."""
    print(f"[MESSAGE] {message}")


def show_error(message):
    """Show an error dialog."""
    print(f"[ERROR] {message}")


def show_warning(message):
    """Show a warning dialog."""
    print(f"[WARNING] {message}")


def ask_confirmation(message):
    """Ask for user confirmation."""
    response = input(f"{message} (yes/no): ")
    return response.lower() in ('yes', 'y')


def choose_file():
    """Open file chooser dialog."""
    return input("Enter file path: ")


def choose_folder():
    """Open folder chooser dialog."""
    return input("Enter folder path: ")


def save_file():
    """Open save file dialog."""
    return input("Enter save path: ")
