# Python Fundamentals

A hands-on collection of Python practice scripts covering core language concepts, from variables and data types to object-oriented programming, plus a few small interactive console games. Each file focuses on one topic and has short inline comments, so you can use it as a quick reference or a learning path for beginners.

## Topics Covered

### Basics
| File | Topic |
|------|-------|
| `app.py` | Variables, strings, indexing and slicing |
| `numbers.py` | Numeric types, arithmetic operators, `math` module |
| `type_conversion.py` | `int()`, `float()`, `bool()`, `str()`, truthy and falsy values |
| `escape_characters.py` | Escape sequences (`\"`, `\'`, `\\`, `\n`) |
| `formatted_strings.py` | f-strings |
| `string_methods.py` | Common string methods (`upper`, `strip`, `find`, `replace`, …) |

### Control Flow
| File | Topic |
|------|-------|
| `operators.py` | Comparison, logical and chained operators |
| `short_circuit_evaluation.py` | Short-circuit evaluation with `and` / `or` |
| `conditional_statements.py` | `if` / `elif` / `else`, ternary operator |
| `loops.py` | `for`, `range`, `for…else`, nested loops, `while` |
| `even_numbers.py` | Loop exercise: counting even numbers |

### Data Structures
| File | Topic |
|------|-------|
| `list.py` | Lists: slicing and methods |
| `tuple.py` | Tuples and immutability |
| `Set.py` | Sets: union, intersection and other set operations |
| `dictionary.py` | Dictionaries: key-value access and methods |

### Functions
| File | Topic |
|------|-------|
| `functions.py` | Defining functions, default parameters, return values |
| `keyword_arguments.py` | Keyword args, `*args`, `**kwargs`, lambda functions |

### Error Handling & File I/O
| File | Topic |
|------|-------|
| `exceptions.py` | `raise`, `assert`, `try` / `except` / `finally` |
| `read.py` | Reading files (`read`, `readline`, `readlines`) |
| `write.py` | Writing files: reversing the lines of `test.txt` |

### Object-Oriented Programming (`oops/`)
| File | Topic |
|------|-------|
| `constructor.py` | Classes, `__init__`, instance vs. class variables |
| `child_implementation.py` | Extending a parent class |
| `inheritance.py` | Single inheritance and method overriding |
| `multiple_inheritance.py` | Multiple inheritance |
| `access_parent_class_members.py` | Accessing parent class members |
| `subclass.py` | `issubclass()` and `isinstance()` |
| `data_hiding.py` | Private members and name mangling |

### Mini Projects (`projects/`)
| File | Description |
|------|-------------|
| `dice_rolling_game.py` | Roll two dice on demand |
| `number_guessing_game.py` | Guess a random number between 1 and 100 |
| `rock_paper_scissor.py` | Rock, paper, scissors against the computer, with emojis |

### Exercises
- `exercises.py`: mixed practice problems covering the topics above

## Getting Started

**Requirements:** Python 3.6+ (f-strings are used throughout). No external packages are needed.

```bash
git clone https://github.com/keshavjha06/Python.git
cd Python

# Run any script
python3 loops.py

# Play a game
python3 projects/rock_paper_scissor.py

# Scripts that import from the oops package should be run as modules from the repo root
python3 -m oops.child_implementation
```
