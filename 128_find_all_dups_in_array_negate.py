class Solution(object):
    def findDuplicates(self, nums):
        """
	- levrage index property: if there were no dups
          in the array, all would have been arranged in
	  index + 1 fashion iff sorted.

	- negate when encountered, check which ones are
	  not negated and collect them
        """
        res = []
        for item in nums:
            if nums[abs(item) - 1] > 0:
                # mark it by negating it
                nums[abs(item) - 1] *= -1
            else:
                # this has been marked previously,
                # store it
                res.append(abs(item))
        return res
