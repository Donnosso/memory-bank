# Session Notes — Debugging & Refactoring
### Memory Bank · Week 1, Day 4

---

## Bug 1 — `==` vs `=`

```python
add_memory == True   # WRONG — this is a question, not an instruction
add_memory = True    # RIGHT — this is an assignment
```

- **`=`** assigns a value to a variable ("make this equal to that").
- **`==`** compares two things and returns `True` or `False` ("is this equal to that?").

Writing `==` where you meant `=` doesn't create the variable at all — Python just evaluates a comparison and throws the result away. That's why the very next line, `while add_memory:`, crashed with `NameError: name 'add_memory' is not defined` — the variable genuinely never existed.

**How to read that error type going forward:** `NameError` always means "this variable was used before it was ever created." When you see it, the fix is almost never in the line the error points to — it's in tracing backward to find where that variable was *supposed* to be assigned and wasn't.

---

## Bug 2 — Incomplete conditional logic

```python
if add_another == "y":
    add_memory = True
# no else — what happens if the answer is "n"?
```

An `if` with no matching `else` only handles the case you wrote. Any other input path falls through with nothing defined. This is a common source of bugs that don't show up in your first test (because you happened to type "y") but break the moment someone answers differently.

**Habit worth building:** whenever you write an `if`, ask "what happens in every other case?" before moving on — even if the answer is "nothing needs to happen," write that consciously rather than by accident.

---

## Refactor — DRY (Don't Repeat Yourself)

**Before:** the four `input()` lines and the dictionary-building logic existed in two separate places — once before the loop, once again inside it. The two copies would inevitably drift out of sync over time (fix one, forget the other).

**After:**
```python
memories = []
add_another = "y"

while add_another == "y":
    title = input("Title: ")
    date = input("Date: ")
    mood = input("Mood: ")
    journal = input("Journal: ")

    memory = {
        'title': title,
        'date': date,
        'mood': mood,
        'journal': journal
    }
    memories.append(memory)

    add_another = input("Add another memory (y/n): ")

for m in memories:
    print(f"\n{m['title']} ({m['date']}) — Mood: {m['mood']}\n{m['journal']}")
```

**What changed conceptually:**
- The input-and-append logic exists in exactly **one place**, inside the loop — no duplication to drift apart.
- The loop's own condition (`add_another == "y"`) does double duty as the stop signal — no separate `add_memory` flag needed at all, which also quietly eliminates Bug 1 and Bug 2 entirely rather than just patching them.

**DRY as a general principle:** if you ever find yourself copy-pasting a block of logic to use it twice, that's usually a sign it belongs in one place — a loop, or eventually a function — rather than two. It's not just neater; duplicated logic is where silent bugs hide, because fixing a mistake in one copy doesn't fix it in the other.

---

## Recurring issue — Interpreter reset

This is the second time PyCharm has shown `<No interpreter>` or a mismatched environment on reopening the project. It's a known PyCharm quirk (project reindexing or a fresh session sometimes drops the binding) rather than something you're doing wrong.

**Standing habit:** check the bottom-right corner of the PyCharm window at the *start* of every session, before running anything. It should read `Python 3.12 (MemoryBank) [3.12.3]`. If it doesn't, redo: Settings → Project: MemoryBank → Python Interpreter → select `~/PycharmProjects/MemoryBank/.venv/bin/python`.

---
*Memory Bank · Week 1, Day 4 · logged for docs/*
