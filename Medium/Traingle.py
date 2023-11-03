class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # first attempt: seems like a greedy approach. past the 2nd level you can only pick 2 nums
        # just need an index for outer list and inner list and keep track of sum
        # need to find smallest path which can change with negative numbers so greedy wont work
        # so instead can create a prefix sum array and choose the min from the botton of the triangle
        # would be easier to do this recursively
        # have to visit every combination of elements so must be atleast O(n^2)
        # could also do this bottom up instead of top down

        

        for i in range(1, len(triangle)):  # outerloop for each row in triangle
            for j in range(i+1):           # inner loop through each element in the row
                triangle[i][j] += min(triangle[i-1][j-(j==i)],  # minimum from (outer-1, inner)
                                      triangle[i-1][j-(j>0)])   # minimum from  (outer-1, inner-1)

        return min(triangle[-1])  # obtain minimum sum from last row

       
        