# Pseudocode

Pseudocode is code or notation that resembles (pseudo) a program, or an explanation of how to solve a problem. It's often used by people to write out an algorithm before turning it into real code, using human language.

## Pseudocode vs Python

| Pseudocode                                                                  | Python                                                           |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Uses human (everyday) language                                              | Uses defined syntax                                              |
| `Write(X)`                                                                  | `print(X)`                                                       |
| `Read(X)`                                                                   | `input(X)`                                                       |
| `if (condition) then`<br>`  code`<br>`else if (condition) then`<br>`  code` | `if (condition):`<br>`  code`<br>`elif (condition):`<br>`  code` |
| `while (condition) do`<br>`  looping here`                                  | `while (condition):`<br>`  looping here`                         |
| `for i ← 1 to x do`<br>`  looping here`                                     | `for i in range(x):`<br>`  looping here`                         |

## Simple Example

Problem: Menghitung luas segitiga (calculating the area of a triangle)

Pseudocode
```
Declare:
   alas : int
   tinggi : int
   luas : float
Algorithm
   Read(alas)
   Read(tinggi)
   luas ← (alas * tinggi) / 2
   Write(luas)
```

Python
```python
alas = input()
tinggi = input()
luas = (alas * tinggi) / 2
print(luas)
```

## Structure

Pseudocode written this way has two parts:
* Declare:      lists the variables used and their types (int, float, etc.)
* Algorithm:    the actual step-by-step logic, using Read(), Write(), ← for assignment, and conditionals/loops as needed