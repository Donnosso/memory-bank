# Day 2 Notes — Terminal & Git Fundamentals
### Memory Bank Academy · Phase 0

---

## 1. Terminal Basics — What You're Actually Doing

A terminal is a text-only way of telling your computer what to do. No clicking — just typing a command, hitting Enter, and reading the result. Every command below follows the same pattern: **command → what it does → why it matters.**

| Command | What it means | Why it matters |
|---|---|---|
| `pwd` | **P**rint **W**orking **D**irectory | Answers "where am I right now?" This is the single most important habit to build — always know your location before running anything that changes or deletes files. |
| `ls` | **L**i**s**t | Shows what's inside your current folder. Your eyes, basically. |
| `cd <folder>` | **C**hange **D**irectory | Moves you into a folder. `cd ..` moves you *up* one level (out of the current folder). |
| `mkdir <name>` | **M**a**k**e **Dir**ectory | Creates a new, empty folder. |
| `mv <old> <new>` | **M**o**v**e | Renames a file or folder (renaming *is* moving — just to a new name in the same place), or physically relocates it elsewhere. |
| `rmdir <name>` | **R**e**m**ove **Dir**ectory | Deletes an *empty* folder. Won't work if there's anything inside it (a safety feature). |

### The lesson that mattered most today
**A terminal tab remembers the location it started in — it does not auto-refresh when things change outside it.** You renamed a folder through PyCharm's UI, but an already-open terminal tab kept quietly using the *old* folder name behind the scenes. That's what caused the stray "Memory Bank" (with space) folder to reappear. The fix — and the habit — is: **when in doubt, run `pwd` first.** It costs one second and prevents real mistakes later, especially once you're running commands that delete or overwrite things.

---

## 2. Why Spaces in Folder Names Cause Problems

The terminal splits commands into pieces wherever it sees a space. So `cd Memory Bank` (no quotes) is read as *two separate instructions* — "go into a folder called Memory" and then a stray leftover word "Bank" — which is why you saw "too many arguments." Two fixes exist:
- Quote it: `cd "Memory Bank"`
- Escape the space: `cd Memory\ Bank`

But the real, permanent fix is what you did: **rename the folder to remove the space entirely** (`MemoryBank`). Professional projects almost never use spaces in file or folder names, for exactly this reason.

---

## 3. Git — The Big Picture

Git tracks changes to your project over time, like an infinitely detailed undo history with checkpoints you choose yourself. There are **three zones** your files move through:

```
Working Directory  →  Staging Area  →  Committed (repository history)
   (unsaved edits)      (git add)         (git commit)
```

- **Working directory**: your files as they currently sit on disk — git isn't tracking any changes to them yet.
- **Staging area**: files you've marked as "yes, include this in the next save point" via `git add`.
- **Committed**: a permanent checkpoint in your project's history, created via `git commit`. Each commit has a message describing what changed and why.

Only *after* committing do things get pushed to GitHub — the remote copy.

```
Committed (local)  →  git push  →  GitHub (remote copy)
```

### Commands used today

| Command | What it does | Why you ran it |
|---|---|---|
| `git --version` | Confirms git is installed | Sanity check before doing anything else |
| `git config --global user.name "..."` | Sets your name on all future commits | So commits are attributed to you |
| `git config --global user.email "..."` | Sets your email on all future commits | Same reason — identity tagging |
| `git init` | Turns the current folder into a git repository | Nothing is tracked until this runs — it's the "start recording" button |
| `git status` | Shows what's changed, staged, or untracked | Your main "what's going on right now" command — run it often |
| `git add .` | Stages *everything* in the current folder for the next commit | The `.` means "everything, recursively" — without it, git stages nothing |
| `git commit -m "message"` | Creates a permanent checkpoint of everything staged | The actual save point in your project's history |
| `git remote add origin <url>` | Tells your local repo where its GitHub copy lives | Links local ↔ remote, one time only |
| `git branch -M main` | Renames your current branch to `main` | `master` was the old default name; `main` is the modern standard |
| `git push -u origin main` | Uploads your committed history to GitHub | Delivers what's local up to the remote copy |

### A subtlety worth remembering
Running `git add .` a **second** time with nothing new to stage produces no output and no error — that's not a bug, it just means "nothing has changed since the last commit." Green (in `git status` or PyCharm's file colors) only means "staged, waiting to be committed." Once committed, files return to their normal color — that's success, not something going wrong.

---

## 4. `.gitignore` — Telling Git What to Skip

Not everything in a project folder should be tracked. Two culprits:
- **`.venv/`** — your virtual environment. It's huge, machine-specific, and easily recreated from `requirements.txt` — no reason to store it in git history.
- **`__pycache__/`** — Python's auto-generated compiled bytecode. Regenerated automatically every run; tracking it is pure clutter.
- *(Optional, added today)* **`.idea/`** — PyCharm's own personal settings folder (window layout, run configs). Not project code, just IDE preference clutter.

A `.gitignore` file is a plain text list of patterns git should never stage, no matter what. One pattern per line.

**Important nuance you hit today:** these entries must live *inside* a file named `.gitignore` — typing `.venv/` directly into the terminal makes bash try to *execute* it as a command, which fails ("Is a directory"). The instruction meant "write this line into a file," not "run this as a command."

---

## 5. Personal Access Tokens (PAT)

GitHub no longer accepts your regular account password for git operations over HTTPS — it requires a **Personal Access Token** instead, a special password generated specifically for this purpose (Settings → Developer settings → Personal access tokens). It gets pasted once at the `Password for...` prompt during a push. The terminal often shows *nothing* as you paste it — no dots, no characters — that's normal, not a sign it failed.

---

## 6. IDE Actions vs. Terminal Commands

Two ways to do the same thing exist, and today mixed both:
- **PyCharm's Refactor → Rename** (used to attempt the folder rename) doesn't just change a label — when done correctly, it updates the folder on disk *and* every internal reference PyCharm holds (interpreter path, project config). Powerful, but worth double-checking it actually reflected on disk (which is what the `pwd`/`ls` check caught today).
- **Terminal `mv`** does the equivalent renaming manually, with no IDE-side awareness — useful to know for later projects where you're not inside an IDE at all.

Neither is "more correct" — knowing both, and knowing how to verify either worked, is the actual skill.

---

## 7. Today's Real Wins (beyond just the commands)

- Built and verified a professional project skeleton matching industry convention.
- Created and activated an isolated virtual environment.
- Initialized a real git repository, made a real first commit, and pushed it to a real GitHub remote — this repo now exists publicly as proof of work.
- Debugged four separate real errors (stale terminal path, bad `cd` syntax, `.gitignore` typed as a command instead of file content, empty `git add`) using the actual error messages as the guide — which is, genuinely, most of what professional debugging looks like day to day.

---
*Memory Bank Academy — Phase 0, Day 2 · logged for the console*
