# Git Tutorial: Essential Commands 1

## Overview
Git is a version control system that tracks changes to your code. Here are the core commands you'll use:

## Essential Git Commands

### **git clone**
Downloads a remote repository to your local machine.
```bash
git clone <repository-url>
```
Use this when you first want to work on a project.

---

### **git pull**
Fetches updates from the remote repository and merges them into your current branch.
```bash
git pull origin main
```
Use this to sync your local code with the latest changes from the remote (like when teammates push updates).

---

### **git add**
Stages files for commit (marks them as ready to be saved).
```bash
git add <filename>        # Stage specific file
git add .                 # Stage all changes
```
This prepares your changes before committing.

---

### **git commit**
Saves your staged changes to the local repository with a message describing what changed.
```bash
git commit -m "Add data visualization functions"
```
Always use meaningful commit messages so you and others understand what changed.

---

### **git push**
Uploads your committed changes to the remote repository.
```bash
git push origin main
```
Use this to share your work with teammates and back it up to the remote server.

---

### **git rebase**
Reapplies your commits on top of another branch, creating a linear commit history.
```bash
git rebase main           # Rebase current branch onto main
git rebase -i HEAD~3      # Interactive rebase last 3 commits
```
Use this to:
- Keep commit history clean and linear
- Avoid merge commits
- Reorganize, squash, or edit commits before pushing
- **Warning**: Don't rebase commits already pushed to shared branches (it rewrites history)

---

## Typical Workflow
```bash
git pull origin main           # Get latest changes
# Make edits to your files
git add .                      # Stage changes
git commit -m "Your message"   # Commit locally
git push origin main           # Push to remote
```

This ensures you have the latest code, make changes, save them locally, and share them!

## Git Rebase vs Merge
| Operation | Use Case | Result |
|-----------|----------|--------|
| **Merge** | Combining branches from multiple developers | Creates a merge commit, preserves history |
| **Rebase** | Cleaning up local commits before pushing | Linear history, cleaner log |

---

## Hands-On Example: Adding course.pdf to the Repo

Here's a practical example of adding a PDF file called `course.pdf` to your repository:

```bash
# Step 1: Make sure you're up to date with the remote
git pull origin main

# Step 2: Add the course.pdf file to staging area
git add course.pdf

# Step 3: Check the status to confirm the file is staged
git status

# Step 4: Commit the file with a descriptive message
git commit -m "Add course.pdf - Data Visualization Course materials"

# Step 5: Push the changes to the remote repository
git push origin main
```

**Expected output after each command:**
```
# After git add course.pdf:
# (no output means success)

# After git status:
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --cached <file>..." to unstage)
        new file:   course.pdf

# After git commit:
[main abc1234] Add course.pdf - Data Visualization Course materials
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 course.pdf

# After git push:
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 456 bytes | 456.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), reused pack 0 (delta 0)
To github.com:your-username/your-repo.git
   xyz7890..abc1234 main -> main
```

The `course.pdf` file is now part of your repository and accessible to all collaborators!