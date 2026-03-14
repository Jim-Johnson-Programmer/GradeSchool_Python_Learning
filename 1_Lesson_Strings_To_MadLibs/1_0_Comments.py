# ============================================================
# Lesson 1.0 - Comments
# ============================================================
# A COMMENT is a note you write in your code FOR HUMANS.
# Python ignores comments completely — they do NOT run.
# Comments help YOU (and others) understand what the code does.
# ============================================================


# ============================================================
# PART 1: Single-Line Comments
# ============================================================
# A single-line comment starts with the # symbol.
# Everything after the # on that line is ignored by Python.

# This is a comment. Python skips right over it.
print("This line DOES run!")   # You can also add a comment at the end of a line

# Notice: the print above runs, but the comment next to it does not.


# ============================================================
# PART 2: Multi-Line Comments (Block Comments)
# ============================================================
# If you have a lot to say, you can use triple quotes.
# This is called a multi-line comment or a "docstring".
# Python also ignores this text.

"""
This is a multi-line comment.
You can write as many lines as you want inside triple quotes.
Great for longer explanations!
"""

# Let's prove Python still runs code after a multi-line comment:
print("Multi-line comments don't stop the code!")


# ============================================================
# PART 3: CODE vs. COMMENTS — Side by Side
# ============================================================
# Below, each piece of CODE is paired with a COMMENT explaining it.
# See how comments describe WHAT the code is doing.

# --- Code runs, comment explains ---

name = "Sam"                    # Store the name "Sam" in a variable
print("Hello, " + name + "!")   # Print a greeting using that name

age = 10                        # Store the number 10 in a variable called age
print("I am " + str(age) + " years old.")  # Print the age as part of a sentence


# ============================================================
# PART 4: Commenting OUT Code
# ============================================================
# You can "turn off" a line of code by putting a # in front.
# This is called commenting OUT — useful for testing!

print("This line runs.")
# print("This line is commented out — it does NOT run.")
print("This line runs too.")


# ============================================================
# PART 5: Why Comments Matter
# ============================================================

# BAD example — no comments, hard to understand:
x = 5
y = 3
z = x + y
print(z)

# GOOD example — comments make it clear:
apples = 5        # number of apples in the basket
oranges = 3       # number of oranges in the basket
total = apples + oranges   # add them together
print(total)      # prints the total number of fruits


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Write a single-line comment above a print() that explains what it prints.
# 2. Write a multi-line comment describing your favorite game.
# 3. Comment OUT one of your print() lines and run the code — what happens?
# ============================================================
