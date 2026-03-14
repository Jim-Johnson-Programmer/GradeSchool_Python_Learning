# ============================================================
# Lesson 1.1 - Strings
# ============================================================
# A STRING is just text! Any letters, words, or sentences
# inside quotes are called a string.
# You can use single quotes '' or double quotes ""
# ============================================================


# --- PART 1: Your First String ---
# The print() function shows text on the screen.

print("Hello, World!")
print('Python is awesome!')


# --- PART 2: Strings Can Be Stored in Variables ---
# A variable is like a labeled box that holds information.

my_name = "Alex"
my_pet  = "a golden retriever"

print(my_name)
print(my_pet)


# --- PART 3: Joining Strings Together (Concatenation) ---
# You can glue strings together using the + sign.

first_name = "Super"
last_name  = "Coder"

full_name = first_name + last_name
print(full_name)           # prints: SuperCoder

# Add a space between them:
full_name_with_space = first_name + " " + last_name
print(full_name_with_space)   # prints: Super Coder


# --- PART 4: String Length ---
# len() tells you how many characters are in a string.

word = "Dinosaur"
print(len(word))    # prints: 8


# --- PART 5: UPPER and lower case ---
# .upper() makes everything CAPITAL letters.
# .lower() makes everything small letters.

animal = "elephant"
print(animal.upper())   # prints: ELEPHANT
print(animal.lower())   # prints: elephant


# --- PART 6: Putting It All Together ---
# Let's use everything we learned!

favorite_food = "pizza"
print("My favorite food is " + favorite_food + "!")
print("It has " + str(len(favorite_food)) + " letters.")


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Create a variable called my_hobby and store your hobby in it.
# 2. Print: "I love " + my_hubby + "!"
# 3. Print my_hubby in ALL CAPS using .upper()
# 4. Print how many letters are in your hobby using len()
# ============================================================
