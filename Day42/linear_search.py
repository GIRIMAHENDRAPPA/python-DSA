def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

arr=[10,20,30,40,50]
target = 30

result = linear_search(arr, target)

if result !=-1:
    print(f"found at index {result}")
else:
    print("not found")