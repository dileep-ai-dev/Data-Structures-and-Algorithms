# Problems Solved 

## LeetCode 131 — Palindrome Partitioning

### Problem
Given a string `s`, partition it so that every substring of the partition is a palindrome.

### Pattern Used

Choose → Check → Explore → Undo

### Approach

At every index, try all possible ending positions.

If the substring is a palindrome:

- Add it to the current partition.
- Recursively process the remaining string.
- Remove it after returning.

### Example

Input:

"aab"

Output:

[["a","a","b"],["aa","b"]]

### Complexity

Time: O(n² × 2ⁿ)

Output Space: O(n × 2ⁿ)

Auxiliary Space: O(n)

### Status

✅ Solved independently