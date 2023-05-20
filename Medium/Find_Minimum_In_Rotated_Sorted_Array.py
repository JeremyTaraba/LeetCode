class Solution:
    def findMin(self, nums: List[int]) -> int:
        # first attempt: use left and right pointers and try to find smallest number
        left = 0
        right = len(nums)-1

        while right - left > 1:
            mid = math.ceil((left + right) / 2) 

            if(nums[mid] > nums[right]): # only move up to mid so we don't go past it
                left = mid
            else:
                right = mid

        if(nums[left] < nums[right]):
            return nums[left]

        return nums[right]

