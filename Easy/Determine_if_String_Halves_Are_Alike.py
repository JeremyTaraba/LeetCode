class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = 'aeiou'
        
        def numVowels(string):
            count = 0
            for char in string:
                if char.lower() in vowels:
                    count += 1
            return count
        
        
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        
        return numVowels(s1) == numVowels(s2)
        