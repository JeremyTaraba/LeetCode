# Definition for a binary tree node.
# class TreeNode: 
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # First Attempt: Recursion and append to list. Same as postorder

    def preOrder(self, root, ans):
        if(root == None):
            return
        
        ans.append(root.val)          # append here for preorder, first time you visit a node
        if(root.left != None):
            self.preOrder(root.left, ans)
        # ans.append(root.val)          # append here for inorder, second time you visit a node
        if(root.right != None):
            self.preOrder(root.right, ans)
        # ans.append(root.val)            # append here for postorder, last time you visit a node
        return

 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.preOrder(root, ans)

        return ans
