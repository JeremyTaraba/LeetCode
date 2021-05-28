class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for i in range(len(nums) - 1):
            if(nums[i] >= nums[i+1]):
                count += nums[i] - nums[i+1] + 1
                nums[i+1] = nums[i] + 1
           
        return count