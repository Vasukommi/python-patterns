# Python Patterns

A focused Python learning repository for strengthening core programming skills, problem-solving ability, data structures, algorithms, and production-ready Python concepts.

This repo is designed from the perspective of someone preparing for Python-heavy engineering interviews and backend development work. It starts with Python fundamentals, builds toward LeetCode-style problem solving, and then connects those skills to real-world Python engineering with FastAPI, Pydantic, testing, async programming, and performance basics.

## What This Repository Covers

- Python core syntax and problem-solving foundations
- Data structures commonly used in DSA and interviews
- Python fluency patterns for writing cleaner solutions
- Algorithmic thinking and complexity analysis
- Production Python concepts used in backend engineering
- FastAPI, Pydantic, async Python, and testing foundations

## Python Core Foundations

- Variables, conditionals, and loops
- Functions, arguments, and return values
- Local, global, and nonlocal scope
- Short-circuiting with `and` and `or`
- Conditional expressions: `x if condition else y`
- Strings and common string methods
- `range()`, `enumerate()`, `zip()`, and `reversed()`
- `join()` for string building
- Mutable vs immutable objects
- References and object mutation
- Shallow vs deep copies
- Mutable default-argument behavior

## Data Structures for Problem Solving

### Lists and Tuples

- Indexing and slicing
- Reversing with `[::-1]`
- `append()`, `extend()`, `insert()`, `remove()`, and `pop()`
- Unpacking and starred unpacking
- Sorting with `sort()` and `sorted()`
- Custom sorting with `key=...`
- `lambda` with sorting

### Dictionaries

- Creation, access, and updates
- Membership checks with `in`
- `.get()`
- `.items()`, `.keys()`, and `.values()`
- Storing indexes
- Frequency counting
- `dict.fromkeys()`

### Sets

- Membership checks
- Uniqueness
- `add()` and `remove()`
- Intersection with `&`
- Union with `|`
- Difference with `-`
- Symmetric difference with `^`

### Useful Standard Library Tools

- `Counter`
- `defaultdict`
- `deque`
- `any()` and `all()`
- `min()` and `max()` with `key=...`
- `heapq`
- `bisect`

## Python Fluency and Algorithms

- Comprehensions
- `lambda`
- Iterators
- Generators and `yield`
- Recursion
- Big-O notation
- Recursion space complexity
- List vs dictionary/set performance
- Stack and queue concepts
- Binary search
- Two pointers
- Sliding window
- BFS and DFS
- Heaps
- Basic trees

## Production Python and Backend Engineering

### Object-Oriented Programming

- Classes and instances
- `__init__`
- `__str__` and `__repr__`
- Inheritance
- Composition
- Class methods
- Static methods
- Properties

### Typing

- `list[int]`
- `dict[str, int]`
- `str | None`
- `Literal`
- `Annotated`
- Basic generics

### Pydantic

- `BaseModel`
- Validation
- Serializers
- Nested models
- Validators
- Model configuration

### FastAPI

- Routing
- Dependency injection
- Validation
- Middleware
- Exception handling
- Request/response lifecycle
- Authentication patterns

### Async Python

- Coroutines
- `async` and `await`
- Event loop basics
- Concurrency vs parallelism
- Blocking vs non-blocking operations
- When `def` vs `async def` matters in FastAPI

### Engineering Practices

- Decorators
- `functools.wraps`
- Context managers
- Working with files and JSON
- Exceptions
- Modules and packages
- Environment management
- `pytest`
- Fixtures
- Mocks
- Async testing

## Optional Advanced Topics

These are useful, but they are not the first priority while building core Python and DSA confidence.

- Walrus operator: `:=`
- GIL
- Threading
- Multiprocessing
- Performance profiling and optimization

## Complexity Cheat Sheet

| Structure | Typical Operation | Complexity |
| --- | --- | --- |
| `list` | Index access | O(1) |
| `list` | Search with `in` | O(n) |
| `list` | Append | O(1) amortized |
| `list` | Insert/delete near beginning | O(n) |
| `dict` | Lookup | O(1) average |
| `set` | Membership | O(1) average |
| `deque` | Append/popleft | O(1) |
| `heap` | Push/pop | O(log n) |
| Binary search | Search sorted data | O(log n) |

## Goal

The goal of this repository is to build Python confidence in a practical order:

1. Learn the language fundamentals well.
2. Get comfortable with lists, dictionaries, sets, and common standard library tools.
3. Practice algorithmic patterns used in interviews.
4. Connect Python knowledge to production backend development.

