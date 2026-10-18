# Problems Solved

## 1. LeetCode 40 — Combination Sum II

* **Difficulty:** Medium
* **Topic:** Backtracking
* **Pattern:** For-loop backtracking
* **Status:** Solved

### Techniques

* Sorting
* Duplicate skipping
* Pruning
* Recursive exploration
* Backtracking with `append()` and `pop()`

### Key Learning

* `i + 1` prevents reusing an element.
* Duplicate skipping prevents duplicate combinations.
* Sorting allows early termination when a candidate exceeds the remaining target.

---

## 2. LeetCode 216 — Combination Sum III

* **Difficulty:** Medium
* **Topic:** Backtracking
* **Pattern:** For-loop backtracking
* **Status:** Solved independently

### Techniques

* Choosing numbers from 1 to 9
* Fixed-length combinations
* Recursive exploration
* Pruning
* Backtracking with `append()` and `pop()`

### Key Learning

* `i + 1` ensures each number is selected at most once.
* `len(current) == k` ensures the required number of elements.
* `remaining == 0` ensures the target sum is reached.
* Pruning avoids exploring candidates that exceed the remaining sum.

---

## Day 27 Summary

Practiced recognizing and applying backtracking patterns through combination problems, with attention to duplicate handling, element reuse, fixed-length constraints, and pruning.
