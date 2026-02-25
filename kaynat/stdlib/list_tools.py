"""
Kaynat List Tools - List manipulation operations.

Provides comprehensive list functionality for Kaynat programs.
"""

from kaynat.interpreter.runtime_types import KaynatList, KaynatNumber, KaynatBoolean
from kaynat.errors.error_types import TypeError as KaynatTypeError, ValueError as KaynatValueError, RuntimeError as KaynatRuntimeError


def list_append(lst, item):
    """Add item to end of list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Append requires a list")
    
    lst.value.append(item)
    return lst


def list_prepend(lst, item):
    """Add item to beginning of list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Prepend requires a list")
    
    lst.value.insert(0, item)
    return lst


def list_insert(lst, index, item):
    """Insert item at specified index."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Insert requires a list")
    
    idx = int(index.value if isinstance(index, KaynatNumber) else index)
    lst.value.insert(idx, item)
    return lst


def list_remove(lst, item):
    """Remove first occurrence of item."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Remove requires a list")
    
    try:
        lst.value.remove(item)
    except ValueError:
        raise KaynatValueError(f"Item not found in list")
    
    return lst


def list_remove_at(lst, index):
    """Remove item at specified index."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Remove at requires a list")
    
    idx = int(index.value if isinstance(index, KaynatNumber) else index)
    
    if idx < 0 or idx >= len(lst.value):
        raise KaynatValueError(f"Index {idx} out of range")
    
    removed = lst.value.pop(idx)
    return removed


def list_get(lst, index):
    """Get item at specified index."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Get requires a list")
    
    idx = int(index.value if isinstance(index, KaynatNumber) else index)
    
    if idx < 0 or idx >= len(lst.value):
        raise KaynatValueError(f"Index {idx} out of range")
    
    return lst.value[idx]


def list_length(lst):
    """Get length of list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Length requires a list")
    
    return KaynatNumber(len(lst.value))


def list_is_empty(lst):
    """Check if list is empty."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Is empty requires a list")
    
    return KaynatBoolean(len(lst.value) == 0)


def list_contains(lst, item):
    """Check if list contains item."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Contains requires a list")
    
    return KaynatBoolean(item in lst.value)


def list_index_of(lst, item):
    """Find index of item (-1 if not found)."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Index of requires a list")
    
    try:
        return KaynatNumber(lst.value.index(item))
    except ValueError:
        return KaynatNumber(-1)


def list_sort(lst, reverse=False):
    """Sort list in place."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Sort requires a list")
    
    rev = reverse.value if isinstance(reverse, KaynatBoolean) else reverse
    
    try:
        lst.value.sort(key=lambda x: x.value if hasattr(x, 'value') else x, reverse=rev)
    except Exception as e:
        raise KaynatRuntimeError(f"Cannot sort list: {e}")
    
    return lst


def list_reverse(lst):
    """Reverse list in place."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Reverse requires a list")
    
    lst.value.reverse()
    return lst


def list_copy(lst):
    """Create a shallow copy of list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Copy requires a list")
    
    return KaynatList(lst.value.copy())


def list_clear(lst):
    """Remove all items from list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Clear requires a list")
    
    lst.value.clear()
    return lst


def list_extend(lst, other):
    """Extend list with items from another list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Extend requires a list")
    if not isinstance(other, KaynatList):
        raise KaynatTypeError("Extend requires another list")
    
    lst.value.extend(other.value)
    return lst


def list_slice(lst, start, end=None):
    """Get slice of list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Slice requires a list")
    
    start_idx = int(start.value if isinstance(start, KaynatNumber) else start)
    
    if end is None:
        return KaynatList(lst.value[start_idx:])
    
    end_idx = int(end.value if isinstance(end, KaynatNumber) else end)
    return KaynatList(lst.value[start_idx:end_idx])


def list_count(lst, item):
    """Count occurrences of item in list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Count requires a list")
    
    return KaynatNumber(lst.value.count(item))


def list_min(lst):
    """Find minimum value in list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Min requires a list")
    
    if len(lst.value) == 0:
        raise KaynatValueError("Cannot find min of empty list")
    
    return min(lst.value, key=lambda x: x.value if hasattr(x, 'value') else x)


def list_max(lst):
    """Find maximum value in list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Max requires a list")
    
    if len(lst.value) == 0:
        raise KaynatValueError("Cannot find max of empty list")
    
    return max(lst.value, key=lambda x: x.value if hasattr(x, 'value') else x)


def list_sum(lst):
    """Calculate sum of numeric list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Sum requires a list")
    
    total = 0
    for item in lst.value:
        val = item.value if hasattr(item, 'value') else item
        total += val
    
    return KaynatNumber(total)


def list_average(lst):
    """Calculate average of numeric list."""
    if not isinstance(lst, KaynatList):
        raise KaynatTypeError("Average requires a list")
    
    if len(lst.value) == 0:
        raise KaynatValueError("Cannot calculate average of empty list")
    
    total = list_sum(lst).value
    return KaynatNumber(total / len(lst.value))
