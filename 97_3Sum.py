#!/usr/bin/python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        - [1] sort the array so that we can use the L and R
          pointers expansion/contraction logic

        - all elements are thought to be as targets. When
          other elements are added to this target and if they
          make sum as zero, that's our deal

        - [2] if consecutve numbers are same, skip the following
          one as previous has already been processed as a
          target

        - [3] if sum is less, we expand, if its more we contract
          we do this for whole range i.e. L to R. And if sum is
          0, we add it to res

        """
        res = set()
        # [1]
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]:
                # [2]
                continue
            l, r = i+1, n-1
            while l < r:
                # [3]
                sum = nums[i] + nums[r] + nums[l]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1
        return [list(i) for i in res]

if __name__ == "__main__":
    sum = Sum()
    nums = [-1,0,1,2,-1,-4]
    print(sum.three_sum(nums))
