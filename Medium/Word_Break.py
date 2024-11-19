class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # these dynamic programming problems tend to have a map called dp and you either take a top down approach 
        # or a bottom up approach. The bottom up approach is usually simpler and easier to understand.
        # start from the last index and go to the first index, using memoization to reduce memory usage
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]