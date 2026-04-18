# ============================================================
# Lesson 5.5 - Mad Libs with Functions
# ============================================================
# In Lesson 1.4 we wrote Mad Libs as one long script.
# Now we will split it into clear functions:
#
#   collect_words()  — asks the player for all the silly words
#                      and returns them
#   print_story()    — receives all the words and prints the story
#   main()           — ties everything together
#
# Notice how collect_words() RETURNS values so that print_story()
# can use them — this is the return value skill from Lesson 5.3!
# ============================================================


# ============================================================
# FUNCTION 1: Collect all the words
# ============================================================
# Parameters: none
# Returns:    a list of all the words the player typed in
#
# The story is hidden inside print_story() so the player
# cannot see it while they are choosing their words!

def collect_words():
    print("=== WELCOME TO MAD LIBS! ===")
    print("Answer each question with ANY word — the sillier the better!")
    print("")

    a_name         = input("Type a funny name: ")
    an_animal      = input("Type an animal: ")
    a_body_part    = input("Type a body part: ")
    an_adjective1  = input("Type a describing word (e.g. slimy, purple, tiny): ")
    an_adjective2  = input("Type another describing word: ")
    a_verb1        = input("Type an action word ending in -ed (e.g. jumped, exploded, wiggled): ")
    a_verb2        = input("Type another action word ending in -ing (e.g. running, burping, flying): ")
    a_place        = input("Type a place (e.g. school, the moon, a taco shop): ")
    a_food         = input("Type a food: ")
    a_number       = input("Type a number: ")
    an_exclamation = input("Type a silly exclamation (e.g. YIKES, ZOINKS, OH BEANS): ")

    print("")

    # Return all the words together as a list
    return [a_name, an_animal, a_body_part,
            an_adjective1, an_adjective2,
            a_verb1, a_verb2,
            a_place, a_food, a_number, an_exclamation]


# ============================================================
# FUNCTION 2: Print the story
# ============================================================
# Parameters: words — the list returned by collect_words()
# Returns:    nothing (just prints the story)
#
# We unpack the list into named variables first so the
# story lines below are easy to read.

def print_story(words):
    # Unpack each word from the list into a clear variable name
    a_name         = words[0]
    an_animal      = words[1]
    a_body_part    = words[2]
    an_adjective1  = words[3]
    an_adjective2  = words[4]
    a_verb1        = words[5]
    a_verb2        = words[6]
    a_place        = words[7]
    a_food         = words[8]
    a_number       = words[9]
    an_exclamation = words[10]

    print("============================================")
    print("        ** YOUR MAD LIBS STORY **          ")
    print("============================================")
    print("")

    print("One " + an_adjective1 + " morning, " + a_name +
          " woke up to find a " + an_adjective2 + " " + an_animal)
    print("sitting right on their " + a_body_part + "!")
    print("")

    print(an_exclamation + "! screamed " + a_name +
          ", leaping out of bed and " + a_verb2 +
          " all the way to " + a_place + ".")
    print("")

    print("When they arrived, they discovered " + a_number +
          " plates of " + a_food + " stacked on the floor.")
    print("The " + an_animal.upper() +
          " had followed them and immediately " + a_verb1 +
          " right into the biggest pile!")
    print("")

    print("Everyone at " + a_place +
          " laughed so hard that their " + a_body_part + " fell off.")
    print("")

    print(a_name + ' just shook their head and said,')
    print('"I can\'t believe a ' + an_adjective2 + " " + an_animal +
          " ruined my " + a_food + " again. " + an_exclamation + '!"')
    print("")
    print("                    THE END")
    print("============================================")


# ============================================================
# FUNCTION 3: main() — ties the whole program together
# ============================================================

def main():
    player_words = collect_words()   # step 1: get the words (no story visible yet!)
    print_story(player_words)        # step 2: reveal the story with their silly words


# ============================================================
# Run the program!
# ============================================================
main()


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Add two new inputs inside collect_words() — a colour and
#    a planet — then use them somewhere in print_story().
#    Remember to add them to the returned list AND unpack them
#    at the top of print_story()!
# 2. Create a new function called print_banner() that prints
#    the "============" borders. Replace the raw print() lines
#    in print_story() with calls to print_banner().
# 3. Write a SECOND story function called print_story_2() that
#    uses the SAME list of words but tells a completely
#    different adventure. Call it from main() after print_story().
# ============================================================
