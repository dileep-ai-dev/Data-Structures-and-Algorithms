
# Maximum Depth of Binary Tree

## Overview
Maximum depth is the number of nodes on the longest path from the root to a leaf.

## Example

```text
       3
      / \
     9   20
        /  \
       15   7
```

Output: 3

## Approach
Use recursion:
1. If the root is None, return 0.
2. Calculate the depth of the left subtree.
3. Calculate the depth of the right subtree.
4. Return 1 plus the larger depth.

## Complexity
- Time: O(n)
- Auxiliary Space: O(h)

Here, n is the number of nodes and h is the maximum depth.

## Key Learning
LeetCode maximum depth counts nodes, whereas our earlier tree height convention counts edges.
