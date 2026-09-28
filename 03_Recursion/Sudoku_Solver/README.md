# Sudoku Solver

## Topic

Recursion + Backtracking

## Problem

Solve a partially completed 9 × 9 Sudoku board.

The Sudoku rules are:

1. Each row must contain the numbers 1 to 9 without repetition.
2. Each column must contain the numbers 1 to 9 without repetition.
3. Each 3 × 3 box must contain the numbers 1 to 9 without repetition.
4. Empty cells are represented by `.`.
5. The board must be modified in-place.

## Core Idea

For every empty cell:

1. Try a number from 1 to 9.
2. Check whether the number is valid.
3. Place the number.
4. Recursively solve the remaining board.
5. If the choice leads to a solution, return `True`.
6. If it leads to a dead end, undo the choice.
7. Try the next number.

The main backtracking pattern is:

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
        TRY NEXT CHOICE

## Validity Checking

A number can be placed only when it does not already exist in:

### 1. Current Row

Check all cells in the current row.

### 2. Current Column

Check all cells in the current column.

### 3. Current 3 × 3 Box

The starting row of the box is calculated using:

    start_row = (row // 3) * 3

The starting column is calculated using:

    start_col = (col // 3) * 3

This identifies the correct 3 × 3 box.

## Backtracking

When a number is placed:

    board[r][c] = num

The algorithm recursively explores the next cell.

If the choice does not lead to a solution:

    board[r][c] = "."

The number is removed and another number is tried.

This is the undo step of backtracking.

## Why Return True?

When the entire board is solved, the recursive function returns:

    True

This success value propagates through all previous recursive calls and stops further unnecessary searching.

## Example

Input:

    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

The algorithm fills all empty cells while satisfying the Sudoku constraints.

## Complexity

For a 9 × 9 Sudoku, there can be up to 81 cells.

A very loose worst-case backtracking bound is:

    O(9^81)

This is a theoretical upper bound because each empty cell can potentially try up to 9 numbers.

The actual search is much smaller because row, column, and 3 × 3 box constraints eliminate many invalid choices.

### Auxiliary Space

The recursion depth can reach at most 81 cells:

    O(81)

Since Sudoku always uses a fixed 9 × 9 board, this is effectively constant with respect to the fixed problem size.

The board is modified in-place.

## Current Implementation Note

This implementation correctly demonstrates the Sudoku backtracking algorithm.

However, the current validation method repeatedly scans the row, column, and 3 × 3 box for every candidate number.

This can cause Time Limit Exceeded on some online judge test cases.

Optimization will be studied separately using faster constraint tracking techniques such as sets.

## Key Learning

Sudoku Solver strengthened the backtracking pattern:

    Choose → Check → Explore → Undo

It also introduced:

- Constraint checking
- Recursive success propagation
- In-place board modification
- 3 × 3 box indexing
- Early termination after finding a valid solution