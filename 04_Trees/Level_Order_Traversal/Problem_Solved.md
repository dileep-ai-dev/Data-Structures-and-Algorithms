
# Problem Solved: Binary Tree Level Order Traversal

- **Platform:** LeetCode
- **Problem Number:** 102
- **Difficulty:** Medium
- **Topic:** Trees, BFS, Queue

## Problem Link
https://leetcode.com/problems/binary-tree-level-order-traversal/

## Approach
Used Breadth-First Search (BFS) with a queue.

At each iteration, stored the current queue length to process only the nodes at that level. Added their values to a list and enqueued their children.

## Complexity
- Time: O(n)
- Space: O(n)

## Key Learning
- How to implement BFS on a binary tree.
- How to process nodes level by level.
- How to use `deque` for efficient queue operations.


## Reflection
The important part was storing the queue length before processing a level. This prevents nodes from the next level from being included in the current level.
