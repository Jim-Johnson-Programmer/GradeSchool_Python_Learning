# ============================================================
# Lesson 6.5 - Inheritance  (Minecraft Edition)
# ============================================================
# Inheritance means one class can BUILD ON another class.
#
# Think of it like this:
#
#   Mob            <- parent class / base class
#   Zombie         <- child class
#   Skeleton       <- child class
#
# The child class gets the parent's data and methods.
# Then the child can also add new things of its own.
#
# This saves time because we do not have to rewrite the same
# code again and again.
# ============================================================


# ============================================================
# PART 1: A Parent Class
# ============================================================
# This class has data and methods that many mobs can share.

class Mob:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def describe(self):
        print(self.name + " has " + str(self.health) + " health.")

    def take_damage(self, amount):
        self.health = self.health - amount
        print(self.name + " takes " + str(amount) + " damage.")
        print("Health is now: " + str(self.health))


# ============================================================
# PART 2: Child Classes Inherit From the Parent Class
# ============================================================
# Zombie(Mob) means Zombie inherits from Mob.
# Skeleton(Mob) means Skeleton inherits from Mob.

class Zombie(Mob):
    def groan(self):
        print(self.name + " says: Braaaains...")


class Skeleton(Mob):
    def rattle(self):
        print(self.name + " rattles its bones!")


zombie1 = Zombie("Zed", 20)
skeleton1 = Skeleton("Bones", 15)

zombie1.describe()      # inherited from Mob
skeleton1.describe()   # inherited from Mob

zombie1.groan()        # Zombie's own method
skeleton1.rattle()     # Skeleton's own method

zombie1.take_damage(5)     # inherited from Mob
skeleton1.take_damage(3)   # inherited from Mob


# ============================================================
# PART 3: Child Classes Can Add More Data
# ============================================================
# We can use super().__init__(...) to set up the parent part.
# super() means "the parent class". We call the parent's __init__

class Creeper(Mob):
    def __init__(self, name, health, explosion_power):
        super().__init__(name, health)
        self.explosion_power = explosion_power

    def explode(self):
        print(self.name + " explodes with power " + str(self.explosion_power) + "!")
        self.health = 0


creeper1 = Creeper("Boomy", 25, 10)
creeper1.describe()    # inherited from Mob
creeper1.explode()     # Creeper's own method
creeper1.describe()


# ============================================================
# PART 4: A Child Class Can Change a Parent Method
# ============================================================
# This is called OVERRIDING.
# The parent has describe(), but Villager will make its own
# version of describe().

class Villager(Mob):
    def __init__(self, name, health, job):
        super().__init__(name, health)
        self.job = job

    def describe(self):
        print(self.name + " is a villager with the job: " + self.job)
        print("Health: " + str(self.health))


villager1 = Villager("Bob", 12, "Farmer")
villager1.describe()   # uses Villager's version, not Mob's version
villager1.take_damage(2)


# ============================================================
# PART 5: isinstance() Still Works With Inheritance
# ============================================================
# A Zombie object is:
#   - a Zombie
#   - also a Mob

print(isinstance(zombie1, Zombie))   # True
print(isinstance(zombie1, Mob))      # True
print(isinstance(skeleton1, Mob))    # True
print(isinstance(villager1, Mob))    # True
print(isinstance(villager1, Zombie)) # False


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Make a class called Spider that inherits from Mob.
# 2. Give Spider a method called climb().
# 3. Create a Spider object and call describe(), climb(),
#    and take_damage().
# 4. Make a class called IronGolem that inherits from Mob
#    and give it its own describe() method.
# ============================================================