"""
Prompt:
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def dividingCheck(num):
            for digit in str(num):
                if digit == '0' or num % int(digit) > 0:
                    return False
            return True
        
        
        result = []
        for i in range(left, right + 1):
            if dividingCheck(i):
                result.append(i)
        return result


"""
Notes:
Two for loops so O(n^2) worst run time although if the number has a zero in it or isnt divisible by itself then the loop will exit sooner


Constraints:
The boundaries of each input argument are 1 <= left <= right <= 10000.

"""