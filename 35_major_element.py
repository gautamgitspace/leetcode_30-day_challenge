class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                count += 1
            elif count == 0:
                # time to change major
                major = nums[i]
                count += 1
            else:
                count -= 1
        return major
                
