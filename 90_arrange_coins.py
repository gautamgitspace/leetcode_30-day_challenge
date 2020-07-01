"""

this solution hits memory limit
for big inputs. So will the stack
approach. Alternatives?

"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        s = 0
        for i in range(1, n):
            s = i
            while i:
                n -= 1
                if n < 0:
                    return s - 1
                i -= 1  
        return s

"""
approach 2: compute and store running sum
n must be in running sum if its a stable
stair arrangement. If the stair arrangement
is unstable, we return index of item LT n

use BS to search n in the running_sum arr

Guess what? this gives memory error too for
large integers like 1804289383
"""
    def arrangeCoins(self, n):
        if n == 1:
            return 1
        running_sum = []
        sum = 0
        for i in range (1, n):
            sum += i
            running_sum.append(sum)
        low, high = 0, len(running_sum) - 1
        while low <= high:
            mid = low + (high - low)/2

            if n < running_sum[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

"""
approach 3: hit and trial. NOOB question
"""
    def arrangeCoins(self, n):
        i = 1
        while n >= 0:
            n -= i
            i += 1
        return i - 2
