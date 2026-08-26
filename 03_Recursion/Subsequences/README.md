# Day 19 - Subsequences & Include/Exclude Pattern

## Topics Covered

* What is a subsequence?
* Subsequence vs Subarray
* Include / Exclude Pattern
* Recursion Tree
* Backtracking
* `append()` and `pop()`
* Generating all subsequences
* Generating all subsets
* Complexity Analysis

---

## Subsequence

A subsequence is obtained by selecting elements while maintaining their original order.

For example:

```text
[1, 2, 3]

Valid subsequences:
[]
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
```

The number of subsequences for `n` elements is:

```text
2^n
```

---

## Include / Exclude Pattern

For every element, there are two choices:

```text
Include the element
Exclude the element
```

The recursive pattern is:

```text
Include
    ↓
Recursive Call
    ↓
Backtrack (pop)
    ↓
Exclude
    ↓
Recursive Call
```

---

## Backtracking

The general pattern learned:

```python
current.append(element)

recursive_call()

current.pop()

recursive_call()
```

`pop()` restores the previous state before exploring another choice.

---

## Complexity

For `n` elements:

**Number of subsequences/subsets:** O(2^n)

**Time Complexity:** O(n × 2^n)

**Auxiliary Recursion Space:** O(n)

**Output Space:** O(n × 2^n)

---

## Key Learning

The Include/Exclude pattern is one of the fundamental recursion patterns.

It will be reused in:

* Subsets
* Combination Sum
* Subsequences
* Other Backtracking Problems
* N Queens
* Sudoku
