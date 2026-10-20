# Problem Solved — Tree Diameter

- **LeetCode Number:** 543
- **Problem:** Diameter of Binary Tree
- **Difficulty:** Easy
- **Link:** https://leetcode.com/problems/diameter-of-binary-tree/
- **Status:** Solved

## Approach
Use recursion to calculate each node's left and right subtree heights. Update the maximum diameter using the sum of these heights.

## Complexity
- **Time:** O(n)
- **Auxiliary Space:** O(h)

## Key Learning
The diameter may pass through any node, not only the root. Track the maximum diameter during recursion while returning the height to the parent.
