class Person:
    # All classes have a function called __init__(), which is always executed when the class is being initiated.
    # Use the __init__() function to assign values to object properties,
    # or other operations that are necessary to do when the object is being created
    # The __init__() function is called automatically every time the class is being used to create a new object
    def __init__(self, name, age):
        # The self parameter is a reference to the current instance of the class,
        # and is used to access variables that belong to the class
        # It does not have to be named self , you can call it whatever you like,
        # but it has to be the first parameter of any function in the class
        self.name = name
        self.age = age

    # The __str__() function controls what should be returned when the class object is represented as a string.
    # If the __str__() function is not set, the string representation of the object is returned
    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)
