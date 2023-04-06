# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # first attempt: going to go left on the root and then right on the root and 
        # compare. could save into a list and compare lists? or could check in real time?
        # will try to use recursion

        if root == None:
            return True
        
        return isMirror(root.left, root.right)


def isMirror(left, right):
    if left==None and right==None:
        return True
    if left==None or right==None:
        return False
    if left.val != right.val:
        return False

    return isMirror(left.left, right.right) and isMirror(left.right, right.left)