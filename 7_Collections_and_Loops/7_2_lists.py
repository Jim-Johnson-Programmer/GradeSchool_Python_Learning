# ============================================================
# Lesson 7.2 - Lists
# ============================================================
# A LIST is a collection that holds multiple values in ORDER.
# You can have as many items as you want.
# Items can be added, removed, and changed.
#
# Key facts:
#   - Created with square brackets:  [ ]
#   - Items are separated by commas
#   - Each item has an INDEX (position number) starting at 0
#   - Lists are ORDERED — items stay in the order you put them
#   - Lists are MUTABLE — you CAN change them after creating them
# ============================================================


# ============================================================
# PART 1: Creating a List []
# ============================================================

# fruits = ["apple", "banana", "cherry"] 
# scores = [95, 87, 72, 100, 60] 
# # not best practice to mix types
# # which type is coming next in your loop?
# mixed = ["Eric", 14, True, 3.5] # a list can mix types 
# empty = [] 

# print(fruits)
# print(scores) # → [95, 87, 72, 100, 60]
# print(mixed)  # → ['Eric', 14, True, 3.5]
# print(empty)  # → []  (empty list)


# # ============================================================
# # PART 2: Accessing Items by Index
# # ============================================================
# # Index starts at 0 — the FIRST item is index 0.
# #
fruits = ["apple", "banana", "cherry"]
# #   index:       0         1         2
# first_fruit = fruits[0]   # index 0 is "apple"

# print(first_fruit)    # → apple
# print(fruits[1])    # → banana
# print(fruits[2])    # → cherry

# # Negative index counts from the END:
# print(fruits[-1])   # → cherry  (last item)
# print(fruits[-2])   # → banana  (second to last)


# # ============================================================
# # PART 3: Checking the Length
# # ============================================================
# # len() tells you how many items are in the list.

# length_of_list = len(fruits) - 1
# print(length_of_list)   # -> 3
# print(fruits[length_of_list])  #this is an error! Why?
# print(len(fruits))   # → 3
# print(len(scores))   # → 5
# print(len(empty))    # → 0


# # ============================================================
# # PART 4: Changing an Item
# # ============================================================
# # Lists are mutable — you can replace any item.
# print(fruits)    # → ['apple', 'banana', 'cherry']
# fruits[1] = "blueberry"
# print(fruits)    # → ['apple', 'blueberry', 'cherry']


# # ============================================================
# # PART 5: Adding Items
# # ============================================================
# # .append()  — adds one item to the END
# # .insert()  — adds one item at a specific index

# fruits.append("mango")
# print(fruits)    # → ['apple', 'blueberry', 'cherry', 'mango']

# fruits.insert(7, "grape")   # insert "grape" at index 1
# print(fruits)    # → ['apple', 'grape', 'blueberry', 'cherry', 'mango']


# # ============================================================
# # PART 6: Removing Items
# # ============================================================
# # .remove()  — removes the first item with that VALUE
# # .pop()     — removes the item at a specific INDEX (default: last)
# # del        — removes an item at a specific index

# fruits.remove("grape")
# print(fruits)    # → ['apple', 'blueberry', 'cherry', 'mango']

# fruits.pop()         # removes last item ("mango")
# print(fruits)        # → ['apple', 'blueberry', 'cherry']

# fruits.pop(0)        # removes item at index 0 ("apple")
# print(fruits)        # → ['blueberry', 'cherry']

#del fruits[0]       # also removes item at index 0 ("blueberry")

# # ============================================================
# # PART 7: Checking if an Item Is in a List
# # ============================================================
# # Use  in  to check membership.

# colors = ["red", "green", "blue"]

# if "green" in colors:
#     print("green is in the list")       # → green is in the list

# if "yellow" not in colors:
#     print("yellow is NOT in the list")  # → yellow is NOT in the list


# # ============================================================
# # PART 8: Slicing a List
# # ============================================================
# # You can grab a PORTION of a list using a slice.
# # Syntax:  list[start : stop]
# # start is INCLUDED, stop is NOT included.

# numbers = [10, 20, 30, 40, 50]

# print(numbers[1:4])   # → [20, 30, 40]  (index 1 up to but not including 4)
# print(numbers[:3])    # → [10, 20, 30]  (from beginning up to index 3)
# print(numbers[2:])    # → [30, 40, 50]  (from index 2 to the end)
# print(numbers[:])     # → [10, 20, 30, 40, 50]  (full copy)


# # ============================================================
# # PART 9: Useful List Methods
# # ============================================================

# nums = [3, 1, 4, 1, 5, 9, 2, 6]

# nums.sort()
# print(nums)              # → [1, 1, 2, 3, 4, 5, 6, 9]  (sorted ascending)

# nums.reverse()
# print(nums)              # → [9, 6, 5, 4, 3, 2, 1, 1]  (reversed)

# print(nums.count(1))     # → 2  (how many times 1 appears)
# print(nums.index(5))     # → 2  (index of first 5 in the sorted list)

# nums.clear()
# print(nums)              # → []  (all items removed)


# # ============================================================
# # PART 10: Mini Challenge
# # ============================================================
# # 1. Create a list of 4 of your favorite video games.
# # 2. Print the first and last game using indexes.
# # 3. Add a new game to the end.
# # 4. Remove the second game.
# # 5. Print the final list.

# games = ["Minecraft", "Mario Kart", "Zelda", "Roblox"]
# print(games[0])         # first
# print(games[-1])        # last
# games.append("Fortnite")
# games.remove("Mario Kart")
# print(games)
