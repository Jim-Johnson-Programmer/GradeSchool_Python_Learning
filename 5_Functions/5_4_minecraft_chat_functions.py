# ============================================================
# Lesson 5.4 - Minecraft Chat with Functions
# ============================================================
# In Lesson 1.3 we wrote the Minecraft chat program,
# but ALL the code was in one long block.
#
# Now we know about FUNCTIONS!
# In this version we will break the program into clear,
# named functions so each part has its own job:
#
#   collect_player_info()  — asks the player questions,
#                            returns their answers
#   print_chat()           — prints the full conversation
#   main()                 — ties everything together
#
# This makes the code easier to READ, UNDERSTAND, and CHANGE.
# ============================================================


# ============================================================
# FUNCTION 1: Collect info for one player
# ============================================================
# Parameters: player_number — which player this is (1 or 2)
# Returns:    a list with [name, biome, item, extra_info]
#
# NOTE ON LISTS: A list lets us group several values together
#   player_data = [name, biome, item, extra]
#   player_data[0] is name, player_data[1] is biome, etc.
# We will learn more about lists in a later lesson!

def collect_player_info(player_number):
    label = "Player " + str(player_number)
    print("--- " + label + " ---")

    name  = input(label + " - Enter your Minecraft username: ")
    biome = input(label + " - What biome are you in? (e.g. jungle, desert, snow): ")
    item  = input(label + " - What item are you holding? (e.g. diamond sword, pickaxe): ")

    if player_number == 1:
        extra = input(label + " - What mob are you fighting? (e.g. creeper, zombie): ")
    else:
        extra = input(label + " - What are you building? (e.g. a castle, a farm): ")

    print("")
    return [name, biome, item, extra]


# ============================================================
# FUNCTION 2: Print a single chat line
# ============================================================
# Parameters: sender  — the player whose turn it is to talk
#             message — what they are saying
# Returns:    nothing (just prints)

def print_chat_line(sender, message):
    print(sender + ": " + message)


# ============================================================
# FUNCTION 3: Print the full chat conversation
# ============================================================
# Parameters: p1 — list of Player 1's info [name, biome, item, mob]
#             p2 — list of Player 2's info [name, biome, item, building]
# Returns:    nothing (just prints)

def print_chat(p1, p2):
    # Pull values out of the lists so the code below is easier to read
    p1_name     = p1[0]
    p1_biome    = p1[1]
    p1_item     = p1[2]
    p1_mob      = p1[3]

    p2_name     = p2[0]
    p2_biome    = p2[1]
    p2_item     = p2[2]
    p2_building = p2[3]

    print("============================================")
    print("           ** MINECRAFT CHAT **            ")
    print("============================================")
    print("")

    print_chat_line(p1_name, "Hey " + p2_name + "! Where are you right now?")
    print("")

    print_chat_line(p2_name, "I'm in a " + p2_biome + " biome! I'm building " + p2_building + ".")
    print_chat_line(p2_name, "What about you?")
    print("")

    print_chat_line(p1_name, "I'm in the " + p1_biome + "! It's crazy here!")
    print_chat_line(p1_name, "I've got my " + p1_item + " ready.")
    print("")

    print_chat_line(p2_name, "Oh no — are you in trouble?")
    print("")

    print_chat_line(p1_name, "YES! There's a " + p1_mob + " right behind me!!")
    print("")

    print_chat_line(p2_name, "Use your " + p1_item + " and fight it!")
    print_chat_line(p2_name, "I'll come help — let me grab my " + p2_item + "!")
    print("")

    print_chat_line(p1_name, "HURRY! Meet me in the " + p1_biome + "!")
    print("")

    print_chat_line(p2_name, "On my way! Don't die " + p1_name + " !!")
    print("")

    print("============================================")
    print("              ** END OF CHAT **            ")
    print("============================================")


# ============================================================
# FUNCTION 4: main() — ties the whole program together
# ============================================================
# It is a convention (common habit) in many programs to put
# ALL the "start-up" code inside a function called main().
# That way the program flow is easy to find and understand.

def main():
    print("=== MINECRAFT CHAT SETUP ===")
    print("Answer the questions for both players.")
    print("")

    player1_info = collect_player_info(1)
    player2_info = collect_player_info(2)

    print_chat(player1_info, player2_info)


# ============================================================
# Run the program!
# ============================================================
# This line calls main() to start everything.
main()


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Add a third player — write a new block inside main() that
#    calls collect_player_info(3) and then add that player
#    into the print_chat() function's conversation.
# 2. Create a new function called print_header() that prints
#    the "=== MINECRAFT CHAT SETUP ===" banner. Replace the
#    raw print() lines inside main() with a call to it.
# 3. Add a line to print_chat where Player 2 asks Player 1
#    how many health points they have left. You will need to
#    collect that info inside collect_player_info() first!
# ============================================================
