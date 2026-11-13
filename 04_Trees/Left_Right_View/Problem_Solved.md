# Problem Solved

## LeetCode 199 — Binary Tree Right Side View

**Platform:** LeetCode

**Problem Link:** https://leetcode.com/problems/binary-tree-right-side-view/

**Status:** Accepted

### Approach Used
Breadth-First Search (BFS) / Level Order Traversal.

### Logic
1. Handle an empty tree.
2. Initialize a queue with the root node.
3. Process the tree one level at a time.
4. Record the last node in the queue at the beginning of each level.
5. Add the current node's left and right children to the queue.
6. Return the right-side view.

### Complexity
- Time Complexity: O(N)
- Auxiliary Space Complexity: O(W)

### Concepts Practiced
- Queue
- Deque
- BFS
- Level Order Traversal
- Binary Tree Views

### Additional Implementation
Implemented both left and right views of a binary tree independently using BFS in `left_right_view.py`.