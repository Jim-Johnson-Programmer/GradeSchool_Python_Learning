"""Practice file for the virtual environment lesson.

Run this file inside and outside your virtual environment to see how the
Python interpreter changes.

Try these steps in VS Code:
1. Create a virtual environment with: python -m venv .venv
2. Activate it in the terminal
3. Select the .venv interpreter in VS Code
4. Run this file again and compare the output
"""

import sys


def show_python_info():
    """Print the Python version and the interpreter path."""

    print("Python version:", sys.version)
    print("Python executable:", sys.executable)


def student_tasks():
    """Print the practice steps for the student."""

    print("\nPractice Tasks:")
    print("1. Create a folder for a new project.")
    print("2. Make a virtual environment named .venv.")
    print("3. Activate the virtual environment.")
    print("4. Install a package such as requests or pygame.")
    print("5. Run: pip freeze > requirements.txt")
    print("6. Open VS Code and select the .venv interpreter.")
    print("7. Run this file again and look at the interpreter path.")


if __name__ == "__main__":
    print("Virtual Environment Practice")
    print("----------------------------")
    show_python_info()
    student_tasks()
