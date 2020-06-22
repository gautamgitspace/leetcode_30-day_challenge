class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumberAltA(self, nums):
        """
        using dict
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for k, v in d.items():
            if v == 1:
                return k

    def singleNumberAltB(self, nums):
        """
        using set
        """
        collect = set()
        for num in nums:
            if num not in collect:
                collect.add(num)
            else:
                collect.remove(num)

        for item in collect:
            return item
