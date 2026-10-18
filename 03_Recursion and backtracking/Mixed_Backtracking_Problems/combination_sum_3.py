class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        nums = [num for num in range(1, 10)]
        result = []

        def backtrack(index, remaining, current):

            if remaining == 0 and len(current) == k:
                result.append(current.copy())
                return

            if remaining < 0 or index >= len(nums):
                return

            for i in range(index, len(nums)):

                if remaining - nums[i] < 0:
                    break

                current.append(nums[i])
                backtrack(i + 1, remaining - nums[i], current)
                current.pop()

        backtrack(0, n, [])
        return result