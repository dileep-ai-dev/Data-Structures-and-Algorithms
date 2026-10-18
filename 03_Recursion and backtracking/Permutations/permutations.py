# Permutations
# Generate all permutations using Backtracking and used[]

def permute(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        # Base case: permutation is complete
        if len(current) == len(nums):
            result.append(current.copy())
            return

        # Try every number
        for i in range(len(nums)):

            # Skip already used numbers
            if used[i]:
                continue

            # Choose
            current.append(nums[i])
            used[i] = True

            # Explore
            backtrack(current)

            # Undo / Backtrack
            used[i] = False
            current.pop()

    backtrack([])
    return result


# Test
nums = [1, 2, 3]

result = permute(nums)

for permutation in result:
    print(permutation)