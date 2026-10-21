# Balanced Binary Tree

## Definition
A binary tree is height-balanced if the heights of the left and right subtrees differ by at most 1 at every node.

## Approach
1. Calculate the left and right subtree heights recursively.
2. If either subtree is unbalanced, propagate a special value (`-1`).
3. If the height difference is greater than 1, return `-1`.
4. Otherwise, return the current height.

## Complexity
- Time: O(n)
- Auxiliary Space: O(h)

## Key Learning
Combining height calculation and balance checking in one traversal avoids repeated work.
