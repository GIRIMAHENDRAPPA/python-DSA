#move_zeros
def move_zeros(arr):
    result=[]
    zero_count=0
    
    for x in arr:
        if x !=0:
            result.append(x)
        else:
            zero_count+=1
    result.extend([0]*zero_count)
    return result
print(move_zeros([1,0,2,0,3]))

#remove_duplicates
def remove_duplicates(arr):
    if not arr:
        return []
    result=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i] !=arr[i-1]:
            result.append(arr[i])
    return result

print(remove_duplicates([1,1,2,2,3,3,4]))