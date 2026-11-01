arr = [10,3,6,3,5,9]

largest=arr[0]
for i in arr:
    if i > largest:
        largest=i
    
print("Largest number in the array is:", largest)