"""
Prompt:
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.


"""



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


"""
Notes:
O(n) runtime.
if the current number in the loop is greater than the next number then we add to count the difference between them plus 1
since the next number needs to be one greater than the previous number. then we set the next number to one greater than the 
previous number


Constraints:
1 <= nums.length <= 5000
1 <= nums[i] <= 104


"""