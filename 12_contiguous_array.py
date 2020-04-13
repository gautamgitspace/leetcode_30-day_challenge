class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # make all zeroes ones
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] = -1
        d = {}
        d [0] = -1
        pre_sum, max_len = 0, 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum in d:
                max_len = max(max_len, i - d[pre_sum])
            else:
                d[pre_sum] = i
        return max_len
