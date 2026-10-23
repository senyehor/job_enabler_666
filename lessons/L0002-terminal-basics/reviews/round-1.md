# Review round 1: approved

Tests: 8 passed, 0 failed

## What's good
- `mv ideas.txt ../notes` from inside `scratch/` (`work/commands.txt:81`) is exactly right. `..` took you up one level to `projects/`, and then `notes` took you down into the folder next door. That's the trickiest idea in this lesson, and you used it correctly in a real command.
- `cd ../..` from `notes/` (`work/commands.txt:171`) put you back in `work/`, two levels up, which the next prompt confirms. You also checked your work as you went (`ls` after `mv` and `rm`, `cat` after each `echo`), which is a good habit to keep.

## Issues
### 1. The step 1 path on line 1 isn't what `pwd` printed (minor)
`work/commands.txt:1`: line 1 says the absolute path from step 1 was `/c/Users/ШАРП/job_enabler_666`. Now look at line 27, right after you ran `pwd` in step 1. Which folder did `pwd` actually print? The full transcript below is correct, so the tests passed. But the summary line gives a wrong fact, and that's the line someone would read first.
Hint (level 1): Compare line 1 with line 27. Which of the two is the folder you were in when you ran `pwd`, and which one is only where the terminal opened?

## For next time
- The labels at the bottom (lines 176-177) show whole commands. Next time, put just the path after the label (`relative: ../notes`) so it's clear which part is the path.
- You could also have listed `..` and `../..` as relative paths. You used both correctly.

## Explain back
Take `../notes` from line 81. In your own words, say which folder it pointed to and why it worked only because you were in `scratch/` at that moment. Then write the absolute version of the same folder. As a bonus, say what `../..` meant on line 171 and why it put you in `work/` and not somewhere else.
