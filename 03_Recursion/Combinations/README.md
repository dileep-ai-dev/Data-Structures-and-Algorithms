#  Combinations

## Topics Learned

* What is a Combination?
* Combination vs Permutation
* Why order does not matter in combinations
* General Combination Generation
* Include / Exclude recursion
* Backtracking
* Using an index to avoid duplicate combinations
* Combination formula
* Combination Sum concept
* LeetCode 39 — Combination Sum

---

## Combination vs Permutation

### Permutation

Order matters.

Example:

```text
[1,2] and [2,1]
```

These are different permutations.

### Combination

Order does not matter.

Example:

```text
[1,2] and [2,1]
```

These represent the same combination.

---

## General Combination

General combinations mean selecting exactly `k` elements from a given collection.

Example:

```text
nums = [1,2,3]
k = 2
```

Output:

```text
[1,2]
[1,3]
[2,3]
```

We do not generate `[2,1]` separately because it represents the same combination as `[1,2]`.

---

## Combination Formula

The number of ways to choose `k` elements from `n` elements is:

```text
C(n,k) = n! / (k!(n-k)!)
```

Example:

```text
n = 4
k = 2

C(4,2) = 6
```

---

## General Combination Backtracking

The Include / Exclude approach is used.

For every element:

1. Include the current element.
2. Explore further.
3. Undo the choice using `pop()`.
4. Explore without the current element.

When an element is selected, we move to `index + 1`.

This ensures that:

* An element is not reused.
* We move only forward through the array.
* Duplicate orderings are avoided.

---

## Backtracking Pattern

```text
Choose
   ↓
Explore
   ↓
Undo
   ↓
Explore without the choice
```

---

## Important Code Concepts

### Include

```python
current.append(nums[index])
```

### Explore

```python
backtrack(current, index + 1)
```

### Undo

```python
current.pop()
```

### Exclude

```python
backtrack(current, index + 1)
```

---

## General Combination vs Combination Sum

| General Combination         | Combination Sum                |
| --------------------------- | ------------------------------ |
| Select exactly `k` elements | Reach a target sum             |
| Fixed `k`                   | No fixed `k`                   |
| Usually no reuse            | Candidates can be reused       |
| Include → `index + 1`       | Include → same `index`         |
| Example: `[1,2,3], k=2`     | Example: `[2,3,6,7], target=7` |

---

## LeetCode 39 — Combination Sum

LeetCode 39 was solved independently and pushed previously.

The important concept learned from it is that when a candidate is included, the same index is used because the candidate can be selected multiple times.

```text
Include → same index
Exclude → index + 1
```

---

## Complexity

For general combination generation:

```text
Time: O(2^n + k × C(n,k))
Space: O(n + k × C(n,k))
```

Where:

* `n` = number of input elements
* `k` = number of elements selected
* `C(n,k)` = number of generated combinations

The `O(n)` space comes from the recursion stack.

The `O(k × C(n,k))` space comes from storing the generated combinations.

---

## Problems / Practice

* General Combination Generation — Implemented independently
* LeetCode 39 — Combination Sum — Previously solved and pushed


