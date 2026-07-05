"""
Merge Sort

Time Complexity:
Best    : O(n log n)
Average : O(n log n)
Worst   : O(n log n)

Space Complexity:
O(n)

Stable   : Yes
In-place : No
Adaptive : No
"""

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    L = 0
    R = 0

    result = []

    while L < len(left) and R < len(right):

        if left[L] <= right[R]:
            result.append(left[L])
            L += 1

        else:
            result.append(right[R])
            R += 1

    result.extend(left[L:])
    result.extend(right[R:])

    return result


if __name__ == "__main__":

    arr = [10,1,0,1,90,98,34,9,2,8,4,8,2,87]

    print("Original Array :", arr)
    print("Sorted Array   :", merge_sort(arr))