class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1) # +1 since we want to start at 0 and go until amount
        dp[0] = 0
        for i in range(1,amount+1): # only have array of size amount so only need loop for amount times
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i],1 + dp[i-c])
        return dp[amount] if dp[amount] != float("inf") else -1