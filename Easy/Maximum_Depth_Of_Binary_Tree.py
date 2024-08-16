# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
       
        def recur(node, height):
            if not node:
                return height
            leftHeight = height
            rightHeight = height
            if node.left:
                leftHeight = recur(node.left, height+1)
            if node.right:
                rightHeight =  recur(node.right, height+1)
            return max(leftHeight, rightHeight)

     
        return recur(root, 1)
        