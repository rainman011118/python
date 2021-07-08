#!/usr/bin/python3.8

# Watch the video python classes by socratica
class User:
    pass


user1 = User()
# user1 is an Instance of the class aka object.
user1.first_name = "Bob"
user1.last_name = "Marley"
# .first_name and .last_name are called fields
# they contain data specific to the object user1

print(user1.first_name)
print(user1.last_name)

# Below is an example of separate variables that
# are not attached to class objects
first_name = "Marie"
last_name = "Kelley"
print(first_name, last_name)

print(user1.first_name, user1.last_name)

user2 = User()
user2.first_name = "Michael"
user2.last_name = "Jackson"

print(first_name, last_name)
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)

user1.age = 27
user2.favorite_book = "Game of Thrones"

print(user1.age)
print(user2.age)  # .age for user2 has not been assigned
# therefore Attribute error pops up.
