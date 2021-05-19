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
        