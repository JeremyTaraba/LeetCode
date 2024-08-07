class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # count how many 1s there are and do a sliding window thats the size of those ones and find window with least amount 
        # of 0s. This works until we factor in the circle. We can make it so if the right side reaches the end we make it go
        # back to the beginning. The loop ends when we have the left side reaching the end (as opposed to the right side reaching the end normally)
        left = 0
        right = sum(nums)-1 # counting ones
        if right == left:
            return 0
        length = len(nums)
        size = right + 1
        minSwap = size - sum(nums[left:right+1])
        currentOnes = size - minSwap
        while left <= length-1:
            right+=1
            if right == length:
                right = 0
            if nums[right]:
                currentOnes+=1
            if nums[left]:
                currentOnes-=1
            left+=1
            
            minSwap = min(minSwap, size - currentOnes)

            

        return minSwap
        