# Make sure the number of variables matches the number of values
# or else you will get an error.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print()

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.
print("------ Unpack a Collection ------")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print()
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x, y, z, sep="->")

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


def myfunc2():
    global x
    x = "fantastic"
    print("Python is " + x)


myfunc2()
print("Python is " + x)