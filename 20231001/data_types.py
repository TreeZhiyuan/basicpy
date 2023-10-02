# Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Getting the Data Type
# You can get the data type of any object by using the type() function:

x = "s"
y = 5
print(type(x), type(y))

print(10 // 3, 10 % 3)
print(-10 // 3, -10 % 3)

# Return an object that produces a sequence of integers
# from start (inclusive) to stop (exclusive) by step.
x = range(2, 6, 2)

for n in x:
    print("range(2, 6, 2): ", n)

print()
llst = [1, 2, 3, "abc", 4.5]
for item in llst:
    print(item, type(item))

print()
y = {"name": "John", "age": 36}
x = dict(name="John", age=36)
print(x["name"], y.keys())
for key in y.keys():
    print("y[" + key + "]:", y[key])

print()
import random

print(random.randrange(1, 10))


