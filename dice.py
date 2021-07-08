list = [3,4,2,6,7,8,3,2,7,10]

# You can save this function to a 'utils' library and then import it for other programs.  (there is already a 'max' fn that exists within python normal libraries but this is just an idea of what's possible).

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

big = find_max(list)
print(big)

import random

for i in range(3):
    print(random.random())
    print(random.randint(10,20))

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

a = Dice()
print(a.roll())


