"""
Heap Sort

Time Complexity:
Best    : O(n log n)
Average : O(n log n)
Worst   : O(n log n)

Space Complexity:
O(1)

Stable   : No
In-place : Yes
Adaptive : No
"""

def heapify(arr, n, i):

    largest = i

    left = (2 * largest) + 1
    right = (2 * largest) + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":

    arr = [10,1,0,1,90,98,34,9,2,8,4,8,2,87]

    print("Original Array :", arr)
    print("Sorted Array   :", heap_sort(arr))