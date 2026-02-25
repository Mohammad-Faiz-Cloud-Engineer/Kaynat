#!/usr/bin/env python3
"""
Kaynat Programming Language - Main Entry Point

A fully production-grade, Turing-complete programming language with English syntax.
Named after someone worth remembering. Built into something worth using.

Author: Mohammad Faiz
"""

import sys
import argparse
from pathlib import Path
from kaynat.repl import start_repl
from kaynat.interpreter.interpreter import Interpreter
from kaynat.errors.error_types import KaynatError


def run_file(filepath: str) -> int:
    """
    Execute a Kaynat source file.
    
    Args:
        filepath: Path to the .kaynat source file
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        path = Path(filepath)
        if not path.exists():
            print(f"Error: File '{filepath}' not found.")
            return 1
            
        if not path.suffix == '.kaynat':
            print(f"Warning: File '{filepath}' does not have .kaynat extension.")
            
        source_code = path.read_text(encoding='utf-8')
        interpreter = Interpreter()
        interpreter.execute(source_code)
        return 0
        
    except KaynatError as e:
        print(f"Kaynat Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return 1


def main() -> int:
    """Main entry point for the Kaynat interpreter."""
    parser = argparse.ArgumentParser(
        description='Kaynat Programming Language - Code that reads like poetry',
        epilog='Named after someone special. Built with purpose.'
    )
    parser.add_argument(
        'file',
        nargs='?',
        help='Path to .kaynat source file to execute'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='Kaynat 1.0.0'
    )
    
    args = parser.parse_args()
    
    if args.file:
        return run_file(args.file)
    else:
        return start_repl()


if __name__ == '__main__':
    sys.exit(main())
