# Design

A Claude Code-driven programming course: one learner, one maintainer, one shared git repo.

## Decisions

| Topic | Decision |
|---|---|
| Target | Junior Python backend developer, from zero |
| Language | English |
| Learner's platform | Windows; Claude Code; terminal is required from lesson 1 |
| Lesson size | 60–75 min, then a 15 min break |
| Pace | 3 lessons/day, 15 planned per week (adjust later) |
| Planning | Maintainer runs `/plan-week`; planned lessons are visible to the learner (trust-based) |
| Break | Soft: `next` warns, learner can override with a reason, which is logged |
| Theory | Planner writes an outline; tutor writes the full theory at `/next` |
| Storage | One `lesson.json` per lesson, written only by `tools/learn.py`; no global DB |
| Reference solutions | None. To save tokens, builders don't solve their own tasks. `validate` checks that the tests fail on the starter, and the reviewer flags broken tests during the lesson, logging them to `MAINTAINER_NOTES.md` |
| Models | Planner and lesson builder run on Sonnet (`model:` in their agent files). Tutor and reviewer use the session's model |
| Lesson tests | Python's built-in `unittest` plus `tools/lessonkit.py`, so nothing needs installing |

## Roles

- **Tutor**: the main Claude Code session, ruled by `CLAUDE.md`. Runs `/next`, `/review`, `/done`.
- **Reviewer** (subagent): reads and runs the learner's code, writes the review, gives hints step by step. Can't edit `work/`.
- **Planner** (subagent, via `/plan-week`): turns the roadmap plus progress data into the next 15 lessons. Writes `plans/week-NN.md` and scaffolds each lesson folder.
- **Lesson builder** (subagent, one per lesson, up to 5 in parallel): writes the outline, task, rubric, tests and starter for one lesson, then checks the tests against the task text.
- **Learner**: writes everything under `lessons/*/work/`, and the takeaways (which the tutor saves).
- **Maintainer**: owns `roadmap/`, runs `/plan-week`, reads `/status`.

## Lesson lifecycle

```
planned ──next──▶ theory ──▶ check ──▶ task ──review──▶ in_review ──approved──▶ takeaways ──done──▶ done
   (curriculum/)                        ▲                    │
                                        └──changes_requested─┘
any active state ──park──▶ parked ──resume──▶ (previous state)
```

- `planned`: lives in `curriculum/`. On `next` it moves into `lessons/`.
- `theory`: tutor writes `theory.md` from `outline.md`. The learner's questions and answers are appended to it.
- `check`: 2–3 quick questions. Wrong answers lead to re-explaining, not to blocking.
- `task`: `starter/` is copied into `work/`. For a project lesson with `continues`, his `work/` from that lesson is copied first and the starter only adds missing files. From here on, only the learner edits `work/`.
- `in_review`: the reviewer runs the tests and checks against `rubric.md`, then writes `reviews/round-N.md` (for him) and `round-N.json` (issues for `learn.py`). Approved means all tests pass and there are no major issues; `learn.py` refuses an approval with major issues.
- `takeaways`: the learner gives his takeaways in his own words. The tutor pushes back if they're vague or wrong, then saves them to `takeaways.md`.
- Only one lesson can be active at a time. Any others are `parked`.

## Folder layout

```
CLAUDE.md                      tutor's rules
DESIGN.md
README.md                      setup and daily use
roadmap/roadmap.json           modules → concepts → outcomes (maintainer)
schema/lesson.example.json
plans/week-NN.md               the planner's week plan: calibration notes, a brief per lesson
tools/learn.py                 the only writer of lesson.json; Python standard library only
tools/lessonkit.py             test helpers: run_script(), load_module()
curriculum/                    planned, not started
  L0031-list-copying/
    lesson.json  outline.md  task.md  rubric.md  tests/  starter/
lessons/                       started or finished
  L0023-dict-counting/
    lesson.json  outline.md  theory.md  task.md  rubric.md
    tests/  starter/  work/  reviews/round-1.{md,json}  takeaways.md
.claude/
  settings.json                permissions and hooks
  commands/  next.md review.md done.md park.md status.md plan-week.md
  agents/    reviewer.md planner.md lesson-builder.md
  hooks/     guard.py (Python, so it works on Windows)
.gitattributes                 * text=auto eol=lf
.scratch/                      gitignored; the lesson builder's temporary solutions
```

## Scaffold levels

Decided **per lesson, per part of the task**, based on how well he knows the concepts the provided code would cover.

| Level | What's provided |
|---|---|
| 0 | Empty file (and task.md) |
| 1 | File skeleton, example input/output, any helpers for concepts not taught yet |
| 2 | Function signatures and boilerplate for concepts he's mastered |
| 3 | Project setup and tests; he writes only the core logic |

Rule: code is pre-written only for concepts with mastery ≥ 0.8, or concepts not taught yet (shown as a black box). The first 10 lessons are always level 0.

## Mastery (computed, never stored)

For each concept, from every done lesson that lists it or has an issue tagged with it:
- Per lesson: `1 − 0.35 × weighted issues − 0.1 (new) or 0.05 (practiced) × extra review rounds`. Issue weights: major 1.0, minor 0.4, nit 0.1.
- Lessons are averaged with weight 0.8^k, newest first.
- The average is multiplied by a confidence factor `1 − 0.5^n` for n lessons.

So one perfect lesson gives 0.5, and it takes about three clean lessons to reach the 0.8 scaffold threshold. Tune it in `compute_mastery()` once real data exists.

## Guardrails

- `.claude/hooks/guard.py` (PreToolUse, applies to subagents too) blocks:
  - file edits under `lessons/*/work/` and to any `lesson.json`
  - shell commands that mention `work/` together with a write: redirect, `cp`, `mv`, `rm`, `sed -i`, heredoc, `python -c`
  - git commands that throw away changes (`restore`, `checkout --`, `reset --hard`, `stash`, `clean`)
- `settings.json` also denies `Edit` on those paths, as a second layer.
- The shell checks are pattern-based. A determined script could get around them, and a harmless command that mentions `work/` and writes elsewhere gets blocked too. Their job is to stop Claude from "helpfully" fixing his code by accident, which is the real risk. The no-solutions-in-chat rule lives in `CLAUDE.md` and the reviewer prompt.
- Hooks: `SessionStart` tells the tutor which lesson is active and its state. `UserPromptSubmit` adds a `[lesson timer]` note once a lesson passes 70 minutes.

## Git

- Commit messages: `L0023: start`, `L0023: theory`, `L0023: task setup`, `L0023: review 1 (changes requested)`, `L0023: done`; `plan: week 03 (L0031-L0045)`.
- `git_mode: tutor`: `learn.py` commits on every state change.
- After module m04, `git_mode: student`: the learner commits `work/` himself. `review-start` and `done` refuse if `work/` has uncommitted changes, and `learn.py`'s own commits leave `work/` out.
- `done`, `park` and `commit-plan` push. The other steps only commit locally.
- `next` and `plan-context` run `git pull --rebase --autostash` first. The planner only adds new lessons after the ones still planned.

## `tools/learn.py` commands

| Command | Used by | Does |
|---|---|---|
| `next [--override-break R] [--skip-parked]` | `/next` | Pull, soft break check (exit code 2), move the next planned lesson in, state → theory |
| `advance check` | tutor | Needs `theory.md`; state → check |
| `check-record "Q" ok\|redo [--note]` | tutor | Records one check question |
| `advance task` | tutor | starter (and `continues` work) → `work/`; state → task |
| `test [--lesson ID] [--work DIR] [--json]` | learner, reviewer, builder | Runs the lesson's unittest tests against `work/` or DIR |
| `review-start` | `/review` | JSON for the reviewer: round number, files to write, previous rounds |
| `review-record` | `/review` | Validates and records `reviews/round-N.json`; state → in_review / takeaways |
| `done` | `/done` | Needs takeaways.md (2+ lines); state → done; commit and push |
| `park` / `resume [ID]` | learner | Pause and resume |
| `status [--json]` | `/status` | Module, overall progress, today, streak, active lesson, timing, weakest concepts |
| `mastery [--json]` | tutor, planner | Score per concept |
| `plan-context` | `/plan-week` | Pull, then one JSON with everything the planner needs |
| `scaffold --week --slug --title ...` | planner | Creates `curriculum/<id>-<slug>/` with lesson.json; assigns the next id |
| `validate [IDs]` | builder, `/plan-week` | Schema, required files, concept ids, prerequisites, tests compile and fail on the starter |
| `commit-plan --week N` | `/plan-week` | Validate, commit `curriculum/` and `plans/`, push |
| `hook session-start\|prompt` | hooks | Short context lines for the tutor |

## Rough timeline

Roadmap: 15 modules, 94 concepts, ~126 regular lessons. Review lessons (~1 in 5) and module projects (2–3 lessons each) bring it to about **180 lessons, so ~12 weeks at 15 a week**. Assume it will stretch; the planner adjusts.
