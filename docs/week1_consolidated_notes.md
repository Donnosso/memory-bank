# Week 1 — Consolidated Notes
### Memory Bank Academy & French · Days 1–6

---

## Milestone Summary

By the end of this week, you have:
- A working Python program that captures and displays multiple memories, using functions, dictionaries, and lists.
- A real Git repository, committed and pushed to GitHub over SSH, with no password prompts left.
- Independently diagnosed and fixed four distinct real bugs (a stale terminal path, `==` vs `=`, an `UnboundLocalError` from a function-scope timing gap, and a deliberately-introduced `NameError`).
- Conversational-level French: greetings, self-introduction, numbers 0–20, family vocabulary, and question formation.

**Worth naming directly:** the original roadmap spread this material across three separate weeks (Python Foundations, then Lists/Dicts, then Functions). You covered it in one week — not because it was rushed, but because your prior Angela Yu reps meant the syntax wasn't new, only its application to a real project was. That's a genuine pace, not a shortcut.

---

## Memory Bank — What Was Covered

### Terminal & Git (Day 2)
- Core commands: `pwd`, `ls`, `cd`, `mkdir`, `mv`, `rmdir`.
- Git workflow: working directory → staged (`git add`) → committed (`git commit`) → pushed (`git push`).
- `.gitignore` to exclude `.venv/`, `__pycache__/`, and `.idea/` from tracking.
- SSH key authentication set up — no more password/token prompts on push.
- Lesson: a terminal tab can hold a stale path in memory if something changes outside it (e.g. a folder rename) — always `pwd` to confirm before trusting a prompt.

### Project Architecture (Day 4 discussion)
Four questions to place any new piece of code:
> **What is it? → `models/`**
> **Where is it stored? → `db/`**
> **What can I do with it? → `services/`**
> **How does the user interact with it? → `gui/`**

`memory_entry.py` currently lives in `core/` — an honest placeholder until Week 4 introduces classes, at which point it refactors properly into `models/`.

### Functions, Dictionaries, Lists (Days 4–5)
- Dictionaries group related data under one name: `memory = {'title': ..., 'date': ..., ...}`.
- Lists hold many of those groups: `memories = []`, `memories.append(memory)`.
- Functions (`def name(params): ... return value`) let you name and reuse a block of logic instead of repeating it — the DRY principle (Don't Repeat Yourself).

### Scope — Global vs. Local (Day 5)
- Any variable *assigned* inside a function belongs only to that function's local scope — this is decided by scanning the function's text, before it even runs.
- A variable only *read*, never assigned, inside a function safely falls back to the outer (global) scope.
- **`NameError`**: the name doesn't exist anywhere Python can find it.
- **`UnboundLocalError`**: Python reserved a local slot for the name (saw an assignment somewhere in the function) but the specific line that fills it never actually executed on that run — local, but empty.

### Reading Tracebacks (Day 6)
- Read bottom-up: the last line (error type + message) is the actual failure, always read first.
- The error type is a category — `NameError` and `UnboundLocalError` mean fundamentally different things, even when the symptom looks similar.
- The call stack (File/line entries) shows the path execution took, not necessarily the root cause.
- Python's own "Did you mean: 'x'?" suggestion and the `^^^^` pointer (when present) are often the fastest route to the fix.

---

## French — What Was Covered

| Day | Content |
|---|---|
| 1 | Pronunciation basics (nasal sounds), core greetings (Bonjour, Salut, Merci), self-introduction (Je m'appelle) |
| 2 | Être (to be) — full conjugation; numbers 0–20 (11–16 needed extra reps — they're irregular, not rule-based like 17–19) |
| 3 | Avoir (to have) — full conjugation; articles le/la/les and un/une |
| 4 | Question words (Comment, Où, Quel/Quelle); habiter; full self-introduction Boss Quest combining Days 1–4 |
| 5 | Days of the week; family vocabulary (père, mère, frère, sœur); combining avoir with real family sentences |
| 6 | Cold recall test (no notes); first real listening practice; new technique additions from outside research (below) |

### Method upgrade — from outside research (Day 6)
A video you brought in changed the standing approach going forward, not just today:
- **Questions**: only two methods from here on — add "Est-ce que" to the front of a statement, or raise your voice at the end. Verb inversion is skipped entirely.
- **Four mini-engine verbs** (coming soon as real lesson content): *je veux* (I want), *je peux* (I can), *je dois* (I have to), *je vais* (I'm going to) — each followed by a plain infinitive, unlocking many sentences without conjugation tables.
- **Listening technique**: loop one short line of real audio 4–5 times while reading the transcript, rather than passive long-form listening.
- **Cognates**: French words ending in *-tion* or *-ible* are usually identical or near-identical to English — free vocabulary, flagged as it comes up.
- **Faux amis to remember**: *sympathique* = nice (not sympathetic), *envie* = desire (not envy), *chef* = boss (not a cook).

---

## Your Own Reflection (Day 6)

**Hardest moments this week:**
> Git/GitHub setup, and at one point doubting the whole project's folder architecture — struggling to hold onto what each folder was for before there was real code to anchor it to.

**French:**
> Forcing the brain to adjust to new words, sentence composition, and masculine/feminine noun gender.

Both are exactly the kind of friction that fades with reps, not signs anything is off track — the Git complexity won't repeat itself now that SSH and the staging rhythm are second nature, and the architecture doubt cleared the moment real functions gave the folders something concrete to mean.

---

## Into Week 2

Same rhythm continues — Memory Bank moves toward search, delete, and filter operations on your memory collection; French continues building real, usable sentence patterns. Rest through the rest of today; pick up when ready.

---
*Week 1 · Memory Bank Academy & French · logged for docs/*
