"""
Kaynat Lexer - Tokenizes English source code into tokens.

Converts natural English text into a stream of tokens for parsing.
"""

from typing import List, Optional
from kaynat.lexer.token_types import Token, TokenType
from kaynat.errors.error_types import LexerError


class Lexer:
    """
    Tokenizes Kaynat source code into a stream of tokens.
    
    The lexer reads English text and converts it into tokens that
    the parser can understand. It handles multi-word keywords and
    maintains line and column information for error reporting.
    """
    
    # Keyword mapping - maps English phrases to token types
    KEYWORDS = {
        'set': TokenType.SET,
        'let': TokenType.LET,
        'define': TokenType.DEFINE,
        'always': TokenType.ALWAYS,
        'fixed': TokenType.FIXED,
        'change': TokenType.CHANGE,
        'forget': TokenType.FORGET,
        'to': TokenType.TO,
        'as': TokenType.AS,
        'a': TokenType.A,
        'an': TokenType.AN,
        'the': TokenType.THE,
        'list': TokenType.LIST,
        'map': TokenType.MAP,
        'big': TokenType.BIG,
        'nothing': TokenType.NOTHING,
        'negative': TokenType.NEGATIVE,
        'containing': TokenType.CONTAINING,
        'add': TokenType.ADD,
        'subtract': TokenType.SUBTRACT,
        'multiply': TokenType.MULTIPLY,
        'divide': TokenType.DIVIDE,
        'from': TokenType.FROM,
        'by': TokenType.BY,
        'find': TokenType.FIND,
        'integer': TokenType.INTEGER,
        'division': TokenType.DIVISION,
        'remainder': TokenType.REMAINDER,
        'divided': TokenType.DIVIDED,
        'raise': TokenType.RAISE,
        'power': TokenType.POWER,
        'square': TokenType.SQUARE,
        'root': TokenType.ROOT,
        'absolute': TokenType.ABSOLUTE,
        'value': TokenType.VALUE,
        'round': TokenType.ROUND,
        'decimal': TokenType.DECIMAL,
        'places': TokenType.PLACES,
        'ceiling': TokenType.CEILING,
        'floor': TokenType.FLOOR,
        'logarithm': TokenType.LOGARITHM,
        'base': TokenType.BASE,
        'sine': TokenType.SINE,
        'cosine': TokenType.COSINE,
        'tangent': TokenType.TANGENT,
        'product': TokenType.PRODUCT,
        'join': TokenType.JOIN,
        'and': TokenType.AND,
        'store': TokenType.STORE,
        'length': TokenType.LENGTH,
        'of': TokenType.OF,
        'convert': TokenType.CONVERT,
        'uppercase': TokenType.UPPERCASE,
        'lowercase': TokenType.LOWERCASE,
        'trim': TokenType.WHITESPACE,
        'whitespace': TokenType.WHITESPACE,
        'check': TokenType.CHECK,
        'if': TokenType.IF,
        'starts': TokenType.STARTS,
        'with': TokenType.WITH,
        'ends': TokenType.ENDS,
        'replace': TokenType.REPLACE,
        'in': TokenType.IN,
        'split': TokenType.SPLIT,
        'position': TokenType.POSITION,
        'take': TokenType.TAKE,
        'characters': TokenType.CHARACTERS,
        'reverse': TokenType.REVERSE,
        'repeat': TokenType.REPEAT,
        'times': TokenType.TIMES,
        'contains': TokenType.CONTAINS,
        'is': TokenType.IS,
        'greater': TokenType.GREATER,
        'than': TokenType.THAN,
        'equal': TokenType.EQUAL,
        'not': TokenType.NOT,
        'less': TokenType.LESS,
        'or': TokenType.OR,
        'empty': TokenType.EMPTY,
        'number': TokenType.NUMBER,
        'exists': TokenType.EXISTS,
        'then': TokenType.THEN,
        'otherwise': TokenType.OTHERWISE,
        'end': TokenType.END,
        'when': TokenType.WHEN,
        'do': TokenType.DO,
        'default': TokenType.DEFAULT,
        'repeat': TokenType.REPEAT,
        'while': TokenType.WHILE,
        'until': TokenType.UNTIL,
        'for': TokenType.FOR,
        'each': TokenType.EACH,
        'loop': TokenType.LOOP,
        'stepping': TokenType.STEPPING,
        'stop': TokenType.STOP,
        'skip': TokenType.SKIP,
        'function': TokenType.FUNCTION,
        'called': TokenType.CALLED,
        'that': TokenType.THAT,
        'takes': TokenType.TAKES,
        'give': TokenType.GIVE,
        'back': TokenType.BACK,
        'call': TokenType.CALL,
        'inline': TokenType.INLINE,
        'gives': TokenType.GIVES,
        'calling': TokenType.CALLING,
        'minus': TokenType.MINUS,
        'multiplied': TokenType.MULTIPLIED,
        'plus': TokenType.PLUS,
        'create': TokenType.CREATE,
        'remove': TokenType.REMOVE,
        'item': TokenType.ITEM,
        'at': TokenType.AT,
        'insert': TokenType.INSERT,
        'get': TokenType.GET,
        'front': TokenType.FRONT,
        'sort': TokenType.SORT,
        'ascending': TokenType.ASCENDING,
        'descending': TokenType.DESCENDING,
        'filter': TokenType.FILTER,
        'where': TokenType.WHERE,
        'using': TokenType.USING,
        'reduce': TokenType.REDUCE,
        'copy': TokenType.COPY,
        'flatten': TokenType.FLATTEN,
        'nested': TokenType.NESTED,
        'key': TokenType.KEY,
        'all': TokenType.ALL,
        'keys': TokenType.KEYS,
        'values': TokenType.VALUES,
        'ask': TokenType.ASK,
        'user': TokenType.USER,
        'read': TokenType.READ,
        'say': TokenType.SAY,
        'print': TokenType.PRINT,
        'show': TokenType.SHOW,
        'file': TokenType.FILE,
        'line': TokenType.LINE,
        'write': TokenType.WRITE,
        'append': TokenType.APPEND,
        'delete': TokenType.DELETE,
        'attempt': TokenType.ATTEMPT,
        'it': TokenType.IT,
        'fails': TokenType.FAILS,
        'message': TokenType.MESSAGE,
        'after': TokenType.AFTER,
        'error': TokenType.ERROR,
        'saying': TokenType.SAYING,
        'type': TokenType.TYPE,
        'text': TokenType.TEXT,
        'turn': TokenType.TURN,
        'into': TokenType.INTO,
        'string': TokenType.STRING,
        'flag': TokenType.FLAG,
        'global': TokenType.GLOBAL,
        'bring': TokenType.BRING,
        'use': TokenType.USE,
        'module': TokenType.MODULE,
        'named': TokenType.NAMED,
        'export': TokenType.EXPORT,
        'note': TokenType.NOTE,
        'begin': TokenType.BEGIN,
        'written': TokenType.WRITTEN,
        'care': TokenType.CARE,
        'clarity': TokenType.CLARITY,
        'program': TokenType.PROGRAM,
        'blueprint': TokenType.BLUEPRINT,
        'has': TokenType.HAS,
        'private': TokenType.PRIVATE,
        'initialize': TokenType.INITIALIZE,
        'my': TokenType.MY,
        'parent': TokenType.PARENT,
        'on': TokenType.ON,
        'extends': TokenType.EXTENDS,
        'this': TokenType.THIS,
        'must': TokenType.MUST,
        'be': TokenType.BE,
        'implemented': TokenType.IMPLEMENTED,
        'abstract': TokenType.ABSTRACT,
        'contract': TokenType.CONTRACT,
        'requires': TokenType.REQUIRES,
        'follows': TokenType.FOLLOWS,
        'shared': TokenType.SHARED,
        'starting': TokenType.STARTING,
        'new': TokenType.NEW,
        'other': TokenType.OTHER,
        'true': TokenType.BOOLEAN,
        'false': TokenType.BOOLEAN,
        'yes': TokenType.BOOLEAN,
        'no': TokenType.BOOLEAN,
        'stack': TokenType.STACK,
        'queue': TokenType.QUEUE,
        'linked': TokenType.LINKED,
        'push': TokenType.PUSH,
        'onto': TokenType.ONTO,
        'pop': TokenType.POP,
        'peek': TokenType.PEEK,
        'size': TokenType.SIZE,
        'enqueue': TokenType.ENQUEUE,
        'dequeue': TokenType.DEQUEUE,
        'node': TokenType.NODE,
        'binary': TokenType.BINARY,
        'search': TokenType.SEARCH,
        'tree': TokenType.TREE,
        'traverse': TokenType.TRAVERSE,
        'inorder': TokenType.INORDER,
        'preorder': TokenType.PREORDER,
        'postorder': TokenType.POSTORDER,
        'height': TokenType.HEIGHT,
        'minimum': TokenType.MINIMUM,
        'maximum': TokenType.MAXIMUM,
        'graph': TokenType.GRAPH,
        'edge': TokenType.EDGE,
        'weight': TokenType.WEIGHT,
        'shortest': TokenType.SHORTEST,
        'path': TokenType.PATH,
        'dijkstra': TokenType.DIJKSTRA,
        'breadth': TokenType.BREADTH,
        'first': TokenType.FIRST,
        'depth': TokenType.DEPTH,
        'cycle': TokenType.CYCLE,
        'connected': TokenType.CONNECTED,
        'components': TokenType.COMPONENTS,
        'min': TokenType.MIN,
        'heap': TokenType.HEAP,
        'priority': TokenType.PRIORITY,
        'extract': TokenType.EXTRACT,
        'max': TokenType.MAX,
        'hash': TokenType.HASH,
        'put': TokenType.PUT,
        'load': TokenType.LOAD,
        'factor': TokenType.FACTOR,
        'trie': TokenType.TRIE,
        'word': TokenType.WORD,
        'words': TokenType.WORDS,
        'bubble': TokenType.BUBBLE,
        'merge': TokenType.MERGE,
        'quick': TokenType.QUICK,
        'insertion': TokenType.INSERTION,
        'selection': TokenType.SELECTION,
        'radix': TokenType.RADIX,
        'counting': TokenType.COUNTING,
        'linear': TokenType.LINEAR,
        'pattern': TokenType.PATTERN,
        'knuth': TokenType.KNUTH,
        'morris': TokenType.MORRIS,
        'pratt': TokenType.PRATT,
        'positions': TokenType.POSITIONS,
        'bellman': TokenType.BELLMAN,
        'ford': TokenType.FORD,
        'spanning': TokenType.SPANNING,
        'kruskal': TokenType.KRUSKAL,
        'prim': TokenType.PRIM,
        'topological': TokenType.TOPOLOGICAL,
        'order': TokenType.ORDER,
        'strongly': TokenType.STRONGLY,
        'kosaraju': TokenType.KOSARAJU,
        'window': TokenType.WINDOW,
        'title': TokenType.TITLE,
        'width': TokenType.WIDTH,
        'height': TokenType.HEIGHT,
        'background': TokenType.BACKGROUND,
        'label': TokenType.LABEL,
        'font': TokenType.FONT,
        'color': TokenType.COLOR,
        'place': TokenType.PLACE,
        'row': TokenType.ROW,
        'column': TokenType.COLUMN,
        'button': TokenType.BUTTON,
        'action': TokenType.ACTION,
        'input': TokenType.INPUT,
        'placeholder': TokenType.PLACEHOLDER,
        'area': TokenType.AREA,
        'checkbox': TokenType.CHECKBOX,
        'dropdown': TokenType.DROPDOWN,
        'options': TokenType.OPTIONS,
        'radio': TokenType.RADIO,
        'group': TokenType.GROUP,
        'slider': TokenType.SLIDER,
        'progress': TokenType.PROGRESS,
        'bar': TokenType.BAR,
        'image': TokenType.IMAGE,
        'source': TokenType.SOURCE,
        'grid': TokenType.GRID,
        'layout': TokenType.LAYOUT,
        'flow': TokenType.FLOW,
        'padding': TokenType.PADDING,
        'horizontal': TokenType.HORIZONTAL,
        'vertical': TokenType.VERTICAL,
        'sticky': TokenType.STICKY,
        'alignment': TokenType.ALIGNMENT,
        'left': TokenType.LEFT,
        'span': TokenType.SPAN,
        'across': TokenType.ACROSS,
        'columns': TokenType.COLUMNS,
        'clicked': TokenType.CLICKED,
        'changes': TokenType.CHANGES,
        'closed': TokenType.CLOSED,
        'confirm': TokenType.CONFIRM,
        'choose': TokenType.CHOOSE,
        'folder': TokenType.FOLDER,
        'save': TokenType.SAVE,
        'menu': TokenType.MENU,
        'separator': TokenType.SEPARATOR,
        'attach': TokenType.ATTACH,
        'canvas': TokenType.CANVAS,
        'board': TokenType.BOARD,
        'draw': TokenType.DRAW,
        'rectangle': TokenType.RECTANGLE,
        'fill': TokenType.FILL,
        'circle': TokenType.CIRCLE,
        'radius': TokenType.RADIUS,
        'clear': TokenType.CLEAR,
        'open': TokenType.OPEN,
        'close': TokenType.CLOSE,
        'minimize': TokenType.MINIMIZE,
        'maximize': TokenType.MAXIMIZE,
        'apply': TokenType.APPLY,
        'theme': TokenType.THEME,
        'dark': TokenType.DARK,
        'light': TokenType.LIGHT,
        'accent': TokenType.ACCENT,
        'run': TokenType.RUN,
        'wait': TokenType.WAIT,
        'finish': TokenType.FINISH,
        'finishes': TokenType.FINISHES,
        'timer': TokenType.TIMER,
        'cancel': TokenType.CANCEL,
    }
    
    def __init__(self, source: str):
        """
        Initialize the lexer with source code.
        
        Args:
            source: The Kaynat source code to tokenize
        """
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def current_char(self) -> Optional[str]:
        """Get the current character without advancing."""
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        """Look ahead at a character without advancing."""
        pos = self.position + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self) -> Optional[str]:
        """Move to the next character and return it."""
        if self.position >= len(self.source):
            return None
        
        char = self.source[self.position]
        self.position += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        return char
    
    def skip_whitespace(self):
        """Skip whitespace characters except newlines."""
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_newlines(self):
        """Skip newline characters."""
        while self.current_char() and self.current_char() == '\n':
            self.advance()
    
    def read_number(self) -> Token:
        """Read a numeric literal."""
        start_line = self.line
        start_column = self.column
        num_str = ''
        has_decimal = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_decimal:
                    break
                if self.peek_char() and not self.peek_char().isdigit():
                    break
                has_decimal = True
            num_str += self.current_char()
            self.advance()
        
        if has_decimal:
            value = float(num_str)
        else:
            value = int(num_str)
        
        return Token(TokenType.NUMBER, value, start_line, start_column)
    
    def read_word(self) -> str:
        """Read a word (letters only)."""
        word = ''
        while self.current_char() and self.current_char().isalpha():
            word += self.current_char()
            self.advance()
        return word.lower()
    
    def tokenize(self) -> List[Token]:
        """
        Tokenize the entire source code.
        
        Returns:
            List of tokens
        """
        while self.position < len(self.source):
            self.skip_whitespace()
            
            char = self.current_char()
            
            if char is None:
                break
            
            # Skip newlines
            if char == '\n':
                self.advance()
                continue
            
            # Period - statement terminator
            if char == '.':
                token = Token(TokenType.PERIOD, '.', self.line, self.column)
                self.tokens.append(token)
                self.advance()
                continue
            
            # Comma - separator
            if char == ',':
                token = Token(TokenType.COMMA, ',', self.line, self.column)
                self.tokens.append(token)
                self.advance()
                continue
            
            # Numbers
            if char.isdigit():
                self.tokens.append(self.read_number())
                continue
            
            # Words (keywords or identifiers)
            if char.isalpha():
                start_line = self.line
                start_column = self.column
                word = self.read_word()
                
                # Check if it's a keyword
                if word in self.KEYWORDS:
                    token_type = self.KEYWORDS[word]
                    if token_type == TokenType.BOOLEAN:
                        value = word in ('true', 'yes')
                    else:
                        value = word
                    self.tokens.append(Token(token_type, value, start_line, start_column))
                else:
                    # It's an identifier
                    self.tokens.append(Token(TokenType.IDENTIFIER, word, start_line, start_column))
                continue
            
            # Unknown character
            raise LexerError(
                f"Unexpected character '{char}' at line {self.line}, column {self.column}"
            )
        
        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens
