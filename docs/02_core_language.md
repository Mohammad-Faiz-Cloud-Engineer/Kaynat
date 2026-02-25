# Kaynat Core Language Reference

## Table of Contents

1. [Program Structure](#program-structure)
2. [Comments](#comments)
3. [Variables and Constants](#variables-and-constants)
4. [Data Types](#data-types)
5. [Arithmetic Operations](#arithmetic-operations)
6. [String Operations](#string-operations)
7. [Comparison and Logic](#comparison-and-logic)
8. [Conditionals](#conditionals)
9. [Loops](#loops)
10. [Functions](#functions)
11. [Lists](#lists)
12. [Input and Output](#input-and-output)
13. [Scope](#scope)

---

## Program Structure

Every Kaynat program should start with `begin program.` and end with `end program.`

```kaynat
begin program.

say Hello, World.

end program.
```

**Rules:**
- Every statement ends with a period (.)
- Commas (,) separate items in lists
- No other punctuation is allowed
- Everything is English words

---

## Comments

Comments are marked with `note.`

```kaynat
note. This is a comment.

set x to 5.
```

**Note:** Currently, comments must be just `note.` - additional text after note is not yet parsed.

---

## Variables and Constants

### Variable Declaration

Use `set`, `let`, or `define` to create variables:

```kaynat
set name to Alice.
set age to 25.
set price to 9.99.
set active to true.
```

### Constants

Use `always set` to create constants that cannot be changed:

```kaynat
always set pi as 3.14159.
always set max as 100.
```

### Reassignment

Use `change` to modify existing variables:

```kaynat
set x to 10.
change x to 20.
say x.
```

**Output:** `20`

### Variable Names

- Variable names are lowercase
- Use simple words (no underscores or special characters)
- Multi-word names are treated as single identifiers

---

## Data Types

### Numbers

Integers and floating-point numbers:

```kaynat
set count to 42.
set price to 19.99.
set temperature to negative 10.
```

### Strings

Bare words are treated as strings:

```kaynat
set name to Kaynat.
set greeting to Hello.
```

### Booleans

True or false values:

```kaynat
set active to true.
set finished to false.
```

### Null

The absence of a value:

```kaynat
set result to nothing.
```

### Lists

Collections of values:

```kaynat
set numbers to a list containing 1, 2, 3, 4, 5.
set names to a list containing Alice, Bob, Charlie.
```

Create empty lists:

```kaynat
create a list called items.
```

---

## Arithmetic Operations

### Addition

```kaynat
set x to 10.
add 5 to x.
say x.
```

**Output:** `15`

### Subtraction

```kaynat
set y to 20.
subtract 3 from y.
say y.
```

**Output:** `17`

### Multiplication

```kaynat
set result to 5.
set result to 4.
```

**Note:** Full multiplication syntax planned for future versions.

### Division

```kaynat
set result to 20.
set result to 4.
```

**Note:** Full division syntax planned for future versions.

---

## String Operations

**Note:** String operations are planned for future versions. Currently, strings can be:
- Created as bare words
- Printed with `say`
- Stored in variables

---

## Comparison and Logic

### Comparison Operators

```kaynat
if x is greater than 10 then.
    say x is large.
end.

if x is less than 5 then.
    say x is small.
end.

if x is equal to 10 then.
    say x is exactly 10.
end.

if x is not equal to 0 then.
    say x is not zero.
end.
```

### Logical Operators

**AND:**
```kaynat
if age is greater than 18 and verified is true then.
    say Access granted.
end.
```

**OR:**
```kaynat
if role is admin or role is moderator then.
    say You have permissions.
end.
```

**NOT:**
```kaynat
if not finished then.
    say Still working.
end.
```

---

## Conditionals

### If Statement

```kaynat
set age to 20.

if age is greater than 18 then.
    say You are an adult.
end.
```

### If-Otherwise

```kaynat
if score is greater than 90 then.
    say Excellent.
otherwise.
    say Keep trying.
end.
```

### If-Otherwise If-Otherwise

```kaynat
if score is greater than 90 then.
    say Grade A.
otherwise if score is greater than 80 then.
    say Grade B.
otherwise if score is greater than 70 then.
    say Grade C.
otherwise.
    say Grade F.
end.
```

---

## Loops

### Repeat N Times

Execute a block a fixed number of times:

```kaynat
repeat 5 times.
    say Hello.
end.
```

### While Loop

Execute while a condition is true:

```kaynat
set x to 1.
while x is less than 6 then.
    say x.
    add 1 to x.
end.
```

### For Each Loop

Iterate over a list:

```kaynat
set fruits to a list containing apple, banana, cherry.

for each fruit in fruits.
    say fruit.
end.
```

### Loop From-To

Loop through a range of numbers:

```kaynat
loop from 1 to 10.
    say current.
end.
```

The variable `current` holds the current iteration value.

### Loop With Step

```kaynat
loop from 0 to 100 stepping by 10.
    say current.
end.
```

**Output:** `0 10 20 30 40 50 60 70 80 90 100`

### Break and Continue

**Break (stop):**
```kaynat
loop from 1 to 100.
    if current is equal to 50 then.
        stop.
    end.
    say current.
end.
```

**Continue (skip):**
```kaynat
loop from 1 to 10.
    if current is equal to 5 then.
        skip.
    end.
    say current.
end.
```

---

## Functions

### Function Definition

```kaynat
define a function called greet.
    say Hello from Kaynat.
end.
```

### Function with Parameters

```kaynat
define a function called greetperson that takes name.
    say Hello, name.
end.
```

### Multiple Parameters

```kaynat
define a function called add that takes x, y.
    set sum to 0.
    add x to sum.
    add y to sum.
    give back sum.
end.
```

### Calling Functions

```kaynat
call greet.
call greetperson with Alice.
```

### Return Values

```kaynat
define a function called square that takes n.
    set result to 0.
    add n to result.
    give back result.
end.
```

**Note:** Function call expressions (using return values directly) are planned for future versions.

---

## Lists

### Creating Lists

With initial values:
```kaynat
set numbers to a list containing 1, 2, 3, 4, 5.
```

Empty list:
```kaynat
create a list called items.
```

### Iterating Over Lists

```kaynat
set colors to a list containing red, green, blue.

for each color in colors.
    say color.
end.
```

### List Operations

**Note:** Advanced list operations (add, remove, sort, filter, map) are planned for future versions.

---

## Input and Output

### Output

Use `say`, `print`, or `show`:

```kaynat
say Hello, World.
print Welcome to Kaynat.
show The result is, 42.
```

### Input

Ask the user for input:

```kaynat
ask the user for name.
say Hello, name.
```

---

## Scope

### Local Scope

Variables defined inside functions are local:

```kaynat
define a function called test.
    set local to 10.
    say local.
end.

call test.
```

### Global Scope

Variables defined outside functions are global:

```kaynat
set global to 100.

define a function called showglobal.
    say global.
end.

call showglobal.
```

---

## Best Practices

1. **Use descriptive names:** `set usercount to 10.` not `set x to 10.`
2. **Keep functions small:** Each function should do one thing
3. **Comment your code:** Use `note.` to explain complex logic
4. **Use constants:** For values that shouldn't change
5. **Handle errors:** Check conditions before operations

---

## Common Patterns

### Counter Pattern

```kaynat
set counter to 0.
repeat 10 times.
    add 1 to counter.
end.
say counter.
```

### Accumulator Pattern

```kaynat
set total to 0.
set numbers to a list containing 1, 2, 3, 4, 5.

for each num in numbers.
    add num to total.
end.

say Total is, total.
```

### Flag Pattern

```kaynat
set found to false.

for each item in items.
    if item is equal to target then.
        set found to true.
        stop.
    end.
end.

if found is true then.
    say Item found.
end.
```

---

## Exercises

### Exercise 1: Sum of Numbers

Write a program that calculates the sum of numbers from 1 to 100.

### Exercise 2: Even Numbers

Write a program that prints all even numbers from 1 to 20.

### Exercise 3: Factorial

Write a function that calculates the factorial of a number.

### Exercise 4: List Maximum

Write a program that finds the maximum value in a list.

---

*This is the core language reference for Kaynat 1.0.0*

*For advanced features (OOP, DSA, GUI), see the respective documentation files.*
