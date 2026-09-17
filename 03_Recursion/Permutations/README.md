# Day 20 - Permutations

## 📌 Topic
Recursion & Backtracking - Permutations

## 🧠 What is a Permutation?

A permutation is an arrangement of elements where the **order matters**.

For example, for:

[1, 2, 3]

Some permutations are:

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]

Total permutations:

3! = 6

## 🔄 Permutation vs Subset

### Subset
Order does not matter.

[1, 2] and [2, 1] represent the same subset.

### Permutation
Order matters.

[1, 2] and [2, 1] are different permutations.

## 🌳 Recursion Idea

At every level, choose one unused element.

For [1, 2, 3]:

First position → 3 choices
Second position → 2 choices
Third position → 1 choice

Therefore:

3 × 2 × 1 = 3! = 6

## 🔁 Backtracking Pattern

The main pattern is:

Choose
↓
Mark as used
↓
Explore
↓
Unmark as unused
↓
Undo the choice

In code:

current.append(nums[i])
used[i] = True

backtrack(current)

used[i] = False
current.pop()

## 🧩 used[] Array

The `used[]` array keeps track of which elements are currently selected.

For:

nums = [1, 2, 3]

Initially:

used = [False, False, False]

If we choose 2:

used = [False, True, False]

This means:

1 → available
2 → already used
3 → available

## 📌 Why current.copy()?

`current` keeps changing during backtracking.

Therefore, when storing a completed permutation, we use:

result.append(current.copy())

This stores an independent copy of the current permutation.

## ⏱️ Time Complexity

There are `n!` permutations.

Each permutation contains `n` elements.

Therefore:

O(n × n!)

## 💾 Space Complexity

Recursion depth and current permutation:

O(n)

Result stores `n!` permutations, each of size `n`:

O(n × n!)

## 🎯 Key Learning

- Permutations depend on order.
- Number of permutations = n!
- Use `used[]` to track selected elements.
- Use `append()` to choose.
- Use recursion to explore.
- Use `pop()` to undo.
- Set `used[i] = False` while backtracking.
- Use `current.copy()` when storing results.