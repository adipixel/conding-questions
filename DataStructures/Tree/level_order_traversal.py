"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    
    while(len(queue) > 0):
        print queue[0].data,
        node = queue.pop(0)
        
        if node.left != None:
            queue.append(node.left)
        
        if node.right != None:
            queue.append(node.right)
