# Day 20 - Problems Solved

## 1. LeetCode 46 - Permutations

### Problem
Given an array of distinct integers, return all possible permutations.

### Approach
Used recursion and backtracking.

At each step:

1. Check whether the permutation is complete.
2. Loop through all elements.
3. Skip elements that are already used.
4. Add an unused element to `current`.
5. Mark it as used.
6. Recursively continue.
7. Unmark it as unused.
8. Remove it using `pop()`.

### Main Backtracking Pattern

```python
current.append(nums[i])
used[i] = True

backtrack(current)

used[i] = False
current.pop()


