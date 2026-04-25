# Lesson 5 — Functions

**Unit Goal:** Learn how to write reusable blocks of code called _functions_, pass information into them, and get results back out.

---

## Lesson 5.1 — Introduction to Functions

**File:** `5_1_functions_intro.py`

### What to Teach

- A **function** is a named, reusable block of code.
- Use the `def` keyword to **define** a function.
- A function does nothing until you **call** it by name.
- Indentation marks everything that belongs inside the function.

### Key Vocabulary

| Word     | Meaning                                                               |
| -------- | --------------------------------------------------------------------- |
| `def`    | Keyword that starts a function definition                             |
| function | A named block of code you can run whenever you want                   |
| call     | Running a function by writing its name followed by `()`               |
| indent   | The spaces at the start of a line that show it is inside the function |

### Concepts Covered in the File

1. Defining and calling a simple function (`say_hello`)
2. A function that prints multiple lines (`show_banner`)
3. Why functions avoid repeating code (DRY — Don't Repeat Yourself)

### Talking Points

- "A function is like a recipe. You write the steps once, then you can cook the meal whenever you want."
- "Without functions, you would have to retype the same code over and over — functions fix that."
- "Nothing happens when you _define_ a function. It only runs when you _call_ it."

### Quick Check Questions

1. What keyword do you use to create a function?
2. If you define `say_hello()` but never call it, will anything print?
3. How do you call a function named `show_banner`?

---

## Lesson 5.2 — Functions with Parameters

**File:** `5_2_functions_with_parameters.py`

### What to Teach

- **Parameters** are variables listed inside the `()` when you define a function — they let you send information _into_ the function.
- **Arguments** are the actual values you pass when you _call_ the function.
- Multiple parameters are separated by commas and must be passed in the same order.

### Key Vocabulary

| Word          | Meaning                                               |
| ------------- | ----------------------------------------------------- |
| parameter     | A variable in the `def` line that receives a value    |
| argument      | The actual value sent to the function when calling it |
| order matters | Arguments are matched to parameters left-to-right     |

### Concepts Covered in the File

1. One parameter (`greet(name)`)
2. Multiple parameters (`describe_pet(owner, animal)`)
3. Number parameters with `str()` conversion (`count_items(player, amount)`)
4. Building a player profile with three parameters

### Talking Points

- "A parameter is like a blank label on a jar. When you call the function you fill in what goes in the jar."
- "The _order_ you pass arguments in matters — Python matches them left to right."
- "Type hints like `player: str` are hints to the reader — they do not stop wrong values from being passed."

### Quick Check Questions

1. What is the difference between a parameter and an argument?
2. Write a function `spawn_mob(name, count)` that prints `"[count] [name](s) spawned!"`. Call it with `"creeper"` and `5`.
3. What happens if you call `describe_pet("husky", "Eric")` instead of `describe_pet("Eric", "husky")`?
4. Mad Libs challenge: write `mad_libs_intro(name, adjective, place)` that prints `"[name] was feeling very [adjective] in [place] today."`

---

## Lesson 5.3 — Return Values (Single Value)

**File:** `5_3_functions_return_values.py`

### What to Teach

- The `return` keyword **sends a value back** out of the function.
- The caller can catch that value in a variable and use it later.
- Once Python hits `return`, the function **stops immediately**.
- **Key distinction:** `print` shows something on screen but discards it; `return` hands it back so you can use it.

### Key Vocabulary

| Word         | Meaning                                                   |
| ------------ | --------------------------------------------------------- |
| `return`     | Sends a value out of a function back to the caller        |
| return value | The value that comes back from the function               |
| `None`       | What you get back if a function has no `return` statement |

### Concepts Covered in the File

1. Returning a number (`add(a, b)`)
2. Returning a string (`make_greeting(name)`)
3. Chaining return values (passing a return value into another call)
4. `print` vs. `return` — understanding the difference

### Talking Points

- "Think of `return` like a vending machine — you put money in (arguments), and a snack comes back out (return value)."
- "If a function only `print`s, the value disappears like smoke. If it `return`s, you can save it in a variable and use it again."
- "`return` also _stops_ the function — nothing after it runs."

### Quick Check Questions

1. What does `return` do that `print` does not?
2. Write a function `square(n)` that returns `n * n`.
3. After `result = add(3, 5)`, what is stored in `result`?

---

## Lesson 5.3b — Functions with Optional (Default) Parameters

_(Extend Lesson 5.3 or introduce as a mini-lesson before 5.4)_

### What to Teach

- A parameter can have a **default value** by writing `param=value` in the `def` line.
- If the caller does **not** pass that argument, the default is used automatically.
- If the caller **does** pass a value, it overrides the default.
- Required parameters must always come **before** optional ones.

### Key Vocabulary

| Word               | Meaning                                                        |
| ------------------ | -------------------------------------------------------------- |
| default value      | The value a parameter uses when the caller does not supply one |
| optional parameter | A parameter that has a default and does not need to be passed  |
| keyword argument   | Passing an argument by name: `greet(name="Eric")`              |

### Example Code to Write Together

```python
# Minecraft: announce a player entering a biome — default biome is "Forest"
def enter_biome(player, biome="Forest"):
    print(player + " entered the " + biome + "!")

enter_biome("Eric")                  # → Eric entered the Forest!
enter_biome("Jordan", "Nether")      # → Jordan entered the Nether!
enter_biome("Sam", biome="Desert")   # → Sam entered the Desert!  (keyword argument)


# Minecraft: level up a player — default gain is 1 level
def level_up(player, levels=1):
    print(player + " gained " + str(levels) + " level(s)! ⚔️")

level_up("Eric")         # → Eric gained 1 level(s)!
level_up("Jordan", 5)    # → Jordan gained 5 level(s)!
level_up("Sam", levels=3) # → Sam gained 3 level(s)!  (keyword argument)


# Mad Libs: build a silly story line — default punctuation is "!"
def mad_libs_ending(character, action, punctuation="!"):
    return "The " + character + " " + action + punctuation

print(mad_libs_ending("zombie", "tripped"))          # → The zombie tripped!
print(mad_libs_ending("creeper", "sneezed", "???"))  # → The creeper sneezed???
print(mad_libs_ending("enderman", "vanished", "."))  # → The enderman vanished.


# Minecraft: spawn a mob — default count is 1, default world is "Overworld"
def spawn_mob(mob, count=1, world="Overworld"):
    print(str(count) + " " + mob + "(s) spawned in the " + world + "!")

spawn_mob("creeper")                         # → 1 creeper(s) spawned in the Overworld!
spawn_mob("zombie", 3)                       # → 3 zombie(s) spawned in the Overworld!
spawn_mob("ghast", 2, "Nether")              # → 2 ghast(s) spawned in the Nether!
spawn_mob("blaze", world="Nether")           # → 1 blaze(s) spawned in the Nether!
```

### Talking Points

- "Default parameters are like a Minecraft spawn point — you always land in the Overworld unless you specifically choose the Nether."
- "You can skip optional arguments and the default takes over, or you can override them — your choice."
- "Keyword arguments (`world="Nether"`) let you skip straight to the parameter you care about by name — great when there are several optional ones."
- "Required parameters (no default) must always come first in the `def` line — Python will give an error if you put them after an optional one."

### Quick Check Questions

1. Write `craft_item(item, quantity=1)` that prints `"Crafted [quantity] [item](s)!"`. What does `craft_item("sword")` print? What does `craft_item("arrow", 64)` print?
2. Can you put an optional parameter _before_ a required one? What happens if you try?
3. What is a keyword argument? Write a call to `spawn_mob` that uses a keyword argument to set only the `world` to `"End"`.
4. In the Mad Libs example, what punctuation does `mad_libs_ending("skeleton", "danced")` use if you don't pass a third argument?

---

## Lesson 5.3c — Functions That Return Multiple Values

_(Extend Lesson 5.3 or introduce as a mini-lesson before 5.4)_

### What to Teach

- Python lets a function `return` more than one value by separating them with commas.
- Python automatically packs them into a **tuple** (a group of values in order).
- The caller can **unpack** the tuple into separate variables in one line.

### Key Vocabulary

| Word            | Meaning                                                          |
| --------------- | ---------------------------------------------------------------- |
| tuple           | A group of values packed together, e.g. `(10, 20)`               |
| unpack          | Splitting a tuple into separate variables: `x, y = get_coords()` |
| multiple return | Returning two or more values separated by commas                 |

### Example Code to Write Together

```python
# Return two numbers
def min_and_max(a, b, c):
    return min(a, b, c), max(a, b, c)

low, high = min_and_max(4, 9, 2)
print("Lowest:", low)   # → Lowest: 2
print("Highest:", high) # → Highest: 9


# Return a name and a score
def get_winner(p1_name, p1_score, p2_name, p2_score):
    if p1_score >= p2_score:
        return p1_name, p1_score
    else:
        return p2_name, p2_score

winner, score = get_winner("Eric", 150, "Jordan", 200)
print(winner + " wins with " + str(score) + " points!")
# → Jordan wins with 200 points!


# Ignoring one of the return values with _
def full_name_and_length(first, last):
    full = first + " " + last
    return full, len(full)

name, length = full_name_and_length("Eric", "Smith")
print(name)              # → Eric Smith
print("Length:", length) # → Length: 10
```

### Talking Points

- "Returning multiple values is like getting back a gift bag — it holds more than one thing."
- "Python lines up the return values with the variables on the left, left to right."
- "You can always catch _all_ the returned values in one variable if you want — you get a tuple back."

### Quick Check Questions

1. Write `swap(a, b)` that returns `b, a`. Test it with `x, y = swap(1, 2)`.
2. What does Python actually give you if you write `result = min_and_max(4, 9, 2)` without unpacking?
3. How many variables must be on the left side of `=` when you unpack two return values?

---

## Lesson 5.4 — Applied Project: Minecraft Chat with Functions

**File:** `5_4_minecraft_chat_functions.py`

### What to Teach

- How to break a program into multiple cooperating functions, each with one clear job.
- A function can **return a list** to pass multiple related values back at once.
- A `main()` function ties the whole program together.

### Concepts Covered in the File

1. `collect_player_info(player_number)` — takes input and _returns_ a list of answers
2. `print_chat_line(sender, message)` — simple helper with two parameters
3. `print_chat(p1, p2)` — takes two lists as parameters and formats output
4. `main()` — calls the others in the right order

### Talking Points

- "Now we are using everything from 5.1–5.3 at once: parameters, return values, and multiple functions calling each other."
- "Each function has one job. That makes it easy to fix or change one part without breaking the rest."
- "`main()` is a common convention — it is the starting point that organises everything."

---

## Lesson 5.5 — Applied Project: Mad Libs with Functions

**File:** `5_5_mad_libs_functions.py`

### What to Teach

- Refactoring existing code (from Lesson 1.4) into functions.
- `collect_words()` returns a list of values; `print_story(words)` receives that list.
- The story is hidden inside a function so the player cannot accidentally read ahead.

### Concepts Covered in the File

1. `collect_words()` — no parameters, returns a list of eleven words
2. `print_story(words)` — takes the list and unpacks it into named variables
3. `main()` — calls both functions in order

### Connection to Earlier Lessons

- Input and strings from Lesson 1 → now organised into functions.
- Return values from Lesson 5.3 → `collect_words` returns a list.
- Parameters from Lesson 5.2 → `print_story` receives the list.

---

## Lesson 5.6 — Variable Scope

**File:** `5_6_variable_scope.py`

### Overview

Scope answers one question: **where can a variable be seen and used?**  
This lesson is split into four parts, each building on the last, using Minecraft and Mad Libs examples throughout.

---

### Part A — Local Variables (Created Inside a Function)

#### What to Teach

- Any variable **assigned inside a function** is **local** to that function.
- It springs into existence when the function is called and disappears the moment the function finishes.
- Code outside the function **cannot see or use it** — trying to do so causes a `NameError`.
- Two different functions can use the **same variable name** with no conflict — each has its own private copy.

#### Key Vocabulary

| Word           | Meaning                                                                                 |
| -------------- | --------------------------------------------------------------------------------------- |
| local variable | A variable created inside a function; invisible outside it                              |
| `NameError`    | The error Python raises when you use a variable that doesn't exist in the current scope |
| lifetime       | How long a variable exists — a local variable lives only during one function call       |

#### Minecraft Example Code

```python
def craft_sword():
    material = "diamond"         # local variable — only lives inside here
    print("Crafted a " + material + " sword!")

craft_sword()
# print(material)   ← NameError: 'material' doesn't exist out here


# Same name, completely separate variables — like two separate crafting tables
def nether_score():
    score = 500
    print("Nether score:", score)

def overworld_score():
    score = 100                  # different variable — same name, different function
    print("Overworld score:", score)

nether_score()      # → Nether score: 500
overworld_score()   # → Overworld score: 100
# Neither function touched the other's 'score'
```

#### Talking Points

- "A function is like a chest in Minecraft — items you put inside the chest stay inside the chest. You can't reach into someone else's chest from outside."
- "Once the function finishes running, all its local variables disappear — like a temporary crafting grid that gets cleared."
- "Two functions can both use a variable named `score` and they will never mix, just like two players each having their own inventory."

#### Quick Check Questions

1. A function creates `diamonds = 10`. Can a `print(diamonds)` line _outside_ the function read it? What happens?
2. If `nether_score` and `overworld_score` both have a variable named `score`, do they share it?
3. Why is it useful that functions keep their variables private?

---

### Part B — Parameter Variables

#### What to Teach

- A **parameter** is simply a **local variable** whose starting value is set by the caller.
- Parameters exist only for the duration of that one function call.
- Changing a parameter inside a function **does not change** the variable that was passed in — Python gives the function its own copy of the value.

#### Key Vocabulary

| Word       | Meaning                                                                               |
| ---------- | ------------------------------------------------------------------------------------- |
| parameter  | A local variable in the `def` line whose value comes from the caller                  |
| copy       | Python passes the _value_, not the original variable — the function gets its own copy |
| local copy | The function's private version of the value                                           |

#### Minecraft / Mad Libs Example Code

```python
# Minecraft: parameter is a local copy — changing it does not affect the caller
def try_to_steal_diamonds(amount):
    amount = 0           # only changes the local copy inside this function
    print("Inside steal function, amount:", amount)   # → 0

player_diamonds = 64
try_to_steal_diamonds(player_diamonds)
print("Player still has:", player_diamonds)  # → 64  (unchanged!)


# Mad Libs: parameters carry words into the story — local to the function
def mad_libs_line(animal, verb):
    line = "The " + animal + " " + verb + " over the lava pit!"
    print(line)
    # 'line' is local — it disappears when the function ends

mad_libs_line("creeper", "jumped")   # → The creeper jumped over the lava pit!
mad_libs_line("enderman", "floated") # → The enderman floated over the lava pit!
# print(line)  ← NameError — 'line' only existed inside the function
```

#### Talking Points

- "When you pass a variable to a function, Python hands the function a **copy** — like making a photocopy of your Minecraft map. You can scribble on the copy all you want; the original stays clean."
- "Parameters are local variables that already have a value before the first line of the function runs."
- "In the Mad Libs example, `animal` and `verb` exist only while `mad_libs_line` is running. Once it's done, they're gone."

#### Quick Check Questions

1. A function has `def respawn(player_lives)`. If the function does `player_lives = 0` inside it, does the caller's variable change?
2. After `mad_libs_line("creeper", "jumped")` finishes, can you print `animal` outside the function?
3. What is the difference between a parameter and a regular local variable?

---

### Part C — Variables Outside Functions (Global Variables)

#### What to Teach

- A variable created **outside all functions** is called a **global variable**.
- Global variables can be **read** (looked at) from anywhere in the file, including inside functions.
- Reading a global inside a function requires no special keyword.
- However, **assigning** a new value to a name inside a function creates a brand-new local variable — it does **not** change the global, even if the names match.

#### Key Vocabulary

| Word            | Meaning                                                                             |
| --------------- | ----------------------------------------------------------------------------------- |
| global variable | A variable created outside all functions; readable anywhere                         |
| shadowing       | When a local variable has the same name as a global, hiding it inside that function |

#### Minecraft / Mad Libs Example Code

```python
# Minecraft: global world name readable everywhere
world_name = "SkyBlock"         # global variable

def print_world_banner():
    print("=== Welcome to", world_name, "===")   # reading global — allowed!

print_world_banner()             # → === Welcome to SkyBlock ===
print("Still here:", world_name) # → Still here: SkyBlock


# Watch out — assigning INSIDE a function creates a new local, NOT changing the global
high_score = 0                   # global

def fake_update():
    high_score = 9999            # NEW local variable — global is untouched!
    print("Inside:", high_score) # → Inside: 9999

fake_update()
print("Global unchanged:", high_score)  # → Global unchanged: 0


# Mad Libs: global story title read inside a function
story_title = "The Day the Creeper Laughed"

def print_story_header():
    print("Story:", story_title)   # reading global — works fine

print_story_header()
```

#### Talking Points

- "Global variables are like a sign posted at the entrance to your Minecraft world — every function in the file can read it."
- "But if a function tries to _write_ a new value to `high_score` without permission, Python makes it write on its own sticky note instead — the real sign stays the same."
- "This protects globals from being accidentally changed deep inside a function."

#### Quick Check Questions

1. Can a function read a global variable without any special keyword?
2. If a function does `high_score = 9999` inside itself, does the global `high_score` change? Why not?
3. What is the difference between _reading_ a global and _assigning_ to a global inside a function?

---

### Part D — When Functions CAN Alter a Global Variable (`global` keyword)

#### What to Teach

- To **modify** (not just read) a global variable inside a function, you must declare it with the `global` keyword **at the top** of the function.
- `global variable_name` tells Python: "I mean the one from outside — not a new local copy."
- This is powerful but should be used carefully — overusing `global` makes programs harder to follow.
- A better everyday habit is to `return` the updated value and reassign it outside the function.

#### Key Vocabulary

| Word     | Meaning                                                                               |
| -------- | ------------------------------------------------------------------------------------- |
| `global` | Keyword that tells Python to use the existing global variable, not create a local one |
| modify   | Changing the value of a variable (not just reading it)                                |

#### Minecraft / Mad Libs Example Code

```python
# Minecraft: tracking player lives with global
lives = 3

def lose_a_life():
    global lives           # declare: use the one from outside
    lives = lives - 1
    print("Lives left:", lives)

lose_a_life()   # → Lives left: 2
lose_a_life()   # → Lives left: 1
print("Final lives:", lives)   # → Final lives: 1


# Minecraft: accumulating a score across multiple events
player_score = 0

def collect_diamonds(amount):
    global player_score
    player_score = player_score + amount
    print("Score now:", player_score)

collect_diamonds(10)   # → Score now: 10
collect_diamonds(25)   # → Score now: 35
collect_diamonds(5)    # → Score now: 40


# Mad Libs: counting how many words have been collected
words_collected = 0

def collect_word(prompt):
    global words_collected
    word = input(prompt)
    words_collected = words_collected + 1
    return word

noun   = collect_word("Type a noun: ")
animal = collect_word("Type an animal: ")
print("You've collected", words_collected, "words so far!")


# -------------------------------------------------------
# PREFERRED PATTERN: return instead of global
# -------------------------------------------------------
def safer_lose_a_life(current_lives):
    return current_lives - 1       # return the new value instead

lives = 3
lives = safer_lose_a_life(lives)   # reassign outside
lives = safer_lose_a_life(lives)
print("Final lives:", lives)       # → Final lives: 1
```

#### Talking Points

- "The `global` keyword is like getting the master key to the Minecraft world's scoreboard — now you can actually _change_ what's on it, not just read it."
- "Without `global`, Python assumes any assignment inside a function is a brand-new local variable — it protects the global by default."
- "Most programmers avoid `global` when possible. The `return` version is cleaner — you can see exactly what changed and where."
- "Knowing `global` exists explains _why_ things sometimes don't change when you expect them to — now you know what to look for."

#### Quick Check Questions

1. What keyword lets a function _modify_ a global variable?
2. Write a function `add_points(amount)` that adds `amount` to a global `player_score`.
3. What is the safer alternative to `global` that we learned in Lesson 5.3?
4. Without `global`, what does Python do when it sees `lives = 0` inside a function where `lives` also exists as a global?

---

### Scope Summary Table

| Situation                       | Can the function read it? | Can the function change it?           | How?                      |
| ------------------------------- | ------------------------- | ------------------------------------- | ------------------------- |
| Local variable (created inside) | Yes                       | Yes — it belongs to the function      | just assign               |
| Parameter variable              | Yes                       | Yes — but only the local copy changes | just assign               |
| Global variable — reading only  | Yes                       | —                                     | no keyword needed         |
| Global variable — modifying     | Yes                       | Yes                                   | must use `global` keyword |

### Concepts Covered in `5_6_variable_scope.py`

1. Local variable disappears after the function ends
2. Two functions with the same variable name are independent
3. Parameters are local variables — reassigning one doesn't affect the caller
4. Global variables can be read inside a function without any special keyword

> **Note:** The `global` keyword and the "preferred return pattern" examples above are not yet in `5_6_variable_scope.py` — write them live with the student or add them to the file as a Part 5.

### Talking Points — Big Picture

- "Scope is all about _ownership_. Every variable belongs to either a specific function or the whole file."
- "Functions are meant to be self-contained. Passing data in through parameters and getting data back through `return` keeps everything clean — like a well-organised Minecraft chest."
- "Understanding scope prevents a whole class of bugs where you think you changed something but you actually changed a local copy."

---

## Unit Summary

| Lesson | Topic                         | Key Skill                                                                         |
| ------ | ----------------------------- | --------------------------------------------------------------------------------- |
| 5.1    | Intro to Functions            | `def`, calling a function                                                         |
| 5.2    | Parameters                    | Passing data into a function                                                      |
| 5.3    | Return — Single Value         | Getting data back out                                                             |
| 5.3b   | Optional / Default Parameters | Default values — Minecraft biomes, mobs, Mad Libs punctuation                     |
| 5.3c   | Return — Multiple Values      | Returning and unpacking a tuple                                                   |
| 5.4    | Minecraft Chat Project        | All skills applied together                                                       |
| 5.5    | Mad Libs Project              | Refactoring with functions                                                        |
| 5.6    | Variable Scope                | Local, parameter, global, `global` keyword — all with Minecraft/Mad Libs examples |

### Big Ideas to Reinforce

- Functions make code **reusable** and **readable**.
- Parameters send data **in**; `return` sends data **out**.
- Default parameters make functions **flexible without extra effort**.
- Returning multiple values lets one function answer more than one question.
- Local scope keeps functions **independent** — changes inside do not break outside.
