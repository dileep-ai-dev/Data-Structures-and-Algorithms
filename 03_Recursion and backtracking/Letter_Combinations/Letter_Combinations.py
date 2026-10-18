class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        result = []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return result

        def backtrack(current, index):
            if len(current) == len(digits):
                result.append("".join(current))
                return

            for char in phone[digits[index]]:
                current += char
                backtrack(current, index + 1)

                current = current[:-1]

        backtrack("", 0)

        return result