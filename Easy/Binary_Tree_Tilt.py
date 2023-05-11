# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # first attempt: Start at the root and calculate it then move to left then to right
        # will need to check children of the tree. <- lots of recursion. Can instead create a 
        # global variable(instance variable) to keep track of answer
        self.answer = 0
       
        self.calculateLR(root)
        return self.answer


    def calculateLR(self, root):
        if root == None:
            return 0

        left = self.calculateLR(root.left)  # calculate left
        right = self.calculateLR(root.right) # calculate right
        self.answer+= abs(left - right) # once all left and rights are done, subtract and add result to answer
        return root.val + left + right # return for parent node




    