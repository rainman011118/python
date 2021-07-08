import random
print(dir(random))

print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.random())
print(random.random())
print(random.random())

arr = []
for i in range(10):
    r = random.randint(1,100)
    arr.append(r)
print(arr)
print('max = ', max(arr))
print('min = ', min(arr))
for e in arr:
    print(e, end=',')
first = "Jack"
last = "Sparrow"
print("{} {}".format(first, last))
print(f'{first} {last}')


