# The format() method takes the passed arguments, formats them, and places them in the string where the
# placeholders {} are
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

price = 49.987
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are
# placed in the correct placeholders
# if you want to refer to the same value more than once, use the index number
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
