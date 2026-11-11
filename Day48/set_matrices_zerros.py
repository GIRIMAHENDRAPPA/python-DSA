def setZeroes(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    
    zero_rows=set()
    zero_cols=set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j]=0
                
    return matrix

print(setZeroes([
    [1,1,1],
    [1,0,1],
    [1,1,1]
]))            