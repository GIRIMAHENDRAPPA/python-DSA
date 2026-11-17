#left_array_by_1
def left_array_by_1(arr):
    first=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=first
    return arr
print(left_array_by_1([1,2,3]))

#left_rotate_by_d
def left_rotate_by_d(arr,d):
    d=d%len(arr)
    
    for i in range(d):
        first=arr.pop(0)
        arr.append(first)
    return arr
print(left_rotate_by_d([1,2,3,4,5],2))
        