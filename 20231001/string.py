# starting with string
print()
print('Hello world' == "Hello world")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

ab = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a == ab)
print(ab)

a = "Hello, World!"
print(a, "length is ", len(a))
for item in a:
    print(item)

print()
txt = "The best things in life are free!"
print("free is present: ", "free" in txt)
print("expensive not in txt: ", 'expensive' not in txt)
if "free" in txt:
    print("Yes, 'free' is present.")

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon
# to return a part of the string.
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
