# Python Gaming Learning Plan

**For Grade School & Middle School Students**

Build your Python skills step by step — and finish by making real games you can play!

---

## Where We Are Now

Before jumping into games, make sure you have completed the core Python lessons:

| ✅  | Lesson                 | Topics Covered                        |
| --- | ---------------------- | ------------------------------------- |
| ☐   | 1 – Strings & Mad Libs | Strings, input(), print()             |
| ☐   | 2 – Integers           | Math with whole numbers               |
| ☐   | 3 – Floats & Decimals  | Math with decimal numbers             |
| ☐   | 4 – Data Types         | type(), casting, checking types       |
| ☐   | 5 – Functions          | def, parameters, return values        |
| ☐   | 6 – Classes            | Blueprints, member variables, methods |

---

## Stage 1 — Game Logic Building Blocks

_New topics needed before making games_

### 7 — Booleans & Comparisons

- `True` / `False`
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Mini-project:** "Is the player's health above zero?" checker

### 8 — If / Elif / Else

- Decision-making in code
- Nested conditions
- **Mini-project:** Text-based "Fight or Flee" encounter

### 9 — While Loops

- Repeating actions until a condition changes
- `break` and `continue`
- **Mini-project:** Game loop that keeps running until the player quits

### 10 — For Loops & Lists

- Storing multiple items (inventory, high scores)
- Looping over a list
- `append()`, `len()`, indexing
- **Mini-project:** Player inventory system

### 11 — Dictionaries

- Key-value storage (item name → damage, player name → score)
- **Mini-project:** Minecraft item stat lookup table

---

## Stage 2 — Text-Based Games

_Pure Python, no extra libraries needed_

### 12 — Random Numbers

- `import random`
- `random.randint()`, `random.choice()`
- **Mini-project:** Dice roller for a board game

### 13 — Text Adventure Game

- Rooms, choices, inventory
- Combines: classes, if/else, loops, dictionaries
- **Project:** Build a 5-room dungeon crawler with a win/lose condition

### 14 — Number Guessing Game

- While loops + user input + random numbers
- Track number of guesses
- **Project:** "Guess the number 1–100" with a high-score tracker

### 15 — Rock Paper Scissors

- Functions + random + if/else
- Best-of-3 round system
- **Project:** Rock Paper Scissors vs. the computer

---

## Stage 3 — Graphical Games with Pygame

_Install `pygame` — brings graphics, sound, and keyboard input_

### 16 — Pygame Setup & the Game Loop

- Install pygame: `pip install pygame`
- Create a window, set FPS, draw a background
- Understand the event loop
- **Mini-project:** Colored window that closes when you press X

### 17 — Drawing Shapes & Colors

- `pygame.draw.rect()`, `circle()`, `line()`
- Pixel coordinates and screen layout
- **Mini-project:** Draw a simple Minecraft-style landscape

### 18 — Moving a Sprite

- Keyboard input (`pygame.key.get_pressed()`)
- Updating position every frame
- **Mini-project:** Move a player block around the screen

### 19 — Collision Detection

- `pygame.Rect` and `.colliderect()`
- **Mini-project:** Player collects coins; score goes up

### 20 — Images & Sound

- `pygame.image.load()` — add a character sprite
- `pygame.mixer.Sound()` — add sound effects
- **Mini-project:** Player with custom sprite and jump sound

---

## Stage 4 — Complete Pygame Games

_Put everything together into full, playable games_

### 21 — Platformer Game

- Gravity, jumping, platforms
- Enemies that move back and forth
- Health bar drawn on screen
- **Project:** Side-scrolling platformer (3 levels)

### 22 — Top-Down Shooter

- Player shoots projectiles
- Enemies spawn and move toward the player
- Score and lives display
- **Project:** Space Invaders–style shooter

### 23 — Minecraft Mini-Game

- Tile-based grid world
- Place and break blocks
- Simple crafting system using dictionaries
- **Project:** Mini Minecraft clone with at least 5 block types

---

## Bonus Challenges

| Challenge                                | Skills Used                        |
| ---------------------------------------- | ---------------------------------- |
| Add a high-score file that saves to disk | File I/O (`open`, `read`, `write`) |
| Multiplayer on one keyboard (2 players)  | Multiple input handlers            |
| Procedurally generated dungeon map       | 2D lists + random                  |
| Enemy AI that chases the player          | Distance math + classes            |
| Menu screen with buttons                 | Mouse events + pygame              |

---

## Recommended Tools

| Tool                 | What It's For                       |
| -------------------- | ----------------------------------- |
| **VS Code**          | Writing and running Python          |
| **pygame**           | Graphics, sound, keyboard for games |
| **Python 3.10+**     | Language version to use             |
| **Tiled** (optional) | Draw tile maps for platformers      |

---

## How to Install pygame

Open a terminal and type:

```bash
pip install pygame
```

Test it works:

```python
import pygame
print(pygame.version.ver)
```

---

_Keep building, keep playing — every game starts with one line of code!_
