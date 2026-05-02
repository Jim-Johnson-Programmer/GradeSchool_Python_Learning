# ============================================================
# Lesson 6.1 - Introduction to Classes  (Minecraft Edition)
# ============================================================
# So far we have used variables to store single pieces of data
# and functions to do work.
#
# A CLASS bundles BOTH data AND behavior together into one thing.
# Think of a class as a BLUEPRINT — like Minecraft's mob spawner.
# You can spawn many mobs from the same blueprint!
#
# Each mob spawned from the blueprint is called an OBJECT
# (also called an INSTANCE).
#
#   class Creeper:          ← the blueprint
#       pass
#
#   creeper1 = Creeper()    ← one object built from the blueprint
#   creeper2 = Creeper()    ← another object — completely separate
#
# Key words:
#   class   — starts a class definition
#   pass    — means "nothing here yet" (placeholder)
#   ()      — used to SPAWN an object from a class
# ============================================================


# ============================================================
# PART 1: Your First Class
# ============================================================
# A class name always starts with a CAPITAL letter.
# This is a rule Python programmers follow to make code easy to read.

class Creeper:
    pass

# Now let's SPAWN two Creeper objects from that blueprint:

# instance/object one
creeper1 = Creeper()
# instance/object two
creeper2 = Creeper()

print(creeper1)   # → something like <__main__.Creeper object at 0x...>
print(creeper2)   # → a different memory address — they are separate objects

# Both are Creepers, but they are DIFFERENT objects in memory.


# ============================================================
# PART 2: Every Object Knows What Class It Came From
# ============================================================
# We can ask Python what type an object is with type()

class Zombie:
    pass

class Skeleton:
    pass

zombie1   = Zombie()
skeleton1 = Skeleton()

print(type(zombie1))     # → <class '__main__.Zombie'>   type() tells us which blueprint (class) was used.
print(type(skeleton1))   # → <class '__main__.Skeleton'>

# type() tells us which blueprint (class) was used to make the object.


# ============================================================
# PART 3: isinstance() — Is This Object a Member of a Class?
# ============================================================
# isinstance(object, ClassName) returns True or False

print(isinstance(zombie1,   Zombie))    # → True
print(isinstance(zombie1,   Skeleton))  # → False  (it's a Zombie, not a Skeleton!)
print(isinstance(skeleton1, Skeleton))  # → True


# ============================================================
# PART 4: One Blueprint, Many Objects
# ============================================================
# Let's make a MinecraftPlayer class and spawn three players.
# They all share the same blueprint but are separate objects.

class MinecraftPlayer:
    pass

player1 = MinecraftPlayer()
player2 = MinecraftPlayer()
player3 = MinecraftPlayer()

print(type(player1))   # → <class '__main__.MinecraftPlayer'>
print(type(player2))   # → <class '__main__.MinecraftPlayer'>
print(type(player3))   # → <class '__main__.MinecraftPlayer'>

# Three separate MinecraftPlayer objects — all made from the same class.


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Create a class called Block and make three objects from it.
# 2. Use type() to print the type of each object.
# 3. Use isinstance() to check that each one is a Block.
# ============================================================
