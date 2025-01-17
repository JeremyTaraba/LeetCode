# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(node, curSum, path):
            curSum+= node.val
            path.append(node.val)
            if (curSum == targetSum and node != root) or (node==root and not node.left and not node.right and curSum == targetSum):
                if not node.left and not node.right:
                    res.append(path.copy())

            if node.left:
                dfs(node.left,curSum,path.copy())
            if node.right:
                dfs(node.right,curSum,path.copy())
            
        if root:
            dfs(root, 0, [])

        return res