# Problems Solved

## Problem 1 — Rat in a Maze

### Problem

Find all possible paths from the top-left cell to the bottom-right cell of a maze.

- `1` represents an open cell.
- `0` represents a blocked cell.
- A cell cannot be visited twice in the same path.

### Approach

Used recursion and backtracking.

At every cell:

1. Try Up.
2. Try Left.
3. Try Down.
4. Try Right.
5. Check boundaries.
6. Check whether the next cell is open.
7. Mark the current cell as visited.
8. Explore recursively.
9. Undo the current path choice.
10. Restore the cell.

### Backtracking Pattern

    CHOOSE
       ↓
    CHECK
       ↓
    EXPLORE
       ↓
    UNDO
       ↓
    TRY NEXT

### Visited Technique

Instead of using a separate `visited` matrix, the original matrix is temporarily modified.

    1 → 0

while visiting a cell.

After recursion finishes, the original value is restored.

### Example

Input:

    [
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
    ]

Output:

    [
        ["down", "right", "down", "right"]
    ]

### Complexity

Time:

    O(4^(n*m))

Safe rough upper bound for the backtracking search.

Auxiliary Space:

    O(n*m)

for recursion and current path.

Output space depends on the number of valid paths.

### Status

Completed independently.

Pattern learned:

**Recursion + Backtracking + In-place Visited Tracking**