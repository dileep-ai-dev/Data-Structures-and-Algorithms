# Day 18 - Memoization

## Topics Covered

* Introduction to Memoization
* Overlapping Subproblems
* Recursive Fibonacci
* Memoized Fibonacci
* Tabulation
* Space Optimized Fibonacci

---

## What I Learned

### Recursive Fibonacci

* Solves the problem recursively.
* Repeats the same subproblems many times.
* Time Complexity: **O(2ⁿ)**
* Space Complexity: **O(n)**

---

### Memoization

* Stores previously computed results.
* Avoids repeated recursive calls.
* Time Complexity: **O(n)**
* Space Complexity: **O(n)**

---

### Tabulation

* Solves the problem from smaller subproblems to larger ones.
* Does not use recursion.
* Time Complexity: **O(n)**
* Space Complexity: **O(n)**

---

### Space Optimization

* Uses only the previous two Fibonacci values.
* Eliminates the DP array.
* Time Complexity: **O(n)**
* Space Complexity: **O(1)**

---

## Key Learning

Memoization is an optimization technique for recursion.

Instead of solving the same subproblem repeatedly, we store its answer and reuse it whenever needed.

Tabulation is another way to solve the same problem iteratively.

Space optimization further reduces memory usage by keeping only the required previous states.
