def add(x, y):
    return x+y

a = add(43,77)
print(a)


def loop(x):
    for i in x:
        print(i)

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
loop(x)

print(x[::-1])


class wow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_age(self, x, y):
        print(f"I am {x} and I am {y}")

a = wow(38, 18)
print(a.x)
print(a.y)
a.print_age(21, 44)


