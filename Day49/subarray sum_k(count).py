def count_subarray(arr,k):
    prefix=0
    count=0
    mp={0:1}
    
    for num in arr:
        prefix +=num
        need=prefix-k
        
        if need in mp:
            count+=mp[need]
        mp[prefix]=mp.get(prefix,0)+1
        
    return count

print(count_subarray([1,2,3,-3,1,1,1,4,2,-3],3))