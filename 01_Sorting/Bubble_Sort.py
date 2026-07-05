"""
Bubble Sort

Time Complexity:
Best    : O(n)
Average : O(n²)
Worst   : O(n²)

Space Complexity:
O(1)

Stable   : Yes
In-place : Yes
Adaptive : Yes (Optimized Version)
"""

def bubble_sort(arr):

    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr


if __name__ == "__main__":

    arr = [10,1,0,1,90,98,34,9,2,8,4,8,2]

    print("Original Array :", arr)
    print("Sorted Array   :", bubble_sort(arr))