#!/usr/bin/python3.8

# Simple Class example
# does not have the __init__ method.
class Person:

    age = 37
    height = 181
    weight = 78

    def greet(self):
        print("Hello")


print(Person.age)
print(Person.height)
print(Person.weight)
print(Person)  # Prints what the object is: Class.
print(Person.greet)  # Prints what the object is: method of class

harry = Person()  # An object of the class.
print(harry.greet)  # prints 'Class calls the method'
harry.greet()  # Calling the method = prints "Hello"
