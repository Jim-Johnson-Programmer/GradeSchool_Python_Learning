# ============================================================
# Lesson 7.6 - For Loops
# ============================================================
# A FOR LOOP lets you repeat code once for EACH item
# in a collection — automatically, one at a time.
#
# Key word:  for
#   - "for" goes through each item in a collection
#   - You give the current item a variable name
#   - The indented block runs once for EVERY item
#
# Works with: lists, tuples, sets, dictionaries, strings, range()
# ============================================================


# ============================================================
# PART 1: Looping Over a List
# ============================================================

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# → apple
# → banana
# → cherry


# ============================================================
# PART 2: Looping Over a Tuple
# ============================================================

days = ("Monday", "Tuesday", "Wednesday")

for day in days:
    print("Day:", day)

# → Day: Monday
# → Day: Tuesday
# → Day: Wednesday


# ============================================================
# PART 3: Looping Over a Set
# ============================================================
# Sets are unordered, so the loop order may vary each time.

colors = {"red", "green", "blue"}

for color in colors:
    print(color)    # order is not guaranteed


# ============================================================
# PART 4: Looping Over a String
# ============================================================
# A string is a sequence of characters — you can loop over each one.

word = "Python"

for letter in word:
    print(letter)

# → P
# → y
# → t
# → h
# → o
# → n


# ============================================================
# PART 5: Using range() to Loop a Set Number of Times
# ============================================================
# range(n)        → 0, 1, 2, ..., n-1
# range(a, b)     → a, a+1, ..., b-1
# range(a, b, s)  → a, a+s, a+2s, ..., up to but not including b

for i in range(5):
    print(i)        # → 0  1  2  3  4

print("---")

for i in range(1, 6):
    print(i)        # → 1  2  3  4  5

print("---")

for i in range(0, 10, 2):
    print(i)        # → 0  2  4  6  8  (step of 2)


# ============================================================
# PART 6: Using the Index While Looping — enumerate()
# ============================================================
# enumerate() gives you BOTH the index AND the value.

players = ["Eric", "Alice", "Bob"]

for index, name in enumerate(players):
    print(index, name)

# → 0 Eric
# → 1 Alice
# → 2 Bob

# You can start the count at 1:
for index, name in enumerate(players, start=1):
    print(index, name)

# → 1 Eric
# → 2 Alice
# → 3 Bob


# ============================================================
# PART 7: Looping Over a Dictionary
# ============================================================
# By default, looping a dict gives you its KEYS.

player = {"name": "Eric", "health": 100, "level": 5}

for key in player:
    print(key)            # → name  health  level

# Loop over keys and values together with .items():
for key, value in player.items():
    print(key, ":", value)

# → name : Eric
# → health : 100
# → level : 5

# Loop over only values:
for value in player.values():
    print(value)          # → Eric  100  5


# ============================================================
# PART 8: Doing Math in a Loop
# ============================================================
# Common pattern: start a variable at 0, add to it each loop.

scores = [85, 92, 78, 95, 88]

total = 0
for score in scores:
    total = total + score

print("Total:", total)          # → Total: 438
print("Average:", total / len(scores))  # → Average: 87.6


# ============================================================
# PART 9: Building a New List in a Loop
# ============================================================

numbers = [1, 2, 3, 4, 5]
doubled = []

for n in numbers:
    doubled.append(n * 2)

print(doubled)   # → [2, 4, 6, 8, 10]


# ============================================================
# PART 10: Nested For Loops
# ============================================================
# A loop inside another loop.
# The inner loop runs ALL THE WAY through for EACH step of the outer loop.

rows = ["A", "B", "C"]
cols = [1, 2, 3]

for row in rows:
    for col in cols:
        print(row, col)

# → A 1
# → A 2
# → A 3
# → B 1
# → B 2
# ... and so on


# ============================================================
# PART 11: break and continue
# ============================================================
# break     — EXIT the loop immediately
# continue  — SKIP the rest of this iteration and go to the next one

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print numbers until we hit 5, then stop:
for n in numbers:
    if n == 5:
        break
    print(n)
# → 1  2  3  4

print("---")

# Skip even numbers, only print odd:
for n in numbers:
    if n % 2 == 0:
        continue
    print(n)
# → 1  3  5  7  9


# ============================================================
# PART 12: Mini Challenge
# ============================================================
# 1. Create a list of 5 numbers.
# 2. Loop through and print each number multiplied by 10.
# 3. Use a loop to find the LARGEST number in the list.

nums = [4, 17, 8, 23, 11]

for n in nums:
    print(n * 10)

biggest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n

print("Largest:", biggest)   # → Largest: 23
