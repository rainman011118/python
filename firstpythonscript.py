#!/usr/bin/python3.8

list = ["apple", "banana", "orange", "lemon", "cherry"]
print(list)

# sleep 1  This will not work in python because they are shell scripts.
# echo "sleeping for 1 second"
print("Sorting the list")
list.sort()
print(list)

print("Appending to the list")
list.append("kiwi")
print(list)

print("Going through the indexes with a for loop")
total = 0
for i in list:
    total += 1
    print(total, i)

message = "Use triple quotes if you want to print text over multiple lines as below..."
print(message)

message2 = """The main characters were:
Bugs Bunny
Yosemite Sam
Tom and Jerry
Sylvester and Tweety."""
print(message2)

print(len(message2))
print(message2.count("y"))

new_message2 = message2.replace("Tom and Jerry", "Road-runner and Coyote")
print(new_message2 + "\n")
print(message2)

print("\nI'm am trying this bit out on powershell. Let's see if it works ok.")
football = ["Man utd", "Arsenal", "Liverpool", "Man City", "Chelsea"]
print(football)

football.insert(2, "Burnley")
print(football)
print(len(football))

i = 1
for team in football:
    print(i, team)
    i += 1
print("It worked perfectly! woohooo!!")

print(
    """Notepad is pretty straightforward and handy to use for scripting.
Compared to vim which requires special training.........NOT ANYMORE!  VIM IS THE BEST!  HANDS DOWN, NO ARGUMENTS....THE BEST."""
)
