# GUI Programming in Kaynat

## Status: PLANNED FOR FUTURE RELEASE

This document describes the planned GUI features for Kaynat. These features are not yet implemented in version 1.0.0.

---

## Overview

Kaynat will support desktop GUI application development with:
- Windows and dialogs
- Widgets (buttons, labels, inputs, etc.)
- Layout management
- Event handling
- Canvas for drawing
- Menus and toolbars
- Themes

---

## Creating Windows

### Basic Window

```kaynat
create a window called main window.
set the title of main window to My Kaynat App.
set the width of main window to 800.
set the height of main window to 600.
set the background of main window to white.
show main window.
```

---

## Widgets

### Label

```kaynat
create a label called greeting label.
set the text of greeting label to Hello, Kaynat.
set the font of greeting label to Arial 18 bold.
set the color of greeting label to navy.
place greeting label at row 0 and column 0 in main window.
```

### Button

```kaynat
create a button called submit button.
set the text of submit button to Submit.
set the action of submit button to the function called on submit.
place submit button at row 1 and column 0 in main window.
```

### Text Input

```kaynat
create a text input called name input.
set the placeholder of name input to Enter your name.
place name input at row 0 and column 1 in main window.
```

### Text Area

```kaynat
create a text area called notes area.
set the width of notes area to 40.
set the height of notes area to 10.
place notes area at row 1 and column 1 in main window.
```

### Checkbox

```kaynat
create a checkbox called accept terms.
set the label of accept terms to I accept the terms.
place accept terms at row 2 and column 0 in main window.
```

### Dropdown

```kaynat
create a dropdown called color picker.
set the options of color picker to red, green, blue, yellow.
place color picker at row 2 and column 1 in main window.
```

### Radio Buttons

```kaynat
create a radio group called gender.
set the options of gender to male, female, other.
place gender at row 3 and column 0 in main window.
```

### Slider

```kaynat
create a slider called volume slider.
set the minimum of volume slider to 0.
set the maximum of volume slider to 100.
place volume slider at row 3 and column 1 in main window.
```

### Progress Bar

```kaynat
create a progress bar called loading bar.
set the maximum of loading bar to 100.
place loading bar at row 4 and column 0 in main window.
```

### Image

```kaynat
create an image called logo.
set the source of logo to logo.png.
place logo at row 4 and column 1 in main window.
```

---

## Layout Management

### Grid Layout

```kaynat
use grid layout for main window.
```

### Stack Layout

```kaynat
use stack layout for main window.
```

### Flow Layout

```kaynat
use flow layout for main window.
```

### Padding and Alignment

```kaynat
set padding of name input to 10 horizontal and 5 vertical.
set the sticky alignment of greeting label to left.
span greeting label across 2 columns.
```

---

## Event Handling

### Button Click

```kaynat
define a function called on submit, do.
    read text from name input and store as entered name.
    set the text of greeting label to hello, entered name.
end.

when submit button is clicked, call on submit.
```

### Text Change

```kaynat
define a function called validate input, do.
    read text from name input and store as text.
    if length of text is less than 3 then.
        set the color of name input to red.
    otherwise.
        set the color of name input to green.
    end.
end.

when name input text changes, call validate input.
```

### Window Close

```kaynat
define a function called on close, do.
    say Goodbye.
end.

when main window is closed, call on close.
```

### Slider Change

```kaynat
define a function called update volume, do.
    read value from volume slider and store as volume.
    say Volume is, volume.
end.

when volume slider value changes, call update volume.
```

---

## Dialogs and Popups

### Message Dialog

```kaynat
show a message saying file saved successfully.
```

### Error Dialog

```kaynat
show an error saying please fill in all fields.
```

### Warning Dialog

```kaynat
show a warning saying this action cannot be undone.
```

### Confirmation Dialog

```kaynat
ask the user to confirm with message are you sure you want to delete this, and store as confirmed.

if confirmed is true then.
    say Deleting.
end.
```

### File Dialogs

```kaynat
ask the user to choose a file and store as file path.
ask the user to choose a folder and store as folder path.
ask the user to save a file and store as save path.
```

---

## Menus

### Menu Bar

```kaynat
create a menu bar called app menu.

add menu called file to app menu.
add item called open to file menu with action on open.
add item called save to file menu with action on save.
add separator to file menu.
add item called exit to file menu with action on exit.

add menu called edit to app menu.
add item called copy to edit menu with action on copy.
add item called paste to edit menu with action on paste.

attach app menu to main window.
```

---

## Canvas and Drawing

### Creating a Canvas

```kaynat
create a canvas called drawing board.
set the width of drawing board to 600.
set the height of drawing board to 400.
place drawing board in main window.
```

### Drawing Shapes

```kaynat
draw a line from 0, 0 to 100, 100 on drawing board with color black.
draw a rectangle from 50, 50 to 200, 150 on drawing board with fill blue.
draw a circle at 300, 200 with radius 50 on drawing board with fill red.
draw text hello at 100, 100 on drawing board with font Arial 14.
```

### Clearing Canvas

```kaynat
clear drawing board.
```

---

## Multi-Window Applications

### Opening New Windows

```kaynat
create a window called settings window.
set the title of settings window to Settings.
open settings window.
```

### Window Management

```kaynat
close settings window.
minimize main window.
maximize main window.
bring main window to front.
```

---

## Themes

### Applying Themes

```kaynat
apply theme dark to main window.
apply theme light to main window.
```

### Custom Styling

```kaynat
set global font to Arial 12.
set global accent color to navy.
```

---

## Complete Example: To-Do List App

```kaynat
begin program.

create a window called todo window.
set the title of todo window to My To Do List.
set the width of todo window to 400.
set the height of todo window to 500.

create a label called title label.
set the text of title label to To Do List.
set the font of title label to Arial 20 bold.
place title label at row 0 and column 0 in todo window.

create a text input called task input.
set the placeholder of task input to Enter a task.
place task input at row 1 and column 0 in todo window.

create a button called add button.
set the text of add button to Add Task.
place add button at row 1 and column 1 in todo window.

create a text area called task list.
set the width of task list to 40.
set the height of task list to 20.
place task list at row 2 and column 0 in todo window.

create a list called tasks.

define a function called add task, do.
    read text from task input and store as new task.
    
    if new task is empty then.
        show an error saying please enter a task.
        stop.
    end.
    
    add new task to tasks.
    
    set display to empty.
    for each task in tasks.
        join display and task with newline and store as display.
    end.
    
    set the text of task list to display.
    set the text of task input to empty.
end.

when add button is clicked, call add task.

show todo window.

end program.
```

---

## Implementation Status

**Current Status:** NOT IMPLEMENTED

**Planned for:** Version 3.0.0

**Required Components:**
- GUI framework integration (tkinter)
- Widget system
- Event loop
- Layout engine
- Drawing API
- Theme system

---

## Learning Path

1. **Start with:** Simple window and label
2. **Then add:** Buttons and event handling
3. **Move to:** Input widgets and forms
4. **Advanced:** Canvas drawing
5. **Master:** Multi-window applications

---

*This documentation describes planned features. Check PROJECT_STATUS.md for current implementation status.*
