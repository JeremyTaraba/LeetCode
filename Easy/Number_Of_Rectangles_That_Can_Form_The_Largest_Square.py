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
        
"""
Notes:
O(n) runtime
just counting the largest number and how many their are

Constraints:
1 <= rectangles.length <= 1000
rectangles[i].length == 2
1 <= li, wi <= 109
li != wi

"""