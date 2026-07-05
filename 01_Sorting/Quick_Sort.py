"""
Quick Sort

Time Complexity:
Best    : O(n log n)
Average : O(n log n)
Worst   : O(n²)

Space Complexity:
O(log n)

Stable   : No
In-place : Yes
Adaptive : No
"""

def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        partition_index = partition(arr, low, high)

        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


if __name__ == "__main__":

    arr = [10,1,0,1,90,98,34,9,2,8,4,8,2,87]

    print("Original Array :", arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("Sorted Array   :", arr)