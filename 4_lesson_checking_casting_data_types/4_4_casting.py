# ============================================================
# Lesson 4.4 - Casting (Converting Between Data Types)
# ============================================================
# Sometimes you have a value in one type but you NEED it in
# a different type.  Changing a value's type is called CASTING.
#
# The three casting functions you will use most:
#
#   int(x)    → converts x into a whole number
#   float(x)  → converts x into a decimal number
#   str(x)    → converts x into text
#
# ============================================================


# ============================================================
# PART 1: str → int  (text to whole number)
# ============================================================
# If a string contains only digits, you can turn it into an int.
# The leading zeros and any spaces will disappear.

text_number = "42"
real_number = int(text_number)
print(text_number, type(text_number))   # 42 <class 'str'>
print(real_number, type(real_number))   # 42 <class 'int'>

# What happens to leading zeros when we cast?
code_string  = "007"
code_integer = int(code_string)
print("str: " + code_string)           # 007  ← keeps the zeros
print("int:", code_integer)            # 7    ← zeros are gone!

# What about a string with spaces around the number?
spaced = "  15  "                      # spaces before and after
print(int(spaced))                     # 15  ← int() trims the spaces for us


# ============================================================
# PART 2: str → float  (text to decimal number)
# ============================================================
# Use float() when the string has (or might have) a decimal point.

text_price = "3.99"
real_price = float(text_price)
print(text_price, type(text_price))    # 3.99 <class 'str'>
print(real_price, type(real_price))    # 3.99 <class 'float'>

# int() would CRASH on a decimal string — use float() instead:
# int("3.99")   ← this would cause an error!

# Two-step trick: str with decimal → float → int (drops the decimal)
raw    = "9.75"
as_float = float(raw)     # 9.75
as_int   = int(as_float)  # 9  ← decimal part is cut off (not rounded!)
print(as_float)   # 9.75
print(as_int)     # 9


# ============================================================
# PART 3: int or float → str  (number to text)
# ============================================================
# Use str() when you want to JOIN a number into a sentence.
# Python does not let you glue a number directly onto a string.

player_score = 500

# This would CRASH without str():
# print("Your score: " + player_score)  ← TypeError!

# Correct way:
print("Your score: " + str(player_score))   # Your score: 500

# Same for floats:
pi = 3.14159
print("Pi is about " + str(pi))   # Pi is about 3.14159

# Note: when you cast an int with leading zeros in your code,
# the zeros are already gone — str() cannot bring them back.
agent = 7
print(str(agent))        # "7"   ← not "007", the int never had zeros


# ============================================================
# PART 4: int ↔ float  (whole number ↔ decimal)
# ============================================================

whole  = 4
decimal = float(whole)    # 4.0
print(decimal)            # 4.0

decimal2 = 7.9
chopped  = int(decimal2)  # 7  ← decimal part cut off (not rounded!)
print(chopped)            # 7

# Be careful: int() always cuts (truncates), it does NOT round!
print(int(2.9))   # 2  ← NOT 3
print(int(-2.9))  # -2 ← NOT -3


# ============================================================
# PART 5: The Most Common Casting Mistake — input()
# ============================================================
# input() ALWAYS returns a str.
# If you need math, you must cast it to int or float first.

print("--- Calculator ---")
raw_a = input("Enter first number : ")
raw_b = input("Enter second number: ")

# Without casting, + would JOIN the strings, not add!
print("Joined (wrong) :", raw_a + raw_b)          # e.g. "35"

# Cast first, then do math:
num_a = int(raw_a)
num_b = int(raw_b)
print("Added  (right) :", num_a + num_b)           # e.g. 8


# ============================================================
# PART 6: When Casting Goes Wrong — Errors to Know
# ============================================================
# Not every cast is possible.  Here are the common errors
# and how to avoid them.

# --- int("hello") CRASHES ---
# You cannot turn random text into a number.
# Only try int() if the string is actually a number.

# Uncomment to see the error:
# print(int("hello"))    # ValueError: invalid literal for int()

# --- int("3.14") CRASHES ---
# int() cannot skip over the decimal point.
# Use float() first, then int() if you must.

# Uncomment to see the error:
# print(int("3.14"))     # ValueError: invalid literal for int()

# Safe version:
print(int(float("3.14")))   # 3  ← works fine

# --- Leading zeros after casting back to str ---
# Once you convert "007" to an int, the zeros are permanently gone.
# str(7) gives "7", not "007".
# If you need to keep leading zeros, KEEP IT AS A STRING!

badge = "007"            # store as str to keep the zeros
badge_num = int(badge)   # now it is 7

print("Badge str :", badge)          # 007
print("Badge int :", badge_num)      # 7
print("Back to str:", str(badge_num)) # "7"  ← zeros gone forever


# ============================================================
# PART 7: Putting It All Together — Mini Paycheck Calculator
# ============================================================

print("")
print("=============================")
print("    Mini Paycheck Calculator ")
print("=============================")

raw_hours = input("Hours worked this week : ")
raw_rate  = input("Pay per hour (dollars) : ")

hours = float(raw_hours)   # could be 7.5 hours
rate  = float(raw_rate)    # could be $12.50

total_pay = hours * rate

print("You earned $" + str(round(total_pay, 2)) + " this week!")
