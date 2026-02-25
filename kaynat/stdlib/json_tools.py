"""Kaynat JSON Tools - JSON parsing and generation."""

import json
from kaynat.interpreter.runtime_types import KaynatString, KaynatMap, KaynatList, KaynatNumber, KaynatBoolean, KaynatNull
from kaynat.errors.error_types import ValueError as KaynatValueError


def parse_json(json_string):
    """Parse JSON string to Kaynat data structure."""
    json_str = json_string.value if hasattr(json_string, 'value') else str(json_string)
    
    try:
        data = json.loads(json_str)
        return _python_to_kaynat(data)
    except json.JSONDecodeError as e:
        raise KaynatValueError(f"Invalid JSON: {e}")


def generate_json(data):
    """Generate JSON string from Kaynat data structure."""
    python_data = _kaynat_to_python(data)
    return KaynatString(json.dumps(python_data))


def format_json(data, indent=2):
    """Generate formatted JSON string."""
    python_data = _kaynat_to_python(data)
    indent_val = int(indent.value if hasattr(indent, 'value') else indent)
    return KaynatString(json.dumps(python_data, indent=indent_val))


def _python_to_kaynat(obj):
    """Convert Python object to Kaynat type."""
    if obj is None:
        return KaynatNull()
    elif isinstance(obj, bool):
        return KaynatBoolean(obj)
    elif isinstance(obj, (int, float)):
        return KaynatNumber(obj)
    elif isinstance(obj, str):
        return KaynatString(obj)
    elif isinstance(obj, list):
        return KaynatList([_python_to_kaynat(item) for item in obj])
    elif isinstance(obj, dict):
        pairs = {k: _python_to_kaynat(v) for k, v in obj.items()}
        return KaynatMap(pairs)
    else:
        return KaynatString(str(obj))


def _kaynat_to_python(obj):
    """Convert Kaynat type to Python object."""
    if isinstance(obj, KaynatNull):
        return None
    elif isinstance(obj, KaynatBoolean):
        return obj.value
    elif isinstance(obj, KaynatNumber):
        return obj.value
    elif isinstance(obj, KaynatString):
        return obj.value
    elif isinstance(obj, KaynatList):
        return [_kaynat_to_python(item) for item in obj.value]
    elif isinstance(obj, KaynatMap):
        return {k: _kaynat_to_python(v) for k, v in obj.value.items()}
    else:
        return str(obj)
