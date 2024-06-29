class Solution:
    def rob(self, nums: List[int]) -> int:
        lastMax, firstMax = 0, 0

        # [lastMax, firstMax, n, n+1, ...]
        for n in nums:
            temp = max(lastMax + n, firstMax)
            lastMax = firstMax
            firstMax = temp
            
        return firstMax
        