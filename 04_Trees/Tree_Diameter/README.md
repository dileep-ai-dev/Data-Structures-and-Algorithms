# Tree Diameter

## Definition
The diameter of a binary tree is the number of edges on the longest path between any two nodes.

## Example
```text
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

The longest path can be `4 -> 2 -> 1 -> 3 -> 6` or `4 -> 2 -> 1 -> 3 -> 7`.

Diameter = 4 edges.

## Approach
1. Recursively calculate the left and right subtree heights.
2. Calculate the diameter through the current node using `left_height + right_height`.
3. Update the maximum diameter found so far.
4. Return `1 + max(left_height, right_height)` to calculate the height for the parent.

## Complexity
- Time: O(n)
- Auxiliary space: O(h), where h is the tree height.

## Key Learning
The diameter through a node uses both subtrees, but the height returned to its parent uses only the deeper subtree.
