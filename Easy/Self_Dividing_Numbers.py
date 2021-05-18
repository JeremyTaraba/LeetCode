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