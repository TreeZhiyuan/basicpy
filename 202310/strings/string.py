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

a = "we are slaves, but we fight for freedom"
# Converts the first character to upper case
print(a.capitalize())
# Converts the first character of each word to upper case
print(a.title())

print(a.upper())

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end=' ')

print()

a, b = 5, 10
print(f'{a} * {b} = {a * b}')

str1 = 'hello, world!'
if "hello" in str1:
    print("yes")
else:
    print("no")
