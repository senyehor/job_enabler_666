# Review round 1: approved

Tests: 8 passed, 0 failed

## What's good
- Your traces are right on every line, not just the `final:` lines. In Script A, line 3 still says `y = 5`, so you know `y = x` copies the value at that moment and doesn't link the two names. In Script C, line 2 drops the quotes (`count = 3`), which shows you saw the type change from text to number.
- `profile.py` does what the task asks, step by step. `"29"` and `"1.68"` each appear only once. You store the converted values back (`age = int(age)`). The birthday is `age = age + 1` and the second profile prints the same variables again. The output matches the task exactly.

You also did every task step, including step 2: `check.py` has all three scripts, and its output (`10 5`, `blue blue`, `4 level4`) matches your `final:` lines.

## Issues
### 1. The Script B sentence says what happens, but not why (minor)
`work/trace.txt:23`: you write that the colours don't swap "because in line 3 both values became the same." That's true, but it's the result. The task asks why line 4 can't fix it. Your trace already holds the answer.
Hint (level 1): look at your `line 3:` row for Script B. Which variable held `"red"` just before that line, and does any variable hold `"red"` right after it? So what can `b = a` on line 4 copy?

## For next time
- `work/trace.txt:23`: step 3 asks for one sentence; you wrote two. Also "Colors doesn't" should be "The colours don't".
- `work/profile.py`: you mix `'single'` and `"double"` quotes. Both work, but pick one and use it everywhere.
- `work/profile.py:3`: there's a stray space at the end of the line.

## Explain back
Point at `age = age + 1` on line 15 of `profile.py`. In your own words, say what Python does on that line, step by step. Which side runs first? What is `age` before the line, and what is it after? Then use the same idea to explain why `a = b` on line 3 of Script B makes `"red"` disappear for good. This is the most important idea in the lesson: the right side is worked out first, then the result replaces whatever the left-side variable held before.
