# Standard Library Usage Guide

## How to Use Kaynat's Built-in Functions

**Status:** Planned for v2.0.0 - Syntax designed, implementation pending

---

## Overview

Kaynat's standard library provides ready-to-use functions for common tasks:
- Math operations
- String manipulation
- List operations
- File I/O
- Date and time
- Random numbers
- Networking
- JSON handling
- Cryptography
- Pattern matching

---

## Math Tools

### Basic Operations

```kaynat
use math tools.

note. Square root.
set num to 16.
set root to the square root of num.
say Square root of 16 is, root.

note. Absolute value.
set negative to minus 10.
set positive to the absolute value of negative.
say Absolute value is, positive.

note. Rounding.
set decimal to 3.7.
set rounded to round decimal to 0 decimals.
say Rounded is, rounded.

note. Ceiling and floor.
set up to ceiling of 3.2.
set down to floor of 3.8.
say Ceiling is, up.
say Floor is, down.
```

### Power and Logarithms

```kaynat
use math tools.

note. Power.
set base to 2.
set exponent to 8.
set result to base raised to the power of exponent.
say 2 to the power of 8 is, result.

note. Logarithm.
set num to 100.
set log to the logarithm of num with base 10.
say Log base 10 of 100 is, log.

note. Natural logarithm.
set natural log to the natural logarithm of num.
say Natural log is, natural log.
```

### Trigonometry

```kaynat
use math tools.

note. Angles in degrees.
set angle to 45.

set sine to the sine of angle.
set cosine to the cosine of angle.
set tangent to the tangent of angle.

say Sine of 45 degrees is, sine.
say Cosine of 45 degrees is, cosine.
say Tangent of 45 degrees is, tangent.

note. Inverse trig functions.
set value to 0.5.
set arcsine to the arcsine of value.
say Arcsine of 0.5 is, arcsine, degrees.
```

### Advanced Math

```kaynat
use math tools.

note. Factorial.
set num to 5.
set fact to the factorial of num.
say 5 factorial is, fact.

note. GCD and LCM.
set a to 12.
set b to 18.
set gcd to the greatest common divisor of a and b.
set lcm to the least common multiple of a and b.
say GCD is, gcd.
say LCM is, lcm.

note. Prime check.
set num to 17.
if num is prime then.
    say num, is prime.
otherwise.
    say num, is not prime.
end.

note. Min and max.
set minimum to the minimum of 5, 3, 8, 1, 9.
set maximum to the maximum of 5, 3, 8, 1, 9.
say Minimum is, minimum.
say Maximum is, maximum.
```

### Constants

```kaynat
use math tools.

say Pi is, pi.
say E is, e.
say Tau is, tau.
say Infinity is, infinity.
```

---

## String Tools

### Case Conversion

```kaynat
use string tools.

set text to hello world.

set upper to text in uppercase.
say upper.

set lower to text in lowercase.
say lower.

set title to text in titlecase.
say title.
```

### Trimming

```kaynat
use string tools.

set text to   hello world   .

set trimmed to trim text.
say trimmed.

set left trimmed to trim left side of text.
say left trimmed.

set right trimmed to trim right side of text.
say right trimmed.
```

### Searching

```kaynat
use string tools.

set text to hello world.

if text starts with hello then.
    say Text starts with hello.
end.

if text ends with world then.
    say Text ends with world.
end.

if text contains world then.
    say Text contains world.
end.

set position to find world in text.
say Position is, position.
```

### Manipulation

```kaynat
use string tools.

set text to hello world.

note. Replace.
set replaced to replace world with kaynat in text.
say replaced.

note. Split.
set words to split text by space.
for each word in words.
    say word.
end.

note. Join.
set joined to join words with dash.
say joined.

note. Substring.
set sub to substring of text from 0 to 5.
say sub.

note. Reverse.
set reversed to reverse text.
say reversed.

note. Repeat.
set repeated to repeat text 3 times.
say repeated.
```

### Information

```kaynat
use string tools.

set text to hello.

set length to the length of text.
say Length is, length.

if text is empty then.
    say Text is empty.
end.

if text is numeric then.
    say Text is numeric.
end.

if text is alphabetic then.
    say Text is alphabetic.
end.
```

### Padding

```kaynat
use string tools.

set text to hello.

set left padded to pad text on left to 10 characters with space.
say left padded.

set right padded to pad text on right to 10 characters with space.
say right padded.

set centered to center text in 10 characters.
say centered.
```

---

## List Tools

### Adding Elements

```kaynat
use list tools.

create a list called numbers.

append 10 to numbers.
append 20 to numbers.
append 30 to numbers.

prepend 5 to numbers.

insert 15 at position 2 in numbers.

say numbers.
```

### Removing Elements

```kaynat
use list tools.

set numbers to a list containing 10, 20, 30, 40, 50.

remove 30 from numbers.
remove element at position 0 from numbers.

say numbers.
```

### Accessing Elements

```kaynat
use list tools.

set numbers to a list containing 10, 20, 30, 40, 50.

get element at position 2 from numbers and store as element.
say Element is, element.

get slice from 1 to 3 of numbers and store as slice.
say Slice is, slice.
```

### Information

```kaynat
use list tools.

set numbers to a list containing 10, 20, 30, 40, 50.

set length to the length of numbers.
say Length is, length.

if numbers is empty then.
    say List is empty.
end.

if numbers contains 30 then.
    say List contains 30.
end.

set index to the index of 30 in numbers.
say Index is, index.

set count to count of 30 in numbers.
say Count is, count.
```

### Sorting and Reversing

```kaynat
use list tools.

set numbers to a list containing 50, 20, 40, 10, 30.

sort numbers.
say Sorted, numbers.

reverse numbers.
say Reversed, numbers.
```

### Copying and Clearing

```kaynat
use list tools.

set original to a list containing 10, 20, 30.

copy original and store as duplicate.
say Duplicate, duplicate.

clear original.
say Original is now empty.
```

### Aggregation

```kaynat
use list tools.

set numbers to a list containing 10, 20, 30, 40, 50.

set minimum to the minimum of numbers.
set maximum to the maximum of numbers.
set sum to the sum of numbers.
set average to the average of numbers.

say Minimum is, minimum.
say Maximum is, maximum.
say Sum is, sum.
say Average is, average.
```

---

## File Tools

### Reading Files

```kaynat
use file tools.

note. Read entire file.
read from file called data.txt and store as content.
say content.

note. Read lines.
read lines from file called data.txt and store as lines.
for each line in lines.
    say line.
end.
```

### Writing Files

```kaynat
use file tools.

note. Write to file.
write hello world to file called output.txt.
say File written.

note. Append to file.
append new line to file called output.txt.
say Line appended.
```

### File Operations

```kaynat
use file tools.

note. Check if file exists.
if file called data.txt exists then.
    say File exists.
end.

note. Delete file.
delete file called old.txt.
say File deleted.

note. Copy file.
copy file called source.txt to destination.txt.
say File copied.

note. Move file.
move file called old.txt to new.txt.
say File moved.
```

### Directory Operations

```kaynat
use file tools.

note. Create directory.
create directory called my folder.
say Directory created.

note. Delete directory.
delete directory called old folder.
say Directory deleted.

note. Check if directory exists.
if directory called my folder exists then.
    say Directory exists.
end.

note. List directory contents.
list contents of directory called my folder and store as files.
for each file in files.
    say file.
end.
```

---

## Date and Time Tools

### Current Date and Time

```kaynat
use date tools.

get current date and store as today.
say Today is, today.

get current time and store as now.
say Time is, now.

get current timestamp and store as timestamp.
say Timestamp is, timestamp.
```

### Formatting

```kaynat
use date tools.

get current date and store as today.

format today as YYYY-MM-DD and store as formatted.
say Formatted date is, formatted.

format today as DD/MM/YYYY and store as formatted2.
say Formatted date is, formatted2.
```

---

## Random Tools

### Random Numbers

```kaynat
use random tools.

note. Random integer.
generate random integer from 1 to 100 and store as num.
say Random number is, num.

note. Random float.
generate random float from 0 to 1 and store as decimal.
say Random decimal is, decimal.

note. Random boolean.
generate random boolean and store as coin flip.
if coin flip is true then.
    say Heads.
otherwise.
    say Tails.
end.
```

### Random Selection

```kaynat
use random tools.

set colors to a list containing red, green, blue, yellow.

choose random from colors and store as color.
say Random color is, color.

shuffle colors.
say Shuffled colors, colors.
```

### Random Strings

```kaynat
use random tools.

generate random string of length 10 and store as code.
say Random code is, code.
```

---

## Network Tools

### HTTP Requests

```kaynat
use network tools.

note. Fetch URL.
fetch from url https://api.example.com/data and store as response.
say Response is, response.

note. Check if URL is reachable.
if url https://example.com is reachable then.
    say URL is reachable.
end.
```

---

## JSON Tools

### Parsing JSON

```kaynat
use json tools.

set json text to {"name": "Alice", "age": 25}.

parse json text and store as data.

say Name is, name in data.
say Age is, age in data.
```

### Generating JSON

```kaynat
use json tools.

create a map called person.
set name in person to Alice.
set age in person to 25.

convert person to json and store as json text.
say json text.
```

### Formatting JSON

```kaynat
use json tools.

set json text to {"name":"Alice","age":25}.

format json text with indent 2 and store as pretty.
say pretty.
```

---

## Crypto Tools

### Hashing

```kaynat
use crypto tools.

set text to hello world.

hash text with sha256 and store as hash.
say SHA256 hash is, hash.

hash text with md5 and store as md5 hash.
say MD5 hash is, md5 hash.
```

### Base64 Encoding

```kaynat
use crypto tools.

set text to hello world.

encode text to base64 and store as encoded.
say Encoded is, encoded.

decode encoded from base64 and store as decoded.
say Decoded is, decoded.
```

### Token Generation

```kaynat
use crypto tools.

generate secure token of length 32 and store as token.
say Token is, token.
```

---

## Pattern Tools (Regex)

### Pattern Matching

```kaynat
use pattern tools.

set text to hello world 123.

find all matches of pattern \d+ in text and store as matches.
for each match in matches.
    say match.
end.

if text matches pattern hello.* then.
    say Text matches pattern.
end.
```

### Pattern Replacement

```kaynat
use pattern tools.

set text to hello world 123.

replace pattern \d+ with XXX in text and store as replaced.
say replaced.
```

### Pattern Splitting

```kaynat
use pattern tools.

set text to apple,banana;cherry:date.

split text by pattern [,;:] and store as fruits.
for each fruit in fruits.
    say fruit.
end.
```

### Validation

```kaynat
use pattern tools.

set email to user@example.com.

if email is valid email then.
    say Valid email.
end.

set url to https://example.com.

if url is valid url then.
    say Valid URL.
end.
```

---

## Complete Examples

### Example 1: File Statistics

```kaynat
use file tools.
use string tools.
use list tools.

read from file called data.txt and store as content.

set length to the length of content.
say File has, length, characters.

read lines from file called data.txt and store as lines.
set line count to the length of lines.
say File has, line count, lines.

set words to split content by space.
set word count to the length of words.
say File has, word count, words.
```

### Example 2: Data Processing

```kaynat
use list tools.
use math tools.

set scores to a list containing 85, 92, 78, 95, 88, 76, 90.

set minimum to the minimum of scores.
set maximum to the maximum of scores.
set average to the average of scores.

say Minimum score is, minimum.
say Maximum score is, maximum.
say Average score is, average.

sort scores.
say Sorted scores, scores.
```

### Example 3: Text Analysis

```kaynat
use string tools.
use list tools.

set text to The quick brown fox jumps over the lazy dog.

set upper to text in uppercase.
say Uppercase, upper.

set words to split text by space.
set word count to the length of words.
say Word count, word count.

for each word in words.
    set length to the length of word.
    say word, has, length, letters.
end.
```

### Example 4: Random Password Generator

```kaynat
use random tools.
use string tools.

say Generating random password.

generate random string of length 16 and store as password.
say Password is, password.

set length to the length of password.
say Length is, length, characters.
```

---

## Best Practices

### 1. Always Import What You Need

```kaynat
note. Good.
use math tools.
use string tools.

note. Import only what you use.
```

### 2. Handle Errors

```kaynat
use file tools.

if file called data.txt exists then.
    read from file called data.txt and store as content.
    say content.
otherwise.
    say File not found.
end.
```

### 3. Validate Input

```kaynat
use pattern tools.

ask the user for email.

if email is valid email then.
    say Valid email, email.
otherwise.
    say Invalid email format.
end.
```

### 4. Use Descriptive Variable Names

```kaynat
note. Good.
set user email to user@example.com.
set total score to 95.

note. Bad.
set x to user@example.com.
set y to 95.
```

---

## Implementation Status

**Current Status:** NOT IMPLEMENTED

All standard library functions are designed and documented but not yet implemented in the interpreter.

**Planned for:** Version 2.0.0

**To use these features:** Wait for v2.0.0 release or contribute to the implementation.

---

## Next Steps

1. **Learn the syntax** - Study the examples in this guide
2. **Plan your programs** - Design programs using these functions
3. **Wait for release** - Standard library coming in v2.0.0
4. **Or contribute** - Help implement these features

---

*This guide describes planned features for Kaynat v2.0.0. The syntax is finalized but implementation is pending.*

