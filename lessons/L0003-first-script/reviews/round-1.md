# Review round 1: approved

Tests: 8 passed, 0 failed

## What's good
- `broken.py` is fixed properly. You corrected `prnt` and closed the quote instead of deleting lines, kept the starter comment on line 1, and the script prints all six lines in the right order. Since you kept the layout exactly as given, the line numbers in your comments (7 and 5) match the file.
- Your error comments copy the real messages Python printed (`unterminated string literal`, `name 'prnt' is not defined. Did you mean: 'print'?`). Copying the actual message is a good habit. It shows you read the whole last line of the traceback, not just the error name.

## Issues
### 1. The bottom border of the box is shorter than the top (minor)
`work/hello.py:6`: run `python hello.py` and look at the box. The top border and the middle line are the same width, so the right edge of the top half is straight. Does the bottom border end in the same column? The task asks for "the same border again". What would you need to count to check that?
Hint (level 1): compare line 4 and line 6 of `hello.py` character by character.

### 2. Where did "line 5" for the NameError come from? (minor)
`work/broken.py:9`: your comment says `(detected at line 5)`. Python did print that phrase for the SyntaxError, but for the NameError it shows the line number somewhere else in the traceback. Can you find the exact line in the traceback where the "5" appeared? The number is right. The point is to know which part of the traceback it came from, so you can find it again next time.
Hint (level 1): in your second run's traceback, which line started with `File "...broken.py"`?

## For next time
- `work/hello.py:3`: the task's format is `My name is <your name>.`, with a full stop at the end. Yours has no full stop.
- `work/hello.py:5`: `| Python rocks!|` has no space before the closing `|`, but the example has one. That's fine as it is. Just make the borders match whatever width you choose.
- No `oops.py` this time. The stretch is optional, but it's a cheap way to meet a new error name (for example `IndentationError`).

## Explain back
On your first run of `broken.py` nothing printed at all. On the second run, four lines printed before it crashed. Explain in your own words why. Which error stops Python before it runs anything, and which one only happens when Python reaches that line? This matters because the lines that print before a crash tell you a lot about what kind of bug you're facing.
