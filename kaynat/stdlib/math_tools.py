"""
Kaynat Math Tools - Mathematical operations and constants.

Provides comprehensive math functionality for Kaynat programs.
"""

import math
from kaynat.interpreter.runtime_types import KaynatNumber, KaynatBoolean
from kaynat.errors.error_types import TypeError as KaynatTypeError, ValueError as KaynatValueError


# Mathematical constants
PI = math.pi
E = math.e
TAU = math.tau
INF = math.inf


def sqrt(value):
    """Calculate square root."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Square root requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    if num < 0:
        raise KaynatValueError("Cannot take square root of negative number")
    
    return KaynatNumber(math.sqrt(num))


def abs_value(value):
    """Calculate absolute value."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Absolute value requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    return KaynatNumber(abs(num))


def round_number(value, decimals=0):
    """Round number to specified decimal places."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Round requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    dec = decimals.value if isinstance(decimals, KaynatNumber) else decimals
    
    return KaynatNumber(round(num, int(dec)))


def ceiling(value):
    """Round up to nearest integer."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Ceiling requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    return KaynatNumber(math.ceil(num))


def floor(value):
    """Round down to nearest integer."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Floor requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    return KaynatNumber(math.floor(num))


def power(base, exponent):
    """Raise base to exponent power."""
    if not isinstance(base, (int, float, KaynatNumber)):
        raise KaynatTypeError("Power requires numbers")
    if not isinstance(exponent, (int, float, KaynatNumber)):
        raise KaynatTypeError("Power requires numbers")
    
    b = base.value if isinstance(base, KaynatNumber) else base
    e = exponent.value if isinstance(exponent, KaynatNumber) else exponent
    
    return KaynatNumber(math.pow(b, e))


def logarithm(value, base=math.e):
    """Calculate logarithm."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Logarithm requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    b = base.value if isinstance(base, KaynatNumber) else base
    
    if num <= 0:
        raise KaynatValueError("Logarithm requires positive number")
    
    if b == math.e:
        return KaynatNumber(math.log(num))
    else:
        return KaynatNumber(math.log(num, b))


def sin(angle):
    """Calculate sine (angle in degrees)."""
    if not isinstance(angle, (int, float, KaynatNumber)):
        raise KaynatTypeError("Sine requires a number")
    
    a = angle.value if isinstance(angle, KaynatNumber) else angle
    return KaynatNumber(math.sin(math.radians(a)))


def cos(angle):
    """Calculate cosine (angle in degrees)."""
    if not isinstance(angle, (int, float, KaynatNumber)):
        raise KaynatTypeError("Cosine requires a number")
    
    a = angle.value if isinstance(angle, KaynatNumber) else angle
    return KaynatNumber(math.cos(math.radians(a)))


def tan(angle):
    """Calculate tangent (angle in degrees)."""
    if not isinstance(angle, (int, float, KaynatNumber)):
        raise KaynatTypeError("Tangent requires a number")
    
    a = angle.value if isinstance(angle, KaynatNumber) else angle
    return KaynatNumber(math.tan(math.radians(a)))


def asin(value):
    """Calculate arcsine (returns degrees)."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Arcsine requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    if num < -1 or num > 1:
        raise KaynatValueError("Arcsine requires value between -1 and 1")
    
    return KaynatNumber(math.degrees(math.asin(num)))


def acos(value):
    """Calculate arccosine (returns degrees)."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Arccosine requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    if num < -1 or num > 1:
        raise KaynatValueError("Arccosine requires value between -1 and 1")
    
    return KaynatNumber(math.degrees(math.acos(num)))


def atan(value):
    """Calculate arctangent (returns degrees)."""
    if not isinstance(value, (int, float, KaynatNumber)):
        raise KaynatTypeError("Arctangent requires a number")
    
    num = value.value if isinstance(value, KaynatNumber) else value
    return KaynatNumber(math.degrees(math.atan(num)))


def factorial(n):
    """Calculate factorial."""
    if not isinstance(n, (int, KaynatNumber)):
        raise KaynatTypeError("Factorial requires an integer")
    
    num = n.value if isinstance(n, KaynatNumber) else n
    if num < 0:
        raise KaynatValueError("Factorial requires non-negative integer")
    
    return KaynatNumber(math.factorial(int(num)))


def gcd(a, b):
    """Calculate greatest common divisor."""
    if not isinstance(a, (int, KaynatNumber)) or not isinstance(b, (int, KaynatNumber)):
        raise KaynatTypeError("GCD requires integers")
    
    num_a = int(a.value if isinstance(a, KaynatNumber) else a)
    num_b = int(b.value if isinstance(b, KaynatNumber) else b)
    
    return KaynatNumber(math.gcd(num_a, num_b))


def lcm(a, b):
    """Calculate least common multiple."""
    if not isinstance(a, (int, KaynatNumber)) or not isinstance(b, (int, KaynatNumber)):
        raise KaynatTypeError("LCM requires integers")
    
    num_a = int(a.value if isinstance(a, KaynatNumber) else a)
    num_b = int(b.value if isinstance(b, KaynatNumber) else b)
    
    return KaynatNumber(math.lcm(num_a, num_b))


def is_prime(n):
    """Check if number is prime."""
    if not isinstance(n, (int, KaynatNumber)):
        raise KaynatTypeError("Prime check requires an integer")
    
    num = int(n.value if isinstance(n, KaynatNumber) else n)
    
    if num < 2:
        return KaynatBoolean(False)
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return KaynatBoolean(False)
    
    return KaynatBoolean(True)


def min_value(*args):
    """Find minimum value."""
    if not args:
        raise KaynatValueError("Min requires at least one argument")
    
    values = [arg.value if isinstance(arg, KaynatNumber) else arg for arg in args]
    return KaynatNumber(min(values))


def max_value(*args):
    """Find maximum value."""
    if not args:
        raise KaynatValueError("Max requires at least one argument")
    
    values = [arg.value if isinstance(arg, KaynatNumber) else arg for arg in args]
    return KaynatNumber(max(values))


def clamp(value, min_val, max_val):
    """Clamp value between min and max."""
    v = value.value if isinstance(value, KaynatNumber) else value
    min_v = min_val.value if isinstance(min_val, KaynatNumber) else min_val
    max_v = max_val.value if isinstance(max_val, KaynatNumber) else max_val
    
    return KaynatNumber(max(min_v, min(max_v, v)))
