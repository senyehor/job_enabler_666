#!/usr/bin/env python3
"""Course bookkeeping CLI: the only writer of lesson.json files.

Standard library only, so it runs on a fresh Windows Python install.
Run `python tools/learn.py -h` for the command list; DESIGN.md explains the flow.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROADMAP_PATH = ROOT / "roadmap" / "roadmap.json"
CURRICULUM = ROOT / "curriculum"
LESSONS = ROOT / "lessons"
TOOLS = ROOT / "tools"

ACTIVE_STATES = ("theory", "check", "task", "in_review", "takeaways")
KINDS = ("regular", "review", "project")
VERDICTS = ("approved", "changes_requested")
SEVERITY_WEIGHT = {"major": 1.0, "minor": 0.4, "nit": 0.1}
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_FILES = ("outline.md", "task.md", "rubric.md")
TIMER_WARN_MIN = 70
TEST_TIMEOUT_S = 120

EXIT_ERROR = 1
EXIT_BREAK = 2


class CliError(Exception):
    pass


def now() -> datetime:
    return datetime.now().astimezone()


def stamp() -> str:
    return now().isoformat(timespec="seconds")


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value)


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def warn(message: str) -> None:
    print(f"warning: {message}", file=sys.stderr)


def split_csv(value: str | None) -> list[str]:
    return [item.strip() for item in (value or "").split(",") if item.strip()]


# ---------- roadmap ----------

def load_roadmap() -> dict:
    return json.loads(ROADMAP_PATH.read_text(encoding="utf-8"))


def roadmap_concepts(roadmap: dict) -> list[dict]:
    """All concepts in roadmap order, each tagged with its module id and title."""
    return [
        {**concept, "module": module["id"], "module_title": module["title"]}
        for module in roadmap["modules"]
        for concept in module["concepts"]
    ]


def check_concepts(ids: list[str], roadmap: dict) -> None:
    known = {c["id"] for c in roadmap_concepts(roadmap)}
    unknown = [cid for cid in ids if cid not in known]
    if unknown:
        raise CliError(f"unknown concept id(s): {', '.join(unknown)} (see roadmap/roadmap.json)")


# ---------- lessons ----------

class Lesson:
    def __init__(self, path: Path):
        self.path = path
        self.file = path / "lesson.json"
        self.data = json.loads(self.file.read_text(encoding="utf-8"))

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def num(self) -> int:
        return int(self.data["id"][1:])

    @property
    def state(self) -> str:
        return self.data["state"]

    @state.setter
    def state(self, value: str) -> None:
        self.data["state"] = value

    @property
    def student_git(self) -> bool:
        return self.data.get("git_mode") == "student"

    def concepts(self) -> list[str]:
        return self.data["concepts"]["new"] + self.data["concepts"]["practiced"]

    def event(self, type_: str, **fields) -> None:
        self.data["events"].append({"at": stamp(), "type": type_, **fields})

    def events(self, type_: str) -> list[dict]:
        return [e for e in self.data["events"] if e["type"] == type_]

    def done_at(self) -> datetime | None:
        done = self.events("done")
        return parse_ts(done[-1]["at"]) if done else None

    def minutes(self) -> float:
        """Active minutes: time between start/resume and park/done, plus the current run."""
        total = timedelta()
        running_since = None
        for e in self.data["events"]:
            if e["type"] in ("started", "resumed"):
                running_since = parse_ts(e["at"])
            elif e["type"] in ("parked", "done") and running_since:
                total += parse_ts(e["at"]) - running_since
                running_since = None
        if running_since:
            total += now() - running_since
        return total.total_seconds() / 60

    def save(self) -> None:
        self.file.write_text(json.dumps(self.data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def lessons_in(base: Path) -> list[Lesson]:
    if not base.is_dir():
        return []
    found = [Lesson(p) for p in base.iterdir() if (p / "lesson.json").is_file()]
    return sorted(found, key=lambda lesson: lesson.num)


def all_lessons() -> list[Lesson]:
    return sorted(lessons_in(LESSONS) + lessons_in(CURRICULUM), key=lambda lesson: lesson.num)


def active_lesson() -> Lesson | None:
    active = [lesson for lesson in lessons_in(LESSONS) if lesson.state in ACTIVE_STATES]
    if len(active) > 1:
        raise CliError(f"more than one active lesson: {', '.join(a.id for a in active)}; park all but one")
    return active[0] if active else None


def require_active(*states: str) -> Lesson:
    lesson = active_lesson()
    if not lesson:
        raise CliError("no active lesson; start one with `learn.py next`")
    if states and lesson.state not in states:
        raise CliError(f"{lesson.id} is in state '{lesson.state}', expected one of: {', '.join(states)}")
    return lesson


def find_lesson(lesson_id: str) -> Lesson:
    for lesson in all_lessons():
        if lesson.id == lesson_id.upper():
            return lesson
    raise CliError(f"lesson {lesson_id} not found")


def introduced_before(lessons: list[Lesson], num: int) -> set[str]:
    return {cid for lesson in lessons if lesson.num < num for cid in lesson.data["concepts"]["new"]}


# ---------- git ----------

def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if check and proc.returncode != 0:
        raise CliError(f"git {' '.join(args)} failed:\n{proc.stderr.strip()}")
    return proc


def has_remote() -> bool:
    return bool(git("remote", check=False).stdout.strip())


def sync() -> None:
    if has_remote() and git("pull", "--rebase", "--autostash", check=False).returncode != 0:
        warn("git pull failed; continuing with the local copy")


def push() -> None:
    if has_remote() and git("push", "-u", "origin", "HEAD", check=False).returncode != 0:
        warn("git push failed; changes are committed locally and will go up with the next push")


def commit(message: str, paths: list[Path], exclude: list[Path] = ()) -> bool:
    specs = [rel(p) for p in paths if p.exists() or git("ls-files", "--", rel(p), check=False).stdout.strip()]
    if not specs:
        return False
    specs += [f":(exclude){rel(p)}" for p in exclude]
    git("add", "-A", "--", *specs)
    if git("diff", "--cached", "--quiet", check=False).returncode == 0:
        return False
    git("commit", "-q", "-m", message)
    return True


def commit_lesson(lesson: Lesson, what: str, extra_paths: list[Path] = ()) -> None:
    exclude = [lesson.path / "work"] if lesson.student_git else []
    commit(f"{lesson.id}: {what}", [lesson.path, *extra_paths], exclude)


def work_is_dirty(lesson: Lesson) -> bool:
    work = lesson.path / "work"
    return work.exists() and bool(git("status", "--porcelain", "--", rel(work), check=False).stdout.strip())


def git_mode(roadmap: dict, lessons: list[Lesson]) -> str:
    """'student' once every module that hands git over has all its concepts done."""
    done_new = {cid for lesson in lessons if lesson.state == "done" for cid in lesson.data["concepts"]["new"]}
    mode = "tutor"
    for module in roadmap["modules"]:
        target = module.get("on_complete", {}).get("git_mode")
        if target and all(c["id"] in done_new for c in module["concepts"]):
            mode = target
    return mode


# ---------- tests ----------

def run_tests(tests: Path, work: Path) -> dict:
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join(filter(None, [str(work), str(TOOLS), env.get("PYTHONPATH")]))
    env["LESSON_WORK"] = str(work)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    cmd = [sys.executable, "-m", "unittest", "discover", "-s", str(tests), "-t", str(tests), "-p", "test_*.py", "-v"]
    try:
        proc = subprocess.run(cmd, cwd=work, env=env, stdin=subprocess.DEVNULL, capture_output=True,
                              text=True, encoding="utf-8", timeout=TEST_TIMEOUT_S)
    except subprocess.TimeoutExpired:
        return {"ok": False, "ran": 0, "passed": 0, "failed": 0, "output": f"tests timed out after {TEST_TIMEOUT_S}s"}
    output = proc.stdout + proc.stderr
    ran_match = re.search(r"Ran (\d+) tests?", output)
    ran = int(ran_match.group(1)) if ran_match else 0
    # Each failing subTest is counted separately, so cap at the number of tests run.
    failed = min(ran, sum(int(n) for n in re.findall(r"(?:failures|errors)=(\d+)", output)))
    ok = proc.returncode == 0 and ran > 0
    return {"ok": ok, "ran": ran, "passed": ran - failed, "failed": failed, "output": output}


# ---------- mastery ----------

def compute_mastery(lessons: list[Lesson]) -> dict[str, dict]:
    """Score 0..1 per concept from done lessons: fewer issues, fewer rounds, more lessons, newer = higher."""
    samples: dict[str, list[float]] = {}
    issue_counts: dict[str, int] = {}
    done = sorted((lesson for lesson in lessons if lesson.state == "done"), key=lambda lesson: lesson.num, reverse=True)
    for lesson in done:
        reviews = lesson.data["reviews"]
        extra_rounds = max(0, len(reviews) - 1)
        issue_concepts = [i["concept"] for r in reviews for i in r["issues"]]
        for cid in dict.fromkeys(lesson.concepts() + issue_concepts):
            is_new = cid in lesson.data["concepts"]["new"]
            issues = [i for r in reviews for i in r["issues"] if i["concept"] == cid]
            weight = sum(SEVERITY_WEIGHT.get(i["severity"], 0.4) for i in issues)
            score = 1 - 0.35 * weight - (0.1 if is_new else 0.05) * extra_rounds
            samples.setdefault(cid, []).append(max(0.0, score))
            issue_counts[cid] = issue_counts.get(cid, 0) + len(issues)
    result = {}
    for cid, scores in samples.items():
        weights = [0.8 ** k for k in range(len(scores))]  # newest lesson first
        average = sum(w * s for w, s in zip(weights, scores)) / sum(weights)
        confidence = 1 - 0.5 ** len(scores)
        result[cid] = {"score": round(average * confidence, 2), "lessons": len(scores), "issues": issue_counts[cid]}
    return result


# ---------- commands: lesson flow ----------

def cmd_next(args) -> int:
    sync()
    if lesson := active_lesson():
        raise CliError(f"{lesson.id} is still active (state: {lesson.state}); continue it, or `learn.py park`")
    parked = [lesson for lesson in lessons_in(LESSONS) if lesson.state == "parked"]
    if parked and not args.skip_parked:
        raise CliError(f"{parked[0].id} is parked; `learn.py resume`, or pass --skip-parked")

    roadmap = load_roadmap()
    lessons = all_lessons()
    break_min = roadmap["pace"]["break_minutes"]
    finished = [t for t in (lesson.done_at() for lesson in lessons) if t]
    since = (now() - max(finished)).total_seconds() / 60 if finished else None
    if since is not None and since < break_min and not args.override_break:
        print(f"BREAK: the last lesson finished {since:.0f} min ago; the break is {break_min} min "
              f"({break_min - since:.0f} min left). Rerun with --override-break \"reason\" to start anyway.")
        return EXIT_BREAK

    planned = [lesson for lesson in lessons_in(CURRICULUM) if lesson.state == "planned"]
    if not planned:
        raise CliError("no planned lessons left; ask the maintainer to run /plan-week")
    source = planned[0].path
    LESSONS.mkdir(exist_ok=True)
    target = LESSONS / source.name
    shutil.move(str(source), str(target))

    lesson = Lesson(target)
    lesson.state = "theory"
    lesson.data["git_mode"] = git_mode(roadmap, lessons)
    lesson.event("started")
    if since is not None and since < break_min:
        lesson.event("break_override", reason=args.override_break, break_minutes=round(since))
    lesson.save()
    commit_lesson(lesson, "start", [source])

    print(f"Started {lesson.id}: {lesson.data['title']}")
    print(f"  folder:    {rel(lesson.path)}")
    print(f"  kind:      {lesson.data['kind']}, ~{lesson.data['estimate_min']} min")
    print(f"  new:       {', '.join(lesson.data['concepts']['new']) or '-'}")
    print(f"  practiced: {', '.join(lesson.data['concepts']['practiced']) or '-'}")
    print(f"  scaffold:  level {lesson.data['scaffold']['level']}")
    print(f"  git mode:  {lesson.data['git_mode']}")
    print("Next: write theory.md from outline.md, teach it, then `learn.py advance check`.")
    return 0


def cmd_advance(args) -> int:
    if args.to == "check":
        lesson = require_active("theory")
        theory = lesson.path / "theory.md"
        if not theory.is_file() or not theory.read_text(encoding="utf-8").strip():
            raise CliError(f"write {rel(theory)} before moving to the check questions")
        lesson.event("theory_done")
        lesson.state = "check"
        lesson.save()
        commit_lesson(lesson, "theory")
        print(f"{lesson.id}: check questions. Record each with `learn.py check-record`.")
    else:
        lesson = require_active("check")
        if not lesson.data["check_questions"]:
            warn("no check questions recorded")
        setup_work(lesson)
        lesson.event("check_done")
        lesson.event("task_setup")
        lesson.state = "task"
        lesson.save()
        commit_lesson(lesson, "task setup")
        files = sorted(rel(p) for p in (lesson.path / "work").rglob("*") if p.is_file())
        print(f"{lesson.id}: task ready. Files in work/:")
        for f in files:
            print(f"  {f}")
    return 0


def setup_work(lesson: Lesson) -> None:
    work = lesson.path / "work"
    if work.exists() and any(work.iterdir()):
        raise CliError(f"{rel(work)} is not empty; refusing to overwrite the learner's code")
    work.mkdir(exist_ok=True)
    ignore = shutil.ignore_patterns("__pycache__", "*.pyc")
    if continues := lesson.data.get("continues"):
        previous = find_lesson(continues).path / "work"
        if previous.is_dir():
            shutil.copytree(previous, work, dirs_exist_ok=True, ignore=ignore)
        else:
            warn(f"{continues} has no work/ to continue from")
    starter = lesson.path / "starter"
    for source in sorted(starter.rglob("*")) if starter.is_dir() else []:
        target = work / source.relative_to(starter)
        if source.is_file() and "__pycache__" not in source.parts and not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


def cmd_check_record(args) -> int:
    lesson = require_active("check")
    entry = {"q": args.question, "answered_ok": args.result == "ok"}
    if args.note:
        entry["note"] = args.note
    lesson.data["check_questions"].append(entry)
    lesson.save()
    print(f"{lesson.id}: recorded check question {len(lesson.data['check_questions'])} ({args.result})")
    return 0


def cmd_review_start(args) -> int:
    lesson = require_active("task", "in_review")
    if lesson.student_git and work_is_dirty(lesson):
        raise CliError("work/ has uncommitted changes; commit your work before asking for a review")
    number = len(lesson.data["reviews"]) + 1
    reviews = lesson.path / "reviews"
    print(json.dumps({
        "lesson": lesson.id,
        "path": rel(lesson.path),
        "round": number,
        "write_review_to": rel(reviews / f"round-{number}.md"),
        "write_issues_to": rel(reviews / f"round-{number}.json"),
        "previous_reviews": [rel(reviews / f"round-{n}.md") for n in range(1, number)],
        "scaffold": lesson.data["scaffold"],
        "concepts": lesson.data["concepts"],
    }, indent=2))
    return 0


def cmd_review_record(args) -> int:
    lesson = require_active("task", "in_review")
    number = len(lesson.data["reviews"]) + 1
    reviews = lesson.path / "reviews"
    issues_file = reviews / f"round-{number}.json"
    review_md = reviews / f"round-{number}.md"
    for required in (issues_file, review_md):
        if not required.is_file():
            raise CliError(f"missing {rel(required)}")
    payload = json.loads(issues_file.read_text(encoding="utf-8"))

    verdict = payload.get("verdict")
    if verdict not in VERDICTS:
        raise CliError(f"verdict must be one of {VERDICTS}, got {verdict!r}")
    tests = payload.get("tests", {})
    if not all(isinstance(tests.get(k), int) for k in ("passed", "failed")):
        raise CliError("tests must be {\"passed\": int, \"failed\": int}")
    issues = payload.get("issues", [])
    for issue in issues:
        missing = {"concept", "type", "severity", "note"} - issue.keys()
        if missing:
            raise CliError(f"issue missing {sorted(missing)}: {issue}")
        if issue["severity"] not in SEVERITY_WEIGHT:
            raise CliError(f"severity must be one of {list(SEVERITY_WEIGHT)}: {issue}")
    check_concepts([i["concept"] for i in issues], load_roadmap())
    if verdict == "approved" and any(i["severity"] == "major" for i in issues):
        raise CliError("a review with major issues cannot be approved")

    lesson.data["reviews"].append({"round": number, "at": stamp(), "verdict": verdict,
                                   "tests": {"passed": tests["passed"], "failed": tests["failed"]},
                                   "issues": issues})
    lesson.event("review", round=number, verdict=verdict)
    lesson.state = "takeaways" if verdict == "approved" else "in_review"
    lesson.save()
    commit_lesson(lesson, f"review {number} ({verdict.replace('_', ' ')})")
    print(f"{lesson.id}: review {number} recorded: {verdict}, {len(issues)} issue(s)")
    return 0


def cmd_done(args) -> int:
    lesson = require_active("takeaways")
    takeaways = lesson.path / "takeaways.md"
    lines = []
    if takeaways.is_file():
        lines = [ln for ln in takeaways.read_text(encoding="utf-8").splitlines()
                 if ln.strip() and not ln.lstrip().startswith("#")]
    if len(lines) < 2:
        raise CliError(f"{rel(takeaways)} needs at least two lines of the learner's takeaways")
    if lesson.student_git and work_is_dirty(lesson):
        raise CliError("work/ has uncommitted changes; commit your work first")

    lesson.event("done")
    lesson.state = "done"
    lesson.save()
    commit_lesson(lesson, "done")
    push()

    roadmap = load_roadmap()
    today = sum(1 for le in lessons_in(LESSONS) if (t := le.done_at()) and t.date() == now().date())
    print(f"{lesson.id} done in {lesson.minutes():.0f} min (estimate {lesson.data['estimate_min']}). "
          f"Lessons today: {today}.")
    print(f"Take a {roadmap['pace']['break_minutes']}-minute break before the next one.")
    return 0


def cmd_park(args) -> int:
    lesson = require_active()
    lesson.event("parked", previous_state=lesson.state)
    lesson.state = "parked"
    lesson.save()
    commit_lesson(lesson, "park")
    push()
    print(f"{lesson.id} parked. `learn.py resume` picks it up again.")
    return 0


def cmd_resume(args) -> int:
    if lesson := active_lesson():
        raise CliError(f"{lesson.id} is active; park it first")
    if args.lesson:
        lesson = find_lesson(args.lesson)
        if lesson.state != "parked":
            raise CliError(f"{lesson.id} is not parked")
    else:
        parked = [le for le in lessons_in(LESSONS) if le.state == "parked"]
        if not parked:
            raise CliError("no parked lessons")
        lesson = parked[0]
    lesson.state = lesson.events("parked")[-1]["previous_state"]
    lesson.event("resumed")
    lesson.save()
    commit_lesson(lesson, "resume")
    print(f"{lesson.id} resumed in state '{lesson.state}'.")
    return 0


def cmd_test(args) -> int:
    lesson = find_lesson(args.lesson) if args.lesson else require_active()
    work = Path(args.work).resolve() if args.work else lesson.path / "work"
    if not work.is_dir():
        raise CliError(f"{work} does not exist")
    result = run_tests(lesson.path / "tests", work)
    if args.json:
        print(json.dumps({k: v for k, v in result.items() if k != "output"}))
    else:
        print(result["output"].rstrip())
        print(f"\n{'PASSED' if result['ok'] else 'NOT PASSING'}: {result['passed']}/{result['ran']} tests")
    return 0 if result["ok"] else 1


# ---------- commands: reporting ----------

def cmd_status(args) -> int:
    roadmap = load_roadmap()
    lessons = all_lessons()
    concepts = roadmap_concepts(roadmap)
    mastery = compute_mastery(lessons)
    started = lessons_in(LESSONS)
    done = [lesson for lesson in started if lesson.state == "done"]
    done_new = {cid for lesson in done for cid in lesson.data["concepts"]["new"]}
    planned = [lesson for lesson in lessons_in(CURRICULUM) if lesson.state == "planned"]
    active = active_lesson()
    parked = [lesson for lesson in started if lesson.state == "parked"]

    current = next((c for c in concepts if c["id"] not in done_new), None)
    module = None
    if current:
        module_concepts = [c for c in concepts if c["module"] == current["module"]]
        module = {"id": current["module"], "title": current["module_title"],
                  "done": sum(c["id"] in done_new for c in module_concepts), "total": len(module_concepts)}

    done_days = {t.date() for lesson in done if (t := lesson.done_at())}
    today = now().date()
    streak, day = 0, today if today in done_days else today - timedelta(days=1)
    while day in done_days:
        streak, day = streak + 1, day - timedelta(days=1)
    finished = [t for t in (lesson.done_at() for lesson in done) if t]
    recent = sorted(done, key=lambda lesson: lesson.num)[-10:]
    weakest = sorted(((cid, m) for cid, m in mastery.items() if cid in done_new), key=lambda x: x[1]["score"])[:5]

    status = {
        "module": module,
        "concepts": {"done": len(done_new), "total": len(concepts)},
        "lessons": {"done": len(done), "planned": len(planned)},
        "today": sum(1 for t in finished if t.date() == today),
        "streak_days": streak,
        "active": {"id": active.id, "title": active.data["title"], "state": active.state,
                   "minutes": round(active.minutes())} if active else None,
        "parked": [lesson.id for lesson in parked],
        "minutes_since_last_lesson": round((now() - max(finished)).total_seconds() / 60) if finished else None,
        "timing_last_10": {"actual_avg": round(sum(le.minutes() for le in recent) / len(recent)),
                           "estimate_avg": round(sum(le.data["estimate_min"] for le in recent) / len(recent))}
        if recent else None,
        "weakest": [{"concept": cid, **m} for cid, m in weakest],
    }
    if args.json:
        print(json.dumps(status, indent=2))
        return 0

    print(roadmap["goal"])
    if module:
        print(f"  Module   {module['id']} {module['title']}: {module['done']}/{module['total']} concepts")
    else:
        print("  Module   roadmap complete")
    print(f"  Overall  {status['concepts']['done']}/{status['concepts']['total']} concepts, "
          f"{len(done)} lessons done, {len(planned)} planned")
    print(f"  Today    {status['today']} lesson(s), streak {streak} day(s)")
    if active:
        print(f"  Active   {active.id} {active.data['title']}: {active.state}, {status['active']['minutes']} min")
    if parked:
        print(f"  Parked   {', '.join(status['parked'])}")
    if status["minutes_since_last_lesson"] is not None:
        print(f"  Last     finished {status['minutes_since_last_lesson']} min ago")
    if status["timing_last_10"]:
        t = status["timing_last_10"]
        print(f"  Timing   last {len(recent)}: {t['actual_avg']} min actual vs {t['estimate_avg']} min estimated")
    if weakest:
        print("  Weakest  " + ", ".join(f"{cid} {m['score']:.2f}" for cid, m in weakest))
    if not planned and not active:
        print("  Nothing planned: maintainer, run /plan-week")
    return 0


def cmd_mastery(args) -> int:
    roadmap = load_roadmap()
    mastery = compute_mastery(all_lessons())
    if args.json:
        print(json.dumps(mastery, indent=2))
        return 0
    titles = {c["id"]: c["title"] for c in roadmap_concepts(roadmap)}
    for cid, m in sorted(mastery.items(), key=lambda x: x[1]["score"]):
        print(f"{m['score']:.2f}  {cid:<22} {m['lessons']} lesson(s), {m['issues']} issue(s)  {titles.get(cid, '?')}")
    return 0


def cmd_plan_context(args) -> int:
    sync()
    roadmap = load_roadmap()
    lessons = all_lessons()
    concepts = roadmap_concepts(roadmap)
    introduced = {cid for lesson in lessons for cid in lesson.data["concepts"]["new"]}
    done = [lesson for lesson in lessons if lesson.state == "done"]
    mastery = compute_mastery(lessons)
    recent_issues = [{"lesson": lesson.id, "round": r["round"], **i}
                     for lesson in done[-15:] for r in lesson.data["reviews"] for i in r["issues"]]
    active = active_lesson()
    context = {
        "today": date.today().isoformat(),
        "next_week": max((lesson.data["week"] for lesson in lessons), default=0) + 1,
        "next_lesson_id": f"L{max((lesson.num for lesson in lessons), default=0) + 1:04d}",
        "pace": roadmap["pace"],
        "git_mode": git_mode(roadmap, lessons),
        "introduced_concepts": [c["id"] for c in concepts if c["id"] in introduced],
        "next_concepts": [c for c in concepts if c["id"] not in introduced][:30],
        "planned_not_started": [{"id": lesson.id, "title": lesson.data["title"], "week": lesson.data["week"],
                                 "kind": lesson.data["kind"], "concepts": lesson.data["concepts"]}
                                for lesson in lessons if lesson.state == "planned"],
        "in_progress": {"id": active.id, "state": active.state} if active else None,
        "mastery": mastery,
        "weak_concepts": sorted((cid for cid, m in mastery.items() if m["score"] < 0.6), key=lambda c: mastery[c]["score"]),
        "recent_issues": recent_issues,
        "timing": [{"id": lesson.id, "kind": lesson.data["kind"], "estimate": lesson.data["estimate_min"],
                    "actual": round(lesson.minutes()), "review_rounds": len(lesson.data["reviews"])}
                   for lesson in done[-15:]],
        "recent_takeaways": [rel(lesson.path / "takeaways.md") for lesson in done[-6:]],
    }
    print(json.dumps(context, indent=2, ensure_ascii=False))
    return 0


# ---------- commands: planning ----------

def cmd_scaffold(args) -> int:
    roadmap = load_roadmap()
    if not SLUG_RE.match(args.slug):
        raise CliError("slug must be lowercase words separated by dashes, e.g. for-loops")
    if args.kind not in KINDS:
        raise CliError(f"kind must be one of {KINDS}")
    if not 0 <= args.level <= 3:
        raise CliError("scaffold level must be 0..3")
    new, practiced = split_csv(args.new), split_csv(args.practiced)
    check_concepts(new + practiced, roadmap)
    if args.continues:
        find_lesson(args.continues)

    lessons = all_lessons()
    number = max((lesson.num for lesson in lessons), default=0) + 1
    lesson_id = f"L{number:04d}"
    path = CURRICULUM / f"{lesson_id}-{args.slug}"
    (path / "starter").mkdir(parents=True)
    (path / "tests").mkdir()
    data = {
        "id": lesson_id,
        "slug": args.slug,
        "title": args.title,
        "week": args.week,
        "kind": args.kind,
        "concepts": {"new": new, "practiced": practiced},
        "scaffold": {"level": args.level, "provided": split_csv(args.provided), "reason": args.reason or ""},
        "estimate_min": args.estimate,
        "state": "planned",
        "check_questions": [],
        "reviews": [],
        "events": [{"at": stamp(), "type": "planned", "by": "planner"}],
    }
    if args.continues:
        data["continues"] = args.continues.upper()
    (path / "lesson.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(rel(path))
    return 0


def validate_lesson(lesson: Lesson, lessons: list[Lesson], roadmap: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    d = lesson.data
    required = {"id", "slug", "title", "week", "kind", "concepts", "scaffold", "estimate_min", "state",
                "check_questions", "reviews", "events"}
    if missing := required - d.keys():
        return [f"lesson.json missing keys: {sorted(missing)}"], []
    if lesson.path.name != f"{d['id']}-{d['slug']}":
        errors.append(f"folder name should be {d['id']}-{d['slug']}")
    if d["kind"] not in KINDS:
        errors.append(f"kind must be one of {KINDS}")
    if d["kind"] == "regular" and not d["concepts"]["new"]:
        errors.append("a regular lesson needs at least one new concept")
    if d["kind"] == "review" and d["concepts"]["new"]:
        errors.append("a review lesson must not introduce new concepts")
    try:
        check_concepts(lesson.concepts(), roadmap)
    except CliError as e:
        errors.append(str(e))
    earlier = introduced_before(lessons, lesson.num)
    if not_yet := [c for c in d["concepts"]["practiced"] if c not in earlier]:
        errors.append(f"practiced concepts not introduced in an earlier lesson: {', '.join(not_yet)}")
    if repeated := [c for c in d["concepts"]["new"] if c in earlier]:
        warnings.append(f"new concepts already introduced earlier: {', '.join(repeated)}")
    if not 45 <= d["estimate_min"] <= 80:
        warnings.append(f"estimate {d['estimate_min']} min is outside the usual 60-75")

    for name in REQUIRED_FILES:
        f = lesson.path / name
        if not f.is_file() or not f.read_text(encoding="utf-8").strip():
            errors.append(f"{name} is missing or empty")
    starter = lesson.path / "starter"
    if not starter.is_dir() or not any(p.is_file() for p in starter.rglob("*")):
        errors.append("starter/ needs at least one file (an empty main.py counts)")
    tests = lesson.path / "tests"
    test_files = sorted(tests.glob("test_*.py")) if tests.is_dir() else []
    if not test_files:
        errors.append("tests/ needs at least one test_*.py file")
    for tf in test_files:
        try:
            compile(tf.read_text(encoding="utf-8"), str(tf), "exec")
        except SyntaxError as e:
            errors.append(f"{tf.name} has a syntax error: {e}")

    if not errors and not d.get("continues"):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(starter, tmp, dirs_exist_ok=True)
            if run_tests(tests, Path(tmp))["ok"]:
                errors.append("tests already pass on the starter code")
    return errors, warnings


def cmd_validate(args) -> int:
    roadmap = load_roadmap()
    lessons = all_lessons()
    targets = [find_lesson(i) for i in args.lessons] if args.lessons else lessons_in(CURRICULUM)
    failed = 0
    for lesson in targets:
        errors, warnings = validate_lesson(lesson, lessons, roadmap)
        mark = "FAIL" if errors else "ok"
        print(f"{mark:<4} {rel(lesson.path)}")
        for e in errors:
            print(f"     error: {e}")
        for w in warnings:
            print(f"     warning: {w}")
        failed += bool(errors)
    print(f"\n{len(targets) - failed}/{len(targets)} valid")
    return EXIT_ERROR if failed else 0


def cmd_commit_plan(args) -> int:
    week = [lesson for lesson in lessons_in(CURRICULUM) if lesson.data["week"] == args.week]
    if not week:
        raise CliError(f"no planned lessons for week {args.week}")
    roadmap = load_roadmap()
    lessons = all_lessons()
    broken = [lesson.id for lesson in week if validate_lesson(lesson, lessons, roadmap)[0]]
    if broken:
        raise CliError(f"fix these first (`learn.py validate`): {', '.join(broken)}")
    message = f"plan: week {args.week:02d} ({week[0].id}-{week[-1].id})"
    if commit(message, [CURRICULUM, ROOT / "plans"]):
        push()
        print(f"committed and pushed: {message}")
    else:
        print("nothing to commit")
    return 0


# ---------- hooks (must never fail loudly) ----------

def cmd_hook(args) -> int:
    try:
        lesson = active_lesson()
        if args.event == "session-start":
            roadmap = load_roadmap()
            if lesson:
                print(f"[course] Active lesson {lesson.id} \"{lesson.data['title']}\" in state '{lesson.state}', "
                      f"{lesson.minutes():.0f} min so far. Folder: {rel(lesson.path)}. "
                      f"Pick it up from that state (see CLAUDE.md).")
            elif parked := [le for le in lessons_in(LESSONS) if le.state == "parked"]:
                print(f"[course] No active lesson; {parked[0].id} is parked (`python tools/learn.py resume`).")
            else:
                planned = [le for le in lessons_in(CURRICULUM) if le.state == "planned"]
                print(f"[course] No active lesson. {len(planned)} planned lesson(s) left. "
                      f"Break length is {roadmap['pace']['break_minutes']} min.")
        elif args.event == "prompt" and lesson:
            minutes = lesson.minutes()
            if minutes >= TIMER_WARN_MIN:
                low, high = load_roadmap()["pace"]["lesson_minutes"]
                print(f"[lesson timer] {lesson.id} has been running {minutes:.0f} min (target {low}-{high}). "
                      f"Mention it once and suggest finishing up or parking (`learn.py park`).")
    except Exception as e:  # noqa: BLE001 - a hook must not break the session
        print(f"[course] status unavailable: {e}")
    return 0


# ---------- entry point ----------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="learn.py", description="Course bookkeeping. The only writer of lesson.json.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("next", help="start the next planned lesson")
    p.add_argument("--override-break", metavar="REASON", help="start before the break is over (logged)")
    p.add_argument("--skip-parked", action="store_true", help="start a new lesson even if one is parked")
    p.set_defaults(func=cmd_next)

    p = sub.add_parser("advance", help="move the active lesson to the check questions or the task")
    p.add_argument("to", choices=("check", "task"))
    p.set_defaults(func=cmd_advance)

    p = sub.add_parser("check-record", help="record one check question and how it went")
    p.add_argument("question")
    p.add_argument("result", choices=("ok", "redo"))
    p.add_argument("--note")
    p.set_defaults(func=cmd_check_record)

    p = sub.add_parser("review-start", help="print the review round info (JSON) for the reviewer")
    p.set_defaults(func=cmd_review_start)

    p = sub.add_parser("review-record", help="record reviews/round-N.json for the active lesson")
    p.set_defaults(func=cmd_review_record)

    p = sub.add_parser("done", help="finish the active lesson (needs takeaways.md)")
    p.set_defaults(func=cmd_done)

    p = sub.add_parser("park", help="pause the active lesson")
    p.set_defaults(func=cmd_park)

    p = sub.add_parser("resume", help="resume a parked lesson")
    p.add_argument("lesson", nargs="?")
    p.set_defaults(func=cmd_resume)

    p = sub.add_parser("test", help="run a lesson's tests against work/ (or --work DIR)")
    p.add_argument("--lesson")
    p.add_argument("--work")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_test)

    p = sub.add_parser("status", help="progress overview")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("mastery", help="mastery score per concept")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_mastery)

    p = sub.add_parser("plan-context", help="everything the planner needs, as JSON")
    p.set_defaults(func=cmd_plan_context)

    p = sub.add_parser("scaffold", help="create a planned lesson folder with its lesson.json")
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--week", type=int, required=True)
    p.add_argument("--kind", default="regular", choices=KINDS)
    p.add_argument("--new", default="", help="comma-separated concept ids introduced here")
    p.add_argument("--practiced", default="", help="comma-separated concept ids practiced here")
    p.add_argument("--estimate", type=int, default=65, help="minutes")
    p.add_argument("--level", type=int, default=0, help="scaffold level 0..3")
    p.add_argument("--provided", default="", help="comma-separated list of what the starter provides")
    p.add_argument("--reason", help="why this scaffold level")
    p.add_argument("--continues", metavar="LESSON_ID", help="start work/ from that lesson's work/ (projects)")
    p.set_defaults(func=cmd_scaffold)

    p = sub.add_parser("validate", help="check planned lessons (default: all of curriculum/)")
    p.add_argument("lessons", nargs="*")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("commit-plan", help="validate, commit and push a planned week")
    p.add_argument("--week", type=int, required=True)
    p.set_defaults(func=cmd_commit_plan)

    p = sub.add_parser("hook", help="output for Claude Code hooks")
    p.add_argument("event", choices=("session-start", "prompt"))
    p.set_defaults(func=cmd_hook)
    return parser


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except CliError as e:
        print(f"error: {e}", file=sys.stderr)
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
