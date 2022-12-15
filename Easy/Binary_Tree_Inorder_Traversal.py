# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recur(self, root, list):
        if(root == None):
            return list
        
        self.recur(root.left, list)
        list.append(root.val)
        self.recur(root.right,list)
        #print(list)
        return list



    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        inorder = []

        inorder = self.recur(root,inorder)


        return inorder