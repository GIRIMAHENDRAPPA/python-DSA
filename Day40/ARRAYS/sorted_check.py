arr=[10,9,8,7,6]
asc=True
desc=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        asc=False
    if arr[i]<arr[i+1]:
        desc=False

if asc:
    print("Array is sorted in ascending order:",asc)
elif desc:
    print("Array is sorted in descending order:",desc)
else:
    print("Array is not sorted")
