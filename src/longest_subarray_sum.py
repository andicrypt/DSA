# tag: [prefix sum]

# problem: find longest subarray that sum to k
# input: arr = [3, 4, -2, 1, 2, -3, 5], k = 5
# output: [3, 4, -2]

from typing import List

arr = [3, 4, -2, 1, 2, -3, 5]
k = 5


def longest_subarray_sum(arr: List, k: int):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    max_length = 0
    seen = {0: -1}

    for j in range(len(arr)):

        if prefix_sum[j] - k in seen:
            i = seen[prefix_sum[j] - k]
            max_length = max(max_length, j - i)
        if prefix_sum[j] - k not in seen:
            seen[prefix_sum[j]] = j

    return max_length


res = longest_subarray_sum(arr, k)
print(res)
