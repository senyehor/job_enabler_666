# L0010 Review: variables, arithmetic, strings, I/O

- Today I recapped the previous lessons. After my break from studying, I needed that.
- Indexes are solid now, and `[::-1]` reverses a word.
- I tripped on the badge print. My first variant was `print(f'{name[0] + last_name[0]}, {name[:3]},  sep="-")`, which was a `SyntaxError`. Then I corrected myself to `print(name[0] + last_name[0], name[:3], sep="-")`.
- Next time: no more long breaks, and more self-checks.

## Tutor notes
- All 3 check questions right first try (trace with reassignment, `input()` TypeError, slicing). One precedence slip while teaching: `20 - 9 % 4 * 2` → 19 (did `*` before `%`); got the variant `3 * 10 // 4` right. Approved round 1, 0 majors; traces all correct.
- Explain-back skipped (he pasted an AI-generated answer, then declined to answer himself). His takeaway calls the badge mistake only a SyntaxError; I re-explained that one f-string is one value for `print`, so `sep` has nothing to separate. That's the same misconception as L0009, so keep checking it.
- He came back after a ~6-day break. The timer shows ~250 min, but most of that was time away. Watch for pasting in outside answers.
