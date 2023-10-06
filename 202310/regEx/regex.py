import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

