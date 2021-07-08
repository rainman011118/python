# collections module: counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaaaabbbbbccccc"
my_counter = Counter(a)
print(my_counter) # How many of each item
print(my_counter.keys()) # All the keys
print(my_counter.values()) # All the values for each element(how many times of each)
print(my_counter.most_common(2)) # most common element(1). 2 most common elements(2)
print(list(my_counter.elements()))

from collections import namedtuple

# This is like a structure #################################
Point = namedtuple('Point', 'x, y')
p = Point(1,-4) # This is similar to a pointer in C ..................
print(p)
print(p.x, p.y)

from collections import OrderedDict

od = OrderedDict()
# The following is printed in the order it is written here #########################
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(od)

from collections import defaultdict

dd = defaultdict(int)
dd['a'] = 1
dd['b'] = 2
print(dd)
print(dd['a'])
print(dd['b'])
print(dd['c']) # Not present therefore returns default 0

from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft(4)
print(d)
d.extend([5,6,7]) # Note: the [] brackets inside.  It will not work without these.
print(d)
d.rotate(1) # Like a conveyor belt start-end. Can rotate 1,2,3 etc.... and also backwards with -1
print(d)
d.rotate(-1)
print(d)
