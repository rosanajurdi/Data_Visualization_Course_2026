# Git Lab: Hands-On Practice GIL mathis

## Objectives
By completing this lab, students will:
- Understand Git workflow and commands
- Practice cloning, committing, and pushing changes
- Work with branches and handle merge conflicts
- Use rebase to maintain clean commit history

---

## Lab Setup

### Prerequisites
- Git installed on your machine
- GitHub account created
- SSH keys configured (optional but recommended)

### Initial Setup
```bash
# Configure Git with your credentials (one-time setup)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global user.name  # Verify configuration
```

---

## Exercise 1: Clone and Basic Operations

### Task
Clone a repository, make changes, and push them back.

### Steps
```bash
# Step 1: Create a working directory
mkdir ~/git-lab-workspace
cd ~/git-lab-workspace

# Step 2: Clone the repository (use your own repo or a practice one)
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Step 3: Check the current branch
git branch

# Step 4: View commit history
git log --oneline

# Step 5: Check repository status
git status
```

### Hands-On Task
1. Create a new file called `student_notes.txt`
2. Add the following content:
```
Course: Data Visualization
Date: January 13, 2026
Topics Covered:
- Pandas & Histograms
- Bar Plots
- Scatter Plots & Heatmaps
```

3. Stage and commit the file:
```bash
git add student_notes.txt
git commit -m "Add student notes for Data Visualization course"
```

4. Push to remote:
```bash
git push origin main
```

### Verification
```bash
# Verify your changes were pushed
git log --oneline -n 3
```

---

## Exercise 2: Working with Multiple Files

### Task
Practice staging and committing multiple files.

### Steps
```bash
# Step 1: Create multiple files
echo "Lab 1 - Introduction to Pandas" > lab1_notes.txt
echo "Lab 2 - Bar Plots with Matplotlib" > lab2_notes.txt
echo "Lab 3 - Athlete Sport Event Analysis" > lab3_notes.txt

# Step 2: Check status
git status
```

### Hands-On Task
1. Stage all files at once:
```bash
git add .
```

2. Review what's staged:
```bash
git status
```

3. Commit with a descriptive message:
```bash
git commit -m "Add lab notes for labs 1-3 of Data Visualization course"
```

4. Push changes:
```bash
git push origin main
```

### Verification
```bash
git log --oneline -n 5
```

---

## Exercise 3: Creating and Switching Branches

### Task
Create feature branches and practice branch switching.

### Steps
```bash
# Step 1: Create a new branch
git branch feature/bokeh-visualization

# Step 2: List all branches
git branch -a

# Step 3: Switch to the new branch
git checkout feature/bokeh-visualization

# Step 4: Verify you're on the correct branch
git branch
```

### Hands-On Task
1. On the `feature/bokeh-visualization` branch, create a new file:
```bash
echo "# Bokeh Visualization Guide
- Interactive plots
- Web-based visualizations
- Time series analysis" > bokeh_guide.md
```

2. Stage and commit:
```bash
git add bokeh_guide.md
git commit -m "Add Bokeh visualization guide"
```

3. Push the branch to remote:
```bash
git push origin feature/bokeh-visualization
```

4. Switch back to main branch:
```bash
git checkout main
```

5. Verify you're back on main:
```bash
git log --oneline -n 2
```

### Verification
The `bokeh_guide.md` file should NOT exist on the main branch.

---

## Exercise 4: Pulling Updates

### Task
Simulate a teammate pushing changes and practice pulling updates.

### Steps
```bash
# Step 1: Make sure you're on main
git checkout main

# Step 2: Pull the latest changes from remote
git pull origin main

# Step 3: View the updated history
git log --oneline -n 5
```

### Hands-On Task
1. Have a teammate (or yourself on another machine) push changes to main
2. Pull those changes:
```bash
git pull origin main
```

3. Verify the new files are in your workspace:
```bash
ls -la
```

---

## Exercise 5: Rebasing (Advanced)

### Task
Practice rebasing to maintain a clean commit history.

### Steps
```bash
# Step 1: Create a new branch for features
git checkout -b feature/text-analysis

# Step 2: Create and commit 3 files
echo "NLP basics" > nlp_basics.txt
git add nlp_basics.txt
git commit -m "Add NLP basics notes"

echo "Sentiment analysis" > sentiment_analysis.txt
git add sentiment_analysis.txt
git commit -m "Add sentiment analysis guide"

echo "Text processing" > text_processing.txt
git add text_processing.txt
git commit -m "Add text processing techniques"

# Step 3: Check your commit history
git log --oneline -n 5

# Step 4: Rebase onto main (if main has new commits)
git rebase main

# Step 5: Push the rebased branch
git push origin feature/text-analysis --force-with-lease
```

### Verification
```bash
git log --oneline --graph --all
```

---

## Exercise 6: Interactive Rebase (Advanced)

### Task
Practice squashing commits to clean up history.

### Steps
```bash
# Step 1: View last 3 commits
git log --oneline -n 3

# Step 2: Start interactive rebase
git rebase -i HEAD~3
```

### Hands-On Task
1. In the interactive rebase editor, change the second and third commits from `pick` to `squash`:
```
pick abc1234 Add NLP basics notes
squash def5678 Add sentiment analysis guide
squash ghi9012 Add text processing techniques
```

2. Save and close the editor
3. Edit the commit message to summarize all three:
```
Add NLP and text analysis materials

- NLP basics
- Sentiment analysis
- Text processing techniques
```

4. Save and complete the rebase
5. Verify the history is cleaned up:
```bash
git log --oneline -n 3
```

---

## Challenge Exercise: Complete Workflow

### Task
Perform a complete Git workflow from start to finish.

### Scenario
You need to add a new document called `course_summary.pdf` and make improvements to `README.md`.

### Steps
```bash
# Step 1: Start fresh by pulling latest
git checkout main
git pull origin main

# Step 2: Create a feature branch
git checkout -b feature/add-course-summary

# Step 3: Add the new file (simulate adding course_summary.pdf)
echo "# Data Visualization Course Summary
Date: January 13, 2026
Total Labs: 10
Key Libraries: Pandas, Matplotlib, Seaborn, Plotly, Altair, Bokeh" > course_summary.pdf

# Step 4: Update README.md with a new section
# (Edit README.md and add completion date)

# Step 5: Stage changes
git add .

# Step 6: Check status
git status

# Step 7: Commit
git commit -m "Add course summary PDF and update README with completion info"

# Step 8: Push the feature branch
git push origin feature/add-course-summary

# Step 9: Create a Pull Request (in GitHub UI)
# Then merge and pull back to main
git checkout main
git pull origin main

# Step 10: Verify everything is up to date
git log --oneline -n 5
```

---

## Troubleshooting Guide

### Problem: Changes not showing after commit
**Solution:**
```bash
git log --oneline  # Check if commit was created
git status         # Verify working directory is clean
```

### Problem: Need to undo last commit
**Solution:**
```bash
git reset --soft HEAD~1  # Undo commit but keep changes staged
git reset --hard HEAD~1  # Undo commit and discard changes
```

### Problem: Committed to wrong branch
**Solution:**
```bash
git log --oneline -n 1           # Note the commit hash
git checkout correct-branch
git cherry-pick <commit-hash>    # Apply commit to correct branch
git checkout wrong-branch
git reset --hard HEAD~1          # Remove from wrong branch
```

### Problem: Merge conflict
**Solution:**
```bash
# After pulling conflicting changes:
git status                       # See conflicting files
# Manually edit conflicting files
git add <resolved-files>
git commit -m "Resolve merge conflicts"
git push origin main
```

---

## Checklist for Lab Completion

- [ ] Completed Exercise 1: Clone and basic operations
- [ ] Completed Exercise 2: Multiple files workflow
- [ ] Completed Exercise 3: Branches
- [ ] Completed Exercise 4: Pulling updates
- [ ] Completed Exercise 5: Rebasing
- [ ] Completed Exercise 6: Interactive rebase
- [ ] Completed Challenge exercise
- [ ] Successfully pushed all changes to remote
- [ ] Verified commit history is clean

---

## Additional Resources
- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)