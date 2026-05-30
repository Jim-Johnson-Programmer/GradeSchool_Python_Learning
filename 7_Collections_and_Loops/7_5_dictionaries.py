# ============================================================
# Lesson 7.5 - Dictionaries
# ============================================================
# A DICTIONARY stores data as KEY : VALUE pairs.
# Instead of looking up an item by index number,
# you look it up by its KEY — like looking up a word
# in a real dictionary to find its definition.
#
# Key facts:
#   - Created with curly braces:  { }
#   - Each entry is  key: value
#   - Keys must be UNIQUE — no two entries can have the same key
#   - Keys are usually strings or numbers
#   - Values can be anything: strings, numbers, lists, even dicts
#   - ORDERED (since Python 3.7) — items stay in insertion order
#   - MUTABLE — you can add, change, and remove items
# ============================================================


# ============================================================
# PART 1: Creating a Dictionary
# ============================================================

player = {
    #key : value
    "name":   "Eric",
    "health": 100,
    "level":  5,
    "score":  2400
}

inventory = {
    "sword":  1,
    "potion": 3,
    "gold":   50
}

empty = {}    # empty dictionary

print(player)     # → {'name': 'Eric', 'health': 100, 'level': 5, 'score': 2400}
print(inventory)  # → {'sword': 1, 'potion': 3, 'gold': 50}


# ============================================================
# PART 2: Accessing Values by Key
# ============================================================
# Use square brackets with the KEY to get the VALUE.

print(player["name"])     # → Eric
print(player["health"])   # → 100
print(inventory["gold"])  # → 50


# ============================================================
# PART 3: Changing a Value
# ============================================================

player["health"] = 75
print(player["health"])   # → 75


# ============================================================
# PART 4: Adding a New Key-Value Pair
# ============================================================
# Just assign to a key that doesn't exist yet.

player["weapon"] = "sword"
print(player)    # → {..., 'weapon': 'sword'}


# ============================================================
# PART 5: Removing a Key-Value Pair
# ============================================================
# del      — removes the key and its value
# .pop()   — removes the key and RETURNS the value

del player["weapon"]
print(player)

removed_score = player.pop("score")
print("Removed score:", removed_score)   # → Removed score: 2400
print(player)


# ============================================================
# PART 6: Checking if a Key Exists
# ============================================================
# Use  in  to check if a KEY is in the dictionary.

if "health" in player:
    print("Player has a health value")      # → Player has a health value

if "mana" not in player:
    print("No mana stat found")             # → No mana stat found


# ============================================================
# PART 7: Safe Access with .get()
# ============================================================
# Using [] raises an error if the key doesn't exist.
# .get() returns None (or a default you choose) instead.

print(player.get("level"))       # → 5
print(player.get("mana"))        # → None  (no error!)
print(player.get("mana", 0))     # → 0     (custom default)


# ============================================================
# PART 8: Useful Dictionary Methods
# ============================================================

print(player.keys())      # → dict_keys(['name', 'health', 'level'])
print(player.values())    # → dict_values(['Eric', 75, 5])
print(player.items())     # → dict_items([('name', 'Eric'), ('health', 75), ('level', 5)])

print(len(player))        # → 3  (number of key-value pairs)


# ============================================================
# PART 9: Nested Dictionaries
# ============================================================
# A dictionary value can be ANOTHER dictionary.

team = {
    "player1": {"name": "Eric",  "health": 100},
    "player2": {"name": "Alice", "health": 85},
}

print(team["player1"]["name"])    # → Eric
print(team["player2"]["health"])  # → 85


# ============================================================
# PART 10: Dictionary with a List as a Value
# ============================================================
# Values can be any type — including lists.

bag = {
    "weapons": ["sword", "bow"],
    "potions": ["health potion", "speed potion", "strength potion"],
    "gold":    42
}

print(bag["weapons"])            # → ['sword', 'bow']
print(bag["potions"][0])         # → health potion
bag["weapons"].append("dagger")
print(bag["weapons"])            # → ['sword', 'bow', 'dagger']


# ============================================================
# PART 11: Mini Challenge
# ============================================================
# 1. Create a dictionary for a pet with keys: name, type, age, tricks
#    (tricks should be a list of 2 tricks)
# 2. Print the pet's name.
# 3. Add a new trick to the tricks list.
# 4. Change the pet's age.
# 5. Print the full dictionary.

pet = {
    "name":   "Buddy",
    "type":   "dog",
    "age":    3,
    "tricks": ["sit", "shake"]
}

print(pet["name"])
pet["tricks"].append("roll over")
pet["age"] = 4
print(pet)
