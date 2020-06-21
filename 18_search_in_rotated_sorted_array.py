class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            # normal ascending flow:
            if nums[low] <= nums[mid]:
                # check if target lies between low and mid.
                # if yes,  high becomes left of mid else its
                # to the right of mid, so low becomes mid + 1
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # check if the target lies between mid and high.
                # if yes, low becomes right of mid
                # otherwise high becomes left of mid
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
