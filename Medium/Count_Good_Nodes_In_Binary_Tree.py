# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maximum):
            if not root:
                return 0
            if root.val >= maximum.val:
                maximum = root
                return dfs(root.left,  maximum) + dfs(root.right, maximum) + 1
            
            return dfs(root.left, maximum) + dfs(root.right, maximum)

        
        res = dfs(root, root)
        return res