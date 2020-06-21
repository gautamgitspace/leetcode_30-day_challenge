class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for item in arr:
            if item + 1 in arr:
                count += 1
        return count
