class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # first attempt: could brute force it using nested loops. 
        # could slightly optimize it by checking shorter strings in longer strings but
        # runtime would still be O(n^2)

        ans = set()
        for i in words:
            for k in words:
                if i != k:
                    if i in k:
                        ans.add(i)
        
        return ans