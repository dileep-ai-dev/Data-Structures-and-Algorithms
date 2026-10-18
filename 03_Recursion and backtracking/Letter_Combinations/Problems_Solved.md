# Problems Solved 

## LeetCode 17 - Letter Combinations of a Phone Number

### Problem
Given a string containing digits from 2-9, generate all possible letter combinations using the phone keypad mapping.

### Approach
Used recursive backtracking.

At each recursion level:

1. Get the letters corresponding to the current digit.
2. Choose one letter.
3. Recursively process the next digit.
4. Undo the selected letter.
5. Try the next available letter.

### Backtracking Pattern

Choose -> Explore -> Undo -> Try Next

### Edge Case

Empty input:

`digits = ""`

Return:

`[]`

### Complexity

- Time: O(n * 4^n)
- Output Space: O(n * 4^n)
- Auxiliary Space: O(n)

### Status

- [x] LeetCode 17 - Letter Combinations of a Phone Number