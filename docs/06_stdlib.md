# Kaynat Standard Library Reference

## Status: PLANNED FOR FUTURE RELEASE

This document describes the planned standard library for Kaynat. Most modules are not yet implemented in version 1.0.0.

---

## Overview

The Kaynat standard library will provide:
- Math operations
- String manipulation
- List operations
- File I/O
- Date and time
- Random numbers
- Networking
- JSON handling
- Pattern matching
- Encryption

---

## Math Module

### Constants

```kaynat
say pi.
say e.
```

### Basic Operations

```kaynat
find the square root of 144 and store as result.
find the absolute value of negative 42 and store as result.
round 3.7 to 0 decimal places and store as result.
find the ceiling of 4.2 and store as result.
find the floor of 4.8 and store as result.
```

### Power and Logarithm

```kaynat
raise 2 to the power 10 and store as result.
find the logarithm of 1000 in base 10 and store as result.
find the natural logarithm of 100 and store as result.
```

### Trigonometry

```kaynat
find the sine of 90 and store as result.
find the cosine of 0 and store as result.
find the tangent of 45 and store as result.
find the arcsine of 0.5 and store as result.
find the arccosine of 0.5 and store as result.
find the arctangent of 1 and store as result.
```

### Advanced

```kaynat
find the factorial of 5 and store as result.
find the greatest common divisor of 48 and 18 and store as result.
find the least common multiple of 12 and 18 and store as result.
```

---

## String Module

### Case Conversion

```kaynat
convert name to uppercase and store as upper.
convert name to lowercase and store as lower.
convert name to title case and store as title.
```

### Trimming

```kaynat
trim whitespace from input and store as clean.
trim left whitespace from input and store as clean.
trim right whitespace from input and store as clean.
```

### Searching

```kaynat
check if title starts with Hello.
check if filename ends with txt.
check if description contains error.
find the position of world in greeting and store as index.
```

### Manipulation

```kaynat
replace comma with period in sentence and store as fixed.
split sentence by space and store as words.
join words with comma and store as csv.
take characters from 0 to 5 in name and store as short name.
reverse the string message and store as reversed.
repeat star 10 times and store as border.
```

### Information

```kaynat
find the length of message and store as len.
check if text is empty.
check if text is numeric.
check if text is alphabetic.
```

---

## List Module

### Adding and Removing

```kaynat
add item to list.
add item to the front of list.
insert item at position 2 in list.
remove item from list.
remove item at position 0 from list.
```

### Accessing

```kaynat
get item at position 1 in list and store as first.
get the first item in list and store as first.
get the last item in list and store as last.
```

### Information

```kaynat
find the length of list and store as size.
check if list is empty.
check if list contains item.
find the position of item in list and store as index.
```

### Sorting and Reversing

```kaynat
sort list ascending.
sort list descending.
reverse list.
shuffle list.
```

### Functional Operations

```kaynat
filter list where item is greater than 10 and store as filtered.
map list using uppercase and store as upper list.
reduce list using sum and store as total.
```

### Copying and Combining

```kaynat
copy list and store as backup.
join list one and list two and store as combined.
flatten nested list and store as flat.
```

---

## File Module

### Reading

```kaynat
read the file called data.txt and store as content.
read the file called log.txt line by line and store as lines.
check if the file called config.txt exists.
```

### Writing

```kaynat
write hello world to the file called output.txt.
append new entry to the file called log.txt.
```

### File Operations

```kaynat
delete the file called temp.txt.
copy the file called source.txt to dest.txt.
move the file called old.txt to new.txt.
rename the file called old.txt to new.txt.
```

### Directory Operations

```kaynat
create a folder called data.
delete the folder called temp.
list files in the folder called data and store as files.
check if the folder called data exists.
```

---

## Date and Time Module

### Current Date and Time

```kaynat
get the current date and store as today.
get the current time and store as now.
get the current timestamp and store as timestamp.
```

### Formatting

```kaynat
format date as YYYY-MM-DD and store as formatted.
format time as HH:MM:SS and store as formatted.
```

### Parsing

```kaynat
parse 2024-12-25 as date and store as christmas.
```

### Arithmetic

```kaynat
add 7 days to today and store as next week.
subtract 1 month from today and store as last month.
find the difference between date one and date two in days and store as diff.
```

### Components

```kaynat
get the year from date and store as year.
get the month from date and store as month.
get the day from date and store as day.
get the hour from time and store as hour.
get the minute from time and store as minute.
```

---

## Random Module

### Numbers

```kaynat
generate a random integer from 1 to 100 and store as num.
generate a random float from 0 to 1 and store as num.
generate a random boolean and store as flag.
```

### Lists

```kaynat
choose a random item from list and store as item.
shuffle list.
```

### Strings

```kaynat
generate a random string of length 10 and store as code.
generate a random password of length 16 and store as password.
```

---

## Network Module

### HTTP Requests

```kaynat
fetch https://api.example.com/data with GET and store as response.
fetch https://api.example.com/submit with POST and data payload and store as response.
```

### Response Handling

```kaynat
get the status code from response and store as status.
get the body from response and store as body.
get the headers from response and store as headers.
```

### URL Operations

```kaynat
check if https://example.com is reachable.
parse url https://example.com/path and store as parts.
```

---

## JSON Module

### Parsing

```kaynat
parse json from string and store as data.
```

### Generation

```kaynat
generate json from map and store as json string.
format json with indentation 2 and store as pretty json.
```

### Validation

```kaynat
check if string is valid json.
```

---

## Pattern Module

### Regular Expressions

```kaynat
find all matches of pattern in text and store as matches.
check if text matches pattern.
replace pattern with replacement in text and store as result.
split text by pattern and store as parts.
```

### Common Patterns

```kaynat
check if email is valid.
check if phone number is valid.
check if url is valid.
extract all emails from text and store as emails.
extract all urls from text and store as urls.
```

---

## Crypto Module

### Hashing

```kaynat
hash password using sha256 and store as hashed.
hash data using md5 and store as hashed.
```

### Random

```kaynat
generate a random secure token of length 32 and store as token.
generate a random uuid and store as id.
```

### Encoding

```kaynat
encode text to base64 and store as encoded.
decode base64 from encoded and store as text.
```

---

## Implementation Status

**Current Status:** MOSTLY NOT IMPLEMENTED

**Implemented:**
- Math constants (pi, e)

**Planned for:** Version 2.0.0 - 3.0.0

---

## Usage Example

```kaynat
begin program.

say Math operations.
find the square root of 144 and store as result.
say Square root of 144 is, result.

say String operations.
set name to kaynat.
convert name to uppercase and store as upper.
say Uppercase is, upper.

say File operations.
write Hello, World to the file called test.txt.
read the file called test.txt and store as content.
say File content is, content.

end program.
```

---

*This documentation describes planned features. Check PROJECT_STATUS.md for current implementation status.*
