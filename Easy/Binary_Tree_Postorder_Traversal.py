# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # First attempt: Do recursion and append values to tree. Order you append will affect 
    # which traversal it is

    def postOrder(self, root, ans):
        if(root == None):
            return
        
        # ans.append(root.val)          # append here for preorder
        if(root.left != None):
            self.postOrder(root.left, ans)
        # ans.append(root.val)          # append here for inorder
        if(root.right != None):
            self.postOrder(root.right, ans)
        ans.append(root.val)            # append here for postorder
        return





    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.postOrder(root, ans)

        return ans
    



    # Second attempt: Do an iterative solution with a stack
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root is None:
    #             return []
    #         if root.left is None and root.right is None:
    #             return [root.val]
            
    #         stack, ret_val = list(), deque()
    #         stack.append(root)
            
    #         while stack:
    #             node = stack.pop()
                
    #             ret_val.appendleft(node.val)
                
    #             if node.left:
    #                 stack.append(node.left)
                
    #             if node.right:
    #                 stack.append(node.right)
            
    #         return ret_val