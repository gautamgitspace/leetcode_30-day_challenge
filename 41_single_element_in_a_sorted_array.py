class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return None
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)/2
            if mid % 2 == 0:
                # even case
                if nums[mid] == nums[mid + 1]:
                    # skip mid + 1 as mid == mid+1
                    # move on the next
                    l = mid + 2
                else:
                    r = mid
            else:
                # odd case
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]
