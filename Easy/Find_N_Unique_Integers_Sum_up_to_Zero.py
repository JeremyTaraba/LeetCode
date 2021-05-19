"""
Prompt:
Given an integer n, return any array containing n unique integers such that they add up to 0.


"""


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        result = []
        count = 0
        for i in range(0, n/2):
                count+=1
                result.append(count)
                result.append(-1 * count)
                
        if(n % 2 == 0):
            return result
        else:
            result.append(0)
            return result
        
"""
Notes:
looping for n/2 since we append twice for each iteration. One append for the positive integer and one for the negative interger
so the sum equals zero after every append. If n is odd then we append a zero at the end to keep the sum zero but have a large enough array

Constraints:
1 <= n <= 1000

"""