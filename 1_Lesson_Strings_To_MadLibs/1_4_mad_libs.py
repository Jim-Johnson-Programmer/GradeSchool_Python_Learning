# ============================================================
# Lesson 1.4 - Mad Libs!
# ============================================================
# Mad Libs is a word game where you fill in the blanks with
# silly words — and then read back a hilarious story!
#
# In this program:
#   1. We ask you for a bunch of random words using input()
#   2. We store each word in a variable
#   3. We plug them all into a crazy story and print it out!
#
# The trick is: DON'T tell the player what the story is
# until AFTER they have typed all their words!
# ============================================================


# ============================================================
# PART 1: Collect All the Words (No peeking at the story!)
# ============================================================

print("=== WELCOME TO MAD LIBS! ===")
print("Answer each question with ANY word — the sillier the better!")
print("")

a_name           = input("Type a funny name: ")
an_animal        = input("Type an animal: ")
a_body_part      = input("Type a body part: ")
an_adjective1    = input("Type a describing word (e.g. slimy, purple, tiny): ")
an_adjective2    = input("Type another describing word: ")
a_verb1          = input("Type an action word ending in -ed (e.g. jumped, exploded, wiggled): ")
a_verb2          = input("Type another action word ending in -ing (e.g. running, burping, flying): ")
a_place          = input("Type a place (e.g. school, the moon, a taco shop): ")
a_food           = input("Type a food: ")
a_number         = input("Type a number: ")
an_exclamation   = input("Type a silly exclamation (e.g. YIKES, ZOINKS, OH BEANS): ")


# ============================================================
# PART 2: Print the Mad Libs Story!
# ============================================================

print("")
print("============================================")
print("        ** YOUR MAD LIBS STORY **          ")
print("============================================")
print("")

print("One " + an_adjective1 + " morning, " + a_name + " woke up to find a " + an_adjective2 + " " + an_animal)
print("sitting right on their " + a_body_part + "!")
print("")
print(an_exclamation + "!" + " screamed " + a_name + ", leaping out of bed and " + a_verb2 + " all the way to " + a_place + ".")
print("")
print("When they arrived, they discovered " + a_number + " plates of " + a_food + " stacked on the floor.")
print("The " + an_animal + " had followed them and immediately " + a_verb1 + " right into the biggest pile!")
print("")
print("Everyone at " + a_place + " laughed so hard that their " + a_body_part + " fell off.")
print("")
print(a_name + " just shook their head and said,")
print("\"I can't believe a " + an_adjective2 + " " + an_animal + " ruined my " + a_food + " again. " + an_exclamation + "!\"")
print("")
print("                    THE END")
print("============================================")


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Add TWO more input() questions (like a color and a planet)
#    and work them into the story somewhere.
# 2. Print the animal's name in ALL CAPS using .upper() to
#    make it sound extra dramatic.
# 3. Write your OWN mad libs story using at least 6 variables.
#    Come up with totally different blanks and a new plot!
# ============================================================
