class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        max_ulti = nums[0]

        for i in range (1, len(nums)):
            """
            We gotta track max_ulti (which we return as final) and max_so_far

            basically we gotta add elements 0 and 1 and compare it with 1 for
            max. Gotta remember, even one lone element can be max

            for input [-2,1,-3,4,-1,2,1,-5,4]
            max_so_far will iterate like below:
            max of (-2+1 and 1) => 1
            max of (1+-3 and -3) => -2
            max of (-2+4 and 4) => 4
            max of (4+-1 and -1) => 3
            ... and so on
            """
            max_so_far = max(max_so_far + int(nums[i]), int(nums[i]))
            max_ulti = max(max_so_far, max_ulti)

        return max_ulti
