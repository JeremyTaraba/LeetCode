class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        def backtracking(curPer):
            if len(curPer) == len(nums):
                res.append(curPer.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in curPer:
                    curPer.append(nums[i])
                    backtracking(curPer)
                    curPer.pop()
            

        backtracking([])
        return res