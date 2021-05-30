class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hashSet = set()        
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        
        code = ""
        for eachWord in words:
            for char in eachWord:
                code = code + morseCode[ord(char) - ord('a')]
                
            print(code)
            hashSet.add(code)
            code = ""
        
        return len(hashSet)
        
"""
Notes:


Constraints:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

"""