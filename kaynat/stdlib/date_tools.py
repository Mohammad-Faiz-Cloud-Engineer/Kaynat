"""Kaynat Date and Time Tools."""

from datetime import datetime, timedelta
from kaynat.interpreter.runtime_types import KaynatString, KaynatNumber
from kaynat.errors.error_types import ValueError as KaynatValueError


def current_date():
    """Get current date."""
    return KaynatString(datetime.now().strftime('%Y-%m-%d'))


def current_time():
    """Get current time."""
    return KaynatString(datetime.now().strftime('%H:%M:%S'))


def current_timestamp():
    """Get current Unix timestamp."""
    return KaynatNumber(int(datetime.now().timestamp()))


def format_date(date_obj, format_str='%Y-%m-%d'):
    """Format date with specified format."""
    fmt = format_str.value if hasattr(format_str, 'value') else format_str
    # Simplified implementation
    return KaynatString(datetime.now().strftime(fmt))


def parse_date(date_string):
    """Parse date string."""
    date_str = date_string.value if hasattr(date_string, 'value') else date_string
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        return KaynatString(str(dt.date()))
    except Exception as e:
        raise KaynatValueError(f"Invalid date format: {e}")
