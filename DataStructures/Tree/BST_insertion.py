"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    node = r
    if node != None:
        while True:
            if node.data == val:
                return r
            if val < node.data:
                if node.left is None:
                    node.left = Node(val)
                    return r
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(val)
                    return r
                node = node.right
     return Node(val)
            
