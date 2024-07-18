# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # turn it into an undirect graph using dictionaries?? [1 --> 2] [2 --> 3] [3 --> 4]
        # can get left or right later
        # also need to output it correctly with nulls 
        # could also do [1 --> 2, null] do figure out if its left or right since it will be a valid binary tree
        # do one pass to fill out the dictionary and find root, one pass through dictionary to fill out output starting from root

        nodes = {}
        children = set()
        for parent, child, is_left in descriptions:
            
            children.add(child)
            if not parent in nodes:
                nodes[parent] = TreeNode(parent)
            if not child in nodes:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
                
            
        
        for p,c,l in descriptions:
            if p not in children:
                return nodes[p]
        