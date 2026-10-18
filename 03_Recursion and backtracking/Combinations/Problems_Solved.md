# Problems Solved 

## LeetCode 39 — Combination Sum

### Problem
Given an array of distinct integers `candidates` and a target integer `target`, return all unique combinations of candidates where the chosen numbers sum to target.

The same number may be chosen an unlimited number of times.

### Approach

Used recursive backtracking with an index.

### Main Idea

- Include the current candidate.
- Keep the same index because the candidate can be reused.
- Backtrack using `pop()`.
- Exclude the current candidate.
- Move to the next index.

### Base Cases

If `remaining == 0`:

A valid combination is found.

If `remaining < 0`:

The current combination is invalid.

If `index >= len(candidates)`:

No candidates are left.

### Complexity

The solution has exponential backtracking behavior in the worst case.

Space is used for the recursion stack and the combinations stored in the result.

### Status

Solved independently.