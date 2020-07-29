class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx + 1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
        
            return root
