
# Problem Solved: Maximum Depth of Binary Tree

- **Platform:** LeetCode
- **Problem Number:** 104
- **Difficulty:** Easy
- **Topic:** Trees, Recursion, DFS

## Problem Link
https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Approach
Used recursive DFS to calculate the maximum depth of the left and right subtrees. Added one for the current node and returned the larger depth.

## Complexity
- Time: O(n)
- Auxiliary Space: O(h)

## Key Learning
- Recursive tree traversal
- Base cases
- Maximum depth calculation
- Difference between node-based depth and edge-based height

## Status
- [x] Implemented solution
- [x] Reviewed complexity
- [x] Tested example

## Reflection
The main difference from the earlier height function is the base case. LeetCode counts nodes, so an empty tree has depth 0.
