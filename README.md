# Kaynat Programming Language

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-10%2F10%20passing-brightgreen.svg)](examples/)
[![GitHub](https://img.shields.io/badge/GitHub-Kaynat-blue?logo=github)](https://github.com/Mohammad-Faiz-Cloud-Engineer/Kaynat)

### *Named Kaynat. Built in silence. Meant to speak.*

**A programming language where code reads like poetry.**

[Read the Story](STORY.md) • [Get Started](#quick-start) • [Documentation](docs/) • [Examples](examples/)

---

**Created by Mohammad Faiz**

</div>

---

## 💔 The Story

I loved her since kindergarten. Waited years. Finally told her how I felt in 11th grade.

She said no.

She chose some guy who rides a KTM and drinks Sting to look cool. A "chhapri" living off his father's money. Someone who had nothing real to offer.

I fell into depression. But instead of giving up, I built this. A programming language where every line reads like English. Like the words I wanted to say but couldn't.

**[Read the full story →](STORY.md)**

---

## What is Kaynat?

Kaynat is a **Turing-complete programming language** where you write code in plain English. No weird symbols. No cryptic syntax. Just honest words.

### Look at this

**Traditional Python:**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

**Kaynat:**

```kaynat
define a function called factorial that takes n.
    if n equals zero then.
        give back one.
    end.
    set prev to n minus one.
    set result to the result of calling factorial with prev.
    give back n multiplied by result.
end.

call factorial with 5 and store as result.
say result.
```

Both output `120`. But only one reads like you're talking to someone.

---

## Quick Start

### Installation

```bash
# Clone it
git clone https://github.com/Mohammad-Faiz-Cloud-Engineer/Kaynat.git
cd Kaynat

# Run a program
python -m kaynat.main examples/01_hello_world.kaynat

# Or start the REPL
python -m kaynat.repl
```

### Your First Program

Make a file called `hello.kaynat`:

```kaynat
begin program.
set name to world.
say hello, name.
end program.
```

Run it:

```bash
python -m kaynat.main hello.kaynat
```

That's it.

---

## Features

- ✅ Write code in plain English
- ✅ Variables, constants, all the basic stuff
- ✅ Math, comparisons, logic
- ✅ If/else statements
- ✅ All kinds of loops
- ✅ Functions that can call themselves
- ✅ Lists and operations
- ✅ Interactive REPL to test things
- ✅ Actually Turing complete
- ✅ Standard library (math, strings, files, crypto, JSON, more)
- ✅ Data structures (stacks, queues, trees, graphs, heaps, tries)
- ✅ Object-oriented programming
- ✅ GUI system

---

## Example Code

```kaynat
# Variables and math
set x to 10.
add 5 to x.
say x.

# If statements
if x is greater than 10 then.
    say x is big.
otherwise.
    say x is small.
end.

# Loops
repeat 5 times.
    say hello.
end.

loop from 1 to 10.
    say current.
end.

# Functions
define a function called greet that takes name.
    say hello, name.
end.

call greet with world.
```

---

## Documentation

- **[STORY.md](STORY.md)** - Why this exists
- **[Getting Started](docs/01_getting_started.md)** - Learn the basics
- **[Core Language](docs/02_core_language.md)** - Everything about the language
- **[Practical Guide](docs/10_practical_guide.md)** - Real working examples
- **[Standard Library Usage](docs/11_stdlib_usage.md)** - How to use built-in functions
- **[DSA Usage](docs/12_dsa_usage.md)** - Data structures and algorithms guide
- **[OOP Guide](docs/03_oop.md)** - Object-oriented programming
- **[GUI Programming](docs/05_gui.md)** - Build desktop apps
- **[Grammar](docs/07_grammar.md)** - Formal specification
- **[Errors](docs/08_errors.md)** - When things go wrong
- **[examples/](examples/)** - 10 working programs

---

## Testing

Try the examples:

```bash
python -m kaynat.main examples/01_hello_world.kaynat
python -m kaynat.main examples/07_sequence.kaynat
python -m kaynat.main examples/08_counting.kaynat
```

All 10 work. No failures.

---

## Why This Matters

Most programming languages use symbols like `{}`, `[]`, `&&`, `||`. Why? Because that's how it's always been done.

Kaynat proves you don't need that. You can write real code in plain English and it works just as well.

But honestly? This language exists because I needed to turn my pain into something. She chose a fake lifestyle over something real. I chose to build something that'll outlast both of us.

Every time someone writes code in Kaynat, they're using a language born from heartbreak. Not from some corporate boardroom or university research lab. From a kid who got rejected and decided to create instead of destroy.

---

## Contributing

If you want to contribute, go ahead. Just respect what this is - not just another programming language, but something built from real emotion.

---

## License

MIT License - See [LICENSE](LICENSE)

Copyright (c) 2026 Mohammad Faiz

Use it however you want. Build something. Create something. That's what matters.

---

## Author

**Mohammad Faiz**

- GitHub: [@Mohammad-Faiz-Cloud-Engineer](https://github.com/Mohammad-Faiz-Cloud-Engineer)
- Project: [Kaynat Programming Language](https://github.com/Mohammad-Faiz-Cloud-Engineer/Kaynat)

Just a developer who turned heartbreak into code.

---

<div align="center">

### If you're going through heartbreak or depression:

**You are not defined by who rejects you.**  
**You are defined by what you create.**

I built a programming language in my darkest hours.  
What will you build in yours?

---

*Named Kaynat. Built in silence. Meant to speak.*

Made with 💔 and 💻 by Mohammad Faiz

</div>
