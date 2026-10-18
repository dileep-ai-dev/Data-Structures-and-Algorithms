# Combinations

## Topics Learned

- What is a combination?
- Combination vs Permutation
- Order does not matter in combinations
- Selecting elements from a given collection
- Basic combination generation concept
- Include / Exclude recursion
- Using an index to avoid duplicate orderings
- Combination Sum concept
- LeetCode 39 — Combination Sum

## Important Difference

### Permutation
Order matters.

Example:

[1,2] and [2,1] are different permutations.

### Combination
Order does not matter.

Example:

[1,2] and [2,1] represent the same combination.

## Combination Sum — LeetCode 39

In LeetCode 39:

- We are given candidate numbers.
- We need combinations whose sum equals the target.
- The same candidate can be used multiple times.
- Order does not matter.
- We use recursion and backtracking.

## Backtracking Pattern

1. Choose the current candidate.
2. Reduce the remaining target.
3. Continue recursion.
4. Undo the choice using `pop()`.
5. Move to the next candidate.

## Important Point

For LeetCode 39, when we include a candidate, we call recursion with the same index because the candidate can be reused.

When we exclude it, we move to `index + 1`.

## Problem Solved

- LeetCode 39 — Combination Sum

## Status

Combination Sum implementation completed.

General Combination Generation will be continued tomorrow.