############ Map function - maps a fn to the iterables provided ########################
def myfunc(n):
    return len(n)

x = map(myfunc, ('apple', 'banana', 'orange')) # Notice when func is used no '()' are needed.
print(x)
print(list(x))

def newfunc(a, b):
    return a + b

y = map(newfunc, ('apple', 'banana', 'orange'), ('pie', 'toffee', 'soda'))
print(list(y))

numbers = [-5, -3, 6, 2, -11, 3]
pos = map(abs, numbers)
print(list(pos))
############# map is commonly used with lambda fn ###############################
num = [2,4,5,6,7]
sq = map(lambda x: x ** 2, num)
print(list(sq))

############### Ceaser cipher example with map #########################
def rotate_char(c):
    rot_by = 3
    c = c.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #keep punctuation and white space
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    #if the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]): # If value <= 26
        return chr(rotated_pos)
    #if the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

#### ord() = built-in fn that gives the ASCII value (of the char)
#### chr() = built-in fn that gives char value (of the number)
print("".join(map(rotate_char, "This is my password1")))

