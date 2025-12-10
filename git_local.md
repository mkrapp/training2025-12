---
marp: true
theme: gaia
---

# Git Basics Training

--------------------------------------------------------

## Agenda

**1.00 - 1.30** Intro & Key Concepts\
**1.30 - 2.30** Git (local) Fundamentals\
**2.30 - 2.40** Break\
**2.40 - 3.40** Git (remote) Collaboration\
**3.40 - 4.00** Discussion & Wrap up

--------------------------------------------------------

## What is Git?

Git is a version control system.

**Version control** is a **system** that records changes to a file or set of files over time so that you can recall specific versions later.

--------------------------------------------------------

## What is GitHub?

GitHub is an online platform for files tracked by git which enables:
- Cloud storage
- Sharing/collaborating with others
- Easy integration with other cloud softwares

--------------------------------------------------------

## Why is Git useful?

Git is like a time machine for your code.

It creates snapshots of your work through time, letting you easily revert to previous versions and experiment safely.

--------------------------------------------------------

**Example:**

You're analysing earthquake data with analyse_data.py. You add a new visualisation function, but it breaks your entire analysis. What changed?

*Without Git:* analyse_data_v1.py, analyse_data_v2_final.py etc. 

*With Git:* One file. Instant revert to the last working version with a single command. Essential when working with complex research code or collaborating with others.

--------------------------------------------------------

## How does it work?

Essentailly, Git is an advanced save button.

A save in Git is called a **commit**. When you make a commit, you take a snapshot of all the files you have made visible to git in your directory – otherwise known as your git **repository**, or repo for short.

This snapshot saves the current state, and that particular commit can then be accessed further down the line if you mess anything up.

--------------------------------------------------------

## Key Concepts / Commands

--------------------------------------------------------

### Repository (repo for short)

A folder/directory that is tracked by git (i.e. it has a .git folder)

**Local repository** - on your local machine e.g. laptop, PC

**Remote repository** - hosted on a server e.g. Github, Gitlab

--------------------------------------------------------

### The Three States / Areas
![width:1000px height:500px](https://docs.nesi.org.nz/assets/images/Git-Reference_Sheet.svg)

--------------------------------------------------------

<details> 
  <summary>Q: Why do you need a staging area? Why not just save everything directly from the working directly? </summary>
   A: It allows you to be specific about what you save, and when. You could have a messy working directory with throwaway files you don't want to save to Git. Or you may want to save different files in differents commits so your version control history is easier to understand.
</details>

--------------------------------------------------------

### Commands

`git add` prepares files to be saved in git by 'staging'/'tracking' them

`git commit` saves files to git by taking snapshot. These create the building blocks of version control history and have a unique ID, message, author and timestamp.

--------------------------------------------------------

### Commands

`git init` intialise directory as git repository

`git status` check what changes git is aware of

`git diff` look at the differences made to a file

`git log` look at the commit history

--------------------------------------------------------

### Commands for later

`git branch` creates a parallel version of the codebase to experiment and break things without disrupting the main code or others work.

![width:900px height:400px](https://shrra.github.io/python-intermediate-development/fig/git-feature-branch.svg)

--------------------------------------------------------

### Commands for later

`git merge` brings the changes made on a branch into the main codebase. You can think of it like the work/changes being made 'official'

--------------------------------------------------------

# Activity 1: Setting up our first repostiory

--------------------------------------------------------

## Configure Identity

*You'll only ever need to do this once*

`git config --global user.name "Your Name"`

`git config --global user.email "your.email@example.com"`

Check it worked:

`git config --global --list`

--------------------------------------------------------

## Create repository

> [!TIP] I recommend creating a directory called 'respositories' in your home directly

Mac: `cd ~` Windows: `cd C:\Users\yourUserName`

`mkdir repositories`

`cd repositories`

`mkdir my-first-project`

Mac: `ls`		Windows: `dir`

--------------------------------------------------------

`cd my-first-project`

`git init`

Check for hidden .git file:

Mac: `ls -la` Windows: `dir /a`

Check what git can currently see:

`git status`

--------------------------------------------------------

## Create first file

Create README.md with your text editor OR in the command line:

`echo # My Git Project > README.md`

Check it exists:

Mac: `ls` Windows: `dir`

Look at contents in the file:

`more README.md` or `less README.md` or `cat README.md`

Exit: `q`

--------------------------------------------------------

## First Commit

##### Edit -> Check -> Add -> Commit -> Repeat

Check what Git sees: 

`git status `

> [!NOTE] What do you see here? What colour is it?

Stage the file (prepare it for commit):

`git add README.md `

`git status`

> [!NOTE]
> What has changed?

--------------------------------------------------------

Make your first commit (save the snapshot): 

`git commit`

It will now ask you to enter a commit message, you could use:

"Initial commit: Add README"

> [!TIP]
> Be really descriptive with commit messages. It is easy for your future self to forget what you did and why. And even harder for other people if collaborating!

Exit:

    Press ESC
    type ':wq'
    Press Enter

`git status`

> [!NOTE]
> Now what has changed?

--------------------------------------------------------

## View History

`git log`

--------------------------------------------------------

# Activity 2: Practising the Git Workflow

Edit -> Check -> Add -> Commit -> Repeat

--------------------------------------------------------

## Single file change

Edit and save README.md, add whatever you like to it. e.g.: 

    I am learning about version control

`echo '\nI am learning about version control' >> README.md`

Check what changed for Git: 

`git status`

See the actual changes: 

`git diff`

--------------------------------------------------------

Stage and commit: 

`git add README.md`

> [!TIP]
> If your commit message is one line, you can use `-m` to add commit message in one command

`git commit -m "Add learning section to README"`

Check the log:

> [!TIP]
> If you want a simplified view of commits, you can indicate one line

`git log --oneline`

--------------------------------------------------------

## Multiple file change

Create a python file called ‘test.py’. You can do this in your text editor, add whatever you like e.g.:

    print(“hello, world!”)

or in the command line like this:

`echo 'print("hello, world!")' > test.py`

Now also edit README.md, add anything you like e.g.:

    Learning git is fun

or do so in the command line:

`echo ‘\nLearning git is fun’ >> README.md`

--------------------------------------------------------

Check status: 

`git status`

Stage README.md:

`git add README.md `

`git status`

> [!NOTE]
> Notice what changes here, and the colour of the files

You realise you were told by your manager you have to include your name in the README.md file. To do this you can undo the staging, add your name to the file and stage it again.

`git restore --staged README.md`

`git status`

--------------------------------------------------------

Add your name to the file e.g.:

    Learning git is really fun
 
> [!TIP]
> Now, if you have multiple files you want to add, you can either do so using their separate names, or you can use a shortcut funtion.

`git add README.md test.py`

`git add .` or `git add -A`

> [!WARNING]
> This adds everything that has been changed at the time

`git status`

--------------------------------------------------------

Commit everything together and write a commit message:

`git commit -m 'Add test.py and update README with my feelings about learning git'`

View your history:

`git log --oneline`

--------------------------------------------------------

# Activity 3: Practice the Workflow

Edit -> Check -> Add -> Commit -> Repeat

You could try:
- Changing a file
- Adding another file
- Deleting a file

--------------------------------------------------------

# Activiy 4: Fixing Common Mistakes

> [!TIP]
> There are no real mistakes in Git. It is made for handling errors, breaking things and undoing things

--------------------------------------------------------

## Scenario 1: I staged the wrong file, how do I unstage something?

> [!TIP]
> We use this command earlier when we wanted to add our name to the README file!

Create a temporary file in text editor or command line

`echo "temporary stuff" > temp.txt`

Stage the file

`git add temp.txt`

`git status`

You realise, you didn't mean to stage this file

`git restore --staged temp.txt`

`git status`

--------------------------------------------------------

## Scenario 1: I want to undo the changes I made to a file

Edit test.py but don't commit e.g.:

    print("Learning git is not fun")

Check you have uncommitted changes:

`git status `

`git diff`

Discard the changes: 

`git restore test.py`

`git status` 

File is back to how it was at last commit 

--------------------------------------------------------

## Scenario 3: I commited the wrong thing, how do I undo a commit?

Add and commit temp.txt

`git add temp.txt`

`git commit -m "Add temporary file"`

View log:

`git log --oneline`

You can either undo the commit to the one before, or you can specify the commit hash (unique ID) of the commit you want to undo.

`git reset HEAD~1`

`git reset HEAD~<uniqueCommitHash>`

--------------------------------------------------------

Check:

`git status`

Actually we don't want this file at all:

`git restore temp.txt`

Check:

`git status`

`git log --oneline`

--------------------------------------------------------



