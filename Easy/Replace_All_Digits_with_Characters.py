class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        str1 = ""
        for index, char in enumerate(s):
            if index % 2 == 0:
                str1+= char
            if index % 2 == 1:
                x = s[index - 1]
                str1+=chr(ord(x) + int(char))
            
        return str1