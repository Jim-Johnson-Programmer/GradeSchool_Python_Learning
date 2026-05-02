# ============================================================
# Lesson 6.3 - Class Methods  (Minecraft Edition)
# ============================================================
# We know a class can store DATA in member variables.
# A class can also have FUNCTIONS — called METHODS — that
# do work using that data.
#
# A method is just a function defined INSIDE a class.
# The only difference: the first parameter is always "self"
# so the method can access the object's own variables.
#
#   class Creeper:
#       def __init__(self, name):
#           self.name = name
#
#       def hiss(self):              ← a method
#           print(self.name, "says: Ssssss!")
#
#   creeper1 = Creeper("Hissy")
#   creeper1.hiss()                 → Hissy says: Ssssss!
# ============================================================


# ============================================================
# PART 1: Your First Method
# ============================================================

class Creeper:
    def __init__(self, name, health):
        self.name   = name
        self.health = health

    def hiss(self):
        print(self.name + " says: Ssssss!")

    def describe(self):
        print(self.name + " has " + str(self.health) + " health points.")

    def explode(self):
        print(self.name + " explodes! BOOM!")
        self.health = 0

creeper1 = Creeper("Hissy",  20)
creeper2 = Creeper("Boomer", 20)

creeper1.hiss()       # → Hissy says: Ssssss!
creeper2.hiss()       # → Boomer says: Ssssss!

creeper1.explode()    # → Hissy explodes! BOOM!
creeper2.explode()    # → Boomer explodes! BOOM!

creeper1.describe()   # → Hissy has 20 health points.
creeper2.describe()   # → Boomer has 20 health points.


# ============================================================
# PART 2: Methods Can Change Member Variables
# ============================================================
# A method can READ and UPDATE the object's own data.

class MinecraftPlayer:
    def __init__(self, username):
        self.username = username
        self.xp       = 0          # experience points start at zero

    def mine(self, ore):
        self.xp = self.xp + 10
        print(self.username + " mined " + ore + "! XP: " + str(self.xp))

    def reset_xp(self):
        self.xp = 0
        print(self.username + "'s XP has been reset.")

p = MinecraftPlayer("CreeperSlayer")
p.mine("Coal")      # → CreeperSlayer mined Coal! XP: 10
p.mine("Iron")      # → CreeperSlayer mined Iron! XP: 20
p.mine("Diamond")   # → CreeperSlayer mined Diamond! XP: 30
p.reset_xp()        # → CreeperSlayer's XP has been reset.
p.mine("Gold")      # → CreeperSlayer mined Gold! XP: 10


# ============================================================
# PART 3: Methods That Return a Value
# ============================================================
# Just like regular functions, methods can use return.

class MinecraftChest:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def total_slots(self):
        return self.width * self.height

    def describe(self):
        return ("Chest size: " + str(self.width) + "x" + str(self.height) +
                " = " + str(self.total_slots()) + " slots")

small_chest = MinecraftChest(9, 3)
large_chest = MinecraftChest(9, 6)

print(small_chest.describe())              # → Chest size: 9x3 = 27 slots
print(large_chest.describe())              # → Chest size: 9x6 = 54 slots
print("Total slots:", small_chest.total_slots())   # → 27


# ============================================================
# PART 4: Putting It All Together — Minecraft Chat
# ============================================================
# We use EVERYTHING we've learned to build a Minecraft Chat class.
# Each player in chat is an OBJECT with their own:
#   - username and chat_color  (member variables set in __init__)
#   - message_count            (member variable updated by methods)
#   - is_online                (boolean member variable)
# Methods let players send messages, join/leave the server,
# and show their chat stats — just like a real Minecraft server!

class MinecraftChat:
    def __init__(self, username, chat_color):
        self.username      = username
        self.chat_color    = chat_color
        self.message_count = 0
        self.is_online     = True

    def send_message(self, text):
        if self.is_online:
            self.message_count = self.message_count + 1
            print("[" + self.chat_color + "] " + self.username + ": " + text)
        else:
            print(self.username + " is offline and cannot send messages.")

    def go_offline(self):
        self.is_online = False
        print(self.username + " has left the server.")

    def go_online(self):
        self.is_online = True
        print(self.username + " has joined the server!")

    def show_stats(self):
        status = "ONLINE" if self.is_online else "OFFLINE"
        print("--- " + self.username + " ---")
        print("Color    : " + self.chat_color)
        print("Messages : " + str(self.message_count))
        print("Status   : " + status)


# --- Run a Minecraft chat session! ---

player1 = MinecraftChat("CreeperSlayer", "Green")
player2 = MinecraftChat("DiamondQueen",  "Aqua")
player3 = MinecraftChat("SteveThe3rd",   "White")

player1.go_online()
player2.go_online()
player3.go_online()

player1.send_message("Hey everyone!")
player2.send_message("What are we building today?")
player1.send_message("Diamond fortress!")
player3.send_message("I'll get the wood.")

player2.go_offline()
player2.send_message("Can you hear me?")   # offline — message blocked

print()   # blank line for readability
player1.show_stats()
player2.show_stats()
player3.show_stats()

player2.go_online()
player2.send_message("I'm back — sorry, my pickaxe broke!")


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Add a method called whisper(target_name, text) to
#    MinecraftChat that prints:
#      [Whisper → target_name] username: text
#    It should still count as a message (message_count + 1).
# 2. Create a fourth MinecraftChat player, have them join
#    the server, send 3 messages, then show their stats.
# ============================================================
