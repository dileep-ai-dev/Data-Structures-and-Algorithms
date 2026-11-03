# Construct Binary Tree from Preorder and Inorder

## Concept

Construct a binary tree using its preorder and inorder traversal arrays.

### Traversal Types

- Preorder: Root → Left → Right
- Inorder: Left → Root → Right

## Approach

1. The first element of preorder is the root.
2. Find the root in inorder.
3. Split inorder into left and right subtrees.
4. Split preorder according to the number of nodes in each subtree.
5. Recursively construct the left and right subtrees.

## Example

Preorder: `[3, 9, 20, 15, 7]`

Inorder: `[9, 3, 15, 20, 7]`

Constructed tree:

```text
        3
       / \
      9   20
          / \
         15  7
```

## Complexity

- Slicing implementation: O(n²) worst-case time.
- Auxiliary space: Depends on recursion depth and list slicing.

## LeetCode

105. Construct Binary Tree from Preorder and Inorder Traversal

## Status

Completed — Day 10

