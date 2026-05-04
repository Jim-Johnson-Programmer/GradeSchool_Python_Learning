# ============================================================
# Lesson 7.4 - Sets
# ============================================================
# A SET is a collection that holds UNIQUE values.
# If you try to add a duplicate, Python quietly ignores it.
#
# Key facts:
#   - Created with curly braces:  { }
#   - NO duplicate values allowed — every item is unique
#   - UNORDERED — items have no index and no guaranteed order
#   - MUTABLE — you can add and remove items
#   - Because there is no order, you CANNOT access items by index
#
# When to use a set?
#   - When you want to remove duplicates from a collection
#   - When you need to quickly check if something is in a group
#   - When order doesn't matter to you
# ============================================================


# ============================================================
# PART 1: Creating a Set
# ============================================================

colors   = {"red", "green", "blue"}
numbers  = {1, 2, 3, 4, 5}
empty    = set()      # IMPORTANT: {} alone creates a dict, not a set!

print(colors)    # → {'red', 'green', 'blue'}  (order may vary)
print(numbers)   # → {1, 2, 3, 4, 5}


# ============================================================
# PART 2: Duplicates Are Automatically Removed
# ============================================================

dupes = {1, 2, 2, 3, 3, 3, 4}
print(dupes)    # → {1, 2, 3, 4}  — duplicates are gone

names = {"Alice", "Bob", "Alice", "Charlie", "Bob"}
print(names)    # → {'Alice', 'Bob', 'Charlie'}  (order may vary)


# ============================================================
# PART 3: No Index Access
# ============================================================
# Sets are unordered — there is no index 0, 1, 2...
# This line would cause an error:
# print(colors[0])   # ← TypeError: 'set' object is not subscriptable


# ============================================================
# PART 4: Checking Membership
# ============================================================
# The  in  keyword works great with sets — and it is FAST.

if "red" in colors:
    print("red is in the set")       # → red is in the set

if "yellow" not in colors:
    print("yellow is not in the set") # → yellow is not in the set


# ============================================================
# PART 5: Adding and Removing Items
# ============================================================
# .add()     — adds one item (ignored if already in the set)
# .remove()  — removes an item (causes error if not found)
# .discard() — removes an item (NO error if not found — safer!)

colors.add("yellow")
print(colors)    # → {'red', 'green', 'blue', 'yellow'}  (order may vary)

colors.add("red")    # "red" already in set — nothing happens
print(colors)

colors.remove("green")
print(colors)    # → {'red', 'blue', 'yellow'}  (order may vary)

colors.discard("purple")   # "purple" not in set — no error, just ignored
print(colors)


# ============================================================
# PART 6: Length of a Set
# ============================================================

print(len(colors))   # → 3


# ============================================================
# PART 7: Set Operations — Math with Sets
# ============================================================
# Sets support operations from math set theory:
#
#   union        — everything in EITHER set
#   intersection — only items in BOTH sets
#   difference   — items in the first set but NOT the second

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)    # union         → {1, 2, 3, 4, 5, 6, 7, 8}
print(a & b)    # intersection  → {4, 5}
print(a - b)    # difference    → {1, 2, 3}  (in a but not b)
print(b - a)    # difference    → {6, 7, 8}  (in b but not a)


# ============================================================
# PART 8: Removing Duplicates from a List Using a Set
# ============================================================
# A very common trick: convert a list to a set to remove dupes,
# then convert back to a list if you need list features.

high_scores = [100, 85, 100, 72, 85, 90, 100]
print(high_scores)          # → [100, 85, 100, 72, 85, 90, 100]

unique_scores = list(set(high_scores))
print(unique_scores)        # → [72, 85, 90, 100]  (order may vary)


# ============================================================
# PART 9: Converting Between Types
# ============================================================

my_list  = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_set   = set(my_list)       # removes duplicates
print(my_set)                 # → {1, 2, 3, 4, 5, 6, 9}

my_tuple = (10, 20, 10, 30)
print(set(my_tuple))          # → {10, 20, 30}


# ============================================================
# PART 10: Mini Challenge
# ============================================================
# 1. Create a set of 4 different animals.
# 2. Add "dragon" to the set.
# 3. Try adding "dragon" again — notice nothing changes.
# 4. Check if "cat" is in the set.
# 5. Print the length of the set.

animals = {"cat", "dog", "bird", "fish"}
animals.add("dragon")
animals.add("dragon")       # duplicate — ignored
print("cat" in animals)     # → True
print(len(animals))         # → 5
