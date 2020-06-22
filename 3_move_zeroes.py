class Solution(object):
    def moveZeroes(self, nums):
        """
        using extra space and returning that
        using one pointer to track insertion
        """
        space = [0] * len(nums)
        p = 0
        for i in range (len(nums)):
            if nums[i] != 0:
                space[p] = nums[i]
                p += 1
            else:
                pass
        return space

    def moveZeroesNoExtraSpace(self, nums):
        """
        modify nums in-place instead, the snowball approach
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter += 1
            else:
                if counter > 0:
                    nums[i - counter] = nums[i]
                    nums[i] = 0
    def moveZeroesShallowCopy(self, nums):
        """
        shallow copy of list
        """
        counter = nums.count(0)
        nums [:] = [i for i in nums if i != 0]
        nums += [0] * counter
