# List items can be of any data type
thislist = ["apple", "apple", "banana", "cherry"]
print(len(thislist))

thislist.append(23)
thislist.append(True)
print(thislist)

# There are four collection data types in the Python programming language:
# 1, List is a collection which is ordered and changeable. Allows duplicate members.
# 2, Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3, Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# 4, Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# returns ['cherry', 23]
print(thislist[3:-1])

# returns []
print(thislist[13:-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

if "apple1" in thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)