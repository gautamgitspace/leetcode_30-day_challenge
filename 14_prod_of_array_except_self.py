class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        L =     [   1      1*1     1*2*1   1*3*2*1]
        input = [   1       2        3       4    ]
        right = [2*3*4*1  3*4*1     4*1      1    ]
        index = [   0       1        2       3    ]
        """
        res = []
        l, r = 1, 1
        # LEFTS
        for i in range(len(nums)):
            if i > 0:
                l *= nums[i-1]
            res.append(l)
        # RIGHTS
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                r *= nums[i+1]
            # LEFTS * RIGHTS
            res[i] *= r

        return res
