"""
Counting Sort

Time Complexity:
Best    : O(n+k)
Average : O(n+k)
Worst   : O(n+k)

Space Complexity:
O(k)

Stable   : Yes
In-place : No
Adaptive : No
"""

def counting_sort(arr):

    max_value = max(arr)

    index_wise_values = [0] * (max_value + 1)

    res = []

    for val in arr:
        index_wise_values[val] += 1

    for i in range(len(index_wise_values)):
        if index_wise_values[i] > 0:
            res.extend([i] * index_wise_values[i])

    return res


if __name__ == "__main__":

    arr = [2,3,1,1,0,2,5,6,3,3,4,6]

    print("Original Array :", arr)
    print("Sorted Array   :", counting_sort(arr))