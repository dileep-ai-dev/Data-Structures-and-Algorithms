
# Level Order Traversal (BFS)

## Overview
Level Order Traversal visits tree nodes level by level, from left to right.

It uses Breadth-First Search (BFS) and a queue.

## Example

```text
        1
       / \
      2   3
     / \   \
    4   5   6
```

Output:

```python
[[1], [2, 3], [4, 5], [6]]
```

## Algorithm
1. Return an empty list if the root is None.
2. Insert the root into a queue.
3. Find the number of nodes at the current level.
4. Process those nodes and add their children to the queue.
5. Store each level in the result.
6. Return the result.

## Complexity
- Time: O(n)
- Space: O(n)

Here, n is the number of nodes.

## Key Learning
- BFS uses a queue.
- A queue follows FIFO (First In, First Out).
- `len(queue)` helps process one level at a time.
