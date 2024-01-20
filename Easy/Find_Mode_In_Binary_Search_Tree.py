# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # first attempt: naive approach just keep a dictionary with a count of each node. 
        # can we make this better? using definition of BST we can

        # naive approach
        dictNums = {}
        result = []
        def dfs(root, dictNums):
            if(not root):
                return
            if root.val in dictNums:
                dictNums[root.val] = dictNums[root.val] + 1
            else:
                dictNums[root.val] = 1  
            dfs(root.left, dictNums)
            dfs(root.right, dictNums)
        
        dfs(root, dictNums)
        # go through the dict and check for max value
        maxVal = 0
        for key, value in dictNums.items():
            if value > maxVal:
                maxVal = value
                result.clear()
                result.append(key)
            elif value == maxVal:
                result.append(key)
            


        return result
            
        