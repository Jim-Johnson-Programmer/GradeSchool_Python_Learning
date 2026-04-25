# ============================================================
# Lesson 5.6 - Variable Scope  (Minecraft Edition)
# ============================================================
# SCOPE answers one question: WHERE can a variable be seen?
#
# A variable created INSIDE a function is called a LOCAL variable.
# It only exists while that function is running.
# Once the function finishes, that variable disappears.
# Code OUTSIDE the function cannot see or use it.
#
#   def open_chest():
#       loot = "diamond sword"    ← local variable
#
#   print(loot)   ← ERROR! 'loot' only existed inside open_chest()
#
# Think of a function like a chest in Minecraft.
# Items you put inside the chest STAY inside the chest.
# You can't reach into someone else's chest from outside.
# ============================================================


# ============================================================
# PART 1: Local Variables — They Stay Inside the Function
# ============================================================
# When craft_sword() runs, it creates a local variable called
# 'material'.  That variable disappears the moment the function ends.
# Nothing outside the function can see it.

def craft_sword():
    material = "diamond"                         # local variable
    print("You crafted a " + material + " sword!")

craft_sword()    # → You crafted a diamond sword!

# Uncomment the line below and run it to see the error:
# print(material)   # NameError: name 'material' is not defined


# ============================================================
# PART 2: Two Functions — Each Has Its OWN Local Variables
# ============================================================
# Even if two functions use the SAME variable name, they are
# completely separate — like two players each with their own
# inventory.  Changing one NEVER affects the other.

def nether_score():
    score = 500                          # local to nether_score
    print("Nether score:", score)

def overworld_score():
    score = 100                          # different variable — same name, different function
    print("Overworld score:", score)

nether_score()       # → Nether score: 500
overworld_score()    # → Overworld score: 100
# Each function has its own private 'score' — they never mix.


# ============================================================
# PART 3: Parameters Are Local Variables Too
# ============================================================
# A parameter is really just a local variable that gets its
# starting value from what you pass in when you call the function.
#
# Changing a parameter inside a function does NOT change the
# variable that was passed in — Python gives the function its
# OWN COPY of the value (like photocopying a treasure map).

def try_to_steal_diamonds(amount):
    amount = 0       # only changes the LOCAL copy — the original is safe
    print("Inside the function, amount:", amount)

player_diamonds = 64
try_to_steal_diamonds(player_diamonds)
print("Player still has:", player_diamonds)   # → 64  (unchanged!)

# Uncomment the lines below to confirm the parameters are gone:
# print(amount)   # NameError — 'amount' only lived inside the function


# ============================================================
# PART 4: Global Variables — Readable Everywhere
# ============================================================
# A variable created OUTSIDE any function is called GLOBAL.
# Every function in the file can READ a global variable —
# no special keyword needed.
#
# BUT — if you ASSIGN a new value to a name inside a function,
# Python creates a brand-new LOCAL variable.
# It does NOT change the global, even if the names match.

world_name = "SkyBlock"      # global variable — created outside all functions

def print_world_banner():
    print("=== Welcome to", world_name, "===")   # reading a global — allowed!

print_world_banner()                  # → === Welcome to SkyBlock ===
print("Still available:", world_name) # → Still available: SkyBlock

# Watch the trap — assigning inside a function creates a NEW local:
high_score = 0               # global

def fake_update():
    high_score = 9999        # NEW local variable — global is untouched!
    print("Inside fake_update:", high_score)   # → 9999

fake_update()
print("Global high_score unchanged:", high_score)   # → 0


# ============================================================
# PART 5: The 'global' Keyword — Changing a Global Variable
# ============================================================
# To MODIFY (not just read) a global variable inside a function,
# you must declare it with the 'global' keyword first.
# That tells Python: "I mean the one from outside — not a new local copy."

lives = 3                    # global — tracks how many lives the player has

def lose_a_life():
    global lives             # declare: use the global 'lives', not a new local one
    lives = lives - 1
    print("Lives left:", lives)

lose_a_life()    # → Lives left: 2
lose_a_life()    # → Lives left: 1
print("Final lives:", lives)   # → Final lives: 1


# Accumulating a score across multiple events
player_score = 0             # global

def collect_diamonds(amount):
    global player_score
    player_score = player_score + amount
    print("Score now:", player_score)

collect_diamonds(10)    # → Score now: 10
collect_diamonds(25)    # → Score now: 35
collect_diamonds(5)     # → Score now: 40


# ============================================================
# PART 5b: The Safer Way — Use return Instead of global
# ============================================================
# Most of the time, 'return' is cleaner than 'global'.
# Pass the value IN, update it, and return it back OUT.
# Then reassign it outside the function.

def safer_lose_a_life(current_lives):
    return current_lives - 1   # return the new value instead of using global

lives = 3
lives = safer_lose_a_life(lives)   # assign the returned value back
lives = safer_lose_a_life(lives)
print("Final lives (return version):", lives)   # → Final lives (return version): 1


# ============================================================
# SCOPE SUMMARY
# ============================================================
# | Variable type         | Can read inside function? | Can change inside? | How?            |
# |-----------------------|---------------------------|---------------------|-----------------|
# | Local variable        | Yes                       | Yes                 | just assign     |
# | Parameter             | Yes                       | Yes (local copy only)| just assign    |
# | Global — reading only | Yes                       | —                   | no keyword      |
# | Global — modifying    | Yes                       | Yes                 | use 'global'    |
# ============================================================
