# Lesson 2 - Working with Integers in Python

## What Is an Integer?

An integer is a **whole number**. Integers do not have decimal points.

Examples of integers:

- `0`
- `5`
- `42`
- `-3`
- `1000`

These are **not** integers:

- `3.14` because it has a decimal
- `"7"` because it is text, not a number

---

## Why Integers Matter

Integers are used whenever you want to work with whole numbers in a program.

You might use integers for:

- counting points in a game
- tracking how many students are in a class
- storing ages
- doing calculator math
- keeping score

---

## Lesson Files

| File                     | Purpose                                                                |
| ------------------------ | ---------------------------------------------------------------------- |
| `calculator.py`          | Practice using integers with user input and math operations            |
| `rock_paper_scissors.py` | A game example that shows how programs can take input and make choices |

---

## Creating Integer Variables

You can store an integer in a variable.

```python
age = 10
score = 25
temperature = -4
```

Each of these variables stores a whole number.

---

## Basic Math with Integers

Python can do math with integers just like a calculator.

```python
print(2 + 3)   # 5
print(7 - 4)   # 3
print(6 * 2)   # 12
print(8 / 2)   # 4.0
```

### The main math operators

| Symbol | Meaning          | Example  | Result |
| ------ | ---------------- | -------- | ------ |
| `+`    | addition         | `3 + 2`  | `5`    |
| `-`    | subtraction      | `7 - 1`  | `6`    |
| `*`    | multiplication   | `4 * 3`  | `12`   |
| `/`    | division         | `8 / 2`  | `4.0`  |
| `//`   | integer division | `9 // 2` | `4`    |
| `%`    | remainder        | `9 % 2`  | `1`    |

---

## Updating Integer Variables

You can change a number stored in a variable.

```python
score = 10
score = score + 5
print(score)
```

Output:

```python
15
```

This means:

- start with `10`
- add `5`
- store the new answer back into `score`

You can also write:

```python
score += 5
```

---

## Integers and `input()`

This is one of the most important things to remember:

`input()` always gives you **text**.

```python
favorite_number = input("Enter a number: ")
print(favorite_number)
```

If the user types `8`, Python stores it as `"8"`, not `8`.

That means if you want to do math, you must convert the text into an integer using `int()`.

```python
favorite_number = int(input("Enter a number: "))
print(favorite_number + 2)
```

If the user enters `8`, the output will be:

```python
10
```

---

## Using `int()` to Convert Text to an Integer

The `int()` function changes a number written as text into a real integer.

```python
number_text = "25"
number = int(number_text)
print(number)
```

Output:

```python
25
```

Now `number` can be used in math.

```python
print(number + 5)
```

Output:

```python
30
```

---

## Example: A Simple Calculator

This lesson includes [2_Lesson_Integers/calculator.py](/d:/VarsityTutors_Projects_and_Documents/Python_Learning/GradeSchool_Python_Learning/2_Lesson_Integers/calculator.py), which asks the user for two integers and an operation.

```python
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
```

Important ideas from this example:

- the numbers are converted with `int()`
- the operation stays as text because `+`, `-`, `*`, and `/` are characters
- the program uses `if` and `elif` to decide which math to perform

Example:

```python
if operation == "+":
	result = first_number + second_number
```

---

## Division and Zero

You can never divide by zero.

```python
print(10 / 0)
```

That will cause an error.

That is why the calculator lesson checks this first:

```python
if second_number != 0:
	result = first_number / second_number
else:
	print("Error: Division by zero is not allowed.")
```

This is a good example of making your program safer.

---

## Negative Integers

Integers can also be negative.

```python
bank_account_change = -15
winter_temperature = -2
```

Negative integers are useful for:

- temperatures below zero
- losing points in a game
- money owed
- moving backward

---

## Common Mistakes

### Mistake 1: Adding strings instead of integers

```python
number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
print(number1 + number2)
```

If the user types `2` and `3`, the output will be:

```python
23
```

Why? Because Python joined two pieces of text together.

Correct version:

```python
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print(number1 + number2)
```

### Mistake 2: Trying to turn words into integers

```python
age = int("hello")
```

This causes an error because `"hello"` is not a number.

### Mistake 3: Forgetting division may return a decimal

```python
print(5 / 2)
```

Output:

```python
2.5
```

Even though you started with integers, regular division using `/` can produce a decimal.

---

## Practice Ideas

Try making small programs with integers:

1. Ask for a student's age and add 1.
2. Ask for two numbers and print their sum.
3. Ask how many goals a team scored in two games and add them together.
4. Ask for a total number of candies and divide them among friends.

---

## Quick Review

- Integers are whole numbers.
- Use variables to store integers.
- Python can add, subtract, multiply, and divide integers.
- `input()` gives text, so use `int()` when you want a whole number.
- Be careful not to divide by zero.
- Strings and integers are not the same thing.

---

## Mini Challenge

Write a program that:

1. asks the user for their age
2. converts the answer to an integer
3. prints how old they will be next year

Example:

```python
age = int(input("How old are you? "))
print("Next year you will be", age + 1)
```
