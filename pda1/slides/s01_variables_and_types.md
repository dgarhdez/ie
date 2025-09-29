---
marp: true
author: 
  - name: Daniel Garcia
  - email: dgarciah@faculty.ie.edu
  - url: www.linkedin.com/in/dgarhdez
header: ![center width:100px](../../img/ie_logo.png)
size: 16:9
footer: "Python Programming, dgarciah@faculty.ie.edu"
theme: default
math: katex
style: |
    img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }
---

<!-- _color: "rgb(31,56,94)" -->

# Python Programming

# Session 1: Variables, Types, and Operations

---

<!-- paginate: true -->

## Agenda

- Variables and Objects
- Numeric Types
- Operations with Numeric Types
- Text-Sequence Type
- Boolean Type

---

## Variables and Objects

Variables store data in memory and reference objects

- Assignment using `=`
- Naming conventions: descriptive, no numbers at start, no special characters
- Everything in Python is an object with properties and methods

---

## Numeric Types

### Integer (`int`)

Represents whole numbers: 1, 3, 18756394

- Created using standard notation
- Type: `int`

### Float (`float`)

Represents numbers with fractional parts: 1.5, 3.141592

- Created with decimal point
- Type: `float`

---

## Operations with Numeric Types

| Operation | Operator | Description | Example |
|-----------|----------|-------------|---------|
| Addition | + | Adds two numbers | 2 + 3 = 5 |
| Subtraction | - | Subtracts second from first | 5 - 2 = 3 |
| Multiplication | * | Multiplies two numbers | 3 * 4 = 12 |
| Division | / | Divides first by second | 8 / 2 = 4.0 |
| Exponentiation | ** | Raises first to power of second | 2 ** 3 = 8 |
| Floor division | // | Quotient of division (floor) | 17 // 3 = 5 |
| Modulo | % | Remainder of division | 17 % 3 = 2 |
| Absolute value | abs() | Absolute value | abs(-4) = 4 |

---

## Order of Operations

1. Parentheses
2. Exponentiation
3. Multiplication and division
4. Addition and subtraction

---

## Type Conversion

Converting between numeric types:

- `int()`: float to int (truncates decimal)
- `float()`: int to float
- `round()`: rounds to nearest integer (banker's rounding)

---

## Text-Sequence Type

### String (`str`)

Represents sequences of text characters

- Immutable sequences
- Created with single, double, or triple quotes
- Type: `str`

---

## Boolean Type

Represents truth values: `True` or `False`

- Assimilated as numbers: True = 1, False = 0
- Result of comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Result of logical operations: `not`, `and`, `or`

---

## Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| == | equality | 4 == 4 → True |
| != | inequality | 4 != 5 → True |
| > | greater than | 5 > 3 → True |
| < | less than | 3 < 5 → True |
| >= | greater than or equal | 5 >= 5 → True |
| <= | less than or equal | 3 <= 5 → True |

---

## Logical Operations

### `not`

Negates a boolean value: `not True` → `False`

### `and`

True if all operands are True: `True and False` → `False`

### `or`

True if at least one operand is True: `True or False` → `True`

Order of operations: `not`, `and`, `or`

---

## Thank You

Questions? [dgarciah@faculty.ie.edu](mailto:dgarciah@faculty.ie.edu)
