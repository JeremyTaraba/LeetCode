class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # if we sort it, will take nlogn if we use heapify will take n since only heapifying 4 elements
        length = len(nums)
        if(length <= 4):
            return 0

        
        minDiff = float("inf")
        
        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))
        
        for i in range(4):
            minDiff = min(minDiff, max_four[i] - min_four[i])

        return minDiff

        