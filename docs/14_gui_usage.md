# GUI Programming Usage Guide

## Building Desktop Applications with Kaynat

**Status:** Planned for v3.0.0 - Syntax designed, implementation pending

---

## Overview

Kaynat will support desktop GUI applications with:
- Windows and dialogs
- Buttons, labels, inputs
- Event handling
- Layouts
- Menus
- Canvas drawing
- Themes

---

## Your First GUI App

### Hello World Window

```kaynat
use gui tools.

create a window called main window.
set the title of main window to Hello Kaynat.
set the width of main window to 400.
set the height of main window to 300.

create a label called greeting.
set the text of greeting to Hello, World.
place greeting at row 0 and column 0 in main window.

show main window.
```

**What this does:**
- Creates a 400x300 window
- Adds a label with "Hello, World"
- Displays the window

---

## Widgets

### Labels

```kaynat
use gui tools.

create a window called main window.

create a label called title.
set the text of title to Welcome to Kaynat.
set the font of title to Arial 20 bold.
set the color of title to navy.
place title at row 0 and column 0 in main window.

show main window.
```

### Buttons

```kaynat
use gui tools.

create a window called main window.

create a button called click me.
set the text of click me to Click Me.
place click me at row 0 and column 0 in main window.

define a function called on button click.
    say Button was clicked.
end.

when click me is clicked, call on button click.

show main window.
```

### Text Inputs

```kaynat
use gui tools.

create a window called main window.

create a label called name label.
set the text of name label to Enter your name.
place name label at row 0 and column 0 in main window.

create a text input called name input.
set the placeholder of name input to Your name here.
place name input at row 0 and column 1 in main window.

create a button called submit.
set the text of submit to Submit.
place submit at row 1 and column 0 in main window.

define a function called on submit.
    read text from name input and store as user name.
    say Hello, user name.
end.

when submit is clicked, call on submit.

show main window.
```

---

## Complete Examples

### Example 1: Counter App

```kaynat
use gui tools.

create a window called counter window.
set the title of counter window to Counter App.
set the width of counter window to 300.
set the height of counter window to 200.

set count to 0.

create a label called counter label.
set the text of counter label to Count 0.
set the font of counter label to Arial 24 bold.
place counter label at row 0 and column 0 in counter window.

create a button called increment button.
set the text of increment button to Increment.
place increment button at row 1 and column 0 in counter window.

create a button called decrement button.
set the text of decrement button to Decrement.
place decrement button at row 2 and column 0 in counter window.

create a button called reset button.
set the text of reset button to Reset.
place reset button at row 3 and column 0 in counter window.

define a function called update display.
    set the text of counter label to Count, count.
end.

define a function called on increment.
    add 1 to count.
    call update display.
end.

define a function called on decrement.
    subtract 1 from count.
    call update display.
end.

define a function called on reset.
    set count to 0.
    call update display.
end.

when increment button is clicked, call on increment.
when decrement button is clicked, call on decrement.
when reset button is clicked, call on reset.

show counter window.
```

### Example 2: To-Do List App

```kaynat
use gui tools.

create a window called todo window.
set the title of todo window to My To Do List.
set the width of todo window to 500.
set the height of todo window to 600.

create a list called tasks.

create a label called title.
set the text of title to To Do List.
set the font of title to Arial 24 bold.
place title at row 0 and column 0 in todo window.

create a text input called task input.
set the placeholder of task input to Enter a task.
place task input at row 1 and column 0 in todo window.

create a button called add button.
set the text of add button to Add Task.
place add button at row 1 and column 1 in todo window.

create a text area called task display.
set the width of task display to 40.
set the height of task display to 20.
place task display at row 2 and column 0 in todo window.

define a function called update display.
    set display text to empty.
    set counter to 1.
    
    for each task in tasks.
        set line to counter.
        note. Would concatenate here.
        add 1 to counter.
    end.
    
    set the text of task display to display text.
end.

define a function called add task.
    read text from task input and store as new task.
    
    if new task is empty then.
        show an error saying Please enter a task.
        stop.
    end.
    
    append new task to tasks.
    call update display.
    set the text of task input to empty.
end.

when add button is clicked, call add task.

show todo window.
```

### Example 3: Calculator App

```kaynat
use gui tools.

create a window called calc window.
set the title of calc window to Calculator.
set the width of calc window to 400.
set the height of calc window to 500.

create a label called display.
set the text of display to 0.
set the font of display to Arial 32 bold.
place display at row 0 and column 0 in calc window.

create a text input called num1 input.
set the placeholder of num1 input to First number.
place num1 input at row 1 and column 0 in calc window.

create a text input called num2 input.
set the placeholder of num2 input to Second number.
place num2 input at row 2 and column 0 in calc window.

create a button called add button.
set the text of add button to Add.
place add button at row 3 and column 0 in calc window.

create a button called subtract button.
set the text of subtract button to Subtract.
place subtract button at row 3 and column 1 in calc window.

define a function called do add.
    read text from num1 input and store as num1.
    read text from num2 input and store as num2.
    
    set result to num1.
    add num2 to result.
    
    set the text of display to result.
end.

define a function called do subtract.
    read text from num1 input and store as num1.
    read text from num2 input and store as num2.
    
    set result to num1.
    subtract num2 from result.
    
    set the text of display to result.
end.

when add button is clicked, call do add.
when subtract button is clicked, call do subtract.

show calc window.
```

### Example 4: Login Form

```kaynat
use gui tools.

create a window called login window.
set the title of login window to Login.
set the width of login window to 400.
set the height of login window to 300.

create a label called title.
set the text of title to Please Login.
set the font of title to Arial 20 bold.
place title at row 0 and column 0 in login window.

create a label called username label.
set the text of username label to Username.
place username label at row 1 and column 0 in login window.

create a text input called username input.
place username input at row 1 and column 1 in login window.

create a label called password label.
set the text of password label to Password.
place password label at row 2 and column 0 in login window.

create a text input called password input.
set the password mode of password input to true.
place password input at row 2 and column 1 in login window.

create a button called login button.
set the text of login button to Login.
place login button at row 3 and column 0 in login window.

define a function called do login.
    read text from username input and store as username.
    read text from password input and store as password.
    
    if username is empty then.
        show an error saying Please enter username.
        stop.
    end.
    
    if password is empty then.
        show an error saying Please enter password.
        stop.
    end.
    
    show a message saying Login successful.
    close login window.
end.

when login button is clicked, call do login.

show login window.
```

---

## Dialogs

### Message Dialogs

```kaynat
use gui tools.

show a message saying Operation completed successfully.

show an error saying An error occurred.

show a warning saying This action cannot be undone.
```

### Confirmation Dialog

```kaynat
use gui tools.

ask the user to confirm with message Are you sure and store as confirmed.

if confirmed is true then.
    say User confirmed.
otherwise.
    say User cancelled.
end.
```

### File Dialogs

```kaynat
use gui tools.

ask the user to choose a file and store as file path.
say Selected file, file path.

ask the user to choose a folder and store as folder path.
say Selected folder, folder path.

ask the user to save a file and store as save path.
say Save to, save path.
```

---

## Menus

### Creating Menus

```kaynat
use gui tools.

create a window called main window.

create a menu bar called app menu.

add menu called File to app menu.
add item called New to File menu with action on new.
add item called Open to File menu with action on open.
add item called Save to File menu with action on save.
add separator to File menu.
add item called Exit to File menu with action on exit.

add menu called Edit to app menu.
add item called Copy to Edit menu with action on copy.
add item called Paste to Edit menu with action on paste.

attach app menu to main window.

define a function called on new.
    say New file.
end.

define a function called on open.
    ask the user to choose a file and store as file path.
    say Opening, file path.
end.

define a function called on save.
    say Saving file.
end.

define a function called on exit.
    close main window.
end.

show main window.
```

---

## Implementation Status

**Current Status:** NOT IMPLEMENTED

GUI features are designed but not yet implemented.

**Planned for:** Version 3.0.0

---

*This guide describes planned features for Kaynat v3.0.0.*

