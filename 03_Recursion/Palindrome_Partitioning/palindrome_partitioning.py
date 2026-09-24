class Solution:
    def partition(self, s: str) -> list[list[str]]:

        result=[]
        current=[]

        def backtrack(index):

            if index==len(s):
                result.append(current.copy())
                return
            

            for i in range(index,len(s)):

                substring=s[index:i+1]

                if substring==substring[::-1]:
                    current.append(substring)
                    backtrack(index+1)

                    current.pop()

        backtrack(0)
        return result
        
