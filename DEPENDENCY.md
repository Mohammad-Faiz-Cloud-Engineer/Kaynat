# Kaynat Programming Language - Dependencies

This document provides a comprehensive overview of all dependencies required to run the Kaynat programming language and its features.

---

## Part 1: Installation Requirements

To run Kaynat programming language fully, you need to install the following on your machine:

### 1. Core Requirements

#### Python 3.8 or Higher
- **Required Version:** Python 3.8, 3.9, 3.10, or 3.11+
- **Purpose:** Kaynat is implemented in Python and requires Python runtime
- **Installation:**
  ```bash
  # Check your Python version
  python3 --version
  
  # Install Python (if needed)
  # Ubuntu/Debian
  sudo apt-get install python3.8
  
  # macOS (using Homebrew)
  brew install python@3.8
  
  # Windows
  # Download from https://www.python.org/downloads/
  ```

### 2. Python Standard Library Modules

The following Python standard library modules are used (these come pre-installed with Python):

- **sys** - System-specific parameters and functions
- **argparse** - Command-line argument parsing
- **pathlib** - Object-oriented filesystem paths
- **math** - Mathematical functions
- **hashlib** - Secure hash and message digest algorithms
- **base64** - Base64 encoding/decoding
- **secrets** - Cryptographically strong random numbers
- **datetime** - Date and time manipulation
- **timedelta** - Time duration calculations
- **os** - Operating system interface
- **shutil** - High-level file operations
- **json** - JSON encoding and decoding
- **urllib.request** - URL handling
- **urllib.error** - URL error handling
- **urllib.parse** - URL parsing
- **re** - Regular expression operations
- **random** - Random number generation
- **string** - String operations
- **collections.deque** - Double-ended queue

### 3. Optional Dependencies (for GUI Features)

#### Tkinter (Python's standard GUI library)
- **Purpose:** Required for GUI applications and graphical interfaces
- **Installation:**
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-tk
  
  # macOS (usually pre-installed with Python)
  # If not: brew install python-tk
  
  # Windows (usually pre-installed with Python)
  # If not, reinstall Python with tkinter option checked
  ```

### 4. Installation via setup.py

```bash
# Clone the repository
git clone https://github.com/Mohammad-Faiz-Cloud-Engineer/Kaynat.git
cd Kaynat

# Install Kaynat (optional, for system-wide access)
python3 setup.py install

# Or install in development mode
python3 setup.py develop
```

### 5. Running Without Installation

```bash
# Run a Kaynat program directly
python3 -m kaynat.main examples/01_hello_world.kaynat

# Start the REPL
python3 -m kaynat.repl
```

---

## Part 2: Feature-Specific Dependencies

This section maps each dependency to the specific features it enables in Kaynat.

### Core Language Features (No External Dependencies)

These features work with Python standard library only:

#### 1. **Lexer & Parser** (`kaynat/lexer/`, `kaynat/parser/`)
- **Dependencies:** None (pure Python)
- **Features:**
  - Tokenization of English-like syntax
  - Abstract Syntax Tree (AST) generation
  - Syntax parsing and validation

#### 2. **Interpreter** (`kaynat/interpreter/`)
- **Dependencies:** None (pure Python)
- **Features:**
  - Program execution
  - Variable management
  - Function calls
  - Control flow (if/else, loops)
  - Expression evaluation

#### 3. **Error Handling** (`kaynat/errors/`)
- **Dependencies:** None (pure Python)
- **Features:**
  - Custom error types
  - Error messages
  - Stack traces

---

### Standard Library Features

#### 1. **Math Tools** (`kaynat/stdlib/math_tools.py`)
- **Dependencies:**
  - `math` (Python standard library)
- **Features Enabled:**
  - Square root, absolute value, rounding
  - Ceiling, floor operations
  - Power and logarithm calculations
  - Trigonometric functions (sin, cos, tan, asin, acos, atan)
  - Factorial, GCD, LCM
  - Prime number checking
  - Min/max/clamp operations
- **Functions:** 20 mathematical functions

#### 2. **String Tools** (`kaynat/stdlib/string_tools.py`)
- **Dependencies:** None (pure Python)
- **Features Enabled:**
  - Case conversion (uppercase, lowercase, titlecase)
  - Trimming whitespace
  - String searching (starts_with, ends_with, contains, find_position)
  - String manipulation (replace, split, join, substring)
  - String reversal and repetition
  - String validation (is_empty, is_numeric, is_alphabetic, is_alphanumeric)
  - Padding operations (pad_left, pad_right, center)
- **Functions:** 24 string manipulation functions

#### 3. **List Tools** (`kaynat/stdlib/list_tools.py`)
- **Dependencies:** None (pure Python)
- **Features Enabled:**
  - List modification (append, prepend, insert, remove)
  - List access (get, slice, index_of)
  - List properties (length, is_empty, contains, count)
  - List operations (sort, reverse, copy, clear, extend)
  - List aggregation (min, max, sum, average)
- **Functions:** 20 list manipulation functions

#### 4. **File Tools** (`kaynat/stdlib/file_tools.py`)
- **Dependencies:**
  - `os` (Python standard library)
  - `shutil` (Python standard library)
  - `pathlib` (Python standard library)
- **Features Enabled:**
  - File reading (read_file, read_lines)
  - File writing (write_file, append_file)
  - File operations (file_exists, delete_file, copy_file, move_file)
  - Directory operations (create_directory, delete_directory, directory_exists, list_directory)
- **Functions:** 12 file system functions

#### 5. **Date & Time Tools** (`kaynat/stdlib/date_tools.py`)
- **Dependencies:**
  - `datetime` (Python standard library)
  - `timedelta` (Python standard library)
- **Features Enabled:**
  - Current date/time retrieval
  - Unix timestamp generation
  - Date formatting
  - Date parsing
- **Functions:** 5 date/time functions

#### 6. **Random Tools** (`kaynat/stdlib/random_tools.py`)
- **Dependencies:**
  - `random` (Python standard library)
  - `string` (Python standard library)
- **Features Enabled:**
  - Random integer generation
  - Random float generation
  - Random boolean generation
  - Random choice from list
  - List shuffling
  - Random string generation
- **Functions:** 6 random generation functions

#### 7. **Network Tools** (`kaynat/stdlib/network_tools.py`)
- **Dependencies:**
  - `urllib.request` (Python standard library)
  - `urllib.error` (Python standard library)
  - `urllib.parse` (Python standard library)
- **Features Enabled:**
  - HTTP requests (fetch_url)
  - URL reachability checking (is_url_reachable)
- **Functions:** 2 network functions
- **Note:** Requires internet connection for functionality

#### 8. **JSON Tools** (`kaynat/stdlib/json_tools.py`)
- **Dependencies:**
  - `json` (Python standard library)
- **Features Enabled:**
  - JSON parsing (parse_json)
  - JSON generation (generate_json)
  - JSON formatting (format_json)
- **Functions:** 3 JSON manipulation functions

#### 9. **Crypto Tools** (`kaynat/stdlib/crypto_tools.py`)
- **Dependencies:**
  - `hashlib` (Python standard library)
  - `base64` (Python standard library)
  - `secrets` (Python standard library)
- **Features Enabled:**
  - SHA-256 hashing
  - MD5 hashing
  - Secure token generation
  - Base64 encoding/decoding
- **Functions:** 5 cryptographic functions

#### 10. **Pattern Tools** (`kaynat/stdlib/pattern_tools.py`)
- **Dependencies:**
  - `re` (Python standard library - regular expressions)
- **Features Enabled:**
  - Pattern matching (find_matches, matches_pattern)
  - Pattern replacement (replace_pattern)
  - Pattern splitting (split_by_pattern)
  - Email validation (is_valid_email)
  - URL validation (is_valid_url)
- **Functions:** 6 pattern matching functions

---

### Data Structures & Algorithms (DSA) Features

#### 1. **Stack** (`kaynat/dsa/stack.py`)
- **Dependencies:** None (pure Python)
- **Features:** LIFO data structure with push, pop, peek operations

#### 2. **Queue** (`kaynat/dsa/queue.py`)
- **Dependencies:**
  - `collections.deque` (Python standard library)
- **Features:** FIFO data structure with enqueue, dequeue operations

#### 3. **Linked List** (`kaynat/dsa/linked_list.py`)
- **Dependencies:** None (pure Python)
- **Features:** Singly linked list with append, prepend, delete, find operations

#### 4. **Binary Search Tree** (`kaynat/dsa/binary_search_tree.py`)
- **Dependencies:** None (pure Python)
- **Features:** BST with insert, search, delete, traversal operations

#### 5. **Graph** (`kaynat/dsa/graph.py`)
- **Dependencies:** None (pure Python)
- **Features:** Graph data structure with BFS, DFS, shortest path algorithms

#### 6. **Heap** (`kaynat/dsa/heap.py`)
- **Dependencies:** None (pure Python)
- **Features:** Min/max heap with insert, extract operations

#### 7. **Hash Map** (`kaynat/dsa/hash_map.py`)
- **Dependencies:** None (pure Python)
- **Features:** Hash table implementation with put, get, remove operations

#### 8. **Trie** (`kaynat/dsa/trie.py`)
- **Dependencies:** None (pure Python)
- **Features:** Prefix tree for string operations

#### 9. **Sorting Algorithms** (`kaynat/dsa/sorting.py`)
- **Dependencies:** None (pure Python)
- **Features:** Bubble sort, merge sort, quick sort, insertion sort, etc.

#### 10. **Searching Algorithms** (`kaynat/dsa/searching.py`)
- **Dependencies:** None (pure Python)
- **Features:** Linear search, binary search, pattern matching

---

### Object-Oriented Programming (OOP) Features

#### 1. **Blueprint System** (`kaynat/oop/blueprint.py`)
- **Dependencies:** None (pure Python)
- **Features:** Class definitions, inheritance, methods, properties
- **Status:** Stub implementation (planned for v2.0.0)

#### 2. **Instance System** (`kaynat/oop/instance.py`)
- **Dependencies:** None (pure Python)
- **Features:** Object instantiation, property access, method calls
- **Status:** Stub implementation (planned for v2.0.0)

#### 3. **Contract System** (`kaynat/oop/contract.py`)
- **Dependencies:** None (pure Python)
- **Features:** Interface definitions, contract validation
- **Status:** Stub implementation (planned for v2.0.0)

---

### GUI Features

#### 1. **GUI Engine** (`kaynat/gui/engine.py`, `kaynat/gui/tkinter_engine.py`)
- **Dependencies:**
  - `tkinter` (Python standard library - requires separate installation on some systems)
  - `tkinter.ttk` (themed widgets)
  - `tkinter.messagebox` (dialog boxes)
  - `tkinter.filedialog` (file selection dialogs)
- **Features Enabled:**
  - Window creation and management
  - Event loop handling
  - Widget management
- **Installation Required:** See "Optional Dependencies" section above

#### 2. **Window Management** (`kaynat/gui/window.py`)
- **Dependencies:**
  - `tkinter` (via GUI engine)
- **Features:** Window creation, show/hide, close operations

#### 3. **Widgets** (`kaynat/gui/widgets.py`)
- **Dependencies:**
  - `tkinter` (via GUI engine)
- **Features:**
  - Labels, buttons, text inputs
  - Text areas, checkboxes, dropdowns
  - All standard GUI widgets

#### 4. **Events** (`kaynat/gui/events.py`)
- **Dependencies:**
  - `tkinter` (via GUI engine)
- **Features:** Event handling, callbacks, user interactions

#### 5. **Canvas** (`kaynat/gui/canvas.py`)
- **Dependencies:**
  - `tkinter` (via GUI engine)
- **Features:** Drawing operations, shapes, graphics

#### 6. **Dialogs** (`kaynat/gui/dialogs.py`)
- **Dependencies:**
  - `tkinter.messagebox`
  - `tkinter.filedialog`
- **Features:** Message boxes, file selection, user prompts

#### 7. **Menus** (`kaynat/gui/menu.py`)
- **Dependencies:**
  - `tkinter` (via GUI engine)
- **Features:** Menu bars, context menus, menu items

#### 8. **Themes** (`kaynat/gui/themes.py`)
- **Dependencies:**
  - `tkinter.ttk` (themed widgets)
- **Features:** Dark/light themes, color schemes, styling

---

## Summary

### Minimal Installation (Core Features Only)
- **Python 3.8+** - That's it!
- **Features Available:** All core language features, standard library (99 functions), DSA modules

### Full Installation (Including GUI)
- **Python 3.8+**
- **Tkinter** (python3-tk package)
- **Features Available:** Everything including GUI applications

### No External pip Packages Required
Kaynat uses only Python's standard library, making it:
- Easy to install
- Lightweight
- No dependency conflicts
- Works offline (except network tools)

---

## Verification

To verify your installation has all required dependencies:

```bash
# Test core features
python3 -m kaynat.main examples/01_hello_world.kaynat

# Test standard library
python3 -m kaynat.main examples/11_stdlib_demo.kaynat

# Test GUI (requires tkinter)
python3 -m kaynat.main examples/calculator_gui.kaynat
```

---

## Troubleshooting

### Issue: "No module named 'tkinter'"
**Solution:** Install tkinter for your system (see Optional Dependencies section)

### Issue: "Python version too old"
**Solution:** Upgrade to Python 3.8 or higher

### Issue: Network tools not working
**Solution:** Check internet connection; network tools require connectivity

---

**Last Updated:** 2026-02-26  
**Kaynat Version:** 1.0.0  
**Author:** Mohammad Faiz
