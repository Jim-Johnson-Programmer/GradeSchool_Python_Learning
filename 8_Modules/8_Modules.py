"""Lesson 8 - Python Modules (Beginner Tutorial)

A module is a Python file that contains reusable code.
You import a module when you want to use code from somewhere else.

This lesson shows:
1. Importing built-in modules
2. Importing specific names from a module
3. Using aliases with imports
4. Why modules are useful for clean projects
"""

# ------------------------------------------------------------
# PART 1: Import a full module
# ------------------------------------------------------------
# "import math" gives access to math functions using dot notation.
import math


def part_1_full_module_import():
	print("PART 1: Full module import")
	print("math.sqrt(81) =", math.sqrt(81))
	print("math.pi =", math.pi)
	print()


# ------------------------------------------------------------
# PART 2: Import specific names
# ------------------------------------------------------------
# "from module import name" lets you use that name directly.
from random import randint


def part_2_specific_import():
	print("PART 2: Import specific names")
	print("Random integer from 1 to 10:", randint(1, 10))
	print()


# ------------------------------------------------------------
# PART 3: Import with alias
# ------------------------------------------------------------
# Aliases shorten long names.
import datetime as dt


def part_3_alias_import():
	print("PART 3: Import with alias")
	now = dt.datetime.now()
	print("Current date and time:", now)
	print()


# ------------------------------------------------------------
# PART 4: Why modules matter
# ------------------------------------------------------------
# Modules help you split a big program into smaller files.
# This makes code easier to read, test, and reuse.
def part_4_why_modules_matter():
	print("PART 4: Why modules matter")
	print("- Reuse code instead of rewriting it")
	print("- Keep files smaller and easier to understand")
	print("- Organize projects by responsibility")
	print("- Work better in teams")
	print()


# ------------------------------------------------------------
# PART 5: Student practice challenge
# ------------------------------------------------------------
def challenge():
	print("CHALLENGE")
	print("1. Import the 'statistics' module.")
	print("2. Make a list of numbers.")
	print("3. Print the mean using statistics.mean().")
	print("4. Try importing one function directly from statistics.")
	print()


def main():
	print("========================================")
	print("Lesson 8: Python Modules")
	print("========================================")
	print()

	part_1_full_module_import()
	part_2_specific_import()
	part_3_alias_import()
	part_4_why_modules_matter()
	challenge()


if __name__ == "__main__":
	main()
