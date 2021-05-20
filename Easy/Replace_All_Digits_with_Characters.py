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

"""
Notes:
runtime O(n) 
ord returns the integer of a unicode character then we add that to the shift. Then chr returns a character from an integer

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
shift(s[i-1], s[i]) <= 'z' for all odd indices i

"""