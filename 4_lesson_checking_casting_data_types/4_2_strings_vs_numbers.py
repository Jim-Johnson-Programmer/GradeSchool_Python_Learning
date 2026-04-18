# ============================================================
# Lesson 4.2 - Tricky Differences Between Strings and Numbers
# ============================================================
# Strings and numbers can *look* the same but behave VERY
# differently.  This lesson covers the most common surprises:
#
#   1. Leading zeros  — "007" vs 7
#   2. Spaces         — " cat" vs "cat"  and  " 5" vs 5
#   3. + means JOIN for strings, ADD for numbers
#   4. Comparing a string to a number
#   5. input() always returns a string — even if you type a number
# ============================================================


# ============================================================
# PART 1: Leading Zeros — Strings Keep Them, Numbers Drop Them
# ============================================================
# A number can never start with a zero (except 0 itself).
# Python would get confused: does 007 mean 7? Or something else?
# So Python simply does not allow integers with leading zeros.
#
# But a STRING doesn't care — it stores every single character,
# including zeros at the front!

secret_agent_text   = "007"   # str — keeps both leading zeros
secret_agent_number = 7       # int — no leading zeros allowed

print("String version :", secret_agent_text)    # 007
print("Number version :", secret_agent_number)  # 7

# Other real-world examples where leading zeros matter:
zip_code    = "07302"   # ZIP codes must keep the leading zero!
phone_ext   = "0812"    # extension numbers often start with 0
student_id  = "00042"   # ID badges with fixed-width numbers

print("ZIP code   :", zip_code)     # 07302
print("Phone ext  :", phone_ext)    # 0812
print("Student ID :", student_id)   # 00042

# If we stored these as ints, the leading zeros would vanish:
zip_as_int = 7302
print("ZIP as int :", zip_as_int)   # 7302  ← oops, wrong ZIP!


# ============================================================
# PART 2: Spaces — Every Character Counts in a String
# ============================================================
# A space is a real character.  " cat" and "cat" are different!
# This surprises a lot of people, especially with input().

word_a = "cat"
word_b = " cat"    # one space at the front

print("word_a =", word_a)            # cat
print("word_b =", word_b)            #  cat   ← notice the gap
print("Are they equal?", word_a == word_b)   # False!

# Length proves the difference:
print("Length of 'cat'  :", len(word_a))   # 3
print("Length of ' cat' :", len(word_b))   # 4

# Spaces can be at the START, the END, or in the MIDDLE:
padded   = "  hello  "    # two spaces before, two after
print("padded ='" + padded + "'")   # '  hello  '
print("length  :", len(padded))     # 9

# .strip() removes spaces from both ends (very useful!):
clean = padded.strip()
print("clean  ='" + clean + "'")    # 'hello'
print("length  :", len(clean))      # 5


# ============================================================
# PART 3: + Means JOIN for Strings, ADD for Numbers
# ============================================================
# The + operator has two completely different jobs:
#   str  + str  → joins (concatenates) the text
#   int  + int  → adds  the numbers

# --- Strings: + JOINS ---
part_one = "5"
part_two = "3"
result_text = part_one + part_two
print("String + String:", result_text)   # "53"  ← NOT 8!

# --- Numbers: + ADDS ---
num_one = 5
num_two = 3
result_num = num_one + num_two
print("  Int  +   Int :", result_num)    # 8

# More string-joining surprises:
print("10" + "20")    # "1020"  — joined, not added
print("9"  + "1")     # "91"    — joined, not added

# To actually add the numbers, convert them first:
print(int("10") + int("20"))   # 30  ← correct math
print(int("9")  + int("1"))    # 10  ← correct math


# ============================================================
# PART 4: Comparing a String to a Number — They Are Never Equal
# ============================================================
# Even if they look the same, a string and an int/float
# are NEVER == to each other.

print("5" == 5)       # False — one is str, one is int
print("3.14" == 3.14) # False — one is str, one is float
print("True" == True) # False — one is str, one is bool
print("0" == 0)       # False — one is str, one is int

# Why does this matter?
user_score = "10"   # imagine this came from input()
high_score = 10     # stored as an int in our program

# This check will NEVER be True, even if the user typed "10":
if user_score == high_score:
    print("New high score!")
else:
    print("No match — types are different!")   # this line runs

# Fix: convert first
if int(user_score) == high_score:
    print("Now it matches!")   # this line runs


# ============================================================
# PART 5: input() Always Returns a String
# ============================================================
# This is the most common surprise for new programmers.
# No matter what the user types, input() gives back a STRING.

print("--- Testing input() type ---")
user_age = input("How old are you? ")

# user_age is a str, even if they typed a number like 12
print("You typed:", user_age)
print("Type is  :", type(user_age))    # <class 'str'>

# This comparison would be broken without a conversion:
# if user_age > 10:   ← ERROR! Can't compare str > int

# Always cast first!
age_as_int = int(user_age)
if age_as_int > 10:
    print("You are older than 10!")
else:
    print("You are 10 or younger!")
