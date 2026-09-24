# Palindrome Partitioning

## Topic
Palindrome Partitioning using Recursion and Backtracking

## Problem

Given a string `s`, partition it so that every substring in the partition is a palindrome.

Example:

Input:
"aab"

Output:
[["a","a","b"],["aa","b"]]

## Core Idea

At every index, try every possible substring starting from that index.

For each substring:

1. Check whether it is a palindrome.
2. If it is a palindrome, choose it.
3. Recursively solve the remaining string.
4. Remove it and try another partition.

## Backtracking Pattern

Choose → Check → Explore → Undo

## Important Concepts

- Recursion
- Backtracking
- Substrings
- Palindrome checking
- Recursion tree
- Base case
- Choose → Explore → Undo

## Palindrome Check

A string is a palindrome if it reads the same from both directions.

Example:

"aba" → palindrome

"abc" → not a palindrome

## Recursion State

`backtrack(index)` represents the position from where the next partition should be selected.

## Base Case

When:

`index == len(s)`

the entire string has been partitioned successfully.

## Example

Input:

"aab"

Valid partitions:

["a", "a", "b"]
["aa", "b"]

## Complexity

Time: O(n² × 2ⁿ) for this implementation

Output Space: O(n × 2ⁿ)

Auxiliary Recursion Space: O(n)