"""
Kaynat Error Types - All custom exception classes.

Every error in Kaynat is clear, specific, and helpful.
"""


class KaynatError(Exception):
    """Base exception for all Kaynat errors."""
    
    def __init__(self, message: str, line: int = None, column: int = None):
        """
        Initialize a Kaynat error.
        
        Args:
            message: Human-readable error description
            line: Line number where error occurred
            column: Column number where error occurred
        """
        self.message = message
        self.line = line
        self.column = column
        
        if line is not None:
            if column is not None:
                full_message = f"{message} (line {line}, column {column})"
            else:
                full_message = f"{message} (line {line})"
        else:
            full_message = message
        
        super().__init__(full_message)


class LexerError(KaynatError):
    """Error during tokenization phase."""
    pass


class ParserError(KaynatError):
    """Error during parsing phase."""
    pass


class RuntimeError(KaynatError):
    """Error during program execution."""
    pass


class TypeError(RuntimeError):
    """Type mismatch or invalid type operation."""
    pass


class NameError(RuntimeError):
    """Undefined variable or function reference."""
    pass


class ValueError(RuntimeError):
    """Invalid value for an operation."""
    pass


class FileError(RuntimeError):
    """File system operation failed."""
    pass


class ImportError(RuntimeError):
    """Module import failed."""
    pass
