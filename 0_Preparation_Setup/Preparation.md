# Lesson 0: Setup & Preparation

---

## Step 1: Download and Install VS Code

**VS Code** is a free code editor where you will write your Python programs.

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com)
2. Click the big **Download** button (it will detect your operating system automatically)
3. Open the downloaded file and follow the installer steps
4. When finished, open VS Code — you should see a welcome screen

---

## Step 2: Download and Install Python

**Python** is the programming language you will be learning.

1. Go to [https://www.python.org/downloads](https://www.python.org/downloads)
2. Click the **Download Python** button (the latest version is fine)
3. Open the downloaded file
4. **Important:** Check the box that says **"Add Python to PATH"** before clicking Install
5. Click **Install Now** and wait for it to finish
6. To verify it worked, open a terminal and type:
   ```
   python --version
   ```
   You should see something like `Python 3.x.x`

---

## Step 3: Install the Python Extension in VS Code

The **Python extension** helps VS Code understand Python code (highlights errors, runs programs, etc.).

1. Open **VS Code**
2. Click the **Extensions** icon on the left sidebar (it looks like 4 squares)
3. In the search box, type **Python**
4. Click on the extension called **"Python"** made by **Microsoft**
5. Click the **Install** button
6. Once installed, VS Code is ready for Python programming!

---

## Step 4: Download and Install Git

**Git** is a tool that saves your code history and lets you upload your work to the internet so it is never lost.

1. Go to [https://git-scm.com/install/windows](https://git-scm.com/install/windows)
2. Click the **Download** button for Windows
3. Open the downloaded file and follow the installer steps (the default options are fine for beginners)
4. To verify it worked, open a terminal and type:
   ```
   git --version
   ```
   You should see something like `git version 2.x.x`

---

## Step 5: Download Code from Jim's Code Storage Website

**GitHub** is a website where your code is stored online. Think of it like Google Drive, but for code!

Your teacher's example code is uploaded here so you can always look it back up:
[https://github.com/Jim-Johnson-Programmer/GradeSchool_Python_Learning](https://github.com/Jim-Johnson-Programmer/GradeSchool_Python_Learning)

### Tell Git your name and email (do this once)

Open a terminal and type these two commands, replacing the example name and email with your own:

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

---

## Step 6: Clone Jim's Code to Your Computer

**Cloning** means downloading a copy of the code from GitHub directly onto your computer so you can open and run it in VS Code.

### Find Jim's Code Page

1. Open your web browser and go to:
   [https://github.com](https://github.com)
2. Click in the browser address bar at the top — it should show `github.com`
3. At the end of `github.com`, add this text so the full address looks like this:
   ```
   github.com/Jim-Johnson-Programmer/GradeSchool_Python_Learning
   ```
4. Press **Enter** — you should now see Jim's code page

### Clone the Code into VS Code

5. Click the green **"< > Code"** button near the top right of the page
6. In the dropdown that appears, click **"Open with Visual Studio Code"**
   - Your browser may ask for permission to open VS Code — click **"Open"** or **"Allow"**
7. VS Code will open and ask you **"Where would you like to clone the repository?"**
   - Choose a folder on your computer (for example, your Desktop or Documents folder)
   - Click **"Select as Repository Destination"**
8. VS Code will download all the files — you will see a progress bar at the bottom
9. When it finishes, a pop-up will ask **"Would you like to open the cloned repository?"** — click **"Open"**
10. You should now see all of Jim's lesson files in the VS Code sidebar on the left!

---

## You're All Set!

You now have everything you need to start writing Python. Open VS Code, create a new file ending in `.py`, and you're ready to code!
