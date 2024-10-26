# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traverse through p and q at the same time

        def dfs(rootP, rootQ):
            if not rootP and not rootQ:
                return True
            if not rootP or not rootQ:
                return False
            if rootP.val != rootQ.val:
                return False
            
            return dfs(rootP.left, rootQ.left) and dfs(rootP.right, rootQ.right)
            
        return dfs(p,q)