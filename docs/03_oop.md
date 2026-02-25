# Object-Oriented Programming in Kaynat

## Status: PLANNED FOR FUTURE RELEASE

This document describes the planned OOP features for Kaynat. These features are not yet implemented in version 1.0.0.

---

## Overview

Kaynat will support full object-oriented programming with:
- Blueprints (classes)
- Properties and methods
- Inheritance
- Encapsulation
- Polymorphism
- Abstract blueprints
- Contracts (interfaces)

---

## Blueprints (Classes)

### Basic Blueprint

```kaynat
define a blueprint called animal.
    it has name.
    it has sound.
    it has age.
    
    to initialize, take name, sound, and age.
        set my name to name.
        set my sound to sound.
        set my age to age.
    end.
    
    to speak, do.
        say my name, says, my sound.
    end.
    
    to describe, do.
        say my name, is, my age, years old.
    end.
end.
```

### Creating Instances

```kaynat
create a new animal with Whiskers, meow, and 3, and store as cat.
call speak on cat.
call describe on cat.
```

**Expected Output:**
```
whiskers says meow
whiskers is 3 years old
```

---

## Inheritance

### Extending Blueprints

```kaynat
define a blueprint called dog that extends animal.
    to initialize, take name and age.
        call parent initialize with name, woof, and age.
    end.
    
    to fetch, do.
        say my name, fetches the ball.
    end.
    
    to speak, do.
        say my name, barks loudly.
    end.
end.
```

### Using Inherited Blueprints

```kaynat
create a new dog with Rex and 5, and store as rex.
call speak on rex.
call fetch on rex.
call describe on rex.
```

---

## Encapsulation

### Private Properties

```kaynat
define a blueprint called bankaccount.
    it has private balance.
    it has owner.
    
    to initialize, take owner and starting balance.
        set my owner to owner.
        set my private balance to starting balance.
    end.
    
    to deposit, take amount.
        if amount is less than or equal to 0 then.
            raise an error saying deposit amount must be positive.
        end.
        add amount to my private balance.
    end.
    
    to withdraw, take amount.
        if amount is greater than my private balance then.
            raise an error saying insufficient funds.
        end.
        subtract amount from my private balance.
    end.
    
    to get balance, do.
        give back my private balance.
    end.
end.
```

---

## Polymorphism

### Using Different Types Uniformly

```kaynat
define a list called animals.
add cat to animals.
add rex to animals.

for each creature in animals.
    call speak on creature.
end.
```

**Expected Output:**
```
whiskers says meow
rex barks loudly
```

---

## Abstract Blueprints

### Defining Abstract Blueprints

```kaynat
define an abstract blueprint called shape.
    to calculate area, do.
        this must be implemented.
    end.
end.

define a blueprint called circle that extends shape.
    it has radius.
    
    to initialize, take radius.
        set my radius to radius.
    end.
    
    to calculate area, do.
        give back pi multiplied by my radius multiplied by my radius.
    end.
end.
```

---

## Contracts (Interfaces)

### Defining Contracts

```kaynat
define a contract called printable.
    it requires a function called print details.
end.

define a blueprint called invoice that follows printable.
    it has amount.
    
    to initialize, take amount.
        set my amount to amount.
    end.
    
    to print details, do.
        say invoice amount is my amount.
    end.
end.
```

---

## Static Members

### Shared Properties and Methods

```kaynat
define a blueprint called counter.
    it has shared count starting at 0.
    
    to increment, do.
        add 1 to shared count.
    end.
    
    to get count, do.
        give back shared count.
    end.
end.
```

---

## Operator Overloading

### Custom Operators

```kaynat
define a blueprint called vector.
    it has x.
    it has y.
    
    to initialize, take x and y.
        set my x to x.
        set my y to y.
    end.
    
    to add with other, do.
        give back a new vector with my x plus other x and my y plus other y.
    end.
    
    to describe, do.
        say vector, my x, my y.
    end.
end.
```

---

## Complete Example: Student Management System

```kaynat
begin program.

define a blueprint called student.
    it has name.
    it has id.
    it has private grades.
    
    to initialize, take name and id.
        set my name to name.
        set my id to id.
        create a list called my private grades.
    end.
    
    to add grade, take grade.
        add grade to my private grades.
    end.
    
    to calculate average, do.
        set total to 0.
        set count to 0.
        
        for each grade in my private grades.
            add grade to total.
            add 1 to count.
        end.
        
        if count is equal to 0 then.
            give back 0.
        end.
        
        give back total divided by count.
    end.
    
    to print report, do.
        say Student, my name.
        say ID, my id.
        say Average, the result of calling calculate average.
    end.
end.

create a new student with Alice and 1001, and store as alice.
call add grade on alice with 85.
call add grade on alice with 90.
call add grade on alice with 88.
call print report on alice.

end program.
```

---

## Implementation Status

**Current Status:** NOT IMPLEMENTED

**Planned for:** Version 2.0.0

**Required Components:**
- Blueprint parser
- Instance management system
- Method dispatch
- Inheritance chain
- Access control (private/public)
- Abstract class validation
- Interface checking

---

## When Will This Be Available?

OOP features are planned for a future release. The core language (v1.0.0) focuses on:
- Variables and functions
- Control flow
- Basic data structures

OOP will be added in version 2.0.0 once the core is stable and well-tested.

---

*This documentation describes planned features. Check PROJECT_STATUS.md for current implementation status.*
