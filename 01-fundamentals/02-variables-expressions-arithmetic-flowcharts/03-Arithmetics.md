## Arithmetics

Arithmetic is the use of mathematical operators to compute values. It's the foundation expressions are built on top of.

# Simple Example

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333...
```

## List of Operators

| Operator | Name           | Description                      | Example  | Result |
| :------: | -------------- | -------------------------------- | :------: | :----: |
|   `+`    | Addition       | Adds two values                  | `5 + 2`  |  `7`   |
|   `-`    | Subtraction    | Subtracts one value from another | `5 - 2`  |  `3`   |
|   `*`    | Multiplication | Multiplies two values            | `5 * 2`  |  `10`  |
|   `/`    | Division       | Divides, always returns a float  | `5 / 2`  | `2.5`  |
|   `//`   | Floor Division | Divides, drops the decimal       | `5 // 2` |  `2`   |
|   `%`    | Modulus        | Returns the remainder            | `5 % 2`  |  `1`   |
|   `**`   | Exponent       | Raises to a power                | `5 ** 2` |  `25`  |

## Order of Operations

Same rule as math class — PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

```python
result = (2 + 3) * 2 ** 2
print(result)  # 20
```

Breakdown:
1. (2 + 3) → 5
2. 2 ** 2 → 4
3. 5 * 4 → 20

## Mixing Types

```python
a = 7
b = 2.0

print(a + b)   # 9.0 → int + float becomes float
print(a // b)  # 3.0
print(a % b)   # 1.0
```