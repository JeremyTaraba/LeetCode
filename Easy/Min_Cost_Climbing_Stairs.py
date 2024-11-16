class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # since you can only climb 1 or 2 stairs we only need to compute those stairs
        # try starting at last index
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
            
            
        return min(cost[0],cost[1])