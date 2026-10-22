class Solution:
    def moveZeroes(self, nums):
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        if j == -1:
            return

        for i in range(j + 1, len(nums)):
            if nums[i] !=0:
                nums[i], nums[j] = nums[j],nums[i]
                j +=1
    
    
nums = [0, 1, 0, 3, 12]
obj = Solution()
obj.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]