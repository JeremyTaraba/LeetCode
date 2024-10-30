# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # try a dfs preorder for both

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.li = ""
        def dfs(root):
            if not root:
                self.li += "_,"
                return
            self.li += str(root.val)+","
            left = dfs(root.left)
            right = dfs(root.right)
            return 
        dfs(root)
        return "".join(self.li)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "_,":
            return []
        root = TreeNode(0)
        listData = data.split(",")
        
        def dfs(root, data):
            if len(data) == 0:
                return None
            value = data.pop(0)
            if value == "_":
                return None
            root.val = int(value)
            root.left = dfs(TreeNode(0), data)
            root.right = dfs(TreeNode(0), data)
            return root

        dfs(root,listData)
        print(root)
        return root




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))