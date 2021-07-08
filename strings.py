######################## Sets - Notice the curly braces  #################
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

inter = odds.intersection(evens)
print(inter) # This will show: 'set()' since the numbers are not shared between either set.

inter = odds.intersection(primes)
print(inter) # This will show something since numbers: '3,5,7' are shared.

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

setA.update(setB)
print(setA)

setA.difference_update(setB)
print(setA)

setC = {7,6,5,4}
# setD = setC ####This changes both sets. (Similar to pass by reference)
# setD = setC.copy() #### Copy
setD = set(setC) #### Copy
setC.add(2)
print(setC)
print(setD)

######## Strings #######################
my_string = 'Hello World'
char = my_string[0]
print(char)
substring = my_string[1:5]
print(substring)
########## Reverse string ##################
reverse_string = my_string[::-1]
print(reverse_string)
######### Every 2nd letter ####################
every_two_string = my_string[::2]

mystring = 'Hello World!'
print(mystring.replace('World', 'Universe'))
print(mystring)

newstring = 'The quick brown fox jumped over the lazy dog!'
print(newstring)
list_of_string = newstring.split()
print(list_of_string)

# To join a list together ###################
rejoin_list = ' '.join(list_of_string)# If you put a space between ' ', it reverts the list accordingly.
print(rejoin_list)

print(every_two_string)

############# how to remove the '\n' when printing out a list ###################
arr = []
for i in range(10):
    arr.append(i)
print(arr)
for elem in arr:
    print(elem, end='') ##### This 'end=''' means end each elem with 'blank' rather than '\n'
print('')
