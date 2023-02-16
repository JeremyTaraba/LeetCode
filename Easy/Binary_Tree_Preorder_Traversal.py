# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preOrder(self, root, ans):
        if(root == None):
            return
        
        ans.append(root.val)          # append here for preorder
        if(root.left != None):
            self.preOrder(root.left, ans)
        # ans.append(root.val)          # append here for inorder
        if(root.right != None):
            self.preOrder(root.right, ans)
        # ans.append(root.val)            # append here for postorder
        return

 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.preOrder(root, ans)

        return ans