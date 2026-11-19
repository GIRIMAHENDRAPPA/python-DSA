#two_sum
def two_sum(arr,target):
    seen={}
    
    for i in range(len(arr)):
        need = target - arr[i]
        
        if need in seen:
            return[seen[need],i]
        seen[arr[i]]=i
    return [-1,-1]
print(two_sum([2,7,6,15,17],9))