def max_subarray(arr):
    curr_sum=0
    max_sum=0
    for i in range(0,len(arr)):
        curr_sum=max(arr[i],curr_sum+arr[i])
        max_sum=max(max_sum,curr_sum)
    return max_sum
print(max_subarray([-2,2,-3,4,-1,2,1,-5,4]))