import re
import sys
import unittest

from lessonkit import WORK

TOOLS = ["Python", "Git", "VS Code", "Claude Code"]
SHAPE = "Tool: ... / Purpose: ... / Version: ..."


def read_card():
    path = WORK / "tools.txt"
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8", errors="replace")


def which_tool(name):
    name = name.lower()
    if "claude" in name:
        return "Claude Code"
    if "python" in name:
        return "Python"
    if "git" in name:
        return "Git"
    if "code" in name or "vs" in name or "visual" in name:
        return "VS Code"
    return None


def blocks():
    """Split tools.txt into {tool: {"purpose": str, "version": str}} using the Tool:/Purpose:/Version: lines."""
    found = {}
    current = None
    for line in (read_card() or "").splitlines():
        m = re.match(r"\s*(tool|purpose|version)\s*:\s*(.*)$", line, re.IGNORECASE)
        if not m:
            continue
        label, value = m.group(1).lower(), m.group(2).strip()
        if label == "tool":
            current = which_tool(value)
            if current:
                found.setdefault(current, {"purpose": "", "version": ""})
        elif current:
            found[current][label] = value
    return found


class TestToolCard(unittest.TestCase):
    def test_tools_txt_exists_in_work(self):
        self.assertIsNotNone(read_card(), "Expected a file called tools.txt in your work/ folder.")

    def test_has_a_block_for_each_of_the_four_tools(self):
        found = blocks()
        missing = [t for t in TOOLS if t not in found]
        self.assertEqual(missing, [], f"No 'Tool:' line found for: {', '.join(missing)}. Each block starts "
                                      f"with a line like 'Tool: Python' ({SHAPE}).")

    def test_every_tool_has_a_purpose_sentence(self):
        found = blocks()
        problems = []
        for tool in TOOLS:
            purpose = found.get(tool, {}).get("purpose", "")
            if len(purpose.split()) < 5:
                problems.append(f"{tool}: {purpose!r}")
        self.assertEqual(problems, [], "Each 'Purpose:' line should be a sentence of at least 5 words saying what "
                                       "the tool is for. Too short or missing for: " + "; ".join(problems))

    def test_every_tool_has_a_version_number(self):
        found = blocks()
        problems = []
        for tool in TOOLS:
            version = found.get(tool, {}).get("version", "")
            if not re.search(r"\d+\.\d+", version):
                problems.append(f"{tool}: {version!r}")
        self.assertEqual(problems, [], "Each 'Version:' line should contain the version number your terminal "
                                       "printed (like 1.2.3). Missing for: " + "; ".join(problems))

    def test_python_version_is_copied_as_the_terminal_prints_it(self):
        version = blocks().get("Python", {}).get("version", "")
        self.assertRegex(version, re.compile(r"python\s+3\.\d+\.\d+", re.IGNORECASE),
                         f"Expected the Python version line exactly as 'python --version' prints it, "
                         f"like 'Python 3.12.4'. Got: {version!r}")

    def test_python_version_matches_this_computer(self):
        version = blocks().get("Python", {}).get("version", "")
        expected = f"{sys.version_info.major}.{sys.version_info.minor}"
        m = re.search(r"3\.(\d+)", version)
        got = m.group(0) if m else None
        self.assertEqual(got, expected, f"The Python on this computer is {expected}.x, but tools.txt says "
                                        f"{version!r}. Copy the version from your own terminal.")

    def test_git_version_is_copied_as_the_terminal_prints_it(self):
        version = blocks().get("Git", {}).get("version", "")
        self.assertRegex(version, re.compile(r"git\s+version\s+\d+\.\d+", re.IGNORECASE),
                         f"Expected the Git version line exactly as 'git --version' prints it, "
                         f"like 'git version 2.47.0.windows.1'. Got: {version!r}")

    def test_ends_with_a_workflow_line(self):
        text = read_card() or ""
        m = re.search(r"^\s*workflow\s*:\s*(.*)$", text, re.IGNORECASE | re.MULTILINE)
        self.assertIsNotNone(m, "Expected a line starting with 'Workflow:' that says how the four tools work together.")
        self.assertGreaterEqual(len(m.group(1).split()), 8,
                                "The 'Workflow:' line should be a sentence or two (at least 8 words) about how "
                                "you use the tools together in a lesson.")


if __name__ == "__main__":
    unittest.main()
