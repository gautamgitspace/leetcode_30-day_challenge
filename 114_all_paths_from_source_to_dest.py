class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        
        the nodes are 0,1 ... len(graph)-1
        """
        
        N = len(graph) - 1
        ans = []
        
        """
        starting from Node 0, now we need to check
        what all connects to 0. this will be given
        by graph[0] i.e. [1,2]
        
        we proces [1,2] one by one as both connect
        to node 0. To process them one by one, we
        start with the last element hence path[-1]
        this gives us two 'possible-way(s)'to node
        N. i.e. [0,1] and [0,2].
        
        Since we haven't reached the Node N yet, we
        add these possible-way(s) to roadway
        
        Once a possible_way reaches the node N, we 
        append it to the ans
        """
        roadway = [[0]]
        while roadway:
            possible_way = roadway.pop()
            for node in graph[possible_way[-1]]:
                if node == N:
                    # we reached from 0 to N, add
                    # this to answer
                    ans.append(possible_way + [node])
                else:
                    # we haven't reached N yer, add
                    # this to paths
                    roadway.append(possible_way + [node])
        return ans
