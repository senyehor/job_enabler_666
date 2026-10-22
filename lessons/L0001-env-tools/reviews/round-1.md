# Review round 1: approved

Tests: 8 passed, 0 failed

## What's good
- Your Python `Purpose:` line (line 2) is right: Python is the interpreter that reads and runs the code. That's the exact point that was shaky in the check questions. The terminal is only where you type the command. The program doing the work is `python`. Your card says it the right way round.
- All the versions are your own real output, copied in full (`Python 3.14.9`, `git version 2.53.0.windows.1`). Your "Inside Python" stretch line also gets the `>>>` vs `$` difference right: `git --version` fails at `>>>` because it isn't Python code.

## Issues
### 1. The Workflow line leaves out the "run" step (minor)
`work/tools.txt:19`: your Workflow says you edit in VS Code, Git saves snapshots, and Claude points out mistakes. But where does your code actually get *run*? "The code that I write with Python" describes the language you write in. It doesn't say which tool carries the code out. Your Python `Purpose:` line already knows the answer.
Hint (level 1): Read line 2 and line 19 side by side. After you finish editing a file in VS Code, which of the four tools do you call next, and what does it do with the file?

## For next time
- Nothing to add. Everything else on the card reads clearly.

## Explain back
In your own words: what's the difference between typing `python --version` and typing just `python` in Git Bash? What happens after each one, which prompt do you end up at, and how do you get back? This matters because from L0003 on you'll run `python main.py` all the time. You need to know that `python` is the program doing the work and Git Bash is just the place you type the command.
