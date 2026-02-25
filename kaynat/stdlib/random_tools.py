"""Kaynat Random Number Tools."""

import random
import string
from kaynat.interpreter.runtime_types import KaynatNumber, KaynatBoolean, KaynatString, KaynatList
from kaynat.errors.error_types import TypeError as KaynatTypeError


def random_integer(min_val, max_val):
    """Generate random integer between min and max (inclusive)."""
    min_v = int(min_val.value if hasattr(min_val, 'value') else min_val)
    max_v = int(max_val.value if hasattr(max_val, 'value') else max_val)
    return KaynatNumber(random.randint(min_v, max_v))


def random_float():
    """Generate random float between 0 and 1."""
    return KaynatNumber(random.random())


def random_boolean():
    """Generate random boolean."""
    return KaynatBoolean(random.choice([True, False]))


def random_choice(lst):
    """Choose random item from list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Random choice requires a list")
    
    if len(lst.value) == 0:
        raise KaynatTypeError("Cannot choose from empty list")
    
    return random.choice(lst.value)


def shuffle_list(lst):
    """Shuffle list in place."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Shuffle requires a list")
    
    random.shuffle(lst.value)
    return lst


def random_string(length):
    """Generate random alphanumeric string."""
    len_val = int(length.value if hasattr(length, 'value') else length)
    chars = string.ascii_letters + string.digits
    return KaynatString(''.join(random.choice(chars) for _ in range(len_val)))
