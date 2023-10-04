# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon to return a part of the string.
print("===================== Slicing ====================")
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included)
print(b[:5])

# By leaving out the end index, the range will go to the end
print(b[2:])
print(b[2:len(b)])

# Use negative indexes to start the slice from the end of the string
print(b[-100:-2])
print(b[:-2])
