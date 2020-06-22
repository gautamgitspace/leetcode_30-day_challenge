class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j, res = 0, 0, []
        while i < len(A) and j < len(B):
            # follow the given pattern and find out
            # what needs to be inserted in [L,R]
            l = max(A[i][0], B[j][0])
            r = min(A[i][1], B[j][1])

            if l <= r:
                res.append([l, r])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res
