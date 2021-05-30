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
        