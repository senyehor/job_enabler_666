# L0011 Task: The cinema ticket machine

The small cinema in your town is replacing its grumpy ticket clerk with a machine, and you've been asked to write the program inside it. The clerk kept all the price rules in his head: little kids get in free, children and seniors pay less, and young students get a discount, but only if they really are students. The machine has to ask two questions and then decide on its own which rule applies. It also has to cope with the customer who types a nonsense age, because someone always will.

## What to write

Write one file: `work/ticket_price.py`. The starter already has a one-line comment at the top.

## The price rules

| Who                                    | Category | Price |
|----------------------------------------|----------|-------|
| age 0 to 5                             | free     | 0     |
| age 6 to 17                            | child    | 5     |
| age 18 to 25 **and** a student         | student  | 8     |
| age 18 to 64 (everyone else)           | adult    | 12    |
| age 65 or older                        | senior   | 6     |

Watch the edges: 6 is already a child, 18 is no longer a child, 25 still gets the student price, 26 doesn't, and 65 is a senior. A student aged 30 pays the adult price, and a 15-year-old student pays the child price.

## Requirements

1. Ask for the age with `input()` and convert it to an `int`. Then ask `Are you a student (y/n)? ` with a second `input()`. Always ask both questions, in this order.
2. Treat both `y` and `Y` as "yes, I'm a student". Anything else means "no". Use `or` for this.
3. If the age is negative, print a line containing `Invalid age` and **don't** print a category or a price. Use `if`/`else` for this, nothing else.
4. Otherwise, choose the category and price with one `if`/`elif`/`else` chain that follows the table above.
5. In the 18-64 branch, decide between `student` and `adult` with an `if`/`else` **nested inside** that branch. The student test must combine the age limit and the student answer with `and`.
6. Print two lines at the end, in exactly this shape:
   ```
   Category: <category>
   Price: <price>
   ```
   The price is a whole number of euros, for example `Price: 12`.

## Example runs

From inside `work/`:

```
$ python ticket_price.py
How old are you? 21
Are you a student (y/n)? Y
Category: student
Price: 8
```

```
$ python ticket_price.py
How old are you? 30
Are you a student (y/n)? y
Category: adult
Price: 12
```

```
$ python ticket_price.py
How old are you? 6
Are you a student (y/n)? n
Category: child
Price: 5
```

```
$ python ticket_price.py
How old are you? -4
Are you a student (y/n)? n
Invalid age
```

Your prompt text can be a little different, but the `Category:` and `Price:` lines must look like the ones above.

Before you run the tests, predict the answer and then try these yourself: `5 n`, `17 y`, `18 y`, `25 y`, `26 y`, `64 n`, `65 y`.

## Run and test

- Run it: open the terminal, `cd` into `work/`, then run `python ticket_price.py`.
- Test it: from the repo root, run `python tools/learn.py test`.

## Stretch goal (optional)

Tuesday is cheap day: every ticket that costs more than 0 gets 2 euros off. Do this in a copy, `work/ticket_price_tuesday.py`, because the tests only send two answers and a third `input()` would crash there. Add a third question, `Is it Tuesday (y/n)? `, and apply the discount after your chain with one more `if` that uses `not` (for example `if is_tuesday and not price == 0:`).
