"""
Prompt:
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
 

"""




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