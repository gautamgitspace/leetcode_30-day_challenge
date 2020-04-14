class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        l_shifts, r_shifts = 0, 0
        for item in shift:
            if item[0] == 1:
                r_shifts += item[1]
            elif item[0] == 0:
                l_shifts += item[1]
        if r_shifts > l_shifts:
            return self.helper(s, r_shifts - l_shifts, 1)
        elif l_shifts > r_shifts:
            return self.helper(s, l_shifts - r_shifts, 0)
            # l and r shifts cancel out
        return s

    def helper(self, s, shifts, direction):
        if shifts > len(s):
            # rotate
            shifts %= len(s)
        if direction == 0:
            return s[shifts:] + s[:shifts]
        return s[-shifts:] + s[0:-shifts]
