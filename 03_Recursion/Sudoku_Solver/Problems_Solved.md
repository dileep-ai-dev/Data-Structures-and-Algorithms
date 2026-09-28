# Problems Solved 

## Problem 1 — LeetCode 37: Sudoku Solver

### Problem

Solve a partially completed 9 × 9 Sudoku board in-place.

Empty cells are represented by `.`.

The completed board must satisfy:

- Every row contains 1–9 without duplicates.
- Every column contains 1–9 without duplicates.
- Every 3 × 3 box contains 1–9 without duplicates.

## Approach

Used recursion and backtracking.

For each empty cell:

1. Try numbers from 1 to 9.
2. Check whether the number is valid.
3. Place the number.
4. Recursively solve the next cell.
5. If a solution is found, return `True`.
6. Otherwise undo the number.
7. Try the next number.

## Validity Check

For every candidate number, check:

    1. Current row
    2. Current column
    3. Current 3 × 3 box

The 3 × 3 box is located using:

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

## Backtracking Pattern

    CHOOSE
       ↓
    CHECK
       ↓
    EXPLORE
       ↓
    SUCCESS?
      /    \
    YES     NO
     ↓       ↓
   RETURN   UNDO
             ↓
        TRY NEXT

## Important Concept

The solution uses `True` and `False` to communicate whether the current recursive path successfully solved the entire Sudoku.

When the board is solved:

    return True

When a candidate fails:

    board[r][c] = "."

and the algorithm tries another number.

## Complexity

Theoretical worst-case time:

    O(9^81)

This is a very loose upper bound.

Actual execution is reduced significantly by row, column, and box constraints.

Auxiliary recursion space:

    O(81)

The board is modified in-place.

## Result

Implemented independently using recursion and backtracking.

The solution correctly follows the Sudoku constraints but the current implementation can receive TLE because validity checking repeatedly scans rows, columns, and boxes.

Optimization is planned for a later revision.

## Status

Completed

LeetCode 37 — Sudoku Solver

Concepts practiced:

- Recursion
- Backtracking
- Constraint checking
- In-place modification
- 3 × 3 box calculation
- Recursive success propagation
- Undo operation