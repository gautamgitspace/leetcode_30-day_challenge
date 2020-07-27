class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        - init low, high and iteratively calculate mid
        - if the number at mid is GT number at high this
          clearly means that rotation exists int the
          right portion i.e. [mid -> high]
          otherwise it exists in the portion [low -> mid]
        
        - what extra needs to be done to handle dups?
          for cases like [3,3,1,3] where dups are in the
          end of the ascent and then the array is rotated
          we need to decide what would new j be? mid or 
          just j - 1. this is highly case by case and can
          be mastered by examples
        """
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) / 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid if nums[j] != nums[mid] else j - 1
        return nums[i]
