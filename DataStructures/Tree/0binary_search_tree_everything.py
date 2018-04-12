class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self, root):
    self.root = root

  def insert(self, nodeIn):
    node = self.root
    while node != None:
      if nodeIn.data > node.data:
        if node.right:
          node = node.right
        else:
          node.right = nodeIn
          print("Added to right", nodeIn.data)
          break
      else:
        if node.left:
          node = node.left
        else:
          node.left = nodeIn
          print("Added to left", nodeIn.data)
          break
          
  def preOrder_iterative(self):
    node = self.root
    path = [node]
    result = []
    while path:
      curNode = path.pop()
      if curNode:
        result.append(curNode.data)
        path.append(curNode.right)
        path.append(curNode.left)
    return result
  
  def preOrder_recursive(self):
    def preOrder_helper(node):
      if node == None:
        return
      result.append(node.data)
      preOrder_helper(node.left)
      preOrder_helper(node.right)
    result = []
    node = self.root
    preOrder_helper(node)
    return result

  def postOrder_recursive(self):
    def postOrder_helper(node):
      if node == None:
        return
      postOrder_helper(node.left)
      postOrder_helper(node.right)
      result.append(node.data)
    result = []
    node = self.root
    postOrder_helper(node)
    return result
  
  

  
def main():
  root = Node(43)
  bst = BST(root)
  #arr = [3,2,7,8,4,6]
  arr = [23,37,29,31,41,47,53]
  for x in (arr):
    bst.insert(Node(x))
    
  preOrder =  bst.preOrder_iterative()
  print("Pre Order: "),
  print(preOrder)
  #print(bst.preOrder_recursive())
  print(bst.postOrder_recursive())

main()
