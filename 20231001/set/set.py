# True and 1 is considered the same value, but not 2 and others
thisset = {"apple", "banana", "cherry", True, 1, 2}
thisset.add("apple")
print(thisset)
print(bool(2))

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# add elements of a list to at set
thisset = {"apple", "banana", "cherry"}
mylist = ["apple", "kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# The union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# get intersection of two set with intersection_update,
# The intersection_update() method will keep only the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
# Keep the items that are not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method will return a new set
# that contains only the elements that are NOT present in both sets
# Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
