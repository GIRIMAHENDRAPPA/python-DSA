def longest_subarray_sum_k(arr, k):
    prefix_map={0:1}
    prefix_sum=0
    max_len=0
    
    for i, num in enumerate(arr):
        prefix_sum +=num
        
        need = prefix_sum - k
        
        if need in prefix_map:
            length = i - prefix_map[need]
            max_len = max(max_len, length)
            
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum]=i
            
    return max_len

print(longest_subarray_sum_k([1,2,3,1,1,1],3))