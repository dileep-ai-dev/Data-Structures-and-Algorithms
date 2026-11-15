# Top View and Bottom View of Binary Tree

## Topics Covered

- Breadth-First Search (BFS)
- Level Order Traversal
- Horizontal Distance
- Top View of Binary Tree
- Bottom View of Binary Tree
- Zigzag Level Order Traversal

## 1. Horizontal Distance (HD)

Horizontal distance helps identify the horizontal position of each node.

Rules:
- Root node: HD = 0
- Left child: HD = HD - 1
- Right child: HD = HD + 1

## 2. Top View of Binary Tree

The top view contains the nodes visible when looking at a binary tree from above.

Approach:
- Use BFS with a queue.
- Store each node along with its horizontal distance.
- Store only the first node encountered at each horizontal distance.
- Sort the horizontal distances to return nodes from left to right.

## 3. Bottom View of Binary Tree

The bottom view contains the nodes visible when looking at a binary tree from below.

Approach:
- Use BFS with a queue.
- Store each node along with its horizontal distance.
- Update the dictionary whenever another node is encountered at that horizontal distance.
- Sort the horizontal distances to return nodes from left to right.

Note: With BFS, deeper levels are processed later. If nodes have the same depth and horizontal distance, the selected node depends on traversal order.

## 4. Zigzag Level Order Traversal

Zigzag traversal visits alternate levels in opposite directions.

Approach:
- Use BFS.
- Process one level at a time.
- Reverse every alternate level.
- Store each level in the result list.

## Complexity Analysis

For Top View and Bottom View:
- Time Complexity: O(N log N) due to sorting.
- Space Complexity: O(N).

For Zigzag Level Order Traversal:
- Time Complexity: O(N).
- Auxiliary Space Complexity: O(W), where W is the maximum width of the tree.

## LeetCode Problem

103. Binary Tree Zigzag Level Order Traversal

## Learning Outcome

Learned how to use BFS and horizontal distance to identify top and bottom views of a binary tree.

Also practiced processing alternate levels in reverse order using BFS.