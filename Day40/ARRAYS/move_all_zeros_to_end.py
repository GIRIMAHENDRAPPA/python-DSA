def move_zeros_to_end(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    return arr
arr=[1,2,0,0,4,0]
print(move_zeros_to_end(arr))
    