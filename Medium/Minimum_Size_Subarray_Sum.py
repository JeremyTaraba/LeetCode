class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # first attempt: Sounds like a sliding window, lets try to use this, O(n) runtime, O(1) space
        if len(nums) == 0:
            return 0

        l = 0
        r = 1
        minLen = 0
        sumNum = nums[0]

        
        while r < len(nums):
            if sumNum == target:
                if minLen != 0:
                    minLen = min(minLen, r-l)
                else:
                    minLen = r-l
                sumNum += nums[r]
                r+=1
            elif sumNum > target:
                if minLen != 0:
                    minLen = min(minLen, r-l)
                else:
                    minLen = r-l
                sumNum-=nums[l]
                l+=1
            elif sumNum < target:
                sumNum += nums[r]
                r+=1
        
        while l != r:
            if sumNum == target:
                if minLen != 0:
                    minLen = min(minLen, r-l)
                else:
                    minLen = r-l
            elif sumNum > target:
                if minLen != 0:
                    minLen = min(minLen, r-l)
                else:
                    minLen = r-l
            sumNum-=nums[l]
            l+=1

        return minLen



        