tuple1 = ('a', 'p', 'p', 'l', 'e')
print(tuple1)
print(tuple1.count('p'))

my_list = list(tuple1)
print(my_list)

tuple2 = tuple(my_list)
print(tuple2)

#unpacking ##########
name_tuple = "Jonny", 37, "London"
a, b, c = name_tuple # Can be done directly also (without the need for 'name_tuple')
print(a, b, c)

#NOTE: the list will be larger in bytes compared to the tuple.
import sys
tuple3 = (0,1,2,"Jack", True)
list2 = [0,1,2, "Jack", True]
print(sys.getsizeof(tuple3), "bytes")
print(sys.getsizeof(list2), "bytes")


