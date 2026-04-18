# ============================================================
# Lesson 4.1 - Introducing Data Types
# ============================================================
# Every value in Python has a DATA TYPE.
# The type tells Python WHAT kind of thing the value is
# and WHAT you are allowed to do with it.
#
# The four main types we will learn about:
#
#   str   — text (short for "string")
#   int   — whole numbers (short for "integer")
#   float — decimal numbers (short for "floating point")
#   bool  — True or False (short for "boolean")
# ============================================================


# ============================================================
# PART 1: str  (text / string)
# ============================================================
# Anything inside quotes is a str.
# It can be a single letter, a word, a sentence,
# a number that looks like text, or even empty!

greeting    = "Hello, world!"   # a sentence
first_name  = "Eric"            # a word
digit_text  = "9"               # looks like a number — but it is TEXT
empty_str   = ""                # a string with nothing in it

print(greeting)
print(first_name)
print(digit_text)
print(empty_str)


# ============================================================
# PART 2: int  (whole number / integer)
# ============================================================
# An int is a number with NO decimal point.
# It can be positive, negative, or zero.
# IMPORTANT: do NOT put quotes around it — that would make it a str!

score       = 100
temperature = -5
nothing     = 0

print(score)
print(temperature)
print(nothing)


# ============================================================
# PART 3: float  (decimal number)
# ============================================================
# A float has a decimal point somewhere in it.
# Even "3.0" is a float because it has the dot.

price       = 2.99
pi          = 3.14159
half        = 0.5
whole_float = 4.0       # still a float even though the decimal part is 0

print(price)
print(pi)
print(half)
print(whole_float)


# ============================================================
# PART 4: bool  (True / False)
# ============================================================
# A bool can only be one of two values: True  or  False
# Notice: capital T and capital F — spelling matters!
# Python uses bools whenever it needs to make a YES/NO decision.

is_raining  = False
has_won     = True
game_over   = False

print(is_raining)
print(has_won)
print(game_over)


# ============================================================
# PART 5: Each Type Has Its Own "Superpower"
# ============================================================
# str   → you can join text, count letters, make it UPPER or lower
# int   → you can add, subtract, multiply, divide (whole results)
# float → you can do math with decimals
# bool  → you can make decisions with if/else

# --- str superpower: joining text ---
first = "Super"
last  = "Coder"
print(first + last)           # SuperCoder

# --- int superpower: whole-number math ---
apples = 3
oranges = 5
total_fruit = apples + oranges
print(total_fruit)            # 8

# --- float superpower: decimal math ---
item_price = 1.25
quantity   = 4
total_cost = item_price * quantity
print(total_cost)             # 5.0

# --- bool superpower: making a decision ---
lives_left = 0
game_over  = lives_left == 0   # True if no lives remain
if game_over:
    print("Game Over!")
else:
    print("Keep playing!")
