import sys

x = 10
y = 55
print(x+y)

list = [1,3,5,7,7,22,42,98]
print(list)

for i in list:
    print(i)

def mul(x,y):
    return x*y

z = mul(12,5)
print("12 x 5 = {}".format(z))
print(f"12 x 5 = {z}")