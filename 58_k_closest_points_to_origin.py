import math
import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        results, ret = [], []
        for coords in points:
            x, y = coords
            compute = math.sqrt(math.pow((x - 0), 2) + math.pow((y - 0), 2))
            print compute
            heapq.heappush(results, (compute, x, y))

        while K:
            cherry = heapq.heappop(results)[1:3]
            ret.append(list(cherry))
            K -= 1
        return ret

        
