class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = [0]
        self.depth(root, diameter)
        return diameter[0]

    def depth(self, root, diameter):
        if not root:
            return 0
        # compute left height
        left = self.depth(root.left, diameter)
        # compute right height
        right = self.depth(root.right, diameter)
        # find max of stored and new
        diameter[0] = max(diameter[0], left + right)
        print diameter
        # 1 is added for only one child BT
        return 1 + max(left, right)
