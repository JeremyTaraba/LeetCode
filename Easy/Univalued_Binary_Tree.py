# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # first attempt: search through the whole tree, doesn't seem very efficient tho
        # Another way to do it is to add every node to a 
        # dictionary or something that doesn't take in duplicates and check the size
        # of it at the end. Will have more space complexity with this method

        value = root.val
        
        return isUnivalueZero(root, value)




def isUnivalue(root, value):
    if(root == None):
        return True
    if(root.val == value):
        return True & isUnivalueZero(root.left, value) & isUnivalueZero(root.right, value)
    return False







