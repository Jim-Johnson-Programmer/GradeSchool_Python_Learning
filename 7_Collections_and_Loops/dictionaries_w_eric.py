player = {
    "name":   "Eric",
    "health": 100,
    "level":  5,
    "score":  2400
}

print(player["name"])     # → Eric

for key in player:
    print(key)        # → name, health, level, score
    print(player[key]) # → Eric, 100, 5, 2400

while True:
    key = input("Enter a key to look up (or 'quit' to exit): ")
    if key == "quit":
        break
    elif key in player:
        print(player[key])
    else:
        print("Key not found.")