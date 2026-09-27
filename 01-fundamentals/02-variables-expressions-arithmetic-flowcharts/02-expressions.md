# Expressions

An expression is a combination of values, variables, and operators that evaluates to a single value. Whenever Python sees an expression, it computes it down to one result.

Think of it as a math sentence:
* The pieces are values, variables, and operators.
* The result is what Python gives back after solving it.
you can combine expressions inside other expressions and likewise

## Simple Example

```python
x = 5
y = 3

result = x + y * 2
print(result)  # 11
```

## Types of Expressions

| Expression Type       | Description                     | Example           |
| --------------------- | ------------------------------- | ----------------- |
| Arithmetic Expression | Produces a number               | `x + y`           |
| Relational Expression | Produces a boolean (comparison) | `x > y`           |
| Logical Expression    | Combines booleans               | `x > 0 and y > 0` |
| Assignment Expression | Stores a result into a variable | `z = x + y`       |
| String Expression     | Combines or builds text         | `"Hi " + name`    |

## Operator Precedence

Python doesn't solve expressions left to right blindly — it follows an order, just like normal math.

```python
result = 2 + 3 * 4
print(result)  # 14, not 20
```

'*' runs before '+', so 3 * 4 is solved first, then 2 + is added on.

| Precedence  | Operators                   | Example       |
| :---------: | --------------------------- | ------------- |
| 1 (highest) | `()`                        | `(2 + 3) * 4` |
|      2      | `**`                        | `2 ** 3`      |
|      3      | `*` `/` `//` `%`            | `10 // 3`     |
|      4      | `+` `-`                     | `5 - 2`       |
| 5 (lowest)  | `==` `!=` `>` `<` `>=` `<=` | `x >= y`      |

## Checking an Expression's Result

```python
x = 10
y = 4

print(x + y)        # 14
print(x > y)        # True
print(x + y > 12)   # True
```