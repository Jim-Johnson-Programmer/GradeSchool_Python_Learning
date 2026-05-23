# file_append_example.py
# This script appends text to an existing file and then reads it back.

filename = "sample_file.txt"

# Append to the file
with open(filename, "a") as file:
    file.write("This is an appended line.\n")

print(f"Appended a line to '{filename}'.")

# Read the file back
with open(filename, "r") as file:
    content = file.read()
    print("File contents after appending:")
    print(content)
