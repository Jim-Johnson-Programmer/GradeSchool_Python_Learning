# ============================================================
# Lesson 7.1 - If Statements
# ============================================================
# An IF STATEMENT lets your program make a DECISION.
# It asks a YES or NO question and runs different code
# depending on the answer.
#
# Key words:
#   if    — checks a condition; runs the block if True
#   elif  — short for "else if"; checks another condition
#   else  — runs when none of the above conditions are True
#
# The condition must be True or False (a bool).
# Everything INDENTED underneath belongs to that branch.
# ============================================================


# ============================================================
# PART 1: A Simple if Statement
# ============================================================
# Structure:
#   if <condition>:
#       <code that runs when condition is True>

score = 85

if score >= 60:
    print("You passed!")        # → You passed!

# The line below is NOT indented, so it always runs:
print("Done checking score.")   # → Done checking score.


# ============================================================
# PART 2: if / else
# ============================================================
# Use else to handle the case when the condition is False.

lives = 0

if lives > 0:
    print("Keep playing!")
else:
    print("Game over!")         # → Game over!


# ============================================================
# PART 3: if / elif / else
# ============================================================
# Use elif to check more conditions in order.
# Python checks them TOP to BOTTOM and runs the FIRST one
# that is True — then skips the rest.

score = 78

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")              # → C   (78 is >= 70, so this runs)
elif score >= 60:
    print("D")
else:
    print("F")


# ============================================================
# PART 4: Comparison Operators
# ============================================================
# These are used to build conditions:
#
#   ==   equal to             5 == 5   → True
#   !=   not equal to         5 != 3   → True
#   >    greater than         7 > 2    → True
#   <    less than            2 < 7    → True
#   >=   greater or equal     5 >= 5   → True
#   <=   less or equal        4 <= 6   → True

x = 10

print(x == 10)   # → True
print(x != 10)   # → False
print(x > 5)     # → True
print(x < 5)     # → False
print(x >= 10)   # → True
print(x <= 9)    # → False


# ============================================================
# PART 5: Combining Conditions with and / or / not
# ============================================================
# and  — BOTH sides must be True
# or   — AT LEAST ONE side must be True
# not  — flips True → False  or  False → True

age = 14
has_permission = True

if age >= 13 and has_permission:
    print("Welcome to the game!")   # → Welcome to the game!

if age < 10 or has_permission:
    print("Access granted.")        # → Access granted.

is_raining = False
if not is_raining:
    print("Go outside!")            # → Go outside!


# ============================================================
# PART 6: Checking String Values
# ============================================================
# You can compare strings the same way with == and !=

player_name = "Eric"

if player_name == "Eric":
    print("Hi Eric!")           # → Hi Eric!
else:
    print("Hello, stranger!")


# ============================================================
# PART 7: Nested if Statements
# ============================================================
# You can put an if statement INSIDE another if statement.
# Each extra level needs one more level of indentation.

health = 30
has_potion = True

if health < 50:
    print("Health is low!")         # → Health is low!
    if has_potion:
        print("Used a potion!")     # → Used a potion!
        health = health + 25
        print("Health is now:", health)   # → Health is now: 55
    else:
        print("No potion available.")


# ============================================================
# PART 8: Mini Quiz — What Does This Print?
# ============================================================
# Try to guess the output BEFORE you run the code.

temperature = 72

if temperature > 90:
    print("It is very hot.")
elif temperature > 70:
    print("It is warm.")        # ← what prints?
elif temperature > 50:
    print("It is cool.")
else:
    print("It is cold.")

# Answer: "It is warm."   because 72 > 70 is True (and 72 > 90 is False)
