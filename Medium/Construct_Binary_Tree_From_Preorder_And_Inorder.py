# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = val, left, right
        # inorder = left, val, right
        # need to use these to figure out where the null values are

        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # find where the root is in inorder, that is the midpoint

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid] )
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
