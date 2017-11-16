""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
iMAX = 4294967296
iMIN = -4294967296

def checkBST(root):
    return (isBSTUtil(root, iMIN, iMAX))

def isBSTUtil(root, imin, imax):
    if root is None:
        return True
    if root.data < imin or root.data > imax:
        return False
    return (isBSTUtil(root.left, imin, root.data-1) and isBSTUtil(root.right, root.data+1, imax))
    
