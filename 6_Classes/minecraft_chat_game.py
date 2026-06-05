# ============================================================
# Minecraft Chat Game Helper Class
# ============================================================
# This file holds the class that runs the Minecraft chat game.
# Another file can import this class and use it.
# ============================================================


class MinecraftChatGame:
    def __init__(self):
        self.player1_name = ""
        self.player1_biome = ""
        self.player1_item = ""
        self.player1_mob = ""

        self.player2_name = ""
        self.player2_biome = ""
        self.player2_item = ""
        self.player2_building = ""

    def collect_player_info(self):
        print("=== MINECRAFT CHAT SETUP ===")
        print("Answer the questions for both players.")
        print("")

        self.player1_name = input("Player 1 - Enter your Minecraft username: ")
        self.player1_biome = input("Player 1 - What biome are you in? (e.g. jungle, desert, snow): ")
        self.player1_item = input("Player 1 - What item are you holding? (e.g. diamond sword, pickaxe): ")
        self.player1_mob = input("Player 1 - What mob are you fighting? (e.g. creeper, zombie, skeleton): ")

        print("")

        self.player2_name = input("Player 2 - Enter your Minecraft username: ")
        self.player2_biome = input("Player 2 - What biome are you in? (e.g. forest, ocean, nether): ")
        self.player2_item = input("Player 2 - What item are you holding? (e.g. bow, shield, axe): ")
        self.player2_building = input("Player 2 - What are you building? (e.g. a castle, a farm, a house): ")

    def print_chat(self):
        print("")
        print("============================================")
        print("           ** MINECRAFT CHAT **            ")
        print("============================================")
        print("")

        print(self.player1_name + ": Hey " + self.player2_name + "! Where are you right now?")
        print("")

        print(self.player2_name + ": I'm in a " + self.player2_biome + " biome! I'm building " + self.player2_building + ".")
        print(self.player2_name + ": What about you?")
        print("")

        print(self.player1_name + ": I'm in the " + self.player1_biome + "! It's crazy here!")
        print(self.player1_name + ": I've got my " + self.player1_item + " ready.")
        print("")

        print(self.player2_name + ": Oh no - are you in trouble?")
        print("")

        print(self.player1_name + ": YES! There's a " + self.player1_mob + " right behind me!!")
        print("")

        print(self.player2_name + ": Use your " + self.player1_item + " and fight it!")
        print(self.player2_name + ": I'll come help - let me grab my " + self.player2_item + "!")
        print("")

        print(self.player1_name + ": HURRY! Meet me in the " + self.player1_biome + "!")
        print("")

        print(self.player2_name + ": On my way! Don't die " + self.player1_name + " !!")
        print("")

        print("============================================")
        print("              ** END OF CHAT **            ")
        print("============================================")

    def run(self):
        self.collect_player_info()
        self.print_chat()