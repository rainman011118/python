import itertools
import sys
print(sys.version)
print(sys.version_info)

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

"""fname = input('Enter your full name: ')
rev = fname[::-2]# The number prints every 'n' index. (so 2 = every 2nd digit)(-2 = every 2nd in reverse).
print(rev)
print(len(fname))
len = len(fname) """

numbers = [4,2,2,2,2,6,42,62,3,3,3,3,88,32,21,3,20]
print(numbers)
x = numbers.copy()
x.sort()
print(x)

total = 0
for num in numbers:
    total += num
print("Sum of numbers = ", total)
print(dir(list))
print(numbers.count(3))
print('len = ', len(numbers))

########### Counter #########################################
from collections import Counter
d = Counter(numbers)
print(d)
str = 'The World is not enough!'
print(Counter(str))


