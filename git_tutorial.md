# Git Tutorial: Essential Commands

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