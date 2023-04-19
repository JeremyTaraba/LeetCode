# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # first attempt: try to use a recursive dfs approach. 
        return findTargetSum(root, targetSum, 0)
    
def findTargetSum(root, target, sum):
    if(root == None):
        return False
    if( (root.left == None) and (root.right == None) ):
        if(sum + root.val == target):
            return True
        return False
    

    return findTargetSum(root.left, target, sum+root.val) or findTargetSum(root.right, target, sum+root.val)
        
            