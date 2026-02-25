"""Kaynat Network Tools - HTTP requests and networking."""

try:
    import urllib.request
    import urllib.error
    import urllib.parse
except ImportError:
    pass

from kaynat.interpreter.runtime_types import KaynatString, KaynatNumber, KaynatMap, KaynatBoolean
from kaynat.errors.error_types import RuntimeError as KaynatRuntimeError


def fetch_url(url, method='GET'):
    """Fetch URL with HTTP request."""
    url_str = url.value if hasattr(url, 'value') else str(url)
    method_str = method.value if hasattr(method, 'value') else str(method)
    
    try:
        req = urllib.request.Request(url_str, method=method_str.upper())
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            return KaynatString(content)
    except Exception as e:
        raise KaynatRuntimeError(f"Network error: {e}")


def is_url_reachable(url):
    """Check if URL is reachable."""
    url_str = url.value if hasattr(url, 'value') else str(url)
    
    try:
        req = urllib.request.Request(url_str, method='HEAD')
        with urllib.request.urlopen(req, timeout=5) as response:
            return KaynatBoolean(response.status == 200)
    except:
        return KaynatBoolean(False)
