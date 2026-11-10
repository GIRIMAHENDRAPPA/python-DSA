def rearrange_sign(nums):
    n=len(nums)
    result=[0]*n
    pos_index,neg_index=0,1
    
    for i in range(0,len(nums)):
        if nums[i] > 0:
            result[pos_index]=nums[i]
            pos_index+=2
        else:
            result[neg_index]=nums[i]
            neg_index+=2
    return result
print(rearrange_sign([3,1,-2,-5,2,-4]))
