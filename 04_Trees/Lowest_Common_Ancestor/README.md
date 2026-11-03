# Lowest Common Ancestor (LCA)

## Concept
The Lowest Common Ancestor of two nodes is the deepest node in a binary tree that is an ancestor of both nodes.

## Approach
- Start from the root.
- If the current node is `None` or matches either target node, return it.
- Recursively search the left and right subtrees.
- If both sides find a target, the current node is the LCA.
- Otherwise, return the result from the side that found a target.

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(h), where h is the height of the tree.

## LeetCode
236. Lowest Common Ancestor of a Binary Tree

## Status
Completed — Day 9
