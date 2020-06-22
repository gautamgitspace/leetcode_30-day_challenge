class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 1
        if num == 1: return 0
        x = 1
        while x <= num:
            x <<= 1
        return num ^ (x-1)
