"""
Token types and Token class for Kaynat lexer.

Defines all token types used in the Kaynat language.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any


class TokenType(Enum):
    """All token types in the Kaynat language."""
    
    # Literals
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    NULL = auto()
    
    # Identifiers
    IDENTIFIER = auto()
    
    # Keywords - Variables
    SET = auto()
    LET = auto()
    DEFINE = auto()
    ALWAYS = auto()
    FIXED = auto()
    CHANGE = auto()
    FORGET = auto()
    
    # Keywords - Data Types
    TO = auto()
    AS = auto()
    A = auto()
    AN = auto()
    THE = auto()
    LIST = auto()
    MAP = auto()
    BIG = auto()
    NOTHING = auto()
    NEGATIVE = auto()
    CONTAINING = auto()
    
    # Keywords - Arithmetic
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    FROM = auto()
    BY = auto()
    FIND = auto()
    INTEGER = auto()
    DIVISION = auto()
    REMAINDER = auto()
    DIVIDED = auto()
    RAISE = auto()
    POWER = auto()
    SQUARE = auto()
    ROOT = auto()
    ABSOLUTE = auto()
    VALUE = auto()
    ROUND = auto()
    DECIMAL = auto()
    PLACES = auto()
    CEILING = auto()
    FLOOR = auto()
    LOGARITHM = auto()
    BASE = auto()
    SINE = auto()
    COSINE = auto()
    TANGENT = auto()
    PRODUCT = auto()
    
    # Keywords - String Operations
    JOIN = auto()
    AND = auto()
    STORE = auto()
    LENGTH = auto()
    OF = auto()
    CONVERT = auto()
    UPPERCASE = auto()
    LOWERCASE = auto()
    TRIM = auto()
    WHITESPACE = auto()
    CHECK = auto()
    IF = auto()
    STARTS = auto()
    WITH = auto()
    ENDS = auto()
    REPLACE = auto()
    IN = auto()
    SPLIT = auto()
    POSITION = auto()
    TAKE = auto()
    CHARACTERS = auto()
    REVERSE = auto()
    REPEAT = auto()
    TIMES = auto()
    CONTAINS = auto()
    
    # Keywords - Comparison
    IS = auto()
    GREATER = auto()
    THAN = auto()
    EQUAL = auto()
    NOT = auto()
    LESS = auto()
    OR = auto()
    EMPTY = auto()
    EXISTS = auto()
    
    # Keywords - Control Flow
    THEN = auto()
    OTHERWISE = auto()
    END = auto()
    WHEN = auto()
    DO = auto()
    DEFAULT = auto()
    WHILE = auto()
    UNTIL = auto()
    FOR = auto()
    EACH = auto()
    LOOP = auto()
    STEPPING = auto()
    STOP = auto()
    SKIP = auto()
    
    # Keywords - Functions
    FUNCTION = auto()
    CALLED = auto()
    THAT = auto()
    TAKES = auto()
    GIVE = auto()
    BACK = auto()
    CALL = auto()
    INLINE = auto()
    GIVES = auto()
    RESULT = auto()
    CALLING = auto()
    MINUS = auto()
    MULTIPLIED = auto()
    PLUS = auto()
    
    # Keywords - Lists
    CREATE = auto()
    REMOVE = auto()
    ITEM = auto()
    AT = auto()
    INSERT = auto()
    GET = auto()
    FRONT = auto()
    SORT = auto()
    ASCENDING = auto()
    DESCENDING = auto()
    FILTER = auto()
    WHERE = auto()
    USING = auto()
    REDUCE = auto()
    COPY = auto()
    FLATTEN = auto()
    NESTED = auto()
    
    # Keywords - Dictionaries
    KEY = auto()
    ALL = auto()
    KEYS = auto()
    VALUES = auto()
    
    # Keywords - I/O
    ASK = auto()
    USER = auto()
    READ = auto()
    SAY = auto()
    PRINT = auto()
    SHOW = auto()
    
    # Keywords - File System
    FILE = auto()
    LINE = auto()
    WRITE = auto()
    APPEND = auto()
    DELETE = auto()
    
    # Keywords - Error Handling
    ATTEMPT = auto()
    IT = auto()
    FAILS = auto()
    MESSAGE = auto()
    AFTER = auto()
    ERROR = auto()
    SAYING = auto()
    TYPE = auto()
    
    # Keywords - Type System
    TEXT = auto()
    TURN = auto()
    INTO = auto()
    FLAG = auto()
    
    # Keywords - Scope
    GLOBAL = auto()
    BRING = auto()
    USE = auto()
    MODULE = auto()
    NAMED = auto()
    EXPORT = auto()
    
    # Keywords - Comments
    NOTE = auto()
    BEGIN = auto()
    WRITTEN = auto()
    CARE = auto()
    CLARITY = auto()
    
    # Keywords - Program
    PROGRAM = auto()
    
    # Keywords - OOP
    BLUEPRINT = auto()
    HAS = auto()
    PRIVATE = auto()
    INITIALIZE = auto()
    MY = auto()
    PARENT = auto()
    ON = auto()
    EXTENDS = auto()
    THIS = auto()
    MUST = auto()
    BE = auto()
    IMPLEMENTED = auto()
    ABSTRACT = auto()
    CONTRACT = auto()
    REQUIRES = auto()
    FOLLOWS = auto()
    SHARED = auto()
    STARTING = auto()
    NEW = auto()
    OTHER = auto()
    
    # Keywords - Data Structures
    STACK = auto()
    QUEUE = auto()
    LINKED = auto()
    PUSH = auto()
    ONTO = auto()
    POP = auto()
    PEEK = auto()
    SIZE = auto()
    ENQUEUE = auto()
    DEQUEUE = auto()
    NODE = auto()
    BINARY = auto()
    SEARCH = auto()
    TREE = auto()
    TRAVERSE = auto()
    INORDER = auto()
    PREORDER = auto()
    POSTORDER = auto()
    HEIGHT = auto()
    MINIMUM = auto()
    MAXIMUM = auto()
    GRAPH = auto()
    EDGE = auto()
    WEIGHT = auto()
    SHORTEST = auto()
    PATH = auto()
    DIJKSTRA = auto()
    BREADTH = auto()
    FIRST = auto()
    DEPTH = auto()
    CYCLE = auto()
    CONNECTED = auto()
    COMPONENTS = auto()
    MIN = auto()
    HEAP = auto()
    PRIORITY = auto()
    EXTRACT = auto()
    MAX = auto()
    HASH = auto()
    PUT = auto()
    LOAD = auto()
    FACTOR = auto()
    TRIE = auto()
    WORD = auto()
    WORDS = auto()
    BUBBLE = auto()
    MERGE = auto()
    QUICK = auto()
    INSERTION = auto()
    SELECTION = auto()
    RADIX = auto()
    COUNTING = auto()
    LINEAR = auto()
    PATTERN = auto()
    KNUTH = auto()
    MORRIS = auto()
    PRATT = auto()
    POSITIONS = auto()
    BELLMAN = auto()
    FORD = auto()
    SPANNING = auto()
    KRUSKAL = auto()
    PRIM = auto()
    TOPOLOGICAL = auto()
    ORDER = auto()
    STRONGLY = auto()
    KOSARAJU = auto()
    
    # Keywords - GUI
    WINDOW = auto()
    TITLE = auto()
    WIDTH = auto()
    BACKGROUND = auto()
    LABEL = auto()
    FONT = auto()
    COLOR = auto()
    PLACE = auto()
    ROW = auto()
    COLUMN = auto()
    BUTTON = auto()
    ACTION = auto()
    INPUT = auto()
    PLACEHOLDER = auto()
    AREA = auto()
    CHECKBOX = auto()
    DROPDOWN = auto()
    OPTIONS = auto()
    RADIO = auto()
    GROUP = auto()
    SLIDER = auto()
    PROGRESS = auto()
    BAR = auto()
    IMAGE = auto()
    SOURCE = auto()
    GRID = auto()
    LAYOUT = auto()
    FLOW = auto()
    PADDING = auto()
    HORIZONTAL = auto()
    VERTICAL = auto()
    STICKY = auto()
    ALIGNMENT = auto()
    LEFT = auto()
    SPAN = auto()
    ACROSS = auto()
    COLUMNS = auto()
    CLICKED = auto()
    CHANGES = auto()
    CLOSED = auto()
    CONFIRM = auto()
    CHOOSE = auto()
    FOLDER = auto()
    SAVE = auto()
    MENU = auto()
    SEPARATOR = auto()
    ATTACH = auto()
    CANVAS = auto()
    BOARD = auto()
    DRAW = auto()
    RECTANGLE = auto()
    FILL = auto()
    CIRCLE = auto()
    RADIUS = auto()
    CLEAR = auto()
    OPEN = auto()
    CLOSE = auto()
    MINIMIZE = auto()
    MAXIMIZE = auto()
    APPLY = auto()
    THEME = auto()
    DARK = auto()
    LIGHT = auto()
    ACCENT = auto()
    
    # Keywords - Concurrency
    RUN = auto()
    WAIT = auto()
    FINISH = auto()
    FINISHES = auto()
    TIMER = auto()
    CANCEL = auto()
    
    # Punctuation
    PERIOD = auto()
    COMMA = auto()
    
    # Special
    EOF = auto()


@dataclass
class Token:
    """
    Represents a single token in the source code.
    
    Attributes:
        type: The type of token
        value: The literal value of the token
        line: Line number where token appears
        column: Column number where token starts
    """
    type: TokenType
    value: Any
    line: int
    column: int
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Token({self.type.name}, {self.value!r}, {self.line}:{self.column})"
