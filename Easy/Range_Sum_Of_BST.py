# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addNodes(self, root, low, high):
        if(root == None):
            return 0
        if(root.val >= low and root.val <= high):
            return root.val + self.addNodes(root.left,low,high) + self.addNodes(root.right,low,high)
        if(root.val < low):
            return self.addNodes(root.right,low,high)
        if(root.val > high):
            return self.addNodes(root.left,low,high)
        return 0
        
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
      
        sum = self.addNodes(root,low,high)
        return sum

    