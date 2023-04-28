# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # first attempt: Do a tree traversal - preorder?? Then put parenthesis around 
        # each new set of numbers <- Inefficient as you go through whole tree with if statements.  
        # maybe don't use recursion so you get better runtime??

        
        return treeTraversal(root,"")



    
def treeTraversal(root,answer):
    if(root == None):
        return ""
    
    answer += str(root.val)


    if(root.left != None):
        answer += "("+ treeTraversal(root.left, "") + ")"
        if(root.right != None):  
            answer += "(" + treeTraversal(root.right, "") + ")"
    if(root.left == None and root.right != None):
        answer += "()" + "("+ treeTraversal(root.right, "") + ")"
       
    
   
    return answer