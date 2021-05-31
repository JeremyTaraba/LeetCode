"""
Prompt:
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

"""



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
        


"""
Notes:


Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters

"""