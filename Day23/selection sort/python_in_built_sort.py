arr = [64,25,12,22,11]

# Method 1: sorted() - returns new list
new_arr = sorted(arr)

# Method 2:.sort() - sorts same list
arr.sort()

# Descending
arr.sort(reverse=True)

# Sort by key - MOST ASKED
students = [("Mahendra", 85), ("Rahul", 90)]
students.sort(key=lambda x: x[1]) # sort by marks

# Dict sorting
data = [{"name":"A","age":22},{"name":"B","age":20}]
data.sort(key=lambda x: x["age"])

print(new_arr)