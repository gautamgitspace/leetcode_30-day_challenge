tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        - if tree were to be represented as an array
          the indices would have been this way for
          node i:
          i, left child (2*i), right child(2*i + 1)..
          
        - at each node we maintain a list like this:
          lst[(node, position)] where node will be
          the node being visited and position will
          be based on the calculation of left child
          or right child and i
          
        - at any level, width then would be:
          last elem pos in lst - first elem pos in lst + 1
        """
        width = 0
        level = [(root, 0)]
        while level:
            next_level = []
            width = max(width, level[-1][1] - level[0][1] + 1)
            # traverse the level lst now
            # for each node we scan L & R
            for node, pos in level:
                if node.left:
                    next_level.append((node.left, pos * 2))
                if node.right:
                    next_level.append((node.right, pos * 2 + 1))
            level = next_level
        return width
    
