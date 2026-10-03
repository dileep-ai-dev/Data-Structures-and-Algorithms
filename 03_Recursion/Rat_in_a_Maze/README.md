# Rat in a Maze

## Topic
Recursion + Backtracking

## Problem

Given a matrix representing a maze:

- `1` = open cell
- `0` = blocked cell

Start from the top-left cell `(0, 0)` and find all possible paths to the bottom-right cell.

A cell cannot be visited again in the same path.

## Example

Input:

    [
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
    ]

Valid path:

    (0,0)
       ↓
    (1,0)
       →
    (1,1)
       ↓
    (2,1)
       →
    (2,2)

Path:

    down → right → down → right

## Core Backtracking Idea

At every cell:

1. Try every possible direction.
2. Check whether the next cell is valid.
3. Add the direction to the current path.
4. Recursively explore the next cell.
5. Remove the direction after returning.
6. Restore the current cell.
7. Try the next direction.

Pattern:

    CHOOSE
       ↓
    CHECK
       ↓
    EXPLORE
       ↓
    UNDO
       ↓
    TRY ANOTHER CHOICE

## Four Directions

The four possible movements are represented as:

    Up    = (-1, 0)
    Left  = (0, -1)
    Down  = (1, 0)
    Right = (0, 1)

## Visited Handling

Instead of creating a separate `visited` matrix, the matrix itself is used.

Before exploring:

    original_value = matrix[row][col]
    matrix[row][col] = 0

After exploring:

    matrix[row][col] = original_value

This follows:

    MARK → EXPLORE → RESTORE

## Base Case

When the current position reaches the bottom-right cell:

    row == len(matrix) - 1
    col == len(matrix[0]) - 1

The current path is stored.

## Why Backtracking?

A path that looks promising may lead to a dead end.

Backtracking allows us to:

- explore one possibility
- undo that choice
- return to the previous state
- try another possibility

## Important Learning

The first valid path is not necessarily the shortest path.

If the requirement is to find all paths, backtracking is appropriate.

If the requirement is specifically to find the shortest path in an unweighted maze, BFS is generally more suitable.

## Complexity

For an `n × m` grid, the number of possible paths can be exponential.

A safe rough upper bound for the search is:

    O(4^(n*m))

Auxiliary space:

    O(n*m)

for recursion depth and the current path.

The output space depends on the number of valid paths.

## Key Takeaway

Rat in a Maze strengthened the backtracking pattern:

    Choose → Check → Explore → Undo

It also introduced in-place visited-state management by temporarily modifying and restoring the matrix.