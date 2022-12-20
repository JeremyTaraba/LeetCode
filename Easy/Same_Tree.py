# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recur(self, p,q, isSame):
        if((p == None and q != None) or (p != None and q == None)):
            return isSame + 1
        if(p == None and q == None):
            return isSame + 0
        if(p.val != q.val):
            return isSame + 1
        isSame += self.recur(p.left, q.left, isSame)
        isSame += self.recur(p.right, q.right, isSame)
        return isSame + 0

        


    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        isSame = 0
        isSame += self.recur(p,q, isSame)

        return not isSame