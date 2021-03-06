# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def height(root):
    if root != None:
        if root.level == None:
            root.level = 0
            
        h1 = root.level
        h2 = root.level
        
        if root.left != None:
            root.left.level = root.level + 1
            h1 = height(root.left)
            
        if root.right != None:
            root.right.level = root.level + 1
            h2 = height(root.right)
            
        return max([h1,h2])
    else:
        return 0
    
