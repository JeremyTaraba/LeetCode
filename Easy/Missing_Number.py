class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # first attempt: always starts at 0, amount of numbers is from 0 to len(nums)
        # multiple ways to do this, since there is no order, can create a hash table and then
        # mark the ones we have found. O(n) runtime and O(n) space
        # can also add up all numbers from list 0..n and then subtract the numbers from the list
        # and whatever we have left in our sum is the missing number. O(n) runtime, O(1) space
        # is there a way to do this in less than O(n) time?

        sumList = sum(range(0,len(nums)+1))

        for i in nums:
            sumList -= i
        return sumList