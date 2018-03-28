# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def reconstructTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """
        start, end = 0, len(pre/in)
        preorder[start] -> root
        find root in inorder and split into LST and RST
        LST -> inorder[start:rootindex] and preorder[start+1:start+1size_of_LST]
        RST -> inorder[rootindex+1:end] and preorder[start+1size_of_LST:end]
        
        """
        hm_inorder = {data: i for i, data in enumerate(inorder)}
        
        def buildTree(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end or in_start >= in_end:
                return None
            root_inorder_index = hm_inorder[preorder[pre_start]]
            size_LST = root_inorder_index - in_start
            
            node = TreeNode(preorder[pre_start])
            node.left = buildTree(pre_start+1, pre_start+1+size_LST, in_start, root_inorder_index)
            node.right = buildTree(pre_start+1+size_LST, pre_end, root_inorder_index+1, in_end)
            
            return node
        
        
        return buildTree(0, len(preorder), 0, len(inorder))
