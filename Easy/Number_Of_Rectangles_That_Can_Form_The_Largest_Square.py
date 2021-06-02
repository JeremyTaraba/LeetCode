class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        count = 0
        largest = 0
        for rect in rectangles:
            if(largest < min(rect)):
                largest = min(rect)
                count = 1
            elif(largest == min(rect)):
                count += 1
            
        return count
        