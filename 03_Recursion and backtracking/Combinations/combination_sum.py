class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]

        def backtracking(remaining,current,index):

            if remaining==0:
                result.append(current.copy())
                return
            
            if remaining<0 or index>=len(candidates):
                return

            current.append(candidates[index])
            backtracking(remaining-candidates[index],current,index)

            current.pop()
            backtracking(remaining,current,index+1)

        backtracking(target,[],0)

        return result
        