matrix = [
        [1,2,3],
        [1,2,3],
        [1,2,3]
]

print(matrix)
for row in matrix:
    print(row)
    for item in row:
        print(item)

#A method to remove duplicates from a list
numbers = [2,3,5,5,6,6,2,8,7,0]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
