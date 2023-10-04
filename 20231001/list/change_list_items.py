thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values
# and refer to the range of index numbers where you want to insert the new values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[1:3])
thislist[1:3] = ["blackcurrant"]
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly
thislist[1:2] = ["gooo", "watermelon"]
print(thislist)

thislist.insert(len(thislist), "goodby")
print(thislist)

# To add an item to the end of the list, use the append() method
thislist.append("appended")
print(thislist)

# To append elements from another list to the current list, use the extend() method.
# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thistuple = ("kiwi", "orange")
thislist.extend(tropical)
print(thislist)

thislist.extend(thistuple)
print(thislist)

dikt = {"a": "b", "v": "m"}
thislist.extend(dikt)
print(thislist)

print("'orange' in thislist", "orange" in thislist)
thislist.remove("orange")
print("'orange' in thislist", "orange" in thislist)

print(thislist)
thislist.pop()
print(thislist)

alist = ["apple", "banana", "cherry"]
del alist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# newlist = [expression for item in iterable if condition == True], The condition is optional and can be omitted
print(thislist)
newlist = [x for x in thislist if x != "apple"]
print(newlist)
newlist = [x.upper() for x in thislist]
print(newlist)
