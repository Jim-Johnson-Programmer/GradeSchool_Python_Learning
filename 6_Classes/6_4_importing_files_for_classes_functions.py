"""Lesson 6.4 - Importing a class and a function from another file."""
#from file_name          import ClassName,    function_name
from lesson_6_4_helpers import GameCharacter, greet_character


player = GameCharacter("Alex", "builder")

greet_character(player)
print(player.describe())
