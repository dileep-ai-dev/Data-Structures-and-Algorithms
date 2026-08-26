
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:




        # METHOD-(Backtracking)

        res = []

        def backtrack(current, index):

            if len(nums) == index:
                res.append(current.copy())
                return

            # Include
            current.append(nums[index])
            backtrack(current, index + 1)

            # Execlude
            current.pop()
            backtrack(current, index + 1)

        backtrack([], 0)
        return res