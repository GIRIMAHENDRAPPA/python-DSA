arr = [10, 3, 6, 8, 5]
largest = arr[0]
second_largest = -1
for i in arr:
    if i > largest:
        largest=i
        second_largest = largest
    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest number in the array is:", second_largest)