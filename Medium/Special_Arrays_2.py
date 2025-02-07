class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # there could be a lot of repeated work 
        
        n = len(nums)
        prefix = [0] * n
        ans = [True] * len(queries)
        for i in range(len(nums)-1):
            prefix[i+1] = prefix[i]
            cur = nums[i]
            nex = nums[i+1]
            if cur % 2 == nex % 2:
                prefix[i+1] += 1
        
        index = 0
        for start,finish in queries:
            ans[index] = prefix[start] == prefix[finish]
            index+=1
            

        return ans

