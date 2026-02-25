"""Kaynat Crypto Tools - Hashing and encryption."""

import hashlib
import base64
import secrets
from kaynat.interpreter.runtime_types import KaynatString
from kaynat.errors.error_types import ValueError as KaynatValueError


def hash_sha256(text):
    """Hash text using SHA-256."""
    text_str = text.value if hasattr(text, 'value') else str(text)
    hashed = hashlib.sha256(text_str.encode()).hexdigest()
    return KaynatString(hashed)


def hash_md5(text):
    """Hash text using MD5."""
    text_str = text.value if hasattr(text, 'value') else str(text)
    hashed = hashlib.md5(text_str.encode()).hexdigest()
    return KaynatString(hashed)


def generate_token(length=32):
    """Generate secure random token."""
    len_val = int(length.value if hasattr(length, 'value') else length)
    token = secrets.token_hex(len_val // 2)
    return KaynatString(token)


def encode_base64(text):
    """Encode text to base64."""
    text_str = text.value if hasattr(text, 'value') else str(text)
    encoded = base64.b64encode(text_str.encode()).decode()
    return KaynatString(encoded)


def decode_base64(text):
    """Decode base64 text."""
    text_str = text.value if hasattr(text, 'value') else str(text)
    try:
        decoded = base64.b64decode(text_str).decode()
        return KaynatString(decoded)
    except Exception as e:
        raise KaynatValueError(f"Invalid base64: {e}")
