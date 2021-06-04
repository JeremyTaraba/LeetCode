class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        def combineStrings(shorter, longer):
            count = 0
            combined = ""
            for char in shorter:
                combined+=char
                combined+=longer[count]
                count+=1
            if(count <= len(longer) - 1):
                combined+=longer[count:]
            return combined
        
        def combineStrings2(shorter, longer):
            count = 0
            combined = ""
            for char in shorter:
                combined+=longer[count]
                combined+=char
                count+=1
            if(count <= len(longer) - 1):
                combined+=longer[count:]
            return combined
        
        
    
        if(len(word1) > len(word2)):
            return combineStrings2(word2, word1)
        else:
            return combineStrings(word1, word2)