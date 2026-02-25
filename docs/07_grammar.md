# Kaynat Language Grammar Reference

## Formal Grammar (EBNF-style)

This document describes the formal grammar of the Kaynat programming language.

---

## Notation

- `::=` means "is defined as"
- `|` means "or"
- `[]` means optional
- `{}` means zero or more repetitions
- `()` means grouping
- `"text"` means literal text

---

## Program Structure

```
program ::= ["begin" "program" "."] {statement} ["end" "program" "."]

statement ::= variable_declaration
            | constant_declaration
            | assignment
            | print_statement
            | input_statement
            | conditional
            | while_loop
            | repeat_loop
            | for_each_loop
            | loop_statement
            | function_definition
            | function_call
            | return_statement
            | break_statement
            | continue_statement
            | arithmetic_statement
            | comment
            | list_creation
```

---

## Variables

```
variable_declaration ::= ("set" | "let" | "define") identifier "to" expression "."

constant_declaration ::= "always" "set" identifier "as" expression "."

assignment ::= "change" identifier "to" expression "."
```

---

## Data Types

```
expression ::= number
             | string
             | boolean
             | null
             | identifier
             | list_literal
             | binary_operation
             | unary_operation
             | comparison
             | logical_operation

number ::= ["-"] digit {digit} ["." digit {digit}]

string ::= identifier

boolean ::= "true" | "false" | "yes" | "no"

null ::= "nothing"

list_literal ::= "a" "list" "containing" expression {"," expression}
```

---

## Operators

```
binary_operation ::= expression operator expression

operator ::= "plus" | "minus" | "multiplied" "by" | "divided" "by"

unary_operation ::= ("negative" | "not") expression

comparison ::= expression comparison_op expression

comparison_op ::= "is" "greater" "than"
                | "is" "less" "than"
                | "is" "equal" "to"
                | "is" "not" "equal" "to"
                | "is" "greater" "than" "or" "equal" "to"
                | "is" "less" "than" "or" "equal" "to"

logical_operation ::= expression ("and" | "or") expression
                    | "not" expression
```

---

## Arithmetic Statements

```
arithmetic_statement ::= "add" expression "to" identifier "."
                       | "subtract" expression "from" identifier "."
                       | "multiply" identifier "by" expression "."
                       | "divide" identifier "by" expression "."
```

---

## Control Flow

```
conditional ::= "if" condition "then" "."
                {statement}
                {"otherwise" "if" condition "then" "." {statement}}
                ["otherwise" "." {statement}]
                "end" "."

condition ::= expression
```

---

## Loops

```
while_loop ::= "while" condition ["then"] "."
               {statement}
               "end" "."

repeat_loop ::= "repeat" expression "times" "."
                {statement}
                "end" "."

for_each_loop ::= "for" "each" identifier "in" identifier "."
                  {statement}
                  "end" "."

loop_statement ::= "loop" "from" expression "to" expression
                   ["stepping" "by" expression] "."
                   {statement}
                   "end" "."

break_statement ::= "stop" "."

continue_statement ::= "skip" "."
```

---

## Functions

```
function_definition ::= "define" ["a"] "function" "called" identifier
                        ["that" "takes" parameter_list] "."
                        {statement}
                        "end" "."

parameter_list ::= identifier {"," identifier}

function_call ::= "call" identifier ["with" argument_list] "."

argument_list ::= expression {"," expression}

return_statement ::= "give" "back" expression "."
```

---

## Lists

```
list_creation ::= "create" "a" "list" "called" identifier "."
```

---

## Input/Output

```
print_statement ::= ("say" | "print" | "show") print_item {"," print_item} "."

print_item ::= expression | identifier | keyword

input_statement ::= "ask" "the" "user" "for" identifier "."
```

---

## Comments

```
comment ::= "note" "."
```

---

## Lexical Elements

```
identifier ::= letter {letter | digit}

letter ::= "a" | "b" | ... | "z"

digit ::= "0" | "1" | ... | "9"

keyword ::= "set" | "let" | "define" | "always" | "change" | "to" | "as"
          | "if" | "then" | "otherwise" | "end" | "while" | "repeat"
          | "times" | "for" | "each" | "in" | "loop" | "from" | "stepping"
          | "by" | "stop" | "skip" | "function" | "called" | "that" | "takes"
          | "give" | "back" | "call" | "with" | "say" | "print" | "show"
          | "ask" | "user" | "note" | "create" | "list" | "containing"
          | "true" | "false" | "yes" | "no" | "nothing" | "and" | "or" | "not"
          | "is" | "greater" | "less" | "than" | "equal" | "add" | "subtract"
          | "multiply" | "divide" | "negative" | "begin" | "program"
          | ... (see full keyword list in token_types.py)
```

---

## Punctuation

```
period ::= "."
comma ::= ","
```

**Note:** These are the ONLY punctuation marks allowed in Kaynat source code.

---

## Whitespace

Whitespace (spaces, tabs, newlines) is used to separate tokens but is otherwise ignored.

---

## Grammar Rules

### Rule 1: Statement Termination
Every statement must end with a period (`.`).

### Rule 2: Block Structure
Blocks (if, while, for, function) must end with `end.`

### Rule 3: Expression Placement
Expressions can appear:
- After `to` in variable declarations
- After `is` in comparisons
- As arguments in function calls
- In arithmetic statements

### Rule 4: Identifier Rules
- Identifiers are case-insensitive
- Identifiers cannot be keywords
- Identifiers consist of letters only (no digits, underscores, or special characters)

### Rule 5: List Separator
Items in lists are separated by commas.

---

## Example Programs with Grammar Annotations

### Example 1: Variable Declaration

```kaynat
set x to 5.
```

Grammar breakdown:
- `set` - keyword
- `x` - identifier
- `to` - keyword
- `5` - number
- `.` - period

### Example 2: Conditional

```kaynat
if age is greater than 18 then.
    say adult.
end.
```

Grammar breakdown:
- `if` - keyword
- `age` - identifier (expression)
- `is greater than` - comparison operator
- `18` - number (expression)
- `then` - keyword
- `.` - period
- `say` - keyword
- `adult` - identifier (treated as string in print context)
- `.` - period
- `end` - keyword
- `.` - period

### Example 3: Function

```kaynat
define a function called greet that takes name.
    say hello, name.
end.
```

Grammar breakdown:
- `define a function called` - keywords
- `greet` - identifier (function name)
- `that takes` - keywords
- `name` - identifier (parameter)
- `.` - period
- `say` - keyword
- `hello` - identifier (string)
- `,` - comma
- `name` - identifier (variable reference)
- `.` - period
- `end` - keyword
- `.` - period

---

## Precedence and Associativity

### Operator Precedence (highest to lowest)

1. Unary operators (`negative`, `not`)
2. Multiplicative (`multiplied by`, `divided by`)
3. Additive (`plus`, `minus`, `add`, `subtract`)
4. Comparison (`is greater than`, `is less than`, etc.)
5. Logical AND (`and`)
6. Logical OR (`or`)

### Associativity

All binary operators are left-associative.

---

## Reserved Keywords

The following words are reserved and cannot be used as identifiers:

```
set, let, define, always, change, to, as, if, then, otherwise, end,
while, repeat, times, for, each, in, loop, from, stepping, by, stop,
skip, function, called, that, takes, give, back, call, with, say,
print, show, ask, user, note, create, list, containing, true, false,
yes, no, nothing, and, or, not, is, greater, less, than, equal, add,
subtract, multiply, divide, negative, begin, program, a, an, the, my,
has, private, initialize, parent, on, extends, this, must, be,
implemented, abstract, contract, requires, follows, shared, starting,
new, other, do, when, default, join, store, length, of, convert,
uppercase, lowercase, trim, whitespace, check, starts, ends, replace,
split, position, take, characters, reverse, contains, empty, exists,
file, line, write, append, delete, attempt, it, fails, message, after,
error, saying, type, text, turn, into, flag, global, bring, use,
module, named, export, written, care, clarity, blueprint, stack, queue,
linked, push, onto, pop, peek, size, enqueue, dequeue, node, binary,
search, tree, traverse, inorder, preorder, postorder, height, minimum,
maximum, graph, edge, weight, shortest, path, dijkstra, breadth, first,
depth, cycle, connected, components, min, heap, priority, extract, max,
hash, put, load, factor, trie, word, words, bubble, merge, quick,
insertion, selection, radix, counting, linear, pattern, knuth, morris,
pratt, positions, bellman, ford, spanning, kruskal, prim, topological,
order, strongly, kosaraju, window, title, width, height, background,
label, font, color, place, row, column, button, action, input,
placeholder, area, checkbox, dropdown, options, radio, group, slider,
progress, bar, image, source, grid, layout, flow, padding, horizontal,
vertical, sticky, alignment, left, span, across, columns, clicked,
changes, closed, confirm, choose, folder, save, menu, separator, attach,
canvas, board, draw, rectangle, fill, circle, radius, clear, open,
close, minimize, maximize, apply, theme, dark, light, accent, run, wait,
finish, finishes, timer, cancel
```

---

## Grammar Extensions (Planned)

Future versions may include:

- String literals with quotes: `"hello world"`
- Multi-line strings
- String interpolation
- Dictionary literals
- Lambda expressions
- List comprehensions
- Pattern matching
- Type annotations

---

*This grammar describes Kaynat version 1.0.0. Future versions may extend or modify the grammar.*
