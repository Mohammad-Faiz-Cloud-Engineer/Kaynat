"""Kaynat Pattern Tools - Regular expressions and pattern matching."""

import re
from kaynat.interpreter.runtime_types import KaynatString, KaynatList, KaynatBoolean
from kaynat.errors.error_types import ValueError as KaynatValueError


def find_matches(pattern, text):
    """Find all matches of pattern in text."""
    pattern_str = pattern.value if hasattr(pattern, 'value') else str(pattern)
    text_str = text.value if hasattr(text, 'value') else str(text)
    
    try:
        matches = re.findall(pattern_str, text_str)
        return KaynatList([KaynatString(m) for m in matches])
    except re.error as e:
        raise KaynatValueError(f"Invalid pattern: {e}")


def matches_pattern(text, pattern):
    """Check if text matches pattern."""
    pattern_str = pattern.value if hasattr(pattern, 'value') else str(pattern)
    text_str = text.value if hasattr(text, 'value') else str(text)
    
    try:
        return KaynatBoolean(bool(re.match(pattern_str, text_str)))
    except re.error as e:
        raise KaynatValueError(f"Invalid pattern: {e}")


def replace_pattern(text, pattern, replacement):
    """Replace pattern with replacement in text."""
    pattern_str = pattern.value if hasattr(pattern, 'value') else str(pattern)
    text_str = text.value if hasattr(text, 'value') else str(text)
    repl_str = replacement.value if hasattr(replacement, 'value') else str(replacement)
    
    try:
        result = re.sub(pattern_str, repl_str, text_str)
        return KaynatString(result)
    except re.error as e:
        raise KaynatValueError(f"Invalid pattern: {e}")


def split_by_pattern(text, pattern):
    """Split text by pattern."""
    pattern_str = pattern.value if hasattr(pattern, 'value') else str(pattern)
    text_str = text.value if hasattr(text, 'value') else str(text)
    
    try:
        parts = re.split(pattern_str, text_str)
        return KaynatList([KaynatString(p) for p in parts])
    except re.error as e:
        raise KaynatValueError(f"Invalid pattern: {e}")


def is_valid_email(email):
    """Check if string is valid email."""
    email_str = email.value if hasattr(email, 'value') else str(email)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return KaynatBoolean(bool(re.match(pattern, email_str)))


def is_valid_url(url):
    """Check if string is valid URL."""
    url_str = url.value if hasattr(url, 'value') else str(url)
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return KaynatBoolean(bool(re.match(pattern, url_str)))
