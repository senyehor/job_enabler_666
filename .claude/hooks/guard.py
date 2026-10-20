#!/usr/bin/env python3
"""PreToolUse guard: Claude never writes the learner's code or lesson.json.

- lessons/*/work/** belongs to the learner. Claude may read and run it, never change it.
- lesson.json is written only by tools/learn.py.
Exit code 2 blocks the tool call and shows stderr to Claude.
"""
import json
import re
import sys

WORK_PATH = re.compile(r"(^|[\\/])lessons[\\/][^\\/]+[\\/]work([\\/]|$)")
LESSON_JSON = re.compile(r"(^|[\\/])lesson\.json$")
# A "work" path segment mentioned anywhere in a shell command.
WORK_IN_CMD = re.compile(r"(^|[\s'\"=\\/])work([\\/]|[\s'\";|&]|$)")
SCRATCH_PATH = re.compile(r"\S*\.scratch([\\/]\S*)?")
REDIRECT_TARGET =re.compile(r"(?<![0-9&])>{1,2}\s*([^\s;&|]+)")
WRITE_COMMANDS = re.compile(
    r"(^|[;&|(]\s*|\s)(cp|mv|rm|rmdir|touch|tee|truncate|install|ln|sed\s+-i|perl\s+-[a-z]*i|dd)\b"
)
PYTHON_INLINE = re.compile(r"\bpython3?\s+-c\b|<<")
GIT_DISCARD = re.compile(r"\bgit\s+(restore|checkout\s+(--|\.)|reset\s+--hard|stash|clean)\b")

WORK_MSG = ("Blocked: lessons/*/work/ is the learner's code. Do not write, move or delete it. "
            "Explain the problem and give a hint instead; the learner makes the change.")
JSON_MSG = "Blocked: lesson.json is written only by `python tools/learn.py`. Use the matching command."


def block(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(2)


def check_path(path: str) -> None:
    if WORK_PATH.search(path):
        block(WORK_MSG)
    if LESSON_JSON.search(path):
        block(JSON_MSG)


def check_bash(command: str, cwd: str) -> None:
    if GIT_DISCARD.search(command):
        block("Blocked: this git command can throw away the learner's work. Ask the maintainer to run it by hand.")
    for target in REDIRECT_TARGET.findall(command):
        if WORK_PATH.search(target) or LESSON_JSON.search(target):
            block(WORK_MSG if WORK_PATH.search(target) else JSON_MSG)
    # The lesson builder's throwaway solutions live in .scratch/ and may contain a work/ folder.
    outside_scratch = SCRATCH_PATH.sub("", command)
    in_scratch_cwd = bool(SCRATCH_PATH.search(cwd))
    mentions_work = bool(WORK_IN_CMD.search(outside_scratch)) or (
        bool(WORK_PATH.search(cwd + "/")) and not in_scratch_cwd)
    writes = bool(WRITE_COMMANDS.search(command) or PYTHON_INLINE.search(command) or REDIRECT_TARGET.search(command))
    if mentions_work and writes:
        block(WORK_MSG)
    if "lesson.json" in command and (writes or WRITE_COMMANDS.search(command)):
        block(JSON_MSG)


def main() -> None:
    event = json.load(sys.stdin)
    tool = event.get("tool_name", "")
    data = event.get("tool_input", {}) or {}
    if tool == "Bash":
        check_bash(data.get("command", ""), event.get("cwd", ""))
    else:
        for key in ("file_path", "notebook_path", "path"):
            if isinstance(data.get(key), str):
                check_path(data[key])
    sys.exit(0)


if __name__ == "__main__":
    main()
