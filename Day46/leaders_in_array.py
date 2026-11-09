def leaders(arr):
    ans=[]
    max_right=float('-inf')
    
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > max_right:
            ans=ans + [arr[i]]
            max_right=arr[i]
    ans.reverse()
    return ans

print(leaders([10,22,12,3,0,6]))