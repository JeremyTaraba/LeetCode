class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(index,curSub):
            if index == len(nums):
                res.append(curSub.copy())
                return         
            
            curSub.append(nums[index])
            backtracking(index+1, curSub)
            curSub.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index+=1
            backtracking(index+1,  curSub)


        backtracking(0,[])

        return res