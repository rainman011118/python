from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a postive integer")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(100):
    print(n, ": ", fibonacci(n))

#If you try to find a large number of fibonacci sequences (eg anything >30), the whole process will slow down considerably.  Therefore use the import lru_cache.
