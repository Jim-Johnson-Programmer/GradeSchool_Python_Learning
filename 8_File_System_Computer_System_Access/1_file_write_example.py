# file_write_example.py
# This script writes text to a new file and then reads it back.

filename = "sample_file.txt"

# Write to the file
with open(filename, "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print(f"File '{filename}' has been written.")

# Read the file back
with open(filename, "r") as file:
    content = file.read()
    print("File contents:")
    print(content)
