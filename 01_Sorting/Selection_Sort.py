"""
Selection Sort

Time Complexity:
Best    : O(n²)
Average : O(n²)
Worst   : O(n²)

Space Complexity:
O(1)

Stable   : No
In-place : Yes
Adaptive : No
"""

def selection_sort(arr):

    for i in range(0, len(arr)):
        low_val = i

        for j in range(i + 1, len(arr)):
            if arr[low_val] > arr[j]:
                low_val = j

        arr[i], arr[low_val] = arr[low_val], arr[i]

    return arr


if __name__ == "__main__":

    arr = [10,1,0,1,90,98,34,9,2,8,4,8,2,87]

    print("Original Array :", arr)
    print("Sorted Array   :", selection_sort(arr))