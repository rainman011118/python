# lambda is used to create a function.  So below reads, the lambda of x = x + 10. It is identical to the def function. Lambda fn's can usually be written on 1 line.

add10 = lambda x: x + 10
print(add10(5))

################## def add10_fn(x):
##################    return x + 10)

mult = lambda x, y: x*y
print(mult(10,5))

########### INTERESTING WAY OF WRITING THIS ##################
a = [1,2,3,4,5]
b = [x*2 for x in a]
print(b)
########## lambda way (using 'map') #####################
c = map(lambda x: x*2, a)
print(list(c))

################ filter shows values according to fn. (map happened to show boolean result) ############
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#num = map(lambda x: x%2==0, numbers)
num = filter(lambda x: x%2==0, numbers)
print(list(num))
############## alternative way....#############
morenum = [x for x in numbers if x%2==0]
print(morenum)


