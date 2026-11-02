def left_rotate_by_D(arr, d):
    n=len(arr)
    d%=n
    def reverse(l, r):
        while l<r:
            arr[l], arr[r]=arr[r], arr[l]
            l+=1
            r-=1
    reverse(0, d-1)
    reverse(d, n-1)
    reverse(0, n-1)
    return arr
arr=[1,2,3,4,5]
d=2
print(left_rotate_by_D(arr, d))