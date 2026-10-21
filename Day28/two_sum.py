class Solution:
    def twoSum(self,nums,target):
        arr_with_index=[[nums[i],i] for i in range(len(nums))]
        arr_with_index.sort()

        left = 0
        right = len(arr_with_index) - 1

        while left < right:
            s= arr_with_index[left][0] + arr_with_index[right][0]
            if s == target:
                return [arr_with_index[left][1],arr_with_index[right][1]]
            elif s < target:
                left += 1
            else:
                right -= 1
        return[]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target)) # Output: [0, 1]