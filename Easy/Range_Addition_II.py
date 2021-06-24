class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for i in ops:
            m = min(m, i[0])
            n = min(n,i[1])
            
        return m*n

"""
Notes:
This is a shortcut version where we don't need to create a whole matrix to solve it.
Instead, since the matrix can only be incremented from the left corner out ex: [1,1] increments the left corner and [2,2]
increments the left corner as well as the adjacent spaces. So we know that if [1,1] is ever an operation then the max will be
in that square but if [1,1] is not an operation then the next smallest operation will be the max.

Constraints:
1 <= m, n <= 4 * 104
1 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n

"""