# 🚀 Git Quickstart — Course Python2

![Git Badge](https://img.shields.io/badge/Git-Guide-blue?logo=git) ![Easy-to-read](https://img.shields.io/badge/Readability-High-green)

A short, friendly, and easy-to-follow guide for getting your project tracked with Git and pushed to GitHub. This README replaces the previous raw notes with clearer sections, command examples, and short explanations so you can copy/paste and get going quickly.

---

## Table of contents
- [Overview](#overview)
- [Quick checks](#quick-checks)
- [Configure Git (one-time on your machine)](#configure-git-one-time-on-your-machine)
- [Add your project to Git and push to GitHub](#add-your-project-to-git-and-push-to-github)
- [Common tips & troubleshooting](#common-tips--troubleshooting)
- [Contact / Next steps](#contact--next-steps)

---

## Overview
This file explains the most common Git commands beginners need to:
- install and check Git,
- configure identity on their machine,
- initialize a repo, and
- push code to GitHub.

Commands are shown in code blocks — replace placeholders (like your username or repo URL) before running them.

---

## Quick checks
Run these to confirm Git is installed and which version:
```bash
git -v
```

---

## Configure Git (one-time on your machine)
Set your Git identity so commits are attributed to you. Replace the placeholders with your GitHub values:

```bash
git config --global user.name "your-github-username"
git config --global user.email "your-email@example.com"
```

Check what you've set:
```bash
git config --list
```

(Optional) Use the credential helper so Git can remember your credentials:
```bash
git config --global credential.helper store
# or use 'cache' (temporary) on some systems:
# git config --global credential.helper cache
```

---

## Add your project to Git and push to GitHub
These commands assume you are in your project directory.

1) Initialize a local repository:
```bash
git init
```

2) Stage all files:
```bash
git add .
```

3) Create your first commit (replace the message with something descriptive):
```bash
git commit -m "Initial commit: add project files"
```

4) Ensure the main branch name is `main`:
```bash
git branch -M main
```

5) Link your local repo to the GitHub repository (replace the URL with your repo URL):
```bash
git remote add origin https://github.com/your-username/your-repo.git
```

6) Verify the remote:
```bash
git remote -v
```

7) Push to GitHub:
```bash
git push -u origin main
```

Notes:
- If Git prompts for credentials, use your GitHub username and a Personal Access Token (PAT) if password auth is disabled.
- If the remote repo already has commits, you may need to pull first or force a safe merge.

---

## Common tips & troubleshooting
- "Permission denied" or authentication errors: create a PAT on GitHub and use it instead of a password, or set up SSH keys.
- Forgot to include a file? Add it and run:
  ```bash
  git add <file>
  git commit -m "Add missing file"
  git push
  ```
- Want to see commit history:
  ```bash
  git log --oneline --graph --decorate
  ```
- To undo the last commit but keep changes staged:
  ```bash
  git reset --soft HEAD~1
  ```
  Use with care — learn what reset/checkout do before using them.

---

## Contact / Next steps
If you want, I can:
- proofread or tweak this README further,
- convert it into a checklist for an issue, or
- prepare a small CONTRIBUTING.md.

Happy coding! ✨