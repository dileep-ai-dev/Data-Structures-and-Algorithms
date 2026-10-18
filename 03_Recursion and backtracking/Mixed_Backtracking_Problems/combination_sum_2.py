class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result=[]
        candidates.sort()
        def backtrack(current,index,remaining):

            if remaining==0:
                result.append(current.copy())
                return
            
            if remaining<0 or index>=len(candidates):
                return
            
            for i in range(index,len(candidates)):

                if i>index and candidates[i]==candidates[i-1]:
                    continue
                
                current.append(candidates[i])
                backtrack(current,i+1,remaining-candidates[i])

                current.pop()
            
        backtrack([],0,target)
        return result
