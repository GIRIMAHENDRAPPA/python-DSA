def two_sum(arr, target):
    seen ={}
    for i,num in enumerate(arr):
        need=target-num
        
        if need in seen:
            return [seen[need], i]
        seen[num] = i
print(two_sum([2,5,7,8], 9))