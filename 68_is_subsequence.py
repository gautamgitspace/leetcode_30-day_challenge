from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        len(counter(s) & counter(t)) == len(s) won't work
        as the order of occurence of alphabets in s should
        be same as that of in t.
        """
        for char in s:
            i = t.find(char)
            if i == -1:
                return False
            t = t[i + 1:]
        return True

    def isSubsequenceUsingTwoPtrs(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False

    def isSubsequenceOptimizedBS(self, s, t):
        """
        this is needed when the flow of s and t
        is at a high rate and we need to speed
        up our operation of finding Subsequence
        """
        lower_bound = 0
        index_map = defaultdict(list)
        for i, char in enumerate(t):
            index_map[char].append(i)

        for char in s:
            if char not in index_map: return False
            index_list = index_map[char]
            i = bisect_left(index_list, lower_bound)
            if i == len(index_list): return False
            lower_bound = index_list[i] + 1
        return True
