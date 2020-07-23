class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xorian = nums[0]
        for item in nums[1:]:
            xorian ^= item
        
        bit_set = 1
        
        while xorian & bit_set == 0:
            bit_set <<= 1
        """
        now we know the Ith bit which would be
        diff for those two numbers that occur once
        
        now we need to for two groups. One of the
        two that occur only once would fall in
        one of these two groups. these groups will
        have numbers from nums whose Ith bit will
        be either 1 or 0. For the givrn testcase,
        
        it will be:
        
        G1 {1,1,5} and G2 {2,2,3}
        
        whether the bit is 0 or 1 can be evaulated
        by ANDing bit_set with number and checking
        for 1 or 0. Once we have determined these
	groups, we just do xorian for a group and
	find the odd one out, just like simple num1
	problem. So we have:
        """
        n1, n2 = 0, 0
        for num in nums:
            if num & bit_set:
                # xorian for all in say G1
                # off one out will stick to n1
                n1 ^= num
            else:
                # xorian for all in say G2
                # off one out will stick to n2
                n2 ^= num
        return [n1, n2]
