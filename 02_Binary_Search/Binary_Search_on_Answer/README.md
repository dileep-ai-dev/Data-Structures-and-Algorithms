# Day 15 - Binary Search on Answer

## Concepts Learned

- Binary Search on Answer
- Monotonic Property
- Search Space
- Helper Function (is_possible)

## Key Idea

Instead of searching for an element in an array, we search for the minimum or maximum valid answer.

Binary Search guesses a candidate answer, and a helper function checks whether that answer is possible.

## Binary Search Template

1. Define the search space.
2. Find the middle answer.
3. Check if it is possible.
4. If possible, save the answer and search left.
5. Otherwise, search right.

## Time Complexity

O(n log m)

- n = Number of piles
- m = Maximum pile size

## Space Complexity

O(1)

## LeetCode Problems

- [ Solved ] 875. Koko Eating Bananas
- [ yet to solve ] 1011. Capacity to Ship Packages Within D Days
- [ yet to solve ] 1283. Find the Smallest Divisor Given a Threshold