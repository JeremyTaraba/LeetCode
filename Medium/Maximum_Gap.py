class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # try using min heap
        heapq.heapify(nums)
        maxDiff = 0
        a = heapq.heappop(nums)
        for i in range(len(nums)):
            b = heapq.heappop(nums)
            maxDiff = max(maxDiff, b-a)
            a=b
        return maxDiff