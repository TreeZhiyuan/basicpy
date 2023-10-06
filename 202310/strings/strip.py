# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print()
print("testing with strip()")
a = "  Hello, World!    "
print("|", a.strip(), "|", sep="")
print("|", a.lstrip(), "|", sep="")
