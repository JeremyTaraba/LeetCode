"""
Prompt:
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.

 
""" 


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