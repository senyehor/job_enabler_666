"""Helpers for lesson tests. Tests run with the learner's work/ folder as the working directory.

    from lessonkit import run_script, load_module

    result = run_script("main.py", stdin="3\n4\n")
    self.assertIn("7", result.stdout)
"""
from __future__ import annotations

import builtins
import importlib.util
import os
import subprocess
import sys
from pathlib import Path
from types import ModuleType

WORK = Path(os.environ.get("LESSON_WORK", os.getcwd()))


def run_script(name: str, stdin: str = "", args: tuple[str, ...] = (), timeout: float = 5) -> subprocess.CompletedProcess:
    """Run a learner's script as a separate program, feeding it stdin. Returns stdout/stderr/returncode."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run([sys.executable, str(WORK / name), *args], cwd=WORK, input=stdin, env=env,
                          capture_output=True, text=True, encoding="utf-8", timeout=timeout)


def load_module(name: str) -> ModuleType:
    """Import a learner's file (e.g. 'counter.py') by path. input() raises instead of waiting forever."""
    path = WORK / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)

    def no_input(prompt: str = "") -> str:
        raise RuntimeError(f"{name} called input() at import time; put that code under if __name__ == '__main__':")

    original = builtins.input
    builtins.input = no_input
    try:
        spec.loader.exec_module(module)
    finally:
        builtins.input = original
    return module
