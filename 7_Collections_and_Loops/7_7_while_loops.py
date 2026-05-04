# ============================================================
# Lesson 7.7 - While Loops
# ============================================================
# A WHILE LOOP repeats code as long as a condition is True.
# Unlike a for loop (which loops a known number of times),
# a while loop keeps going until something CHANGES.
#
# Key word:  while
#   - Check the condition BEFORE each repetition
#   - If the condition is True  → run the indented block
#   - If the condition is False → skip the block and move on
#
# WARNING: if the condition NEVER becomes False,
# the loop runs forever — called an INFINITE LOOP.
# Always make sure something inside the loop moves toward
# making the condition False!
# ============================================================


# ============================================================
# PART 1: A Basic While Loop
# ============================================================

count = 1

while count <= 5:
    print(count)
    count = count + 1    # ← this moves us toward stopping!

# → 1
# → 2
# → 3
# → 4
# → 5

# After the loop: count is 6, and 6 <= 5 is False, so the loop stops.


# ============================================================
# PART 2: Countdown Example
# ============================================================

countdown = 5

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Blast off!")

# → 5  4  3  2  1  Blast off!


# ============================================================
# PART 3: While Loop with a Flag Variable
# ============================================================
# A "flag" is a True/False variable that controls the loop.
# Very common pattern in games ("keep playing until game_over").

game_over = False
lives = 3

while not game_over:
    print("Playing... lives:", lives)
    lives = lives - 1
    if lives == 0:
        game_over = True

print("Game Over!")

# → Playing... lives: 3
# → Playing... lives: 2
# → Playing... lives: 1
# → Game Over!


# ============================================================
# PART 4: while True and break
# ============================================================
# A very common pattern is  while True:  which loops forever
# until a  break  statement exits it.

attempts = 0
secret = 42

while True:
    attempts = attempts + 1
    guess = 42       # pretending the user guessed correctly on attempt 1
    if guess == secret:
        print("You got it in", attempts, "attempt(s)!")
        break        # exit the loop immediately

# → You got it in 1 attempt(s)!


# ============================================================
# PART 5: Using continue in a While Loop
# ============================================================
# continue — skip the rest of this iteration and re-check the condition.

number = 0

while number < 10:
    number = number + 1
    if number % 2 == 0:
        continue        # skip printing even numbers
    print(number)

# → 1  3  5  7  9


# ============================================================
# PART 6: Processing a List with While
# ============================================================
# You can use a while loop with an index to go through a list.
# (A for loop is usually simpler for this, but it's good to know.)

fruits = ["apple", "banana", "cherry"]
index = 0

while index < len(fruits):
    print(fruits[index])
    index = index + 1

# → apple
# → banana
# → cherry


# ============================================================
# PART 7: Removing Items from a List While Looping
# ============================================================
# While loops are better than for loops when you need to
# REMOVE items from a list AS you process them.

tasks = ["wash dishes", "do homework", "clean room"]

while len(tasks) > 0:
    current_task = tasks.pop(0)     # remove and get the first task
    print("Doing:", current_task)

print("All done!")

# → Doing: wash dishes
# → Doing: do homework
# → Doing: clean room
# → All done!


# ============================================================
# PART 8: Collecting Input Until a Condition (Simulated)
# ============================================================
# In real programs you'd use input() to get data from a user.
# Here we simulate that with a list of "pretend" responses.

responses = ["no", "no", "yes"]    # pretend user answers
index = 0

while responses[index] != "yes":
    print("Not yet...")
    index = index + 1

print("User said yes!")

# → Not yet...
# → Not yet...
# → User said yes!


# ============================================================
# PART 9: for Loop vs while Loop — When to Use Which
# ============================================================
#
#   Use a FOR loop when:               Use a WHILE loop when:
#   - You know how many times          - You don't know how many
#     to loop (or you're going           times you'll loop
#     through a collection)
#   - Looping through a list,          - Waiting for something to
#     tuple, set, or dictionary          happen (user input, game
#                                        event, condition changing)
#   - Looping n times with range()     - "Keep going until..."


# ============================================================
# PART 10: Mini Challenge
# ============================================================
# 1. Write a while loop that prints every multiple of 3
#    from 3 up to and including 30.
# 2. Write a while loop that counts how many items in a list
#    are greater than 10.

# Challenge 1:
n = 3
while n <= 30:
    print(n)
    n = n + 3

# Challenge 2:
values = [5, 12, 8, 20, 3, 15, 7, 11]
count = 0
i = 0

while i < len(values):
    if values[i] > 10:
        count = count + 1
    i = i + 1

print("Numbers greater than 10:", count)   # → 4
