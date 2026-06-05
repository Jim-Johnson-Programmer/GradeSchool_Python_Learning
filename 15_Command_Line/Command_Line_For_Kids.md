# Command Line for Kids: Mac and PC

## What Is the Command Line?

The command line is a place where you type instructions for the computer.

Instead of clicking with a mouse, you type short commands and press `Enter`.

Think of it like giving your computer tiny robot instructions.

## What Is It Called?

- On a Mac, it is usually called **Terminal**.
- On a PC, it is often called **PowerShell** or **Command Prompt**.

This guide uses:

- **Mac:** Terminal
- **PC:** PowerShell

## Important Safety Rule

Only type commands you understand.

If you are not sure what a command does, ask a parent, teacher, or helper first.

## Opening the Command Line

### On Mac

1. Press `Command + Space`
2. Type `Terminal`
3. Press `Enter`

### On PC

1. Press the `Windows` key
2. Type `PowerShell`
3. Press `Enter`

## What You Will See

You will see a blinking cursor.

That blinking line means:

"I am ready for your next command."

## Your First Commands

### 1. Find Where You Are

This command shows your current folder.

#### Mac

```bash
pwd
```

#### PC

```powershell
pwd
```

### 2. See What Is in the Folder

This command lists files and folders.

#### Mac

```bash
ls
```

#### PC

```powershell
ls
```

### 3. Change Folders

Use `cd` to move into a folder.

If you have a folder named `Games`, you can move into it.

#### Mac

```bash
cd Games
```

#### PC

```powershell
cd Games
```

### 4. Go Back One Folder

The two dots `..` mean "go back one level."

#### Mac

```bash
cd ..
```

#### PC

```powershell
cd ..
```

## Making a New Folder

Use `mkdir` to create a folder.

Example: make a folder called `MyProjects`.

#### Mac

```bash
mkdir MyProjects
```

#### PC

```powershell
mkdir MyProjects
```

## Making a New File

### On Mac

```bash
touch notes.txt
```

This creates a new empty file called `notes.txt`.

### On PC

```powershell
New-Item notes.txt -ItemType File
```

This creates a new empty file called `notes.txt`.

## Clearing the Screen

If your screen gets messy, you can clear it.

#### Mac

```bash
clear
```

#### PC

```powershell
clear
```

## Running a Python File

If you have a Python file named `game.py`, you can run it from the command line.

#### Mac

```bash
python3 game.py
```

#### PC

```powershell
python game.py
```

If `python` works on your Mac, that is fine too, but many Macs use `python3`.

## A Tiny Practice Adventure

Try these commands one by one.

### Mac

```bash
pwd
ls
mkdir RobotClub
cd RobotClub
touch ideas.txt
ls
cd ..
```

### PC

```powershell
pwd
ls
mkdir RobotClub
cd RobotClub
New-Item ideas.txt -ItemType File
ls
cd ..
```

## Using the `*` Wildcard

The `*` symbol is called a wildcard.

It means "match many things."

Think of it like saying:

"Show me everything that starts like this" or "show me everything that ends like this."

For example:

- `*.txt` means all files that end in `.txt`
- `cat*` means all names that start with `cat`

You will often use wildcards with `ls` to look for matching files.

### Mac

```bash
ls *.txt
ls cat*
```

### PC

```powershell
ls *.txt
ls cat*
```

## Wildcard Exercises

Try these in a safe practice folder.

### Exercise 1: Make Some Practice Files

Create a folder and a few files with different names.

#### Mac

```bash
mkdir WildcardPractice
cd WildcardPractice
touch cat.txt
touch car.txt
touch dog.txt
touch game.py
ls
```

#### PC

```powershell
mkdir WildcardPractice
cd WildcardPractice
New-Item cat.txt -ItemType File
New-Item car.txt -ItemType File
New-Item dog.txt -ItemType File
New-Item game.py -ItemType File
ls
```

### Exercise 2: Show Only Text Files

Try to list only files that end in `.txt`.

#### Mac

```bash
ls *.txt
```

#### PC

```powershell
ls *.txt
```

You should see:

- `cat.txt`
- `car.txt`
- `dog.txt`

### Exercise 3: Show Only Names That Start With `ca`

Now try to list files that begin with `ca`.

#### Mac

```bash
ls ca*
```

#### PC

```powershell
ls ca*
```

You should see:

- `cat.txt`
- `car.txt`

### Exercise 4: Find Python Files

Try to list only Python files.

#### Mac

```bash
ls *.py
```

#### PC

```powershell
ls *.py
```

You should see:

- `game.py`

### Exercise 5: Make Your Own Guess

Create one more file and test your own wildcard idea.

Example ideas:

- make `castle.txt` and try `ls cas*`
- make `robot.py` and try `ls *.py`
- make `card.txt` and try `ls car*`

## Easy Meanings to Remember

- `pwd` = print working directory = show where you are
- `ls` = list = show files and folders
- `cd` = change directory = move to a folder
- `mkdir` = make directory = create a folder

## Good Habits

- Read the command before you press `Enter`
- Start with simple commands
- Practice in your own folders
- Ask for help if a command looks confusing

## How to Exit

When you are done, type:

#### Mac

```bash
exit
```

#### PC

```powershell
exit
```

## Final Thought

The command line might look plain, but it is powerful.

Once you learn a few commands, you can move around your computer, make folders, create files, and run programs like a computer wizard.
