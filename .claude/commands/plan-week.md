---
description: (Maintainer) Plan and build the next week of lessons
argument-hint: "[optional notes for the planner, e.g. 'go slower on dicts']"
---

You're working for the maintainer here, not the learner.

Maintainer's notes: $ARGUMENTS

1. **Preflight.** `git status` must be clean and you must be on `main`. Otherwise stop and say why. Then run `python tools/learn.py plan-context`; it pulls first.
   - If `planned_not_started` already has more than 5 lessons, ask the maintainer whether to plan more anyway.
2. **Plan.** Launch the `planner` subagent. Give it the full plan-context JSON and the maintainer's notes. It writes `plans/week-NN.md` and scaffolds each lesson folder with `learn.py scaffold`. Wait for its summary.
3. **Build.** For every lesson the planner created, launch a `lesson-builder` subagent. Give it the folder path, the path of `plans/week-NN.md`, and the lesson's id.
   - Run up to 5 builders in parallel.
   - A lesson with `continues` must be built **after** the lesson it continues, since it builds on its interfaces.
4. **Validate.** Run `python tools/learn.py validate`. Send each failing lesson back to a new `lesson-builder`, with the error output, at most twice. If one still fails, stop and report it; don't commit.
5. **Report and ship.** Show the maintainer a short table: id, title, kind, new concepts, estimate, scaffold level. Add the planner's notes on calibration. Then run `python tools/learn.py commit-plan --week NN`; it commits and pushes.
