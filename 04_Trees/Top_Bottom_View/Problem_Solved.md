# Problem Solved

## 1. Top View of Binary Tree

**Implementation:** top_bottom_view.py

**Approach:** BFS with Horizontal Distance

### Logic
1. Initialize the root with horizontal distance 0.
2. Use a queue to process nodes.
3. Decrease HD by 1 when moving left.
4. Increase HD by 1 when moving right.
5. Store only the first node at each HD.
6. Sort HD values to produce the top view.

## 2. Bottom View of Binary Tree

**Implementation:** top_bottom_view.py

**Approach:** BFS with Horizontal Distance

### Logic
1. Initialize the root with horizontal distance 0.
2. Use a queue to process nodes.
3. Update the dictionary for every node encountered at an HD.
4. Sort HD values to produce the bottom view.

## 3. LeetCode 103 — Binary Tree Zigzag Level Order Traversal

**Problem Link:**
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

**Status:** Accepted

**Approach:** BFS / Level Order Traversal

### Logic
1. Handle an empty tree.
2. Initialize a queue with the root.
3. Process one level at a time.
4. Store the values of the current level.
5. Reverse alternate levels.
6. Append each level to the result.
7. Return the result.

### Complexity
- Time Complexity: O(N)
- Auxiliary Space Complexity: O(W)

## Concepts Practiced

- BFS
- Queue and Deque
- Horizontal Distance
- Dictionary
- Sorting
- Top View
- Bottom View
- Zigzag Level Order Traversal