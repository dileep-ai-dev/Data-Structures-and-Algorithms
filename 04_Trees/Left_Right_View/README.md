# Left View and Right View of Binary Tree

## Topics Covered
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Level Order Traversal
- Left View of Binary Tree
- Right View of Binary Tree

## 1. Breadth-First Search (BFS)
BFS visits nodes level by level.

- Uses a Queue.
- Follows First In, First Out (FIFO).
- Also known as Level Order Traversal.

## 2. Depth-First Search (DFS)
DFS explores a path as deeply as possible before backtracking.

Common DFS traversals:
- Preorder: Root → Left → Right
- Inorder: Left → Root → Right
- Postorder: Left → Right → Root

DFS can be implemented using recursion or a stack.

## 3. Left View of Binary Tree
The left view contains the leftmost visible node at every level.

## 4. Right View of Binary Tree
The right view contains the rightmost visible node at every level.

## Approaches

### BFS Approach
- Process the tree level by level.
- For the left view, select the first node at each level.
- For the right view, select the last node at each level.

### DFS Approach
- Track the current depth.
- Visit left-first for the left view.
- Visit right-first for the right view.
- Record the first node encountered at each depth.

## Complexity
For both BFS and DFS:
- Time Complexity: O(N)
- Space Complexity: O(W) for BFS, where W is the maximum width of the tree.

## LeetCode Problem
- 199. Binary Tree Right Side View

## Learning Outcome
Learned how BFS and DFS can be used to identify the visible nodes of a binary tree from the left and right sides.