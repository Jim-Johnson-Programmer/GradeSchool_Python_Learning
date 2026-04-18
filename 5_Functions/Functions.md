# Lesson 5 — Functions

## What Is a Function?

A **function** is a reusable block of code that has a name.  
Instead of writing the same code over and over, you write it once inside a function and then **call** it whenever you need it.

Think of a function like a **recipe**:

- You write the recipe once.
- Any time you want a meal, you just follow the recipe — you don't rewrite it each time!

---

## Lesson Files

| File                               | Topic                                                   |
| ---------------------------------- | ------------------------------------------------------- |
| `5_1_functions_intro.py`           | Define and call your first functions                    |
| `5_2_functions_with_parameters.py` | Pass information _into_ a function using parameters     |
| `5_3_functions_return_values.py`   | Get information _back out_ of a function using `return` |
| `5_4_minecraft_chat_functions.py`  | Minecraft chat rebuilt using functions                  |
| `5_5_mad_libs_functions.py`        | Mad Libs rebuilt using functions                        |

---

## Key Ideas to Remember

### 1. Defining a function — `def`

Use the keyword `def` to create a function.  
The code inside is **indented** (pushed in with spaces).

```python
def say_hello():
    print("Hello!")
```

> Nothing happens yet — you just wrote the recipe.

---

### 2. Calling a function

To actually **run** the function, write its name followed by parentheses `()`.

```python
say_hello()   # → Hello!
say_hello()   # → Hello!  (you can call it as many times as you want!)
```

---

### 3. Parameters — sending information IN

A **parameter** is a variable that lives inside the function.  
You send a value in when you call the function.

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Eric")    # → Hello, Eric!
greet("Jordan")  # → Hello, Jordan!
```

You can have **multiple parameters** separated by commas:

```python
def greet_player(username, biome):
    print(username + " is exploring the " + biome + " biome!")

greet_player("CreeperSlayer", "jungle")
```

---

### 4. Return values — getting information OUT

`return` sends a value back to whoever called the function.

```python
def make_shout(word):
    return word.upper() + "!!!"

result = make_shout("boom")
print(result)   # → BOOM!!!
```

Once Python hits `return`, the function stops — everything after it is skipped.

---

### 5. Functions keep your code organised

**Without functions** (messy — repeated code):

```python
print("=== ROUND 1 ===")
print("Get ready...")
print("GO!")

print("=== ROUND 2 ===")
print("Get ready...")
print("GO!")
```

**With functions** (clean):

```python
def start_round(number):
    print("=== ROUND " + str(number) + " ===")
    print("Get ready...")
    print("GO!")

start_round(1)
start_round(2)
```

---

## The Four Parts of a Function (Quick Reference)

```
def  function_name  (  parameters  )  :
      ↑ keyword      ↑ inputs           ↑ colon required
    [indented code block]
    return  value                      ← optional: sends something back
```

---

## Common Mistakes

| Mistake                                                | Why it happens                                               | Fix                                    |
| ------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------- |
| Forgetting `()` when calling                           | Looks like a variable, not a function call                   | Always write `my_function()`           |
| Forgetting the `:` after `def`                         | Python requires the colon                                    | `def my_function():`                   |
| Code not indented inside the function                  | Python uses indentation to know what belongs to the function | Indent every line inside with 4 spaces |
| Using a variable from _inside_ a function _outside_ it | Variables inside a function only exist there                 | Use `return` to pass the value out     |
| Calling a function before defining it                  | Python reads top-to-bottom; the `def` must come first        | Move the `def` block above the call    |

---

## Lesson Progression

```
5_1  →  Define and call a basic function        (no inputs, no output)
5_2  →  Add parameters                          (send info IN)
5_3  →  Add return values                       (get info OUT)
5_4  →  Minecraft chat rebuilt with functions   (real project)
5_5  →  Mad Libs rebuilt with functions         (real project)
```

Start with `5_1_functions_intro.py` and work your way through!
