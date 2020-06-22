class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # replace all 0s with -1s
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        """
        now this problem is same as max length
        of the subarray that sums up to k (k=0)
        as in [-1, 1, -1, [-1, 1] and [1, -1]
        sum up to 0. so max len is 2 for either

        Recall from running sum + hash table 
        approach that running sum - k is an
        element of the dict OR we can say that
        running sum elem1 - running sum elem2
        give us the value of k.
        """
        # we use a dict to memoize by storing the
        # running sum as they key and index as the
        # value. We init it with base index condition

        d = {}
        d[0] = -1

        max_len, presum, k = 0, 0, 0

        for i in range(len(nums)):
            presum += nums[i]
            # check if running sum - k exists in d
            # if it does, update max with the length
            # of the subarray (current - element in d)
            if presum - k in d:
                max_len = max(max_len, i - d[presum - k])
            else:
                d[presum] = i
        return max_len
