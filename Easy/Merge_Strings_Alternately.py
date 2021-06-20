"""
Prompt:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

"""


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

"""
Notes:
Runtime O(n)
I dont really like the idea of just copy and pasting a function and changing a small part of it
for this amount of code it doesn't have much of an impact and is fine but probably want to fix that

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

"""