# 1D Array - single row
arr1 = [1, 2, 3, 4]

# 2D Array - matrix(rows x columns)
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
print(matrix[1][2])  # Output: 6 (element at row 1, column 2)

#how to create 2D array in zeros
rows, cols = 3, 3
matrix = [[0] * cols for _ in range(rows)]
print(matrix)  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]