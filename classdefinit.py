#!/usr/bin/python3.8

class Tweet:
    def __init__(self):
        print(
            "Remember the space between def and __ . self must be included otherwise a typeError occurs."
        )


a = Tweet()
print(a)
class Tweeter:
    def __init__(self, message):
        self.x = message

t = Tweeter(
    "t is the instance object of class Tweeter.  This text is the argument that is passed"
)

t2 = Tweeter("This is a second instance object of the class Tweeter.")
print(t.x)
print(t2.x)


class Tweeting:
    def __init__(self, message):
        self.message = message

    def print_tweeting(self):
        print(self.message)


tt = Tweeting(
    "This is me calling the print_tweeting func. of the class Tweeting, which is programmed to print the init func. which is the message passed in tt instance."
)

tt.print_tweeting()
