class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = {}
        # prepare map
        for char in s1:
            d[char]  = d.get(char, 0) + 1

        begin, end, counter = 0, 0, len(d)

        while end < len(s2):
            c = s2[end]
            if c in d:
                # CONTRACTION, exhaust keys
                d[c] = d.get(c) - 1
                if d[c] == 0:
                    counter -= 1
            end += 1

            while counter == 0:
                # EXPANSION, formulate keys
                temp_c = s2[begin]
                if temp_c in d:
                    d[temp_c] = d.get(temp_c) + 1
                    if d[temp_c] > 0:
                        counter += 1
                # specific problem logic
                if end - begin == len(s1):
                    return True
                begin += 1
        return False
