# ============================================================
# Lesson 1.2 - User Input
# ============================================================
# So far we have been typing information directly into the code.
# But what if we want the USER to type something while the
# program is running?
#
# We use the input() function!
# input() pauses the program, waits for the user to type
# something and press Enter, then stores what they typed.
# ============================================================


# ============================================================
# PART 1: Basic input()
# ============================================================
# The text inside input("...") is the PROMPT — it tells the
# user what to type.  What they type is saved in a variable.

name = input("What is your name? ")

# Now let's print it back out!
print("Nice to meet you, " + name + "!")


# ============================================================
# PART 2: Asking Multiple Questions
# ============================================================
# You can call input() as many times as you like.

favorite_color = input("What is your favorite color? ")
favorite_animal = input("What is your favorite animal? ")

print("Wow, a " + favorite_color + " " + favorite_animal + " sounds amazing!")


# ============================================================
# PART 3: Using the Variable More Than Once
# ============================================================
# Once the answer is stored in a variable you can use it
# as many times as you want — no need to ask again!

player_name = input("Enter your player name: ")

print("Welcome, " + player_name + "!")
print(player_name + " has entered the game.")
print("Good luck, " + player_name + ". Let's play!")


# ============================================================
# PART 4: Code vs. Input — What is the Difference?
# ============================================================

# HARD-CODED  — the value is typed directly in the code.
#               It is always the same no matter who runs the program.
hard_coded_name = "Alex"
print("Hello, " + hard_coded_name)   # always prints "Hello, Alex"

# USER INPUT  — the value comes from whoever is running the program.
#               It changes every time depending on what they type!
user_name = input("Type your name: ")
print("Hello, " + user_name)         # prints whatever the user typed


# ============================================================
# PART 5: Putting It All Together — Mini Introduction Program
# ============================================================

print("--- Tell Me About Yourself ---")

your_name    = input("What is your name? ")
your_age     = input("How old are you? ")
your_hobby   = input("What is your favorite hobby? ")

print("")   # prints a blank line for spacing
print("Here is what I know about you:")
print("Name  : " + your_name)
print("Age   : " + your_age)
print("Hobby : " + your_hobby)
print("You sound like a really cool person, " + your_name + "!")


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Ask the user for their favorite food and print:
#    "Yum! I love [food] too!"
# 2. Ask for a first name AND a last name separately, then
#    print the full name by joining them together with a space.
# 3. Ask the user to type a word, then print it in ALL CAPS
#    using .upper()
# ============================================================
