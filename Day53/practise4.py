#linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print(linear_search([10,20,30,40,50],50))


#missing number
def missing_number(arr):
    n=len(arr)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(arr)
    return expected_sum - actual_sum
print(missing_number([1,2,3,5,6]))