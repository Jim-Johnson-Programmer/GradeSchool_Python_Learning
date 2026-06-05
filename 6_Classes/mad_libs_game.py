# ============================================================
# Mad Libs Game Helper Class
# ============================================================
# This file stores the Mad Libs game inside a class so another
# Python file can import it and run it.
# ============================================================


class MadLibsGame:
    def __init__(self):
        self.a_name = ""
        self.an_animal = ""
        self.a_body_part = ""
        self.an_adjective1 = ""
        self.an_adjective2 = ""
        self.a_verb1 = ""
        self.a_verb2 = ""
        self.a_place = ""
        self.a_food = ""
        self.a_number = ""
        self.an_exclamation = ""

    def collect_words(self):
        print("=== WELCOME TO MAD LIBS! ===")
        print("Answer each question with ANY word - the sillier the better!")
        print("")

        self.a_name = input("Type a funny name: ")
        self.an_animal = input("Type an animal: ")
        self.a_body_part = input("Type a body part: ")
        self.an_adjective1 = input("Type a describing word (e.g. slimy, purple, tiny): ")
        self.an_adjective2 = input("Type another describing word: ")
        self.a_verb1 = input("Type an action word ending in -ed (e.g. jumped, exploded, wiggled): ")
        self.a_verb2 = input("Type another action word ending in -ing (e.g. running, burping, flying): ")
        self.a_place = input("Type a place (e.g. school, the moon, a taco shop): ")
        self.a_food = input("Type a food: ")
        self.a_number = input("Type a number: ")
        self.an_exclamation = input("Type a silly exclamation (e.g. YIKES, ZOINKS, OH BEANS): ")

    def print_story(self):
        print("")
        print("============================================")
        print("        ** YOUR MAD LIBS STORY **          ")
        print("============================================")
        print("")

        print("One " + self.an_adjective1 + " morning, " + self.a_name + " woke up to find a " + self.an_adjective2 + " " + self.an_animal)
        print("sitting right on their " + self.a_body_part + "!")
        print("")
        print(self.an_exclamation + "! screamed " + self.a_name + ", leaping out of bed and " + self.a_verb2 + " all the way to " + self.a_place + ".")
        print("")
        print("When they arrived, they discovered " + self.a_number + " plates of " + self.a_food + " stacked on the floor.")
        print("The " + self.an_animal + " had followed them and immediately " + self.a_verb1 + " right into the biggest pile!")
        print("")
        print("Everyone at " + self.a_place + " laughed so hard that their " + self.a_body_part + " fell off.")
        print("")
        print(self.a_name + " just shook their head and said,")
        print('"I can\'t believe a ' + self.an_adjective2 + " " + self.an_animal + " ruined my " + self.a_food + " again. " + self.an_exclamation + '!"')
        print("")
        print("                    THE END")
        print("============================================")

    def run(self):
        self.collect_words()
        self.print_story()