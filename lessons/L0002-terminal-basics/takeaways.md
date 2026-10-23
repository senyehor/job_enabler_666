# L0002 Moving around in the terminal

- I learned how to move with `cd`, check the absolute path of the folder I'm in with `pwd`, and check its content with `ls`.
- I learned how to create txt files with `echo "text" > file.txt` and print them with `cat`; to move or rename with `mv` and delete with `rm`.
- I tripped on relative paths a lot. I was not understanding what an upper folder or a lower folder is. Now I know that the disk, as an example, is up, and all the next folders are down, etc.
- Next time I will ask you to break something down in more detail if I'm stuck.

## Tutor notes
- Check Q1: first said `cd ../music` from `.../ann/school` lands in `/c/Users/ann` (treated `..` as two levels and dropped the last step). Fixed by reading paths step by step; then got `../Downloads/old` and `../../photos` right, and used `../notes` and `cd ../..` correctly in the task.
- Review minor: wrote the repo root as his step-1 `pwd` in commands.txt. In L0003 (cd into `work/`, `python hello.py`), have him run `pwd` before running anything, and recheck the L0001 point: `python` is the program, the file is its argument.
- Hit Permission denied on `/d/games` while experimenting; explained folder permissions and not to run as admin.
