# ============================================================
# Lesson 1.1 - Strings
# ============================================================
# A STRING is just text! Any letters, words, or sentences
# inside quotes are called a string.
# You can use single quotes '' or double quotes ""
# ============================================================


# --- PART 1: Your First String ---
# The print() function shows text on the screen.

# print("Hello, World!")
# print('Python is awesome!')


# --- PART 2: Strings Can Be Stored in Variables ---
# A variable is like a labeled box that holds information.

# my_name = "Eric"
# my_pet  = "alaskan husky"

# print(my_name)
# print(my_pet)


# --- PART 3: Joining Strings Together (Concatenation) ---
# You can glue strings together using the + sign.

# first_name = "Eric"
# last_name  = "Choi"

# full_name = first_name + last_name
# print(full_name)           # prints: SuperCoder

# # Add a space between them:
# full_name_with_space = first_name + " " + last_name
# print(full_name_with_space)   # prints: Super Coder


# # --- PART 4: String Length ---
# # len() tells you how many characters are in a string.

# if False:
#     print("this is true")
#     print("this is also true")
# else:
#     print("this is false")



# word = "Dinosaur"
# print(len(word))    # prints: 8

# if len(word) > 0:
#     print("The word is not empty!")
# else:
#     print("The word is empty!")


# # --- PART 5: UPPER and lower case ---
# # .upper() makes everything CAPITAL letters.
# # .lower() makes everything small letters.


animal = "elephant"
print(animal.upper())   # prints: ELEPHANT
print(animal.lower())   # prints: elephant

animal_mixed_case = "eLePhAnT"
animal_all_caps = "ELEPHANT"

user_input = input("Type the word 'elephant': ")
if user_input == "elephant":
    print("You typed it correctly!")

# # --- PART 6: Putting It All Together ---
# # Let's use everything we learned!

# favorite_food = "pizza"
# print("My favorite food is " + favorite_food + "!")
# print("It has " + str(len(favorite_food)) + " letters.")


# # ============================================================
# # YOUR TURN! Try these challenges:
# # 1. Create a variable called my_hobby and store your hobby in it.
# # 2. Print: "I love " + my_hubby + "!"
# # 3. Print my_hubby in ALL CAPS using .upper()
# # 4. Print how many letters are in your hobby using len()
# # ============================================================
