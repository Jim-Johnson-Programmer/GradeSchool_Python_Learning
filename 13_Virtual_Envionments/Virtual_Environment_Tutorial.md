# Virtual Environments in Python

## What Is a Virtual Environment?

A virtual environment is a separate Python setup for one project.
It lets you install packages for that project without changing the packages used by other projects.

Think of it like a private toolbox:

- one project gets its own tools
- another project gets a different set of tools
- they do not step on each other

## Why It Matters

Virtual environments help you:

- keep projects organized
- avoid version conflicts between packages
- make it easier to repeat the same setup later
- protect your main Python installation from clutter
- work better in VS Code because the editor can use the exact Python version and packages for the current project

Without a virtual environment, one project might need `requests` version 2.28 while another needs version 2.31. If both projects share the same Python setup, one project can break the other.

## Common Folder Name

Many Python projects name the virtual environment folder `.venv`.

VS Code recognizes `.venv` easily, so it is a common choice.

## Step 1: Open Your Project Folder in VS Code

Before creating a virtual environment, open the folder for your project.

Example:

```text
my_python_project/
```

In VS Code, open that folder so the virtual environment will belong to that project.

## Step 2: Create the Virtual Environment

Open the VS Code terminal and run:

```bash
python -m venv .venv
```

What this does:

- `python` runs Python
- `-m venv` tells Python to create a virtual environment
- `.venv` is the folder name for the environment

This creates a new folder called `.venv` in your project.

## Step 3: Activate the Virtual Environment

After creating it, activate it.

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```bat
.venv\Scripts\activate.bat
```

### macOS or Linux

```bash
source .venv/bin/activate
```

When it is active, your terminal usually shows `(.venv)` at the beginning of the prompt.

## Step 4: Install Packages Inside the Environment

Now install packages normally with `pip`.

Example:

```bash
pip install pygame
pip install requests
```

These packages will be installed inside the virtual environment instead of globally.

## Step 5: Tell VS Code to Use the Virtual Environment

VS Code can automatically use the correct interpreter, but sometimes you need to select it manually.

In VS Code:

1. Press `Ctrl+Shift+P`
2. Type `Python: Select Interpreter`
3. Choose the interpreter inside `.venv`

That tells VS Code to run your code with the project environment.

## Step 6: Check That It Worked

You can confirm the active Python interpreter with:

```bash
python --version
```

You can also check where Python is running from:

```bash
python -c "import sys; print(sys.executable)"
```

If the virtual environment is active, the path should point into `.venv`.

## Example Workflow

Here is the basic workflow for a new project:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pygame
pip freeze > requirements.txt
```

## What Is `requirements.txt`?

`requirements.txt` is a file that lists the packages used by your project.

It helps you or another person recreate the same environment later.

To install everything from that file:

```bash
pip install -r requirements.txt
```

## Why This Is Important in VS Code

VS Code is often used for many Python projects in the same workspace or on the same computer.
A virtual environment lets VS Code know exactly which Python setup belongs to which project.

That means:

- the right packages appear as available
- code completion works better
- imports are easier to manage
- errors from missing packages are reduced
- each project stays clean and predictable

## Student Checklist

- Create the project folder
- Open it in VS Code
- Run `python -m venv .venv`
- Activate the environment
- Install packages with `pip`
- Select the `.venv` interpreter in VS Code
- Save package names in `requirements.txt`

## Quick Practice

Try this on a test project:

1. Make a new folder called `test_project`
2. Create `.venv` inside it
3. Activate it
4. Install one package, such as `requests`
5. Run `pip freeze`
6. Open VS Code and select the `.venv` interpreter

If you can do that, you understand the basics of package control management with virtual environments.
