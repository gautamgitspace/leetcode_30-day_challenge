class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        
        
        while low < high:
            count_lt = 0
            mid = low + (high - low)/2
            # calculate count of elements
            # in nums that are LT mid
            for num in nums:
                if num <= mid:
                    count_lt += 1
                    """
                    STORY TIME
                    If count_lt > mid, then there are more
                    than mid elements in the range 1 .. mid
                    and thus that range contains a duplicate.
                    
                    So we check to know whether the first half
                    is too crowded, and if it isn't, we know that
                    the second half is.
                    """
            if count_lt <= mid:
                # first half too crowded
                low = mid + 1
            else:
                # if not first half, then second must be
                high = mid
        return low   
