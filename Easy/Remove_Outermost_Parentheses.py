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


"""
Notes:
O(n) runtime.
We add to parentCount for left parenthesis and subtract for right parenthesis and 
don't add to the final string if its the first set of parenthesis.

Constraints:
s.length <= 10000
s[i] is "(" or ")"
s is a valid parentheses string


"""