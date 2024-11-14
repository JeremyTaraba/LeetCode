class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= size:
                size = i
        return size == 0