#find_single
def find_single(arr):
    result=0
    for num in arr:
        result=result ^ num
    return result
print(find_single([1,2,3,2,1,3,4]))



#union of two sorted arrays
def union_sorted(arr1, arr2):
    i=j=0
    result=[]
    while i < len(arr1) and j < len(arr2):
        if i > 0 and arr1[i]==arr1[i-1]:
            i+=1
            continue
        if j > 0 and arr2[j]==arr2[j-1]:
            j+=1
            continue
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        if arr2[j] < arr1[i]:
            result.append(arr2[j])
            j+=1
        else:
            result.append(arr1[i])
            i+=1
            j+=1
            
    while i < len(arr1):
        if not result or arr1[i]==result[-1]:
            result.append(arr[i])
        i+=1
        
             
    while j < len(arr2):
        if not result or arr2[j]==result[-1]:
            result.append(arr[j])
        j+=1
    return result

print(union_sorted([1,2,3,4,5,6],[2,3,4,5,6]))