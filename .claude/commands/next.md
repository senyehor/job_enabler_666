---
description: Start the next lesson (or continue the active one)
---

If a lesson is already active (see the session-start message, or run `python tools/learn.py status`), don't start a new one. Continue it from its current state as described in CLAUDE.md.

## 1. Start

Run `python tools/learn.py next`.

- **Exit code 2, BREAK**: tell him how many minutes of break are left, in one line, and suggest stepping away from the screen. If he wants to start anyway, ask for the reason in his own words and rerun with `--override-break "<his reason>"`.
- **A lesson is parked**: ask whether to resume it (`learn.py resume`) or start a new one (`--skip-parked`).
- **No planned lessons**: tell him the maintainer needs to run `/plan-week`. Meanwhile he can reread his recent `takeaways.md` files.

## 2. Prepare (don't show this to him)

Read, in the new lesson folder: `lesson.json`, `outline.md`, `task.md`, `rubric.md`. Also run `python tools/learn.py mastery` and read his last 2–3 `takeaways.md`. If `lesson.json` has `continues`, read that lesson's `work/` too.

You read the task and rubric so the theory prepares him for them. Never give away the task's solution in the theory.

## 3. Write `theory.md`

Follow `outline.md`. It should take him about 15–20 minutes to read and try out.
- Sections in the outline's order. Each one has a short explanation plus a runnable example on different data than the task.
- A "Common mistakes" section.
- 2–3 tiny "Try it yourself" snippets, not graded.
- A short summary at the end.
- If his mastery data or past takeaways show a weak concept that this lesson touches, add a short recap of it.
- At the top, say what the starter will give him and what he writes himself (from `lesson.json` → `scaffold`).

## 4. Teach

- Open with 2–3 lines: the lesson title, what he'll be able to do afterwards, and the estimated time.
- Show the theory **one section at a time** in chat, not the whole file at once. After each section ask whether he has questions or wants the next section. Tell him once that the full text is in `theory.md`.
- Append his questions and your short answers to `theory.md` under `## Questions`.
- When he says it's clear, run `python tools/learn.py advance check`.

## 5. Check questions

Ask 2–3 questions, **one at a time**: predict the output, find the bug, or explain why. No yes/no questions. Use the ideas in `outline.md` if it has any.

Record each one with `python tools/learn.py check-record "<question>" ok|redo [--note "..."]`.

On a wrong answer, explain again from a different angle with a new example, then ask a variant of the question. After two tries, record `redo` with a note and move on; the task will practise it.

## 6. Task

Run `python tools/learn.py advance task`. Then present:
- the content of `task.md`
- the files he'll work in (`lessons/<id>/work/...`)
- how to run his program and the tests (`python tools/learn.py test`)
- the rules, in two lines: he writes all the code; ask for hints anytime; type `/review` when he thinks it's done

While he works, help only through the hint ladder in CLAUDE.md.
