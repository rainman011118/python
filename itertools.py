from itertools import product

a = [1,2]
b = [3,4]
c = [5,6,7]
d = [1,2,3,4]
prod = product(a,b)
print(list(prod))
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations ######## all variations of values ###############
perm = permutations(c)
print(list(perm))

from itertools import combinations ######### all 2 digit combinations ###############
comb = combinations(d, 2)
print(list(comb))

from itertools import accumulate ########### adds prev digits and sum = next in seq. #############
acc = accumulate(d)
print(d)
print(list(acc))
import operator
acc = accumulate(d, func=operator.mul)
print(list(acc))

from itertools import groupby

def smaller_than_3(x):
    return x < 3
e = [1,2,3,4]
group_obj = groupby(e, key=smaller_than_3) # Groups all values smaller than 3 ###################
for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat

f = [7,8,9]
for i in count(10): ########## prints an infinite loop, starting at 10 ############
    print(i)
    if i == 115:
        break
#for i in cycle(f): ########## prints an infinite loop of the target ##############
#    print(i)

for i in repeat(1, 10): ########## prints an infinite loop (2nd arg is how many times repeated) ############
    print(i)
