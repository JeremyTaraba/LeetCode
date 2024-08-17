# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # get the height of tree, O(n)
        # create a list with lists equal to the height
        # loop through tree once more and insert into list and appropriate index based on height
        if not root:
            return []

        def getHeight(node, height):
            if not node:
                return 1
            left = height+ 1
            right = height + 1
            if node.left:
                left = getHeight(node.left, height + 1)
            if node.right:
                right = getHeight(node.right, height+ 1)
            return max(left, right)
            
        height = getHeight(root, 0)
        ans = []
        for i in range(height):
            ans.append([])
        
        def recur(node, ans, curHeight):
            if not node:
                return
            ans[curHeight].append(node.val)
            if node.left:
                recur(node.left, ans, curHeight+1)
            if node.right:
                recur(node.right, ans, curHeight+1)
       
        recur(root, ans, 0)
        return ans