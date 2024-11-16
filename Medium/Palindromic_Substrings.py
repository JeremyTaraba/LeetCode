class Solution:
    def countSubstrings(self, s: str) -> int:
        # similar to find max palindromix substring
        sumValue = 0
        
        for i in range(len(s)):
            # odd length strings
            l = i
            r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                sumValue+=1
                l-=1
                r+=1
            
            # even length strings
            l = i
            r = i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                sumValue+=1
                l-=1
                r+=1


        return sumValue