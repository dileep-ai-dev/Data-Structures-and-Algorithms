# Binary Search

## 📌 Definition

Binary Search is an efficient searching algorithm used to find a target element in a **sorted array** by repeatedly dividing the search space into two halves.

---

## 📌 Prerequisite

The array **must be sorted**.

---

## 📌 How It Works

1. Set `low = 0` and `high = len(arr) - 1`.
2. Find the middle index.
3. If the middle element equals the target, return its index.
4. If the target is greater than the middle element, search the right half.
5. If the target is smaller than the middle element, search the left half.
6. Repeat until the target is found or the search space becomes empty.

---

## 📌 Time Complexity

- Best Case: **O(1)**
- Average Case: **O(log n)**
- Worst Case: **O(log n)**

---

## 📌 Space Complexity

- Iterative Binary Search: **O(1)**

---

## 📌 Why must the array be sorted?

Binary Search decides whether to discard the left or right half of the array by comparing the target with the middle element. This is only possible if the array is sorted.

---

## 📌 Safe Mid Formula

```python
mid = low + (high - low) // 2
```

This avoids integer overflow in languages like Java and C++.

---

## 📌 Algorithm

1. Initialize `low` and `high`.
2. Repeat while `low <= high`.
3. Compute `mid`.
4. Compare `arr[mid]` with the target.
5. Return the index if found; otherwise continue searching in the appropriate half.
6. Return `-1` if the target is not present.