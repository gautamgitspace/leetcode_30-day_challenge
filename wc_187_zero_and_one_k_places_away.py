"""
Given an array nums of 0s and 1s and an integer k,
return True if all 1's are at least k places away
from each other, otherwise return False.
"""
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        idx = []
        for i, num in enumerate(nums):
            if num == 1:
                idx.append(i)
        for i in range (0, len(idx)-1):
            if idx[i+1] - idx[i] <= k:
                return False
        return True
