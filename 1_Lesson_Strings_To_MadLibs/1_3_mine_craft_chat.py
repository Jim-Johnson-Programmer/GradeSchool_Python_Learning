# ============================================================
# Lesson 1.3 - Minecraft Player Chat
# ============================================================
# Let's use what we know about variables and input() to build
# a fun Minecraft chat conversation between two players!
#
# In this version, the chat game has been moved into a CLASS
# in a separate file so it can be imported and reused.
# ============================================================

from minecraft_chat_game import MinecraftChatGame

game = MinecraftChatGame()
game.run()


# ============================================================
# YOUR TURN! Try these challenges:
# 1. Add a third player to the MinecraftChatGame class.
# 2. Add a new question asking how many diamonds Player 2 found.
# 3. Add coordinates so the players can meet at a location.
# 4. Make a second script file that imports MinecraftChatGame
#    and starts the chat game too.
# ============================================================