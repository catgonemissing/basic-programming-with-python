# Variables

A variable is a **named container that stores a value in memory**. You give it a name, assign it a value, and can use or change that value later in the program.

Think of it as a labeled box:
* The **label** is the variable name
* The **contents** are the value

you can change the contents of the label and likewise

## Simple Example

```python
name = "Alice"
age = 15
height = 145.5
is_princesss = True
```

## List Types 0f Datas

| Data Type           | Description                      | Example                                 |
| ------------------- | -------------------------------- | --------------------------------------- |
| Integer (`int`)     | Whole numbers                    | `age = 20`                              |
| Float (`float`)     | Decimal numbers                  | `height = 165.5`                        |
| String (`str`)      | Text (in quotes)                 | `name = "Alice"`                        |
| Boolean (`bool`)    | True or False                    | `is_student = True`                     |
| List (`list`)       | Ordered collection, changeable   | `fruits = ["apple", "mango"]`           |
| Tuple (`tuple`)     | Ordered collection, unchangeable | `point = (3, 5)`                        |
| Dictionary (`dict`) | Key-value pairs                  | `person = {"name": "Alice", "age": 20}` |
| Set (`set`)         | Unordered, unique values         | `nums = {1, 2, 3}`                      |
| NoneType (`None`)   | Represents "no value"            | `result = None`                         |

## Check Variables Type

```python
x = 42
y = 3.14
z = "hello"

print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
print(type(z))   # <class 'str'>
```
## Converting

```python
# String → Integer
age = int("20")        # 20

# Integer → Float
price = float(10)      # 10.0

# Number → String
text = str(123)        # "123"

# Integer → Boolean
flag = bool(1)         # True
flag2 = bool(0)        # False
```