class Solution(object):
    def swap(self, l, i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        low, mid, high DENOTE 0, 1, 2 respetively
        also, low and high are expansion and contraction
        pointers. whreas Mid is the inspection element.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                # low is taking mid's place
                # swap em and increment mid and low
                self.swap(nums, mid, low)
                mid += 1
                low += 1
            elif nums[mid] == 1:
                # mid is in its place, nothing to swap
                # just move to inspect next element or
                # to make mid take someone's place so
                # that gets rectified in the next iter
                mid += 1
            elif nums[mid] == 2:
                # high is taking mid's place
                # swap em, decrement high
                self.swap(nums, mid, high)
                high -= 1
