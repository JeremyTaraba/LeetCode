class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # sort them so duplicates are next to each other
        def backtracking(index, updatedTarget, curList):
            if updatedTarget == 0:
                res.append(curList.copy())
                return
            if updatedTarget < 0 or index == len(candidates):
                return
            
            curList.append(candidates[index])
            backtracking(index + 1, updatedTarget - candidates[index], curList)
            curList.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            backtracking(index+1, updatedTarget, curList)
        
        backtracking(0,target,[])
        return res