# L0004: print values and their types, then convert between types

# predict: 10 <class 'int'>
print(10, type(10))
# predict: -7 <class 'int'>
print(-7, type(-7))
# predict: 3.14 <class 'float'>
print(3.14, type(3.14))
# predict: 2.0 <class 'float'>
print(2.0, type(2.0))
# predict: "hello" <class 'str'> WRONG: it printed hello <class 'str'> because quotes does not print.
print("hello", type("hello"))
# predict: "10" <class 'str'> WRONG: it printed 10 <class 'str'> because quotes does not print.
print("10", type("10"))
# predict: True <class 'bool'>
print(True, type(True))

# predict: 42 <class 'int'>
print(int("42"), type(int("42")))
# predict: 3.5 <class 'float'>
print(float("3.5"), type(float("3.5")))
# predict: 7 <class 'str'>
print(str(7), type(str(7)))
# predict: 3 <class 'int'>
print(int(3.9), type(int(3.9)))
# predict: 5.0 <class 'float'>
print(float(5), type(float(5)))
# predict: False <class 'bool'>
print(bool(0), type(bool(0)))
# predict: True <class 'bool'>
print(bool("hi"), type(bool("hi")))

# ValueError: invalid literal for int() with base 10: 'abc'. ValueError occurs when trying to convert a non-numeric string to an integer. Right way for print to work would be putting str insted of int. Then result will be: abc
# print(int("abc"))

# predict: True
print(bool("False"))
# predict: 8
print(int("  8  "))
# predict: ValueError WRONG: it printed 1000.0 and I dont kow why.
print(float("1e3"))