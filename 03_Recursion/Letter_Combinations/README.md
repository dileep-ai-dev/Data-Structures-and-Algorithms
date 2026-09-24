# Letter Combinations of a Phone Number

## Topic
Backtracking - Letter Combinations

## Problem

Given a string containing digits from 2-9, return all possible letter combinations that the digits could represent.

The mapping is based on a telephone keypad.

Example:

Input:
"23"

Output:
["ad","ae","af","bd","be","bf","cd","ce","cf"]

---

## Keypad Mapping

2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz

---

## Core Idea

At every recursion level, we process one digit.

For the current digit:

1. Get its possible characters from the phone mapping.
2. Choose one character.
3. Add it to the current combination.
4. Move to the next digit.
5. After returning from recursion, undo the choice.
6. Try the next character.

Pattern:

Choose -> Explore -> Undo -> Try Next

---

## Recursion Structure

For digits = "23":

""
├── a
│   ├── ad
│   ├── ae
│   └── af
├── b
│   ├── bd
│   ├── be
│   └── bf
└── c
    ├── cd
    ├── ce
    └── cf

---

## Backtracking

The current combination is built character by character.

Example:

"" -> "a" -> "ad"

After storing "ad", the last character is removed:

"ad" -> "a"

Then the next choice is tried:

"a" -> "ae"

This is the backtracking step.

---

## Important Edge Case

If the input is empty:

Input:
""

Output:
[]

The empty-input check is handled before starting the recursion.

---

## Complexity

Let n be the number of digits.

In the worst case, every digit has 4 possible characters.

Number of possible combinations:

O(4^n)

Each generated combination has n characters.

Therefore:

Time Complexity: O(n * 4^n)

Output Space: O(n * 4^n)

Auxiliary Recursion Stack: O(n)

---

## What I Learned

- Backtracking with a loop
- Processing one input element at each recursion level
- Using a mapping to generate choices
- Choose -> Explore -> Undo
- Handling an empty input
- Understanding recursion-tree growth
- Understanding why 4 + 4^2 + ... + 4^n is O(4^n)
- Calculating time and space complexity for backtracking