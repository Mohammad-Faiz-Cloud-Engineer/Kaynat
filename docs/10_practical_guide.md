# Kaynat Practical Programming Guide

## Complete Guide with Working Examples

This guide shows you how to actually use Kaynat with real, working code examples.

---

## Table of Contents

1. [Core Language Basics](#core-language-basics)
2. [Working with Numbers](#working-with-numbers)
3. [Working with Text](#working-with-text)
4. [Lists and Collections](#lists-and-collections)
5. [Functions](#functions)
6. [Control Flow](#control-flow)
7. [Building Real Programs](#building-real-programs)
8. [Standard Library (Planned)](#standard-library-planned)
9. [Data Structures (Planned)](#data-structures-planned)
10. [OOP (Planned)](#oop-planned)
11. [GUI (Planned)](#gui-planned)

---

## Core Language Basics

### Your First Program

```kaynat
begin program.

say Hello, World.
say Welcome to Kaynat.

end program.
```

**What this does:**
- `begin program.` starts your program
- `say` prints text to the screen
- `end program.` ends your program

**Run it:**
```bash
python3 -m kaynat.main hello.kaynat
```

---

## Working with Numbers

### Basic Arithmetic

```kaynat
begin program.

set x to 10.
set y to 5.

say x is, x.
say y is, y.

add 3 to x.
say After adding 3, x is, x.

subtract 2 from y.
say After subtracting 2, y is, y.

end program.
```

**Output:**
```
x is 10
y is 5
after adding 3 x is 13
after subtracting 2 y is 3
```

### Constants

```kaynat
begin program.

always set pi as 3.14159.
always set max score as 100.

say Pi is, pi.
say Maximum score is, max score.

end program.
```

**Note:** Constants cannot be changed after declaration.

---

## Working with Text

### String Output

```kaynat
begin program.

set name to Alice.
set age to 25.

say Hello, name.
say You are, age, years old.

end program.
```

**Output:**
```
hello alice
you are 25 years old
```

**Note:** Kaynat automatically converts everything to lowercase for output.

### Getting User Input

```kaynat
begin program.

ask the user for name.
say Welcome, name.

ask the user for age.
say You are, age, years old.

end program.
```

**How it works:**
- `ask the user for X` prompts for input and stores it in variable X
- The user types their response
- The value is stored as a string

---

## Lists and Collections

### Creating Lists

```kaynat
begin program.

set numbers to a list containing 1, 2, 3, 4, 5.
say List created.

create a list called names.
say Empty list created.

end program.
```

### Iterating Over Lists

```kaynat
begin program.

set fruits to a list containing apple, banana, cherry, date.

say Fruits in the list.

for each fruit in fruits.
    say fruit.
end.

end program.
```

**Output:**
```
fruits in the list
apple
banana
cherry
date
```

---

## Functions

### Defining Functions

```kaynat
begin program.

define a function called greet that takes name.
    say Hello, name.
    say Welcome to Kaynat.
end.

call greet with Alice.
call greet with Bob.

end program.
```

**Output:**
```
hello alice
welcome to kaynat
hello bob
welcome to kaynat
```

### Functions with Return Values

```kaynat
begin program.

define a function called double that takes num.
    set result to num.
    add num to result.
    give back result.
end.

call double with 5 and store as answer.
say The answer is, answer.

end program.
```

---

## Control Flow

### If Statements

```kaynat
begin program.

set age to 20.

if age is greater than 18 then.
    say You are an adult.
otherwise.
    say You are a minor.
end.

end program.
```

### Multiple Conditions

```kaynat
begin program.

set score to 85.

if score is greater than 90 then.
    say Grade A.
otherwise if score is greater than 80 then.
    say Grade B.
otherwise if score is greater than 70 then.
    say Grade C.
otherwise.
    say Grade F.
end.

end program.
```

### While Loops

```kaynat
begin program.

set counter to 1.

while counter is less than 6 then.
    say Count, counter.
    add 1 to counter.
end.

end program.
```

### Repeat Loops

```kaynat
begin program.

set counter to 0.

repeat 5 times.
    say Iteration, counter.
    add 1 to counter.
end.

end program.
```

### For Loops

```kaynat
begin program.

say Counting from 1 to 10.

loop from 1 to 10.
    say current.
end.

say Counting by 2s.

loop from 0 to 20 stepping by 2.
    say current.
end.

end program.
```

---

## Building Real Programs

### Example 1: Number Sequence Generator

```kaynat
begin program.

say Number sequence generator.
say Building Fibonacci-like pattern.

set prev to 0.
set curr to 1.

say prev.
say curr.

repeat 8 times.
    set next to curr.
    add prev to next.
    say next.
    set prev to curr.
    set curr to next.
end.

end program.
```

**Output:**
```
number sequence generator
building fibonacci like pattern
0
1
1
2
3
5
8
13
21
34
```

### Example 2: Simple Calculator

```kaynat
begin program.

say Welcome to Kaynat Calculator.

set num1 to 10.
set num2 to 5.

say First number, num1.
say Second number, num2.

set sum to num1.
add num2 to sum.
say Sum is, sum.

set diff to num1.
subtract num2 from diff.
say Difference is, diff.

say Calculator complete.

end program.
```

### Example 3: List Processor

```kaynat
begin program.

say List processing example.

set numbers to a list containing 10, 20, 30, 40, 50.

say Original numbers.
for each num in numbers.
    say num.
end.

say Doubled numbers.
for each num in numbers.
    set doubled to num.
    add num to doubled.
    say doubled.
end.

end program.
```

### Example 4: Grade Calculator

```kaynat
begin program.

say Grade Calculator.

set scores to a list containing 85, 92, 78, 95, 88.

say Student scores.

for each score in scores.
    if score is greater than 90 then.
        say score, Grade A.
    otherwise if score is greater than 80 then.
        say score, Grade B.
    otherwise if score is greater than 70 then.
        say score, Grade C.
    otherwise.
        say score, Grade F.
    end.
end.

end program.
```

---

## Standard Library (Planned)

The following features are planned for future releases. The syntax is designed but not yet implemented.

### Math Operations

```kaynat
note. Planned for v2.0.0.

use math tools.

set num to 16.
set root to the square root of num.
say Square root of, num, is, root.

set angle to 45.
set sine to the sine of angle.
say Sine of, angle, degrees is, sine.

set x to 5.
set y to 3.
set result to x raised to the power of y.
say result is, result.
```

### String Operations

```kaynat
note. Planned for v2.0.0.

use string tools.

set text to hello world.
set upper to text in uppercase.
say upper.

set words to split text by space.
for each word in words.
    say word.
end.

set joined to join words with dash.
say joined.
```

### File Operations

```kaynat
note. Planned for v2.0.0.

use file tools.

write hello world to file called output.txt.
say File written.

read from file called output.txt and store as content.
say Content is, content.

if file called output.txt exists then.
    say File exists.
end.
```

### JSON Operations

```kaynat
note. Planned for v2.0.0.

use json tools.

create a map called person.
set name in person to Alice.
set age in person to 25.

convert person to json and store as json text.
say json text.

parse json text and store as parsed.
say Name is, name in parsed.
```

---

## Data Structures (Planned)

### Stack

```kaynat
note. Planned for v3.0.0.

use data structures.

create a stack called my stack.

push 10 onto my stack.
push 20 onto my stack.
push 30 onto my stack.

pop from my stack and store as top.
say Popped, top.

peek at my stack and store as next.
say Next is, next.
```

### Queue

```kaynat
note. Planned for v3.0.0.

use data structures.

create a queue called my queue.

enqueue 10 into my queue.
enqueue 20 into my queue.
enqueue 30 into my queue.

dequeue from my queue and store as first.
say Dequeued, first.
```

### Binary Search Tree

```kaynat
note. Planned for v3.0.0.

use data structures.

create a binary search tree called my tree.

insert 50 into my tree.
insert 30 into my tree.
insert 70 into my tree.
insert 20 into my tree.
insert 40 into my tree.

search for 30 in my tree and store as found.

if found is true then.
    say Found 30 in tree.
end.
```

---

## OOP (Planned)

### Defining Classes (Blueprints)

```kaynat
note. Planned for v2.0.0.

define a blueprint called Person.
    
    add property called name.
    add property called age.
    
    define method called introduce.
        say Hello, I am, name.
        say I am, age, years old.
    end.
    
end blueprint.

create a Person called alice.
set name of alice to Alice.
set age of alice to 25.

call introduce on alice.
```

### Inheritance

```kaynat
note. Planned for v2.0.0.

define a blueprint called Student that extends Person.
    
    add property called grade.
    
    define method called study.
        say name, is studying.
    end.
    
end blueprint.

create a Student called bob.
set name of bob to Bob.
set age of bob to 20.
set grade of bob to A.

call introduce on bob.
call study on bob.
```

---

## GUI (Planned)

### Simple Window Application

```kaynat
note. Planned for v3.0.0.

use gui tools.

create a window called main window.
set the title of main window to My First App.
set the width of main window to 600.
set the height of main window to 400.

create a label called greeting.
set the text of greeting to Hello, Kaynat.
place greeting at row 0 and column 0 in main window.

create a button called click me.
set the text of click me to Click Me.
place click me at row 1 and column 0 in main window.

define a function called on click.
    say Button clicked.
    set the text of greeting to Button was clicked.
end.

when click me is clicked, call on click.

show main window.
```

### Form Application

```kaynat
note. Planned for v3.0.0.

use gui tools.

create a window called form window.
set the title of form window to User Form.

create a label called name label.
set the text of name label to Name.
place name label at row 0 and column 0 in form window.

create a text input called name input.
place name input at row 0 and column 1 in form window.

create a label called age label.
set the text of age label to Age.
place age label at row 1 and column 0 in form window.

create a text input called age input.
place age input at row 1 and column 1 in form window.

create a button called submit.
set the text of submit to Submit.
place submit at row 2 and column 0 in form window.

define a function called on submit.
    read text from name input and store as user name.
    read text from age input and store as user age.
    say Name, user name.
    say Age, user age.
    show a message saying Form submitted.
end.

when submit is clicked, call on submit.

show form window.
```

---

## Tips and Best Practices

### 1. Always Use begin/end program

```kaynat
begin program.
    note. Your code here.
end program.
```

### 2. Use Descriptive Variable Names

```kaynat
note. Good.
set student name to Alice.
set total score to 95.

note. Bad.
set x to Alice.
set y to 95.
```

### 3. Add Comments

```kaynat
begin program.

note. Calculate the sum of two numbers.
set num1 to 10.
set num2 to 20.

set sum to num1.
add num2 to sum.

say The sum is, sum.

end program.
```

### 4. Break Complex Logic into Functions

```kaynat
begin program.

define a function called calculate total that takes price, quantity.
    set total to price.
    set counter to 1.
    while counter is less than quantity then.
        add price to total.
        add 1 to counter.
    end.
    give back total.
end.

call calculate total with 10, 5 and store as result.
say Total is, result.

end program.
```

### 5. Use Meaningful Output

```kaynat
begin program.

set score to 85.

note. Good - descriptive output.
say Your score is, score.

note. Bad - unclear output.
say score.

end program.
```

---

## Common Patterns

### Pattern 1: Counter Loop

```kaynat
set counter to 0.
repeat 10 times.
    say Iteration, counter.
    add 1 to counter.
end.
```

### Pattern 2: Accumulator

```kaynat
set total to 0.
set numbers to a list containing 10, 20, 30, 40, 50.

for each num in numbers.
    add num to total.
end.

say Total is, total.
```

### Pattern 3: Conditional Processing

```kaynat
set items to a list containing 5, 15, 25, 35, 45.

for each item in items.
    if item is greater than 20 then.
        say item, is large.
    otherwise.
        say item, is small.
    end.
end.
```

### Pattern 4: Function with Validation

```kaynat
define a function called divide that takes numerator, denominator.
    if denominator is equal to 0 then.
        say Cannot divide by zero.
        give back 0.
    end.
    
    note. Actual division would go here.
    say Dividing, numerator, by, denominator.
    give back numerator.
end.
```

---

## Troubleshooting

### Error: Expected THEN

**Problem:**
```kaynat
if x is greater than 10.
    say x is big.
end.
```

**Solution:** Add `then.` after the condition
```kaynat
if x is greater than 10 then.
    say x is big.
end.
```

### Error: Undefined Variable

**Problem:**
```kaynat
say name.
```

**Solution:** Define the variable first
```kaynat
set name to Alice.
say name.
```

### Error: Cannot Modify Constant

**Problem:**
```kaynat
always set pi as 3.14.
set pi to 3.14159.
```

**Solution:** Don't try to change constants, or use regular variables
```kaynat
set pi to 3.14.
set pi to 3.14159.
```

---

## Next Steps

1. **Practice the basics** - Run all the examples in this guide
2. **Modify examples** - Change values and see what happens
3. **Build small programs** - Start with simple calculators and counters
4. **Read the docs** - Check out the other documentation files
5. **Experiment** - Try combining different features

---

## Additional Resources

- **[Core Language Reference](02_core_language.md)** - Complete language syntax
- **[Getting Started](01_getting_started.md)** - Installation and setup
- **[Grammar Reference](07_grammar.md)** - Formal language specification
- **[Error Reference](08_errors.md)** - Understanding error messages
- **[Examples Directory](../examples/)** - 10 working example programs

---

*This guide covers Kaynat v1.0.0. Features marked as "Planned" will be available in future releases.*

**Happy coding in Kaynat!**

