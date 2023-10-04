# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a
# reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict1 = thisdict.copy()
mydict1["tommy"] = "Gina"
print(mydict1, thisdict, sep="\n")

mydict2 = dict(thisdict)
mydict2["festival"] = "spring"
print(mydict2, thisdict, sep="\n")
