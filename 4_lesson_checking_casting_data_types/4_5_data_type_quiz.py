# ============================================================
# Lesson 4.5 - Data Type Quiz
# ============================================================
# For each question, you will be shown a real-world value and
# asked to pick the BEST Python data type to store it:
#
#   A) str   — text / anything with letters, symbols, or
#              numbers that you will NOT do math on
#   B) int   — whole number (no decimal point)
#   C) float — decimal number
#   D) bool  — True or False answer
#
# Type the letter of your answer and press Enter.
# ============================================================

score      = 0
total      = 0

def ask(question, correct_letter, explanation):
    """Ask one question and return 1 if correct, 0 if not."""
    global score, total
    total += 1
    print()
    print(f"Question {total}: {question}")
    print("  A) str    B) int    C) float    D) bool")
    answer = input("  Your answer: ").strip().upper()

    if answer == correct_letter.upper():
        print("  ✓ Correct! " + explanation)
        score += 1
    else:
        print(f"  ✗ Not quite. The answer is {correct_letter.upper()}.")
        print("    " + explanation)


# ============================================================
# Round 1 — License Plates & Vehicle Numbers
# ============================================================
print("=" * 54)
print("  Round 1: License Plates & Vehicle Numbers")
print("=" * 54)

ask(
    'A license plate: "7ABC123"',
    "A",
    "License plates mix letters and digits and you never do "
    "math with them → str."
)

ask(
    'The year a car was manufactured: 2019',
    "B",
    "A whole year with no decimal point → int. "
    "(You might subtract years to find the car's age.)"
)

ask(
    'A vehicle identification number (VIN): "1HGCM82633A123456"',
    "A",
    "A VIN has letters, digits, and a fixed length. "
    "You never add VINs together → str."
)

ask(
    'Miles per gallon rating: 28.5',
    "C",
    "Fuel economy can have a decimal → float."
)

ask(
    'Is the car currently registered? (yes/no)',
    "D",
    "A yes/no question is a True/False value → bool."
)


# ============================================================
# Round 2 — Bar Codes & Product IDs
# ============================================================
print()
print("=" * 54)
print("  Round 2: Bar Codes & Product IDs")
print("=" * 54)

ask(
    'A UPC barcode number: "0 12345 67890 5"',
    "A",
    "Barcodes often start with a leading zero and include "
    "spaces or dashes — must keep them exactly → str."
)

ask(
    'Quantity of an item in stock: 144',
    "B",
    "A count of whole items → int."
)

ask(
    'Item weight shown on a label: 1.75  (pounds)',
    "C",
    "Weight with a decimal → float."
)

ask(
    'Is an item currently on sale? (True/False)',
    "D",
    "On-sale or not is a two-option answer → bool."
)

ask(
    'A product SKU code: "SKU-00482-BLU"',
    "A",
    "A SKU has letters, dashes, and leading zeros — store "
    "it exactly as-is → str."
)


# ============================================================
# Round 3 — Money & Prices
# ============================================================
print()
print("=" * 54)
print("  Round 3: Money & Prices")
print("=" * 54)

ask(
    'Price of a sandwich: $4.99',
    "C",
    "Money almost always has cents (a decimal) → float."
)

ask(
    'Number of items in a shopping cart: 3',
    "B",
    "A plain count of whole items → int."
)

ask(
    'A bank account number: "00739201847"',
    "A",
    "Account numbers have leading zeros and you never do "
    "math with them → str."
)

ask(
    'Has the bill been paid? (True/False)',
    "D",
    "Paid or unpaid is a yes/no → bool."
)

ask(
    'A credit card number: "4532 0151 1283 0366"',
    "A",
    "Credit card numbers include spaces and leading digits "
    "that must be preserved — never do math on them → str."
)

ask(
    'Total tax on a purchase: 1.37',
    "C",
    "Tax is a dollar-and-cents value with a decimal → float."
)


# ============================================================
# Round 4 — Phone Numbers, ZIP Codes & Addresses
# ============================================================
print()
print("=" * 54)
print("  Round 4: Phone Numbers, ZIP Codes & Addresses")
print("=" * 54)

ask(
    'A US phone number: "555-867-5309"',
    "A",
    "Phone numbers have dashes and you never add two phone "
    "numbers together → str."
)

ask(
    'A ZIP code: "07030"',
    "A",
    "ZIP codes can start with a zero — storing as int "
    "would erase it. Always use str for ZIP codes!"
)

ask(
    'Number of floors in a building: 12',
    "B",
    "A count of whole floors → int."
)

ask(
    'A street address: "42 Maple Street"',
    "A",
    "Addresses mix numbers and words → str."
)

ask(
    'Is the address a P.O. Box? (True/False)',
    "D",
    "Yes/no → bool."
)


# ============================================================
# Round 5 — Sports & Games
# ============================================================
print()
print("=" * 54)
print("  Round 5: Sports & Games")
print("=" * 54)

ask(
    "An athlete's jersey number: 23",
    "A",
    "Jersey numbers are labels — you never calculate "
    "\"jersey 23 + jersey 10\". Treat them as str. "
    "(Many coaches store them as str to allow leading zeros "
    "like 07.)"
)

ask(
    "Points scored in a basketball game: 102",
    "B",
    "A game score is a real count you might add or compare → int."
)

ask(
    "A runner's finish time in seconds: 9.58",
    "C",
    "Race times have fractions of a second → float."
)

ask(
    'Did the home team win? (True/False)',
    "D",
    "Win or lose → bool."
)

ask(
    'Player rank/leaderboard position: 1',
    "B",
    "A whole-number rank you might add/subtract → int."
)


# ============================================================
# Round 6 — Science & Measurements
# ============================================================
print()
print("=" * 54)
print("  Round 6: Science & Measurements")
print("=" * 54)

ask(
    'Temperature outside today: 72.4  (°F)',
    "C",
    "Temperatures often have decimals → float."
)

ask(
    'Number of planets in our solar system: 8',
    "B",
    "A whole count → int."
)

ask(
    'A chemical formula label: "H2O"',
    "A",
    "A formula contains letters and digits that are not "
    "meant for math → str."
)

ask(
    'Is water frozen at this temperature? (True/False)',
    "D",
    "A physical yes/no state → bool."
)

ask(
    'Exact mass of a sample: 0.005  (grams)',
    "C",
    "A very small decimal measurement → float."
)


# ============================================================
# Final Score
# ============================================================
print()
print("=" * 54)
print("              QUIZ  COMPLETE!")
print("=" * 54)
print(f"  You got {score} out of {total} correct.")

percentage = round((score / total) * 100)
print(f"  That is {percentage}%!")
print()

if percentage == 100:
    print("  PERFECT SCORE! You are a data type master!")
elif percentage >= 80:
    print("  Great job! Review any questions you missed.")
elif percentage >= 60:
    print("  Good effort! Re-read the lesson notes and try again.")
else:
    print("  Keep studying — you will get there! Review")
    print("  Data_Types.md and the lesson files, then try again.")

print()
