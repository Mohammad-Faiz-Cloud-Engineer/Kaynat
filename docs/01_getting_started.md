# Getting Started with Kaynat

## What is Kaynat?

Kaynat is a programming language that reads like English. Every statement is written in natural language, making it accessible to beginners while remaining powerful enough for real applications.

Named after Kaynat (Saista), built by Mohammad Faiz.

## Installation

1. Ensure Python 3.8+ is installed
2. Clone or download the Kaynat repository
3. Navigate to the kaynat directory

## Running Your First Program

Create a file called `hello.kaynat`:

```kaynat
begin program.
say Hello, World.
end program.
```

Run it:
```bash
python -m kaynat.main hello.kaynat
```

## The REPL

Start the interactive shell:
```bash
python -m kaynat.repl
```

Try these commands:
```kaynat
>>> set x to 5.
>>> say x.
  → 5
>>> add 3 to x.
>>> say x.
  → 8
```

## Basic Syntax Rules

1. Every statement ends with a period (.)
2. Commas (,) separate items in lists
3. No other punctuation is used
4. Everything is English words
5. Programs start with `begin program.` and end with `end program.`

## Your First Real Program

```kaynat
begin program.

set name to Kaynat.
set age to 21.

say Hello, my name is, name.
say I am, age, years old.

end program.
```

## Next Steps

Read the Core Language Reference to learn all features.
