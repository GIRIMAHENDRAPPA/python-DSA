arr = [1,2,3,4,5]
print(arr[2]) 

arr.append(6)
arr.insert(0, 0)
print(arr)  # Output: [1, 2, 3, 4, 5, 6]

print(arr[::-1]) # Output: [6, 5, 4, 3, 2, 1] - reversed array

rows, cols = 3, 3
matrix = [[0] * cols for _ in range(rows)]
print(matrix)  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in matrix:
    for x in row:
        print(x)  # Output: 0, 0, 0, 0, 0, 0, 0, 0, 0
    

