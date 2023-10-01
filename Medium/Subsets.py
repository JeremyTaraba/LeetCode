class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for this one bcr is O(2^n) since we have to atleast mix and match them multiple times
        
        result = []
        
        subset = []
        def backtracking(index):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[index])
            
            backtracking(index + 1)
            

            subset.pop()
            backtracking(index + 1)

        backtracking(0)
        return result

