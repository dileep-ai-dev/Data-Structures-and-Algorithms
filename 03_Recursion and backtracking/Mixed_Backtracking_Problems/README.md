# Mixed Backtracking

## Topics Covered

* Mixed backtracking
* Combination Sum II
* Combination Sum III
* Duplicate skipping
* Pruning
* For-loop backtracking

## Problem 1: LeetCode 40 — Combination Sum II

**Difficulty:** Medium

**Pattern:** For-loop backtracking

### Problem

Find all unique combinations where the selected candidates sum to the target. Each candidate can be used at most once.

### Approach

1. Sort the candidates to group duplicate values.
2. Use a start index to explore combinations.
3. Skip duplicate values at the same recursion level.
4. Use `i + 1` to ensure each element is used only once.
5. Use pruning to stop when the current candidate is too large.
6. Use `append()` to choose and `pop()` to undo.

### Important Condition

`i > index and candidates[i] == candidates[i - 1]`

This skips duplicate choices at the same recursion level while still allowing repeated values in a valid combination when they come from different positions.

### Complexity

* Sorting: O(n log n)
* Search: O(2^n) upper bound, excluding the cost of copying results
* Auxiliary space: O(n), excluding the output

---

## Problem 2: LeetCode 216 — Combination Sum III

**Difficulty:** Medium

**Pattern:** For-loop backtracking

### Problem

Find all combinations of exactly `k` distinct numbers from 1 to 9 whose sum is `n`.

### Approach

1. Generate the available numbers from 1 to 9.
2. Use a start index to prevent reusing elements.
3. Choose a number and subtract it from the remaining target.
4. Recursively explore the next index.
5. Undo the choice using `pop()`.
6. Save the combination only when its length is `k` and its sum equals `n`.

### Important Conditions

* `remaining == 0 and len(current) == k`: identifies a valid combination.
* `remaining - nums[i] < 0`: stops exploring larger numbers because the candidates are sorted.
* `i + 1`: ensures a number is used at most once.

### Complexity

The candidate set has a fixed size of 9.

* Search: At most O(2^9) search states, excluding result-copying costs.
* Auxiliary space: O(9), excluding output.

## Key Learning

Combination Sum II and Combination Sum III both use for-loop backtracking. The key is to identify the constraints:

* Whether candidates can be reused
* Whether duplicates exist
* Whether the combination must have a fixed length
* Whether sorting enables pruning

Backtracking follows the pattern:

**Choose → Explore → Undo → Try the next choice**
