def maxSubArray(nums):
    max_sum=nums[0]
    curr=0

    for num in nums:
        if curr < 0:
            curr = 0
        curr +=num
        max_sum  = max(max_sum, curr)
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))