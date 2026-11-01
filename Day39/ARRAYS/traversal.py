arr = [10,20,30]

# method 1:by value

for x in arr:
    print(x)  # Output: 10, 20, 30
    
# method 2: by index
for i in range(len(arr)):
    print(f"Index {i} = {arr[i]}") 
    
#method 3: both index and value
for i, val in enumerate(arr):
    print(i, val)  # Output: Index 0: 10, Index 1: 20, Index 2: 30
    