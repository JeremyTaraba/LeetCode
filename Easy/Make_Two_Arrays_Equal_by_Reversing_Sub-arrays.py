class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target.sort()
        arr.sort()
        return arr == target

"""
Notes:
We just need to see if one array contains the same numbers as the other. The easiest way to do this is to sort them
and then compare them. We can use the built in sort function for python or we can make our own

Constraints:
target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000

"""