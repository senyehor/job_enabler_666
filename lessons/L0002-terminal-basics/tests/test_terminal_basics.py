"""Tests for L0002: the folder tree in work/projects/ and work/commands.txt."""
import os
import re
import unittest
from pathlib import Path

WORK = Path(os.environ.get("LESSON_WORK", os.getcwd()))
PROJECTS = WORK / "projects"
NOTES = PROJECTS / "notes"
SCRATCH = PROJECTS / "scratch"

# Absolute: C:\... or C:/... (Windows/PowerShell) or a path starting with / (Git Bash /c/..., or ~/ for home).
ABSOLUTE = r"(?:\b[A-Za-z]:[\\/]|(?:^|[\s\"'`(:=])(?:/|~/)\w)"


def read_text(path: Path) -> str:
    """Read a text file whether the terminal saved it as UTF-8 or UTF-16 (older PowerShell)."""
    data = path.read_bytes()
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return data.decode("utf-16")
    return data.decode("utf-8-sig", errors="replace")


def non_empty_lines(path: Path) -> list[str]:
    return [line for line in read_text(path).splitlines() if line.strip()]


class FolderTree(unittest.TestCase):
    def test_projects_has_notes_and_scratch_folders(self):
        self.assertTrue(PROJECTS.is_dir(), "Expected a folder work/projects/ (make it with mkdir).")
        self.assertTrue(NOTES.is_dir(), "Expected a folder work/projects/notes/.")
        self.assertTrue(SCRATCH.is_dir(), "Expected a folder work/projects/scratch/.")

    def test_todo_has_at_least_two_lines(self):
        todo = NOTES / "todo.txt"
        self.assertTrue(todo.is_file(), "Expected a file work/projects/notes/todo.txt.")
        lines = non_empty_lines(todo)
        self.assertGreaterEqual(len(lines), 2,
                                f"todo.txt should have at least 2 lines, found {len(lines)}. "
                                "Did a second '>' overwrite the first line? Use '>>' to add a line.")

    def test_ideas_was_moved_into_notes(self):
        self.assertTrue((NOTES / "ideas.txt").is_file(), "Expected ideas.txt inside work/projects/notes/.")
        self.assertFalse((SCRATCH / "ideas.txt").exists(),
                         "ideas.txt is still in projects/scratch/. Move it with mv, don't copy it.")
        self.assertTrue(non_empty_lines(NOTES / "ideas.txt"), "ideas.txt should contain a line of text.")

    def test_draft_stays_in_scratch(self):
        self.assertTrue((SCRATCH / "draft.txt").is_file(), "Expected draft.txt inside work/projects/scratch/.")

    def test_junk_file_was_deleted(self):
        self.assertTrue(SCRATCH.is_dir(), "Expected a folder work/projects/scratch/ first.")
        leftovers = [str(p.relative_to(WORK)) for p in WORK.rglob("junk.txt")]
        self.assertEqual(leftovers, [], f"junk.txt should be deleted with rm, but found: {leftovers}")


class CommandsFile(unittest.TestCase):
    def setUp(self):
        path = WORK / "commands.txt"
        self.assertTrue(path.is_file(), "Expected work/commands.txt.")
        self.text = read_text(path)

    def test_commands_lists_the_commands_you_used(self):
        missing = [cmd for cmd in ("pwd", "ls", "cd", "mkdir", "cat", "mv", "rm")
                   if not re.search(rf"(?<![\w-]){cmd}(?![\w-])", self.text, re.IGNORECASE)]
        self.assertEqual(missing, [], f"commands.txt should list the commands you ran; missing: {', '.join(missing)}")
        self.assertRegex(self.text, r"cd\s+\.\.", "commands.txt should show that you used 'cd ..' at least once.")

    def test_commands_shows_absolute_path_of_work(self):
        self.assertRegex(self.text, re.compile(ABSOLUTE + r"[^\n]*[\\/]work\b", re.MULTILINE),
                         "commands.txt should contain the absolute path that pwd printed in work/ "
                         "(something like /c/Users/you/.../work).")

    def test_commands_labels_an_absolute_and_a_relative_path(self):
        lower = self.text.lower()
        self.assertIn("absolute", lower, "commands.txt should label at least one path as 'absolute'.")
        self.assertIn("relative", lower, "commands.txt should label at least one path as 'relative'.")
        self.assertIn("..", self.text, "One of your relative paths should use '..'.")


if __name__ == "__main__":
    unittest.main()
