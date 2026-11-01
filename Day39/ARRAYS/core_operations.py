arr = [10, 20, 30]

#A.Access - o(1)
print(arr[0])  # Output: 10
print(arr[-1])  # Output: 30

#B.Update - o(1)
arr[1] =  99
print(arr)  # Output: [10, 99, 30]

#C. Add Element
arr.append(40)  # Add at the end - o(1)
print(arr)  # Output: [10, 99, 30, 40]
arr.insert(1, 15)  # Add at specific index - o(n)
print(arr)  # Output: [10, 15, 99, 30, 40]

#D.remove element
arr.pop()# Remove last element - o(1)
print(arr)  # Output: [10, 15, 99, 30]
arr.pop(1) # Remove element at specific index - o(n)
print(arr)  # Output: [10, 99, 30, 40]
arr.remove(99)  # Remove specific element - o(n)
print(arr)  # Output: [10, 30, 40]

#E. Size
print(len(arr)) # o(1)

#F. slicing - o(k) where k is the size of the slice
arr=[10, 20, 30, 40, 50]
print(arr[1:4])  # Output: [20, 30, 40] - from index 1 to 3
print(arr[:3])  # Output: [10, 20, 30] - first 3 elements
print(arr[::-1])  # Output: [50, 40, 30, 20, 10] - reversed array

#important:address=start_address+(index*size)

#slicing : complete - Most powerful in python - o(k) where k is the size of the slice
#format: arr[start:end:step]
#start - included, end - excluded (stops one before the end index), step - step size

arr = [10, 20, 30, 40, 50,60]

#basic slicing
print(arr[1:4])  # Output: [20, 30, 40]
print(arr[2:5])  # Output: [30, 40, 50]

#if u leave blank
print(arr[:3])  # Output: [10, 20, 30] - first 3 elements
print(arr[3:])  # Output: [40, 50] - from index 3 to 4
print(arr[:] ) # Output: [10, 20, 30, 40, 50, 60] - entire array

#negative indexing
print(arr[-2:])  # Output: [50]
print(arr[:-2])  # Output: [10, 20, 30]

#step-the magic
print(arr[::2])  # Output: [10, 30, 50] - every second element
print(arr[1::2])  # Output: [20, 40, 60] - every second element starting from index 1

print(arr[::-1])  # Output: [60, 50, 40, 30, 20, 10] - reversed array

print(arr[::-2])  # Output: [60, 40, 20] - from index 5 to 0 with step size of 2




