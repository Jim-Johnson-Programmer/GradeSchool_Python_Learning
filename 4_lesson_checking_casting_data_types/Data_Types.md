# Lesson 4 — Checking & Casting Data Types

## What Is a Data Type?

Every piece of information in Python has a **type** that tells Python _what kind of thing it is_ and _what you can do with it_.

| Type         | Python name | Examples                     |
| ------------ | ----------- | ---------------------------- |
| Text         | `str`       | `"hello"`, `"007"`, `" 42 "` |
| Whole number | `int`       | `7`, `0`, `-3`               |
| Decimal      | `float`     | `3.14`, `0.5`, `-2.0`        |
| True/False   | `bool`      | `True`, `False`              |

---

## Lesson Files

| File                        | Topic                                                                         |
| --------------------------- | ----------------------------------------------------------------------------- |
| `4_1_data_types_intro.py`   | Meet the four main data types                                                 |
| `4_2_strings_vs_numbers.py` | Tricky differences — leading zeros, spaces, math vs. joining                  |
| `4_3_type_checking.py`      | Use `type()` to find out what type something is                               |
| `4_4_casting.py`            | Change a value from one type to another with `int()`, `float()`, `str()`      |
| `4_5_data_type_quiz.py`     | Quiz — pick the right data type for license plates, barcodes, money, and more |

---

## Key Ideas to Remember

### 1. Strings remember EVERYTHING — including spaces and zeros

```python
secret_code = "007"   # the two leading zeros are part of the string
agent_number = 7      # just the number 7 — zeros are gone
```

### 2. Spaces inside a string count as characters

```python
word_a = "cat"    # 3 characters
word_b = " cat"   # 4 characters — there is a space at the front!
word_a == word_b  # False — they are NOT equal
```

### 3. `+` means something different for strings vs. numbers

```python
print("5" + "3")   # "53"  ← joins the text together
print(5  +  3)     # 8     ← adds the numbers
```

### 4. `input()` ALWAYS gives you a string

```python
age = input("How old are you? ")   # user types 10
# age is "10", NOT 10
# You must cast it: age = int(age)
```

### 5. Use `type()` to check what type a value is

```python
type("hello")   # <class 'str'>
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type(True)      # <class 'bool'>
```

### 6. Casting converts one type to another

```python
int("42")     # → 42
float("3.14") # → 3.14
str(100)      # → "100"
```

---

## Common Mistakes

| Mistake                          | Why it happens                       | Fix                                             |
| -------------------------------- | ------------------------------------ | ----------------------------------------------- |
| `"007" == 7` is `False`          | One is text, one is a number         | Use the same type on both sides                 |
| `" hello" == "hello"` is `False` | The space is a real character        | Use `.strip()` to remove extra spaces           |
| `"5" + "3"` gives `"53"`         | Both are strings, so `+` joins them  | Convert first: `int("5") + int("3")`            |
| `int("3.14")` crashes            | `int()` can't handle a decimal point | Use `float("3.14")` then `int()` if needed      |
| `int("hello")` crashes           | `"hello"` is not a number            | Make sure the string actually contains a number |
