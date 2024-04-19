class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # increase the right until it reaches the end, then increase the left
        # if right < left then left = right
        # keep track of max

        left = 0
        right = 0
        size = len(prices)
        maxProfit = 0
        while left < size-1 and right < size-1:
            if right < size-1:
                right+=1

            if prices[right] <= prices[left]:
                left = right
                continue
            difference = prices[right] - prices[left]

            if(difference > maxProfit):
                maxProfit = difference
            
        
        return maxProfit