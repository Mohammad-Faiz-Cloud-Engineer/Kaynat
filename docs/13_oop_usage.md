# Object-Oriented Programming Usage Guide

## Practical Guide to OOP in Kaynat

**Status:** Planned for v2.0.0 - Syntax designed, implementation pending

---

## Overview

Kaynat supports object-oriented programming with:
- Blueprints (classes)
- Properties (attributes)
- Methods (functions)
- Inheritance
- Encapsulation
- Polymorphism

---

## Defining Blueprints (Classes)

### Basic Blueprint

```kaynat
define a blueprint called Person.
    
    note. Properties.
    add property called name.
    add property called age.
    
    note. Methods.
    define method called introduce.
        say Hello, I am, name.
        say I am, age, years old.
    end.
    
end blueprint.
```

### Creating Instances

```kaynat
note. Create an object.
create a Person called alice.

note. Set properties.
set name of alice to Alice.
set age of alice to 25.

note. Call methods.
call introduce on alice.
```

---

## Properties

### Setting and Getting Properties

```kaynat
define a blueprint called Car.
    add property called brand.
    add property called model.
    add property called year.
end blueprint.

create a Car called my car.

set brand of my car to Toyota.
set model of my car to Camry.
set year of my car to 2024.

get brand of my car and store as car brand.
say Car brand is, car brand.
```

### Private Properties

```kaynat
define a blueprint called BankAccount.
    add property called account number.
    add private property called balance.
    
    define method called deposit that takes amount.
        add amount to balance.
        say Deposited, amount.
    end.
    
    define method called get balance.
        give back balance.
    end.
end blueprint.

create a BankAccount called my account.
set account number of my account to 12345.

call deposit on my account with 1000.
call get balance on my account and store as current balance.
say Balance is, current balance.
```

---

## Methods

### Methods with Parameters

```kaynat
define a blueprint called Calculator.
    
    define method called add that takes a, b.
        set result to a.
        add b to result.
        give back result.
    end.
    
    define method called multiply that takes a, b.
        set result to 0.
        set counter to 0.
        repeat b times.
            add a to result.
        end.
        give back result.
    end.
    
end blueprint.

create a Calculator called calc.

call add on calc with 5, 3 and store as sum.
say Sum is, sum.

call multiply on calc with 4, 3 and store as product.
say Product is, product.
```

---

## Inheritance

### Basic Inheritance

```kaynat
define a blueprint called Animal.
    add property called name.
    add property called age.
    
    define method called speak.
        say name, makes a sound.
    end.
end blueprint.

define a blueprint called Dog that extends Animal.
    add property called breed.
    
    define method called bark.
        say name, says woof.
    end.
end blueprint.

create a Dog called buddy.
set name of buddy to Buddy.
set age of buddy to 3.
set breed of buddy to Golden Retriever.

call speak on buddy.
call bark on buddy.
```

### Overriding Methods

```kaynat
define a blueprint called Shape.
    define method called area.
        say Calculating area.
        give back 0.
    end.
end blueprint.

define a blueprint called Rectangle that extends Shape.
    add property called width.
    add property called height.
    
    define method called area.
        set result to width.
        set counter to 1.
        while counter is less than height then.
            add width to result.
            add 1 to counter.
        end.
        give back result.
    end.
end blueprint.

create a Rectangle called rect.
set width of rect to 5.
set height of rect to 3.

call area on rect and store as rect area.
say Rectangle area is, rect area.
```

---

## Complete Examples

### Example 1: Student Management

```kaynat
define a blueprint called Student.
    add property called name.
    add property called id.
    add property called grades.
    
    define method called add grade that takes grade.
        append grade to grades.
        say Grade added.
    end.
    
    define method called average.
        set total to 0.
        set count to 0.
        
        for each grade in grades.
            add grade to total.
            add 1 to count.
        end.
        
        set avg to total.
        note. Would divide here if we had division.
        give back avg.
    end.
    
    define method called display.
        say Student, name.
        say ID, id.
        say Grades, grades.
    end.
end blueprint.

create a Student called alice.
set name of alice to Alice.
set id of alice to 12345.
create a list called alice grades.
set grades of alice to alice grades.

call add grade on alice with 85.
call add grade on alice with 92.
call add grade on alice with 88.

call display on alice.
```

### Example 2: Library System

```kaynat
define a blueprint called Book.
    add property called title.
    add property called author.
    add property called isbn.
    add property called available.
    
    define method called borrow.
        if available is true then.
            set available to false.
            say Book borrowed, title.
        otherwise.
            say Book not available.
        end.
    end.
    
    define method called return book.
        set available to true.
        say Book returned, title.
    end.
    
    define method called info.
        say Title, title.
        say Author, author.
        say ISBN, isbn.
        if available is true then.
            say Status Available.
        otherwise.
            say Status Borrowed.
        end.
    end.
end blueprint.

create a Book called book1.
set title of book1 to The Great Gatsby.
set author of book1 to F Scott Fitzgerald.
set isbn of book1 to 9780743273565.
set available of book1 to true.

call info on book1.
call borrow on book1.
call info on book1.
call return book on book1.
```

### Example 3: E-commerce Product

```kaynat
define a blueprint called Product.
    add property called name.
    add property called price.
    add property called stock.
    
    define method called display.
        say Product, name.
        say Price, price.
        say Stock, stock.
    end.
    
    define method called purchase that takes quantity.
        if quantity is greater than stock then.
            say Not enough stock.
            give back false.
        end.
        
        subtract quantity from stock.
        say Purchased, quantity, units.
        give back true.
    end.
    
    define method called restock that takes quantity.
        add quantity to stock.
        say Restocked, quantity, units.
    end.
end blueprint.

create a Product called laptop.
set name of laptop to Gaming Laptop.
set price of laptop to 1200.
set stock of laptop to 10.

call display on laptop.
call purchase on laptop with 3 and store as success.
call display on laptop.
call restock on laptop with 5.
call display on laptop.
```

---

## Best Practices

### 1. Use Descriptive Blueprint Names

```kaynat
note. Good.
define a blueprint called UserAccount.
define a blueprint called ShoppingCart.

note. Bad.
define a blueprint called UA.
define a blueprint called SC.
```

### 2. Group Related Properties

```kaynat
define a blueprint called Person.
    note. Personal info.
    add property called name.
    add property called age.
    
    note. Contact info.
    add property called email.
    add property called phone.
end blueprint.
```

### 3. Use Methods for Actions

```kaynat
define a blueprint called Counter.
    add property called value.
    
    define method called increment.
        add 1 to value.
    end.
    
    define method called decrement.
        subtract 1 from value.
    end.
    
    define method called reset.
        set value to 0.
    end.
end blueprint.
```

---

## Implementation Status

**Current Status:** NOT IMPLEMENTED

OOP features are designed but not yet implemented.

**Planned for:** Version 2.0.0

---

*This guide describes planned features for Kaynat v2.0.0.*

