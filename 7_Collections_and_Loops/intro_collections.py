# ============================================================
# Lesson 7.0 - Introduction to Collections and Loops
# ============================================================
# A COLLECTION is a variable that holds MULTIPLE values at once.
# A LOOP is a way to repeat code — often once for each item
# in a collection.
#
# Together, collections + loops are some of the most powerful
# tools in Python. Almost every real program uses them.
# ============================================================


# ============================================================
# The Four Collection Types in Python
# ============================================================
#
#   Type         | Syntax  | Ordered | Mutable | Duplicates | Access By
#   -------------|---------|---------|---------|------------|----------
#   list         |  [ ]    |   Yes   |   Yes   |    Yes     | index
#   tuple        |  ( )    |   Yes   |   No    |    Yes     | index
#   set          |  { }    |   No    |   Yes   |    No      | (no index)
#   dictionary   |  { : }  |   Yes   |   Yes   | keys: No   | key
#
# See the individual lesson files for full details:
#   7_2_lists.py
#   7_3_tuples.py
#   7_4_sets.py
#   7_5_dictionaries.py
# ============================================================


# ============================================================
# Quick Examples — One of Each Collection Type
# ============================================================

# LIST — ordered, changeable, allows duplicates
shopping_list = ["milk", "eggs", "bread", "eggs"]
print("List:", shopping_list)
print("First item:", shopping_list[0])    # → milk

# TUPLE — ordered, CANNOT be changed, allows duplicates
coordinates = (40.7128, -74.0060)          # lat/lon for New York City
print("Tuple:", coordinates)
print("Latitude:", coordinates[0])         # → 40.7128

# SET — unordered, changeable, NO duplicates
unique_colors = {"red", "blue", "red", "green"}
print("Set:", unique_colors)               # → {'red', 'blue', 'green'}  (no duplicate)

# DICTIONARY — key:value pairs, ordered, changeable
player = {"name": "Eric", "health": 100, "level": 3}
print("Dictionary:", player)
print("Player name:", player["name"])      # → Eric


# ============================================================
# Quick Examples — The Two Loop Types
# ============================================================

# FOR LOOP — repeat once for each item in a collection
print("\n--- For Loop ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# WHILE LOOP — repeat as long as a condition is True
print("\n--- While Loop ---")
count = 1
while count <= 3:
    print("Count:", count)
    count = count + 1

# See the individual lesson files for full details:
#   7_6_for_loops.py
#   7_7_while_loops.py


# ============================================================
# AND: Decisions Inside Loops — if Statements
# ============================================================
# Loops often need to make decisions while going through data.
# An IF STATEMENT checks a condition and runs code if it is True.

print("\n--- If inside a for loop ---")
scores = [45, 82, 60, 91, 33, 75]

for score in scores:
    if score >= 60:
        print(score, "→ PASS")
    else:
        print(score, "→ FAIL")

# See the full lesson:
#   7_1_if_statements.py
