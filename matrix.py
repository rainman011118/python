import numpy as np

a = int(input("Enter the no. rows: "))
b = int(input("Enter the no. cols: "))
print("Enter the no. in a single line separated by space: ")
val = list(map(int, input().split()))
matrix = np.array(val).reshape(a,b)
print(matrix)


