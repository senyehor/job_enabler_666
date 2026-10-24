# L0006 Part 2: store facts about a user in variables, reassign some, print them
name = 'Mara Lind'
age = '29' 
height = "1.68"
is_student = True
age = int(age)
height = float(height)
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
print("age is", type(age))
print("height is", type(height))
print('--- after the birthday ---')
age = age + 1
is_student = False
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)