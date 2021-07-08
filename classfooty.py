#!/usr/bin/python3.8

# Let's create a class.
class Team:
    # Initialise with the 'init' method:
    # Always use self as the first argument.
    def __init__(self, name, table_position):
        self.name = name
        self.pos = table_position

    def print_me(self):
        print("Premier League")

# Create objects of the class: e.g I could make 20 objects for the 20 teams in the Premier League
a = Team("Manchester United", "1st")
b = Team("Arsenal", "3rd")
c = Team("Chelsea", "12th")

print(a.name, a.pos, "'Calling the object of the class'")
print(b.name, b.pos)
print(c.name, c.pos)

# Now to call other methods in the class.
# This seems to be the usefulness of classes.
a.print_me()  # Object calls the method 'print_me()
