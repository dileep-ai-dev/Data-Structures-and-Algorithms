"""
Bucket Sort

Time Complexity:
Best    : O(n + k)
Average : O(n + k)
Worst   : O(n²)

Space Complexity:
O(n)

Stable   : Depends on bucket sorting algorithm
In-place : No
Adaptive : No
"""

def bucket_sort(arr):

    bucket_size = len(arr)

    if not arr:
        return arr

    max_value = max(arr)
    min_value = min(arr)

    if min_value == max_value:
        return arr

    buckets = [[] for _ in range(bucket_size)]

    for num in arr:

        index = int((num - min_value) / (max_value - min_value) * (bucket_size - 1))

        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    res = []

    for bucket in buckets:
        res.extend(bucket)

    return res


if __name__ == "__main__":

    arr = [90,98,45,68,34,92,14,53,5,3]

    print("Original Array :", arr)
    print("Sorted Array   :", bucket_sort(arr))