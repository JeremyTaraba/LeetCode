class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation is any order of characters but same number of characters
        # we could count the characters in s1 and see if those characters appear the same number of times in s2
        # but they must all be next to each other
        # since we know the length of s1 we can use a 2 pointer approach where we use that to check all substrings
        # O(n^2) runtime since Counter takes n time 
        # can do this in n time without using counter

        
        cntr, w = Counter(s1), len(s1)   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
            if i >= w and s2[i-w] in cntr: 
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]): # see optimized code below
                return True



     
        return False
