"""
Prompt:
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.


"""



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