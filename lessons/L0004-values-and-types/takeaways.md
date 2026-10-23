# L0004 Values and types

- I learned 4 types of value: int - round numbers, str - text, float - numbers with the dot, bool - True and False.
- I learned how converting works: bool checks if there is anything, if 0 or "" then False, if anything then True; str("10") is 10 but text, int("10") is 10 as a number; float(10.0) will be 10.0 but int(10.0) will be just 10.
- I can't do int("3.5"), that causes a ValueError: int can't handle numbers with a dot in quotes.
- I tripped on `# predict: "hello" <class 'str'>` and `# predict: "10" <class 'str'>` because I forgot that quotes don't print for a str. I also tripped on print(float("1e3")) because I saw that way of writing numbers for the first time.
- Next time I will triple check my predictions before writing them, to avoid mistakes.

## Tutor notes
- Check Q1: first said int(7.0) raises ValueError (mixed up float vs text); fixed after re-explaining, and Part 2 predictions were all right. Check Q3: first "fix" was int(4) (changed the data); with one hint found int(float("4.5")) himself.
- Predicted print shows a str's quotes (review minor, corrected). Explain-back: said int("10") *causes* the form bug; corrected (it's the fix). Takeaways: first said int("3.5") fails "because of the quotes"; fixed it himself. Recheck "print drops quotes" and str-vs-int in the next lessons that use input() or string concatenation.
- Lesson ran ~107 min vs 65 estimated; asked for simpler breakdowns early ("break it down easier"), so keep explanations in small steps.
