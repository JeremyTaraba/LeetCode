# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        res = TreeNode()
        tempRes = res
        def recur(node, resRoot):
            if not node:
                return
            resRoot.val = node.val
            if node.right:
                resRoot.left = TreeNode()
                recur(node.right, resRoot.left)
            if node.left:
                resRoot.right = TreeNode()
                recur(node.left, resRoot.right)
            
        
        recur(root, res)
        return res