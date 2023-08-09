# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: 
        # first attempt: use inner function to keep the answer saved without returning anything

        def dfs(node, path, answer):
            if node==None:
                return
            path.append(str(node.val))
            if node.left==None and node.right==None:
                answer.append("->".join(path))
            dfs(node.left, path, answer)
            dfs(node.right, path, answer)
            path.pop()
            
        answer = []    # pass this into the inner function, when it comes out it will be differnt
        dfs(root, [], answer)
        return answer

    
