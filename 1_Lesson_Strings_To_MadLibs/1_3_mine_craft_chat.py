# ============================================================
# Lesson 1.3 - Minecraft Player Chat
# ============================================================
# Let's use what we know about variables and input() to build
# a fun Minecraft chat conversation between two players!
#
# We will:
#   1. Ask BOTH players for information using input()
#   2. Store each answer in a variable
#   3. Print out a full chat conversation using those variables
# ============================================================


# ============================================================
# PART 1: Collect Info From Both Players
# ============================================================

print("=== MINECRAFT CHAT SETUP ===")
print("Answer the questions for both players.")
print("")

# --- Player 1 Info ---
player1_name      = input("Player 1 - Enter your Minecraft username: ")
player1_biome     = input("Player 1 - What biome are you in? (e.g. jungle, desert, snow): ")
player1_item      = input("Player 1 - What item are you holding? (e.g. diamond sword, pickaxe): ")
player1_mob       = input("Player 1 - What mob are you fighting? (e.g. creeper, zombie, skeleton): ")

print("")

# --- Player 2 Info ---
player2_name      = input("Player 2 - Enter your Minecraft username: ")
player2_biome     = input("Player 2 - What biome are you in? (e.g. forest, ocean, nether): ")
player2_item      = input("Player 2 - What item are you holding? (e.g. bow, shield, axe): ")
player2_building  = input("Player 2 - What are you building? (e.g. a castle, a farm, a house): ")


# ============================================================
# PART 2: Print the Chat Conversation
# ============================================================

print("")
print("============================================")
print("           ** MINECRAFT CHAT **            ")
print("============================================")
print("")

print(player1_name + ": Hey " + player2_name + "! Where are you right now?")
print("")

print(player2_name + ": I'm in a " + player2_biome + " biome! I'm building " + player2_building + ".")
print(player2_name + ": What about you?")
print("")

print(player1_name + ": I'm in the " + player1_biome + "! It's crazy here!")
print(player1_name + ": I've got my " + player1_item + " ready.")
print("")

print(player2_name + ": Oh no — are you in trouble?")
print("")

print(player1_name + ": YES! There's a " + player1_mob + " right behind me!!")
print("")

print(player2_name + ": Use your " + player1_item + " and fight it!")
print(player2_name + ": I'll come help — let me grab my " + player2_item + "!")
print("")

print(player1_name + ": HURRY! Meet me in the " + player1_biome + "!")
print("")

print(player2_name + ": On my way! Don't die " + player1_name + " !!")
print("")

print("============================================")
print("              ** END OF CHAT **            ")
print("============================================")


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Add a third player — ask for their username, biome, and
#    favorite block, then add them into the chat conversation.
# 2. Add a line where Player 1 asks Player 2 how many diamonds
#    they have found. (Hint: you will need a new input() !)
# 3. Change the chat so the two players plan to meet at a
#    specific location — ask each player for coordinates like
#    x and z and use them in the conversation.
# ============================================================