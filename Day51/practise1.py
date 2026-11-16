#1.largest element
def find_largest(arr):
    largest=arr[0]
    for num in arr:
        if num>largest:
            largest=num
    return largest

#2.second largest and second smallest
def find_second(arr):
    unique=sorted(set(arr))
    second_largest=unique[-2]
    second_smallest=unique[1]
    return second_largest, second_smallest

#3.reverse_array
def reverse_array(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr


#4.is_sorted
def is_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


arr=[10,5,20,8,20,15]
print(arr)
print(find_largest(arr))
print(find_second(arr))
print(reverse_array(arr))
print(is_sorted(arr))

    