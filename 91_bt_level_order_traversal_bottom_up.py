class Solution(object):
    def levelOrderBottom(self, root):
        """
        FUNNY
        """
        # to hold all node data
        # that we need to return
        result = []
        level = [root]
        
        while root and level:
            # for each node in the list 'level'
            # we append the node.val to curr
            # and finally put data from curr to
            # result
            current_nodes, next_level = [], []
            for node in level:
                current_nodes.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            # dump data to result
            result.append(current_nodes)
            # update level
            level = next_level
        return result [::-1]

    def levelOrderBottom(self, root):
        """
        NOT SO FUNNY
        """
        level = [root]
        # res is our storage. for every new level, 
        # we append a sublist to the left which 
        # will contain node vals of the next level. 
        # This way root keeps going further right 
        # and hence  we achieve the reverse order
        res = collections.deque()
        
        while root and level:
            # same as FUNNY approach, we create 
            # space for next level and storage 
            # for nodes at current level
            res.appendleft([])
            next_level = []
            for node in level:
                res[0].append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level = next_level
        return res
            
