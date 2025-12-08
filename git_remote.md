## Overview of second half

- Recap
- Branching and Merging
- Pushing, Pulling, Fetching
- Cloning
- Resolving Merge Conflicts

## Recap

![|overview](https://docs.nesi.org.nz/assets/images/Git-Reference_Sheet.svg)

By now, you have learned why we need `git add ...` and  `git commit ...`.

A few questions to test your understanding:

> [!faq]- What’s a commit hash like `f523039...` that we can see in `git log`?
> a unique identifier assigned to each commit in a Git repository

> [!faq]- What is the “stage”?
> an intermediate space where you prepare changes from your working directory before committing them to your local Git repository

> [!faq]- What is “HEAD”?
> a special pointer that indicates the currently active commit in your repository

> [!faq]- How do figure out the branch I’m working on? What’s the default name of the main branch?
> check the first line in `git status` or look for `*` when typing `git branch`

## Branching and Merging

Git treats your work like a set of parallel tracks instead of a single straight line.

Each track can hold a different idea or version of your project, so you can try things, pause them, switch tasks, and come back later without losing anything.

This makes it easy to experiment safely, keep unfinished ideas separate from finished ones, and combine work from different people when you’re ready.

Thinking about your workflow this way helps you stay organized and avoid mistakes while still moving quickly.

![](https://shrra.github.io/python-intermediate-development/fig/git-feature-branch.svg)

> [!tip] Think of Git branches "throwaway".
> Git's branching model encourages the creation of short-lived, isolated branches for new features, bug fixes, or experiments that are merged and then deleted.

**Let’s try it out**:
- `git branch <branch-name>` Create new branch `branch-name`
- `git merge <branch-name>` Merge `<branch-name>` into current branch.
- `git checkout <branch-name>` Switch to editing branch `<branch-name>`
- `git checkout -b <branch-name>` Shortcut for `git branch` and `git checkout`

## Local vs remote repositories

> [!tip] Every copy of a directory that is version controlled by git is in itself a git repository.

Let’s explore some (remote) repositories on GitHub (https://github.com/explore).

**Let’s try it out**:
- Go to Github and create a new (private) repository. This is our remote for our local git repo.
- Add this Github repo as a remote: `git remote add origin <url-of-your-repo>`
- Check that it’s there: `git remote -vv`

## Clone and the pull/push loop

`git clone` is used once to create an initial local copy of a repository, while the **pull/push loop** describes the ongoing process of synchronizing changes between a local repository and a remote one after the initial clone.

**Let’s try it out**:
- `git status` to see the *before*
- `git push -u origin main`
- `git status` to see the *after*

## Working collaboratively

We will now clone an existing (Github) repository, https://github.com/mkrapp/training2025-12.git. Then we can start working on it together.

**Let’s try it out**:
- Go one level up (out of this local repo of yours); `cd ..`
- `git clone https://github.com/mkrapp/training2025-12.git`
- Create your own branch, make additional commits and push multiple times

> [!warning] You won’t be able to push your local changes to the remote
> unless you are a collaborator. But you can “fork” the repository instead and become the “owner” of that fork.

**Let’s try it out**:
- `git push -u origin <your-branch>`


A few useful commands associated with remote repos:
- `git fetch <repo> <branch>` Gets status of `origin`. Note, `git fetch` **does not** change your working directory or local repository.
- `git pull <repo> <branch>` Incorporates changes from `origin` into local repo.
- `git push <repo> <branch>` Incorporates changes from local repo into `origin`.

## Adding a branch to your remote

`git push -u origin feature-<name>`

Using the `-u` switch with the `git push` command is a handy shortcut for: (1) creating the new remote branch and (2) setting your local branch to automatically track the remote one at the same time. You need to use the `-u` switch only once to set up that association between your branch and the remote one explicitly. After that you could simply use `git push` without specifying the remote repository, if you wished so.

You will commit locally, then push your branch for the first time (introduce `git push -u origin feature-<name>`).
- Show how others can pull and see new branches, then check out each other’s branches.

## Merge with conflicts

We are all working on the same repo, on our own branch. We will change a few things (because we can), commit those revisions, and push them to our remote branch (not main!).

Some people will add stuff to same file. Other will add new files. And still other will modify existing files.

The maintainer’s job is to merge all those changes back into the `main` branch.

## Merge with conflicts (a real-world example)

- Goal: Experience merge and conflict resolution in a safe setting.
- Let’s start without a conflict: `git checkout main`, then `git merge feature-<name>`; finally `git push origin main`. (Good software development practice is to keep the `main` branch stable while you and the team develop and test new functionalities on feature branches)

**Team A (`feature/add`)**
- Implement the *add new task* feature.
- `git checkout -b feature/add` (What is this and why are we doing it?)
```
if choice == "add":
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added.")
```

```
git add .
git commit -m "Add new task feature”
git push origin feature/add
```

**Team B (`feature/done`)**
- Implement the *task is done* feature.
- `git checkout -b feature/done` (What is this and why are we doing it?)
```
if choice == "done":
    for i, task in enumerate(tasks):
        print(i, "-", task)

    index = int(input("Which task is done? "))
    finished = tasks.pop(index)
    save_tasks(tasks)
    print("Completed:", finished)
```

```
git add .
git commit -m "Add mark task as done feature”
git push origin feature/done
```

**Team C (`feature/ui`)**
- Refactor the main method.
- `git checkout -b feature/ui` (What is this and why are we doing it?)
- `git checkout -b feature/ui`
```
def main():
    print("\n--- Task Tracker ---")
    print("1 - Add task")
    print("2 - List tasks")
    print("3 - Mark task as done")

    choice = input("Choose an option: ")

    tasks = load_tasks()

    if choice == "1":
        print("'Add task' not implemented!")
    elif choice == "2":
        for t in tasks:
            print("-", t)
    elif choice == "3":
        print("'Mark task as done' not implemented!")
```

```
git add .
git commit -m "Improve menu and numeric choices”
git push origin feature/ui
```

**Maintainer**
- Merge and resolve conflicts
- This is what *resolved* can look like (`git log --oneline --graph --all --decorate`):
```
*   3bfc60e (HEAD -> main) Merge branch 'feature/ui'
|\  
| * 01f1562 (feature/ui) Improve menu and numeric choices
* |   49eb57c Merge branch 'feature/done'
|\ \  
| * | 4cfc503 (feature/done) Add mark task as done feature
| |/  
* / 9e223eb (feature/add) Add new task feature
|/  
* 813cd21 (origin/main) Add working but incomplete task tracker
* ...
* 500d1cb first commit
```

```
git checkout main
git pull upstream main
git merge feature/add
git merge feature/done
git merge feature/ui
```

```
git add task_tracker.py
git commit -m "Resolve merge conflicts"
git push upstream main
```

## Additonal sources

- https://missing.csail.mit.edu/2020/version-control/ (explains the git data model)
- https://learngitbranching.js.org/ (Interactive tutorial)
- https://ohshitgit.com/ (common git problems)
- [Pro Git book](https://git-scm.com/book/en/v2)

## checkout, reset, revert: What’s the difference 

| Command    | What moves | Danger level | Use when... |
|------------|------------|--------------|-------------|
| `checkout` | HEAD only  | Safe | Exploring history |
| `reset`    | Branch (+working) | Medium-high | Reshaping local work |
| `revert`   | Nothing (new commit) | Safe | Undoing shared history |
