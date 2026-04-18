# ============================================================
# Lesson 4.3 - Checking Data Types with type()
# ============================================================
# How can you ask Python "what TYPE is this value?"
# Use the built-in type() function!
#
#   type(value)  → tells you the type of that value
#
# The answer looks like:  <class 'str'>  or  <class 'int'>
# Don't be scared by the word "class" — it just means TYPE.
# ============================================================


# ============================================================
# PART 1: Basic type() Examples
# ============================================================

print( type("hello") )        # <class 'str'>
print( type(42) )             # <class 'int'>
print( type(3.14) )           # <class 'float'>
print( type(True) )           # <class 'bool'>

# You can also check a variable:
name  = "Alex"
score = 99
price = 0.99
won   = True

print( type(name)  )    # <class 'str'>
print( type(score) )    # <class 'int'>
print( type(price) )    # <class 'float'>
print( type(won)   )    # <class 'bool'>


# ============================================================
# PART 2: Strings That Look Like Numbers Are Still Strings
# ============================================================
# If quotes are involved — it is a str, full stop.

a = "100"     # looks like a number but has quotes → str
b = "3.14"    # same story
c = "True"    # spelled like a bool but has quotes → str
d = "007"     # leading zeros kept because it is a str

print( type(a) )    # <class 'str'>
print( type(b) )    # <class 'str'>
print( type(c) )    # <class 'str'>
print( type(d) )    # <class 'str'>

# Compare the str versions to the real types:
print( type(100) )      # <class 'int'>
print( type(3.14) )     # <class 'float'>
print( type(True) )     # <class 'bool'>


# ============================================================
# PART 3: isinstance() — Asking a True/False Question
# ============================================================
# type() tells you WHAT the type is.
# isinstance() lets you ASK: "Is this value a certain type?"
# It gives back True or False — perfect for if/else checks.
#
#   isinstance(value, type_name)

value = "hello"

print( isinstance(value, str)   )   # True
print( isinstance(value, int)   )   # False
print( isinstance(value, float) )   # False


# ============================================================
# PART 4: Using isinstance() in an if Statement
# ============================================================

def describe_type(thing):
    if isinstance(thing, str):
        print(repr(thing), "is a STRING")
    elif isinstance(thing, bool):
        # bool must be checked BEFORE int because
        # True and False are technically also ints in Python!
        print(repr(thing), "is a BOOL")
    elif isinstance(thing, int):
        print(repr(thing), "is an INT")
    elif isinstance(thing, float):
        print(repr(thing), "is a FLOAT")
    else:
        print(repr(thing), "is something else")

describe_type("007")    # is a STRING
describe_type(7)        # is an INT
describe_type(7.0)      # is a FLOAT
describe_type(True)     # is a BOOL
describe_type("3.14")   # is a STRING  ← quotes make it text!


# ============================================================
# PART 5: Why bool Must Be Checked Before int
# ============================================================
# This is a funny Python quirk:
#   True  is treated like 1
#   False is treated like 0
# So isinstance(True, int) returns True!
# Always check for bool FIRST if you need to tell them apart.

print( isinstance(True, int)  )    # True  ← surprising!
print( isinstance(True, bool) )    # True
print( isinstance(1,    bool) )    # False — 1 is an int, not a bool


# ============================================================
# PART 6: Practice — What Type Is Each Value?
# ============================================================
# Look at each variable below.
# BEFORE running the code, try to guess what type() will say.
# Then run it and check your answers!

mystery_1 = "0"
mystery_2 = 0
mystery_3 = 0.0
mystery_4 = False
mystery_5 = " "      # just a space
mystery_6 = ""       # empty string

print( type(mystery_1) )   # guess first!
print( type(mystery_2) )
print( type(mystery_3) )
print( type(mystery_4) )
print( type(mystery_5) )
print( type(mystery_6) )
