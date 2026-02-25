"""
Kaynat Runtime Types - Value representations at runtime.

Every value in Kaynat has a type and behavior.
"""

from typing import Any, List, Dict, Callable
from dataclasses import dataclass


@dataclass
class KaynatValue:
    """Base class for all runtime values."""
    value: Any
    
    def to_python(self) -> Any:
        """Convert to Python value."""
        return self.value
    
    def to_string(self) -> str:
        """Convert to string representation."""
        return str(self.value)
    
    def is_truthy(self) -> bool:
        """Check if value is truthy."""
        if self.value is None:
            return False
        if isinstance(self.value, bool):
            return self.value
        if isinstance(self.value, (int, float)):
            return self.value != 0
        if isinstance(self.value, str):
            return len(self.value) > 0
        if isinstance(self.value, list):
            return len(self.value) > 0
        return True


@dataclass
class KaynatNumber(KaynatValue):
    """Numeric value (int or float)."""
    
    def to_string(self) -> str:
        if isinstance(self.value, float) and self.value.is_integer():
            return str(int(self.value))
        return str(self.value)


@dataclass
class KaynatString(KaynatValue):
    """String value."""
    pass


@dataclass
class KaynatBoolean(KaynatValue):
    """Boolean value."""
    
    def to_string(self) -> str:
        return 'true' if self.value else 'false'


@dataclass
class KaynatNull(KaynatValue):
    """Null/nothing value."""
    
    def __init__(self):
        super().__init__(None)
    
    def to_string(self) -> str:
        return 'nothing'


@dataclass
class KaynatList(KaynatValue):
    """List value."""
    
    def __init__(self, elements: List[KaynatValue] = None):
        super().__init__(elements if elements is not None else [])
    
    def to_string(self) -> str:
        elements_str = ', '.join(elem.to_string() for elem in self.value)
        return f'[{elements_str}]'


@dataclass
class KaynatMap(KaynatValue):
    """Dictionary/map value."""
    
    def __init__(self, pairs: Dict[str, KaynatValue] = None):
        super().__init__(pairs if pairs is not None else {})
    
    def to_string(self) -> str:
        pairs_str = ', '.join(f'{k}: {v.to_string()}' for k, v in self.value.items())
        return f'{{{pairs_str}}}'


@dataclass
class KaynatFunction(KaynatValue):
    """Function value."""
    
    def __init__(self, name: str, parameters: List[str], body: List, env):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.env = env
        super().__init__(self)
    
    def to_string(self) -> str:
        return f'<function {self.name}>'


class ReturnValue(Exception):
    """Exception used to implement return statements."""
    
    def __init__(self, value: KaynatValue):
        self.value = value
        super().__init__()


class BreakException(Exception):
    """Exception used to implement break statements."""
    pass


class ContinueException(Exception):
    """Exception used to implement continue statements."""
    pass
