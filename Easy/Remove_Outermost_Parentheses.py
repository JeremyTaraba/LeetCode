class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        length = len(s)
        parenCount = 0
        for char in s:
            if(char == '(' ):
                if(parenCount != 0):
                    result += char
                parenCount += 1
            elif(char == ')' ):
                if(parenCount != 1):
                    result += char
                parenCount += -1
            
        
        return result