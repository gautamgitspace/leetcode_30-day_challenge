class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ctr = 0
        for stone in S:
            if stone in J:
                ctr += 1
        return ctr
