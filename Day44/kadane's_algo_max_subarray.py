def maxsubarray(nums):
    max_sum=curr_sum=nums[0]
    
    for num in nums[1:]:
        if curr_sum < 0:
            curr_sum=0
        curr_sum=curr_sum+num
        max_sum=max(max_sum,curr_sum)
    return max_sum

print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))