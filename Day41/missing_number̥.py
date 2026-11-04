def missing_number(arr):
    n = len(arr)+1
    expected = n * (n + 1)// 2
    actual = sum(arr)
    return expected - actual
print(missing_number([1,3,4,5]))