"""
Prompt:
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

"""

 
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int 
        :rtype: str 
        """
        if(n%2 == 1):
            return 'a'*n
        else:
            return 'a'*(n-1) + 'b'

"""
Notes: 
O(1) runtime
Just doing math calculations. Python makes it easy to duplicate characters by doing 'a'*n where in c++ you would have to
concatenate n times.

Constraints:
1 <= n <= 500

"""