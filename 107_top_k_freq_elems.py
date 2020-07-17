class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        c = collections.Counter(nums)
        for item in c.most_common(k):
            ret.append(item[0])
        return ret
