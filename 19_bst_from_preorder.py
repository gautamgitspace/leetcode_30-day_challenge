class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # recursion base condition
        if not preorder:
            return None
        # get root
        node = TreeNode(preorder[0])

        # find pivot
        i = 1
        for i in range(len(preorder)):
            if preorder[i] > node.val:
                break
            i += 1

        # fabricate left and right
        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])

        return node
