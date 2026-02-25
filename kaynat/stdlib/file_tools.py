"""
Kaynat File Tools - File system operations.

Provides file I/O functionality for Kaynat programs.
"""

import os
import shutil
from pathlib import Path
from kaynat.interpreter.runtime_types import KaynatString, KaynatList, KaynatBoolean
from kaynat.errors.error_types import FileError


def read_file(filepath):
    """Read entire file as string."""
    path = filepath.value if isinstance(filepath, KaynatString) else str(filepath)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return KaynatString(content)
    except FileNotFoundError:
        raise FileError(f"File not found: {path}")
    except Exception as e:
        raise FileError(f"Error reading file: {e}")


def read_lines(filepath):
    """Read file as list of lines."""
    path = filepath.value if isinstance(filepath, KaynatString) else str(filepath)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return KaynatList([KaynatString(line.rstrip('\n')) for line in lines])
    except FileNotFoundError:
        raise FileError(f"File not found: {path}")
    except Exception as e:
        raise FileError(f"Error reading file: {e}")


def write_file(filepath, content):
    """Write content to file (overwrites existing)."""
    path = filepath.value if isinstance(filepath, KaynatString) else str(filepath)
    text = content.value if isinstance(content, KaynatString) else str(content)
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return KaynatBoolean(True)
    except Exception as e:
        raise FileError(f"Error writing file: {e}")


def append_file(filepath, content):
    """Append content to file."""
    path = filepath.value if isinstance(filepath, KaynatString) else str(filepath)
    text = content.value if isinstance(content, KaynatString) else str(content)
    
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(text)
        return KaynatBoolean(True)
    except Exception as e:
        raise FileError(f"Error appending to file: {e}")


def file_exists(filepath):
    """Check if file exists."""
    path = filepath.value if isinstance(filepath, KaynatString) else str(filepath)
    return KaynatBoolean(os.path.isfile(path))


def delete_file(filepath):
    """Delete a file."""
    path = filepath.value if isinstance(filepath, KaynatString) else str(filepath)
    
    try:
        os.remove(path)
        return KaynatBoolean(True)
    except FileNotFoundError:
        raise FileError(f"File not found: {path}")
    except Exception as e:
        raise FileError(f"Error deleting file: {e}")


def copy_file(source, destination):
    """Copy file from source to destination."""
    src = source.value if isinstance(source, KaynatString) else str(source)
    dst = destination.value if isinstance(destination, KaynatString) else str(destination)
    
    try:
        shutil.copy2(src, dst)
        return KaynatBoolean(True)
    except Exception as e:
        raise FileError(f"Error copying file: {e}")


def move_file(source, destination):
    """Move file from source to destination."""
    src = source.value if isinstance(source, KaynatString) else str(source)
    dst = destination.value if isinstance(destination, KaynatString) else str(destination)
    
    try:
        shutil.move(src, dst)
        return KaynatBoolean(True)
    except Exception as e:
        raise FileError(f"Error moving file: {e}")


def create_directory(dirpath):
    """Create a directory."""
    path = dirpath.value if isinstance(dirpath, KaynatString) else str(dirpath)
    
    try:
        os.makedirs(path, exist_ok=True)
        return KaynatBoolean(True)
    except Exception as e:
        raise FileError(f"Error creating directory: {e}")


def delete_directory(dirpath):
    """Delete a directory."""
    path = dirpath.value if isinstance(dirpath, KaynatString) else str(dirpath)
    
    try:
        shutil.rmtree(path)
        return KaynatBoolean(True)
    except Exception as e:
        raise FileError(f"Error deleting directory: {e}")


def directory_exists(dirpath):
    """Check if directory exists."""
    path = dirpath.value if isinstance(dirpath, KaynatString) else str(dirpath)
    return KaynatBoolean(os.path.isdir(path))


def list_directory(dirpath):
    """List files in directory."""
    path = dirpath.value if isinstance(dirpath, KaynatString) else str(dirpath)
    
    try:
        files = os.listdir(path)
        return KaynatList([KaynatString(f) for f in files])
    except Exception as e:
        raise FileError(f"Error listing directory: {e}")
