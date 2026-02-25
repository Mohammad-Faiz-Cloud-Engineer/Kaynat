"""
Kaynat String Tools - String manipulation operations.

Provides comprehensive string functionality for Kaynat programs.
"""

from kaynat.interpreter.runtime_types import KaynatString, KaynatNumber, KaynatBoolean, KaynatList
from kaynat.errors.error_types import TypeError as KaynatTypeError, ValueError as KaynatValueError


def to_uppercase(text):
    """Convert string to uppercase."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Uppercase requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatString(s.upper())


def to_lowercase(text):
    """Convert string to lowercase."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Lowercase requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatString(s.lower())


def to_titlecase(text):
    """Convert string to title case."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Title case requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatString(s.title())


def trim(text):
    """Remove whitespace from both ends."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Trim requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatString(s.strip())


def trim_left(text):
    """Remove whitespace from left end."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Trim left requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatString(s.lstrip())


def trim_right(text):
    """Remove whitespace from right end."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Trim right requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatString(s.rstrip())


def starts_with(text, prefix):
    """Check if string starts with prefix."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Starts with requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    p = prefix.value if isinstance(prefix, KaynatString) else str(prefix)
    
    return KaynatBoolean(s.startswith(p))


def ends_with(text, suffix):
    """Check if string ends with suffix."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Ends with requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    suf = suffix.value if isinstance(suffix, KaynatString) else str(suffix)
    
    return KaynatBoolean(s.endswith(suf))


def contains(text, substring):
    """Check if string contains substring."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Contains requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    sub = substring.value if isinstance(substring, KaynatString) else str(substring)
    
    return KaynatBoolean(sub in s)


def find_position(text, substring):
    """Find position of substring (-1 if not found)."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Find position requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    sub = substring.value if isinstance(substring, KaynatString) else str(substring)
    
    return KaynatNumber(s.find(sub))


def replace_text(text, old, new):
    """Replace all occurrences of old with new."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Replace requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    old_str = old.value if isinstance(old, KaynatString) else str(old)
    new_str = new.value if isinstance(new, KaynatString) else str(new)
    
    return KaynatString(s.replace(old_str, new_str))


def split_string(text, delimiter=' '):
    """Split string by delimiter."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Split requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    delim = delimiter.value if isinstance(delimiter, KaynatString) else str(delimiter)
    
    parts = s.split(delim)
    return KaynatList([KaynatString(part) for part in parts])


def join_strings(strings, separator=''):
    """Join list of strings with separator."""
    if not isinstance(strings, (list, KaynatList)):
        raise KaynatTypeError("Join requires a list")
    
    items = strings.value if isinstance(strings, KaynatList) else strings
    sep = separator.value if isinstance(separator, KaynatString) else str(separator)
    
    str_items = [item.value if isinstance(item, KaynatString) else str(item) for item in items]
    return KaynatString(sep.join(str_items))


def substring(text, start, end=None):
    """Extract substring from start to end."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Substring requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    start_idx = int(start.value if isinstance(start, KaynatNumber) else start)
    
    if end is None:
        return KaynatString(s[start_idx:])
    
    end_idx = int(end.value if isinstance(end, KaynatNumber) else end)
    return KaynatString(s[start_idx:end_idx])


def reverse_string(text):
    """Reverse a string."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Reverse requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatString(s[::-1])


def repeat_string(text, count):
    """Repeat string N times."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Repeat requires a string")
    if not isinstance(count, (int, KaynatNumber)):
        raise KaynatTypeError("Repeat count must be a number")
    
    s = text.value if isinstance(text, KaynatString) else text
    n = int(count.value if isinstance(count, KaynatNumber) else count)
    
    return KaynatString(s * n)


def string_length(text):
    """Get length of string."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Length requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatNumber(len(s))


def is_empty(text):
    """Check if string is empty."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Is empty requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatBoolean(len(s) == 0)


def is_numeric(text):
    """Check if string contains only digits."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Is numeric requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatBoolean(s.isdigit())


def is_alphabetic(text):
    """Check if string contains only letters."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Is alphabetic requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatBoolean(s.isalpha())


def is_alphanumeric(text):
    """Check if string contains only letters and digits."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Is alphanumeric requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    return KaynatBoolean(s.isalnum())


def pad_left(text, width, fill_char=' '):
    """Pad string on left to specified width."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Pad left requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    w = int(width.value if isinstance(width, KaynatNumber) else width)
    fill = fill_char.value if isinstance(fill_char, KaynatString) else str(fill_char)
    
    return KaynatString(s.rjust(w, fill[0] if fill else ' '))


def pad_right(text, width, fill_char=' '):
    """Pad string on right to specified width."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Pad right requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    w = int(width.value if isinstance(width, KaynatNumber) else width)
    fill = fill_char.value if isinstance(fill_char, KaynatString) else str(fill_char)
    
    return KaynatString(s.ljust(w, fill[0] if fill else ' '))


def center_string(text, width, fill_char=' '):
    """Center string within specified width."""
    if not isinstance(text, (str, KaynatString)):
        raise KaynatTypeError("Center requires a string")
    
    s = text.value if isinstance(text, KaynatString) else text
    w = int(width.value if isinstance(width, KaynatNumber) else width)
    fill = fill_char.value if isinstance(fill_char, KaynatString) else str(fill_char)
    
    return KaynatString(s.center(w, fill[0] if fill else ' '))
