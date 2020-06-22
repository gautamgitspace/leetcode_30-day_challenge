class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Sample run for [3,2,5,3,2,4], k = 10:
        running_sum looks like: [3,5,10,13,15,19]

        stretches where sum equals k are:
        10 -> 0 : achieved by: sums - k = element already in running_sum
        13 -> 3 : achieved by: sums - k = element already in running_sum
        15 -> 5 : achieved by: sums - k = element already in running_sum

        so we keep track of how many times the element is there in
        the running_sum by storing them in dict

        """
        d = dict()
        running_sum, count = 0, 0
        d[0] = 1
        for i in range(len(nums)):
            # compute running sum
            running_sum += nums[i]
            # calculate count by fetching current running_sum - k from dict
            count += d.get(running_sum - k, 0)
            # store in dict. +1 if a new occurence 
            d[running_sum] = d.get(running_sum, 0) + 1
        return count
