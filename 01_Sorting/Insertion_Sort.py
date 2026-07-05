"""
Insertion Sort

Time Complexity:
Best    : O(n)
Average : O(n²)
Worst   : O(n²)

Space Complexity:
O(1)

Stable   : Yes
In-place : Yes
Adaptive : Yes
"""

def insertion_sort(arr):

    for i in range(len(arr)):

        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr


if __name__ == "__main__":

    arr = [1,3,90,2,98,34,9,2,8,4,8,2,90,78,67,87]

    print("Original Array :", arr)
    print("Sorted Array   :", insertion_sort(arr))