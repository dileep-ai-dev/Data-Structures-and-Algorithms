# Problems Solved 

## 1. General Combination Generation

### Problem

Generate all possible combinations of exactly `k` elements from a given array.

### Example

```text
nums = [1,2,3,4,5]
k = 3
```

Output:

```text
[1,2,3]
[1,2,4]
[1,2,5]
[1,3,4]
[1,3,5]
[1,4,5]
[2,3,4]
[2,3,5]
[2,4,5]
[3,4,5]
```

### Approach

Used recursive backtracking with the Include / Exclude technique.

For every element, there are two choices:

1. Include the element.
2. Exclude the element.

When an element is selected, recursion moves to `index + 1`.

### Backtracking Logic

```text
Choose
   ↓
Explore
   ↓
Undo
   ↓
Explore without choosing
```

### Important Point

`index + 1` is used because each element can be selected only once.

Moving forward also prevents generating duplicate orderings such as:

```text
[1,2]
[2,1]
```

Both represent the same combination.

### Base Condition

When:

```text
len(current) == k
```

the current combination is complete and is stored in the result.

### Complexity

```text
Time: O(2^n + k × C(n,k))
Space: O(n + k × C(n,k))
Auxiliary Space: O(n)
```

### Status

Implemented independently ✅

---

## 2. LeetCode 39 — Combination Sum

### Status

Previously solved and pushed to GitHub.

### Key Concept

Combination Sum uses backtracking to find combinations whose sum equals the target.

The same candidate can be used multiple times.

Therefore:

```text
Include → same index
Exclude → index + 1
```

### Important Difference

General combinations:

```text
Include → index + 1
```

Combination Sum:

```text
Include → same index
```


