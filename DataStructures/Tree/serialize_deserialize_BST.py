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
        if root == None:
            return None
        data = ""
        nodeStack = []
        nodeStack.append(root)
        while(len(nodeStack) > 0):
            node = nodeStack.pop()
            data += str(node.val)+","
            
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)
        
        print(data[:len(data)-1])
        return data[:len(data)-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == None:
            return None
        
        preorder = [int(x) for x in data.split(',')]
        
        def rebuild(lowerbound, upperbound):
            if root_index[0] == len(preorder):
                return None
            
            root = (preorder[root_index[0]])
            if not lowerbound <= root <= upperbound:
                return None
            root_index[0] += 1
            
            node = TreeNode(root)
            node.left = rebuild(lowerbound, root)
            node.right = rebuild(root, upperbound)
            
            return node
            
        root_index = [0]
        return rebuild(float('-inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
