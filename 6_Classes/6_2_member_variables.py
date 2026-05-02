# ============================================================
# Lesson 6.2 - Member Variables (Attributes)  (Minecraft Edition)
# ============================================================
# In the last lesson we made empty blueprints with "pass".
# Now we give our objects DATA to hold.
#
# A MEMBER VARIABLE (also called an ATTRIBUTE) is a variable
# that belongs to a specific object.
#
# We set them up inside a special function called __init__
# (pronounced "dunder init" — the double underscores are the clue).
#
#   class Creeper:
#       def __init__(self, name, health):
#           self.name   = name    ← member variable
#           self.health = health  ← member variable
#
# __init__ runs automatically the moment you create an object.
# "self" is Python's way of saying "this specific object".
#   self.name  means "this object's name variable"
# ============================================================


# ============================================================
# PART 1: Setting Up Member Variables with __init__
# ============================================================

class Creeper:
    def __init__(self, name, health):
        self.name   = name
        self.health = health

# Spawn two Creeper objects — each gets its own name and health:
creeper1 = Creeper("Hissy",  20)   # constructor arguments go here
creeper2 = Creeper("Boomer", 20)

# Read a member variable using a dot ( . ):
print(creeper1.name)    # → Hissy
print(creeper1.health)  # → 20

print(creeper2.name)    # → Boomer
print(creeper2.health)  # → 20


# ============================================================
# PART 2: Each Object Keeps Its Own Data
# ============================================================
# Changing one object does NOT affect the other.

class MinecraftPlayer:
    def __init__(self, username, score):
        self.username = username
        self.score    = score

player1 = MinecraftPlayer("CreeperSlayer", 1500)
player2 = MinecraftPlayer("DiamondQueen",   800)

print(player1.username, "has", player1.score, "points")
print(player2.username, "has", player2.score, "points")

# Change player1's score — player2 is untouched:
player1.score = 2000
print(player1.username, "now has", player1.score, "points")
print(player2.username, "still has", player2.score, "points")


# ============================================================
# PART 3: Member Variables Can Hold Any Data Type
# ============================================================
# Strings, numbers, booleans — any type works!

class Mob:
    def __init__(self, name, health, is_hostile):
        self.name       = name
        self.health     = health
        self.is_hostile = is_hostile

skeleton = Mob("Skeleton", 20, True)
cow      = Mob("Cow",      10, False)

print("Name     :", skeleton.name)
print("Health   :", skeleton.health)
print("Hostile  :", skeleton.is_hostile)

print("Name     :", cow.name)
print("Health   :", cow.health)
print("Hostile  :", cow.is_hostile)


# ============================================================
# PART 4: Adding a Member Variable After Creation
# ============================================================
# You can attach a new variable to an object any time using dot notation.
# (Best practice is to define all variables in __init__, but good to know!)

class Block:
    def __init__(self, block_type, is_solid):
        self.block_type = block_type
        self.is_solid   = is_solid

dirt = Block("Dirt", True)
dirt.color = "brown"      # adding a new attribute after creation

print(dirt.block_type)   # → Dirt
print(dirt.is_solid)     # → True
print(dirt.color)        # → brown


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Create a class called Sword with member variables:
#    blade_material, damage, and is_enchanted.
# 2. Make two Sword objects with different data.
# 3. Print all three variables for each sword.
# ============================================================
