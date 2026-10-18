# N-Queens

## Topic

N-Queens using Recursion and Backtracking

## Problem

The N-Queens problem asks us to place `N` queens on an `N × N` chessboard so that no two queens attack each other.

A queen can attack another queen if they are in:

- The same row
- The same column
- The same diagonal

For LeetCode 51, we need to return all possible valid boards.

---

## Example

For:

`n = 4`

One valid board is:

```text
. Q . .
. . . Q
Q . . .
. . Q .


## Backtracking Pattern
    Try
    ↓
    Check
    ↓
    Choose
    ↓
    Explore
    ↓
    Undo
    ↓
    Try next choice