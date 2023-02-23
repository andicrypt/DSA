# tag: [prefix sum]
# problem: find longest subarray whose sum is divisible by k

# input: 
# output:

arr = [4, 5, 0, -2, -3, 1]
k = 5

def max_length_subarray_divisible_by_k(arr, k):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0] % k
    for i in range(1, len(arr)):
        prefix_sum[i] = (prefix_sum[i-1] + arr[i]) % k
    
    longest_subarray = []
    rem_to_index = {0: -1}
    for j in range(len(arr)):
        rem = prefix_sum[j]
        if rem in rem_to_index:
            candidate_subarray = arr[rem_to_index[rem] + 1 : j + 1]
            if len(candidate_subarray) > len(longest_subarray):
                longest_subarray = candidate_subarray
            
        rem_to_index.setdefault(rem, j)
    
    return candidate_subarray

print(max_length_subarray_divisible_by_k(arr, k))