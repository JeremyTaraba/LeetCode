# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # look for subRoot root node and if found it then do the checking if it is equal

        def checkNodes(rootP, rootQ):
            if not rootP and not rootQ:
                return True
            if not rootP or not rootQ:
                return False
            if rootP.val != rootQ.val:
                return False
            
            return checkNodes(rootP.left, rootQ.left) and checkNodes(rootP.right, rootQ.right)

        def dfs(root, subRoot):
            if not root:
                return False
            if root.val == subRoot.val:
                if checkNodes(root, subRoot):
                    return True

            return dfs(root.left, subRoot) or dfs(root.right, subRoot)



        return dfs(root, subRoot)
            