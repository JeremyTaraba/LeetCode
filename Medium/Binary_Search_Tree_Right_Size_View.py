# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # left side could be greater than right side so have to check that
        if not root:
            return []
        res = []
        queue = []

        cur = root
        queue.append(cur)
        level = 0
        while len(queue) > 0:
            level_size = len(queue)
            firstTime = True
            while level_size > 0:
                temp = queue.pop(0)
                if firstTime:
                    res.append(temp.val)
                    firstTime = False
                level_size -= 1
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)
            


        return res
    
    def checkHeight(self, root, height):
        if not root:
            return height
        left = self.checkHeight(root.left, height + 1)
        right = self.checkHeight(root.right, height + 1)
        return max(left, right)
