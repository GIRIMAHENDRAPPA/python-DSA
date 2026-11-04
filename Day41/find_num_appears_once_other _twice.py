def single_number(arr):
    ans = 0
    for num in arr:
        ans = ans ^ num
    return ans
print(single_number([2,3,3,4,4,]))

