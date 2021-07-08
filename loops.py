#!/usr/bin/python3.8

print("Let's practice loops and loops!")
print(range(10))

for i in range(10):
    print(i)

letters = ["A", "B", "C", "D", "E"]
total = 1
for letter in letters:
    if total != 2 and total != 4:
        print("Gimme a ", letter)
        total += 1
    else:
        total += 1
        continue

names = ["Jack", "Jill", "Mufasa", "Clint", "Jolene"]
index = 0
for index, name in enumerate(names, start=1):
    print(index, name)

supnames = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Mavel", "DC"]

#Looks like 'zip' targets the indexes of each list and prints before moving to next indexes:
for name, hero, universe in zip(supnames, heroes, universes):
    print(f"{name} is actually {hero} from {universe}")

#prints all the contents of each list using the index orders( all 0's, all 1's etc)
for value in zip(supnames, heroes, universes):
    print(value)

#UNPACKING - each variable corresponds to an int.  However if there are more ints than variables OR more var than ints(not including the *c), then it errors. (You cannot have 2 '*' variables.)
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a)
print(b)
print(c)
print(d)
# If you replace a variable name with an underscore (_), the values it points to will be ignored.(the print statement to that variable must be commented out).


