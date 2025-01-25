class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(s1Index, s2Index):
            s3Index = s1Index + s2Index
            if s1Index == len(s1) and s2Index == len(s2):
                return True
            if (s1Index,s2Index) in dp:
                return dp[(s1Index,s2Index)]
            if s1Index < len(s1) and s1[s1Index] == s3[s3Index] and dfs(s1Index+1,s2Index):
                return True
            if s2Index < len(s2) and s2[s2Index] == s3[s3Index] and dfs(s1Index,s2Index+1):
                return True
            dp[(s1Index,s2Index)] = False
            return False
        
        return dfs(0,0)