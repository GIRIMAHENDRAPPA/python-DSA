# Day 30: List Comprehension & Map Filter

# Q1: Move zeroes using comprehension (1 line!)
nums = [0,1,0,3,12]
result = [x for x in nums if x != 0] + [0]*nums.count(0)
print("Q1 Move Zeroes:", result)

# Q2: Filter even numbers
nums2 = [1,2,3,4,5,6]
evens = [x for x in nums2 if x % 2 == 0]
print("Q2 Evens:", evens)

# Q3: map - Convert to square using lambda
squares = list(map(lambda x: x**2, nums2))
print("Q3 Squares via map:", squares)

# Q4: Real Interview Q - Extract names starting with 'A'
names = ["Aman", "Rohan", "Anjali", "Priya"]
a_names = [name for name in names if name.startswith('A')]
print("Q4 A-names:", a_names)