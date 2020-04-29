# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return str(root.val) + "," + left + "," + right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(",")

        def deserialize_helper(lst):
            if lst:
                value = lst.pop(0)
                if value == "N":
                    return None
                node = TreeNode(value)
                node.left = deserialize_helper(lst)
                node.right = deserialize_helper(lst)
                return node
  
        return  deserialize_helper(lst)
        


        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))