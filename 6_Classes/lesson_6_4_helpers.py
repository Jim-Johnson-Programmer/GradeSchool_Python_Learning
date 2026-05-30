# ============================================================
# Lesson 6.4 Helper Module
# ============================================================
# This file holds a class and a function that can be imported
# and used from another Python file.
# ============================================================


class GameCharacter:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return self.name + " is the " + self.role + "."


def greet_character(character):
    print("Hello, " + character.name + " the " + character.role + "!")
