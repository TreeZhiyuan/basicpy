thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
    "year": 1964
}
print(len(thisdict))
key = "brand"
print("thisdict[{}] is ".format(key), thisdict[key], ", thisdict.get({}) is ".format(key), thisdict.get(key))

# print all the keys in dict
for item in thisdict:
    print("value of thisdict[{}] is: ".format(item), thisdict[item])

# The list of the keys and values is a view of the dictionary, meaning that any changes done to the dictionary
# will be reflected in the values list.
k = thisdict.keys()
v = thisdict.values()
print("keys: ", k)
print("values: ", v)

for x, y in thisdict.items():
    print(x, y)

# add all dict values in another list
lst = [1, 2]
lst.extend(v)
print(lst)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict.items())
thisdict["year"] = 2020
print(thisdict.items())
thisdict.update({"year": 2023})
print(thisdict.items())
thisdict.pop("year")
print(thisdict.get("year"))
print(thisdict.items())
del thisdict["model"]
print(thisdict.items())

# empty all the items in dict
thisdict.clear()
print(thisdict.items())

# remove the dict object
del thisdict
