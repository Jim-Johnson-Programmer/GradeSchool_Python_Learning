# ============================================================
# Lesson 7.3 - Tuples
# ============================================================
# A TUPLE is like a list — it holds multiple values in ORDER.
# The big difference: tuples are IMMUTABLE.
# That means once you create a tuple, you CANNOT change it.
# You cannot add, remove, or replace any of its items.
#
# Key facts:
#   - Created with PARENTHESES:  ( )
#   - Items are separated by commas
#   - Indexed the same way as lists (starting at 0)
#   - ORDERED — items stay in the order you put them
#   - IMMUTABLE — cannot be changed after creation
#
# When to use a tuple instead of a list?
#   - When the data should NEVER change (like the days of the week,
#     a player's starting position, or RGB color values)
#   - Tuples are slightly faster and safer than lists
# ============================================================


# ============================================================
# PART 1: Creating a Tuple
# ============================================================

days        = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
coordinates = (10, 25)          # an (x, y) position
rgb_red     = (255, 0, 0)       # red in RGB color values
single      = (42,)             # a tuple with ONE item needs a trailing comma!
empty       = ()                # an empty tuple

print(days)           # → ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
print(coordinates)    # → (10, 25)
print(single)         # → (42,)


# ============================================================
# PART 2: Accessing Items by Index
# ============================================================
# Works exactly like a list — index starts at 0.

print(days[0])     # → Monday
print(days[-1])    # → Friday
print(rgb_red[1])  # → 0


# ============================================================
# PART 3: Tuples Cannot Be Changed
# ============================================================
# If you try to change a tuple, Python will give an error.
# The line below is commented out on purpose — it would crash:

# days[0] = "Sunday"    # ← TypeError: 'tuple' object does not support item assignment


# ============================================================
# PART 4: Checking Length and Membership
# ============================================================

print(len(days))            # → 5
print("Monday" in days)     # → True
print("Sunday" in days)     # → False


# ============================================================
# PART 5: Slicing a Tuple
# ============================================================
# Slicing works the same as with lists.

print(days[1:4])    # → ('Tuesday', 'Wednesday', 'Thursday')
print(days[:3])     # → ('Monday', 'Tuesday', 'Wednesday')
print(days[3:])     # → ('Thursday', 'Friday')


# ============================================================
# PART 6: Tuple Unpacking
# ============================================================
# You can assign each item in a tuple to its own variable
# in a single line. This is called UNPACKING.

x, y = (10, 25)
print(x)    # → 10
print(y)    # → 25

red, green, blue = rgb_red
print(red)    # → 255
print(green)  # → 0
print(blue)   # → 0


# ============================================================
# PART 7: Useful Tuple Methods
# ============================================================
# Tuples only have two built-in methods (because they can't change):
#   .count()  — how many times a value appears
#   .index()  — the index of the first match

scores = (90, 85, 90, 72, 90)

print(scores.count(90))   # → 3
print(scores.index(72))   # → 3


# ============================================================
# PART 8: Converting Between List and Tuple
# ============================================================
# You can convert a list to a tuple and back.

my_list  = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)          # → (1, 2, 3)

back_to_list = list(my_tuple)
print(back_to_list)      # → [1, 2, 3]


# ============================================================
# PART 9: When to Use a Tuple vs a List
# ============================================================
#
#   Use a LIST when:                  Use a TUPLE when:
#   - You need to add/remove items    - The data never changes
#   - The order might change          - You want to protect the data
#   - You're building a collection    - Speed matters (tuples are faster)
#     over time
#
# Example: a player's name and starting health never change mid-game:
player_start = ("Eric", 100)   # tuple — safe from accidental change
print(player_start)             # → ('Eric', 100)


# ============================================================
# PART 10: Mini Challenge
# ============================================================
# 1. Create a tuple with the names of 3 planets.
# 2. Print the second planet.
# 3. Check if "Mars" is in the tuple.
# 4. Unpack the tuple into three variables and print each one.

planets = ("Mercury", "Venus", "Mars")
print(planets[1])                 # → Venus
print("Mars" in planets)          # → True
p1, p2, p3 = planets
print(p1, p2, p3)                 # → Mercury Venus Mars
