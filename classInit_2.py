#!/usr/bin/python3.8

import datetime


class User:
    """A member of Facebook. For now we are
    only storing their name and birthday. But soon
    we will store an uncomfortable amout of user
    information. (This piece of text is called a
    docstring.  When you call the 'help(User)' fn,
    it will display this information for you.)"""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyymmdd format
        # Note: self. objects store the data
        # the otherside  give the values
        # so to access the data, you have to reference
        # the self. objects.  (self.birthday, not 'birthday')

        # Extract first and last names
        first_last = full_name.split(" ")
        self.first_name = first_last[0]
        self.last_name = first_last[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2021, 1, 18)
        # remember to import datetime module
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        # Don't understand this dob bit...
        # because datetime.date = today???
        # Answer: datetime.date here has the args
        # yyyy, mm, dd which are specified above.
        # So it works fine!
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("George Harrison", "19830419")
print(User("George Harrison", "19830419"))
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())

#help(User) prints out a man page about (User) fn.
