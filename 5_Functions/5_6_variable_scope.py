# ============================================================
# Lesson 5.6 - Variable Scope
# ============================================================
# A variable created INSIDE a function is called a LOCAL variable.
# It only exists while the function is running.
# Once the function finishes, that variable disappears.
# Code OUTSIDE the function cannot see or use it.
#
# This is called SCOPE — where a variable is visible.
#
#   def my_function():
#       secret = "I only exist inside here"
#
#   print(secret)   ← ERROR! Python has no idea what 'secret' is
#
# Think of a function like a room with no windows.
# Variables made inside the room stay IN the room.
# ============================================================


# ============================================================
# PART 1: A Local Variable Stays Inside the Function
# ============================================================

def make_message():
    inside_variable = "Hello from inside the function!"
    print(inside_variable)   # this works — we are still inside

make_message()

# Uncomment the line below and run it to see the error:
# print(inside_variable)    # NameError: name 'inside_variable' is not defined


# ============================================================
# PART 2: Two Functions — Each Has Its OWN Local Variables
# ============================================================
# Even if two functions use the same variable NAME, they are
# completely separate — changing one does NOT affect the other.

def function_a():
    score = 100
    print("function_a score:", score)

def function_b():
    score = 999          # same name, but a DIFFERENT variable
    print("function_b score:", score)

function_a()
function_b()
# Each function has its own private 'score' — they never mix.


# ============================================================
# PART 3: Parameters Are Local Too
# ============================================================
# Parameters are really just local variables that get their
# starting value from what you pass in when you call the function.

def double(number):
    result = number * 2
    return result

answer = double(7)
print("Doubled:", answer)

# Uncomment the lines below to see that 'number' and 'result'
# are gone once the function finishes:
# print(number)    # NameError
# print(result)    # NameError


# ============================================================
# PART 4: Global vs Local — Spot the Difference
# ============================================================
# A variable created OUTSIDE any function is called GLOBAL.
# It can be read anywhere in the file.

player_name = "Eric"     # global variable — created outside all functions

def greet_player():
    print("Welcome,", player_name)   # reading a global is allowed

greet_player()
print("Still available:", player_name)   # global works outside too
