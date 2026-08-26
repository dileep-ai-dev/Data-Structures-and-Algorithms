# Problems Solved

## LeetCode 78 - Subsets

### Method 1 - Enumeration

Used Python's `itertools.combinations` to generate subsets based on their size.

**Status:** Solved

### Method 2 - Backtracking

Used the Include/Exclude recursion pattern.

**Pattern:**

```text
Include → Recursive Call → Pop → Exclude → Recursive Call
```

**Status:** Solved

---

## Practice

* Generated all subsequences using recursion.
* Built the recursion tree for `[1,2]`.
* Understood why there are `2^n` possible subsets/subsequences.
* Practiced backtracking using `append()` and `pop()`.
