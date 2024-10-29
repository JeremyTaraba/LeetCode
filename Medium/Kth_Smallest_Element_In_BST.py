# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # try a dfs with a stack and put nodes onto the stack using inorder traversal
        # another way is to count how many nodes in the tree then traverse over it n - k times and return the kth


        def dfs(root, stack):
            if not root:
                return
            dfs(root.right, stack)
            stack.append(root.val)
            dfs(root.left, stack)
            
            return stack
            
        stack = dfs(root, [])

        for i in range(k-1):
            stack.pop()
        
        return stack.pop()