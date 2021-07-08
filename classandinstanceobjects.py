#!/usr/bin/python3.8

class Tweet:
    pass


a = Tweet()

a.message = "Tweet is the class.  a now equals tweet simply to make it easier to type.  So a.message is the same as Tweet.message but to call the function we call a.message"
print(a.message)

b = Tweet()
c = Tweet()

b.message = "b and c are simply other instance objects like a, which can be called as many times as they are needed."
print(b.message)
