def combinations(nums, k):
    result = []

    def backtrack(current, index):

        if len(current) == k:
            result.append(current.copy())
            return

        if index >= len(nums):
            return

        current.append(nums[index])
        backtrack(current, index + 1)

        current.pop()
        backtrack(current, index + 1)

    backtrack([], 0)
    return result


print(combinations([1, 2, 3, 4, 5], 3))