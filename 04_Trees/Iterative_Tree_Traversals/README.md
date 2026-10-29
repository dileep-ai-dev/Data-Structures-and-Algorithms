# Iterative Tree Traversals

This folder contains my Python implementations of iterative binary tree traversals and three LeetCode problems.

## Traversal Types

1. **Preorder:** Root → Left → Right
2. **Inorder:** Left → Root → Right
3. **Postorder:** Left → Right → Root

## Concepts Learned

- Using a stack to perform tree traversal without recursion.
- Understanding the LIFO property of stacks.
- Pushing the right child before the left child in preorder traversal.
- Using a stack to process the left subtree first in inorder traversal.
- Using `collections.deque` with `appendleft()` for iterative postorder traversal.

## Complexity

For a tree containing `n` nodes:

- Time complexity: `O(n)` for all three traversals.
- Auxiliary space complexity: `O(n)` in the worst case.

## LeetCode Problems

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
