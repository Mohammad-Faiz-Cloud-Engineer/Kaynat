# Kaynat Error Reference

## Error Types and Solutions

This document lists all error types in Kaynat with explanations and solutions.

---

## Lexer Errors

### Unexpected Character

**Error Message:**
```
Unexpected character 'X' at line Y, column Z
```

**Cause:**
The lexer encountered a character that is not allowed in Kaynat source code.

**Allowed Characters:**
- Letters (a-z, A-Z)
- Digits (0-9)
- Period (.)
- Comma (,)
- Spaces, tabs, newlines

**Solution:**
Remove or replace the invalid character. Common mistakes:
- Using hyphens (-) in comments or text
- Using underscores (_) in identifiers
- Using quotes (", ') around strings
- Using parentheses, brackets, or braces

**Example:**
```kaynat
Wrong: set user_name to Alice.
Right: set username to Alice.

Wrong: say "Hello World".
Right: say Hello World.
```

---

## Parser Errors

### Expected Token

**Error Message:**
```
Expected TOKEN_TYPE, got ACTUAL_TYPE (line X, column Y)
```

**Cause:**
The parser expected a specific token but found something else.

**Common Cases:**

1. **Missing period:**
```kaynat
Wrong: set x to 5
Right: set x to 5.
```

2. **Missing keyword:**
```kaynat
Wrong: set x 5.
Right: set x to 5.
```

3. **Missing end:**
```kaynat
Wrong:
if x is greater than 5 then.
    say large.

Right:
if x is greater than 5 then.
    say large.
end.
```

### Unexpected Token

**Error Message:**
```
Unexpected token: TOKEN_TYPE (line X, column Y)
```

**Cause:**
The parser found a token that doesn't fit the current context.

**Common Cases:**

1. **Using reserved keyword as identifier:**
```kaynat
Wrong: set result to 10.  (if 'result' is a keyword)
Right: set value to 10.
```

2. **Incorrect statement structure:**
```kaynat
Wrong: say hello to world.
Right: say hello, world.
```

### Unexpected Token in Expression

**Error Message:**
```
Unexpected token in expression: TOKEN_TYPE (line X, column Y)
```

**Cause:**
An invalid token appeared where an expression was expected.

**Solution:**
Check that you're using valid expression syntax:
- Numbers: `5`, `3.14`
- Identifiers: `x`, `name`
- Booleans: `true`, `false`
- Lists: `a list containing 1, 2, 3`

---

## Runtime Errors

### Variable Not Defined

**Error Message:**
```
Variable 'name' is not defined
```

**Cause:**
Trying to use a variable that hasn't been declared.

**Solution:**
Declare the variable before using it:

```kaynat
Wrong:
say x.

Right:
set x to 5.
say x.
```

### Cannot Change Constant

**Error Message:**
```
Cannot change constant 'name'
```

**Cause:**
Trying to modify a constant declared with `always set`.

**Solution:**
Use a regular variable if you need to change the value:

```kaynat
Wrong:
always set pi as 3.14.
change pi to 3.14159.

Right:
set pi to 3.14.
change pi to 3.14159.
```

### Cannot Delete Constant

**Error Message:**
```
Cannot delete constant 'name'
```

**Cause:**
Trying to delete a constant.

**Solution:**
Constants cannot be deleted. Use regular variables if you need this functionality.

---

## Type Errors

### Type Mismatch in Operation

**Error Message:**
```
Cannot add TYPE1 and TYPE2 (line X, column Y)
Cannot subtract TYPE2 from TYPE1 (line X, column Y)
Cannot multiply TYPE1 and TYPE2 (line X, column Y)
Cannot divide TYPE1 by TYPE2 (line X, column Y)
```

**Cause:**
Trying to perform arithmetic on incompatible types.

**Solution:**
Ensure both operands are numbers:

```kaynat
Wrong:
set x to hello.
add 5 to x.

Right:
set x to 10.
add 5 to x.
```

### Cannot Negate Type

**Error Message:**
```
Cannot negate TYPE (line X, column Y)
```

**Cause:**
Trying to use `negative` on a non-number.

**Solution:**
Only use `negative` with numbers:

```kaynat
Wrong:
set x to negative hello.

Right:
set x to negative 10.
```

### Cannot Compare Types

**Error Message:**
```
Cannot compare TYPE1 and TYPE2 (line X, column Y)
```

**Cause:**
Trying to compare incompatible types with `is greater than` or `is less than`.

**Solution:**
Ensure you're comparing compatible types:

```kaynat
Wrong:
if name is greater than 5 then.

Right:
if age is greater than 5 then.
```

### Not a Function

**Error Message:**
```
'name' is not a function (line X, column Y)
```

**Cause:**
Trying to call something that isn't a function.

**Solution:**
Ensure you're calling an actual function:

```kaynat
Wrong:
set x to 5.
call x.

Right:
define a function called greet.
    say hello.
end.
call greet.
```

### Wrong Number of Arguments

**Error Message:**
```
Function 'name' expects X arguments, got Y (line X, column Y)
```

**Cause:**
Calling a function with the wrong number of arguments.

**Solution:**
Match the number of arguments to the function definition:

```kaynat
Wrong:
define a function called add that takes x, y.
    give back x.
end.
call add with 5.

Right:
call add with 5, 10.
```

### Can Only Iterate Over Lists

**Error Message:**
```
Can only iterate over lists, got TYPE (line X, column Y)
```

**Cause:**
Trying to use `for each` on something that isn't a list.

**Solution:**
Ensure you're iterating over a list:

```kaynat
Wrong:
set x to 5.
for each item in x.
    say item.
end.

Right:
set items to a list containing 1, 2, 3.
for each item in items.
    say item.
end.
```

### Repeat Count Must Be Number

**Error Message:**
```
Repeat count must be a number, got TYPE (line X, column Y)
```

**Cause:**
Using a non-number in `repeat N times`.

**Solution:**
Use a number for the repeat count:

```kaynat
Wrong:
set count to hello.
repeat count times.
    say hi.
end.

Right:
set count to 5.
repeat count times.
    say hi.
end.
```

### Loop Bounds Must Be Numbers

**Error Message:**
```
Loop bounds must be numbers (line X, column Y)
```

**Cause:**
Using non-numbers in `loop from X to Y`.

**Solution:**
Use numbers for loop bounds:

```kaynat
Wrong:
loop from hello to world.
    say current.
end.

Right:
loop from 1 to 10.
    say current.
end.
```

---

## Math Errors

### Division by Zero

**Error Message:**
```
Cannot divide by zero (line X, column Y)
```

**Cause:**
Attempting to divide by zero.

**Solution:**
Check for zero before dividing:

```kaynat
Wrong:
set x to 10.
set y to 0.
divide x by y.

Right:
set x to 10.
set y to 5.
if y is not equal to 0 then.
    divide x by y.
end.
```

---

## Common Error Patterns

### Pattern 1: Forgetting Period

```kaynat
Wrong:
set x to 5
say x

Right:
set x to 5.
say x.
```

### Pattern 2: Missing End

```kaynat
Wrong:
if x is greater than 5 then.
    say large.

Right:
if x is greater than 5 then.
    say large.
end.
```

### Pattern 3: Using Undefined Variable

```kaynat
Wrong:
say result.

Right:
set result to 0.
say result.
```

### Pattern 4: Type Mismatch

```kaynat
Wrong:
set name to Alice.
add 5 to name.

Right:
set count to 10.
add 5 to count.
```

### Pattern 5: Wrong Function Arguments

```kaynat
Wrong:
define a function called greet that takes name.
    say hello, name.
end.
call greet.

Right:
call greet with Alice.
```

---

## Debugging Tips

### 1. Read the Error Message Carefully

Error messages include:
- Error type
- Description
- Line number
- Column number

### 2. Check Line and Column

The error location points to where the problem was detected, which may be slightly after the actual mistake.

### 3. Common Mistakes

- Forgetting periods
- Missing `end.` statements
- Using reserved keywords as identifiers
- Type mismatches
- Undefined variables

### 4. Use the REPL

Test small pieces of code in the REPL to isolate problems:

```bash
python3 -m kaynat.repl
```

### 5. Check Example Programs

Look at working examples in the `examples/` directory for correct syntax.

### 6. Simplify

If you have a complex program with errors:
1. Comment out sections
2. Test each part individually
3. Add back sections one at a time

---

## Error Prevention

### Best Practices

1. **Always end statements with periods**
2. **Always close blocks with `end.`**
3. **Declare variables before using them**
4. **Use descriptive variable names**
5. **Check types before operations**
6. **Test functions with different inputs**
7. **Use the REPL for experimentation**

### Code Review Checklist

- [ ] All statements end with periods
- [ ] All blocks have matching `end.`
- [ ] All variables are declared before use
- [ ] Function calls have correct number of arguments
- [ ] Arithmetic operations use numbers
- [ ] Comparisons use compatible types
- [ ] No reserved keywords used as identifiers

---

## Getting Help

If you encounter an error not listed here:

1. Check the line and column number
2. Review the syntax in the Core Language Reference
3. Look at similar examples in the `examples/` directory
4. Try simplifying your code to isolate the problem
5. Use the REPL to test individual statements

---

*This error reference covers Kaynat version 1.0.0. Future versions may add new error types.*
