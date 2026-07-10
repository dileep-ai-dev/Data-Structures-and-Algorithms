# Day 14 - Rotated Sorted Array

## Concepts Learned

- Rotated Sorted Array
- Identifying the Sorted Half
- Binary Search on Rotated Arrays
- Searching in O(log n)

## Key Observation

At every step, at least one half of the array is sorted.

1. Check which half is sorted.
2. Check if the target lies in the sorted half.
3. Discard the other half.
4. Repeat until the target is found.

## Time Complexity

O(log n)

## Space Complexity

O(1)

## LeetCode Problems

33. Search in Rotated Sorted Array
153. Find Minimum in Rotated Sorted Array
81. Search in Rotated Sorted Array II