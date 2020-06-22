class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # recursion base conditon
        if not preorder:
            return None
        # get root i.e. the first element
        node = TreeNode(preorder[0])

        # get the pivot element i.e. element
        # greater than root. This is start
        # of the right branch and end of left
        i = 1
        for i in range(len(preorder)):
            if preorder[i] > node.val:
                break
            i += 1

        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])

        return node
