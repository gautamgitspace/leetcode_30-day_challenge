class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res, d = [], {}
        begin, end = 0, 0

        for item in p:
            d[item] = d.get(item, 0) + 1

        counter = len(d)

        while end < len(s):
            # WINDOW EXPANSION
            c = s[end]
            if c in d:
                d[c] = d.get(c) - 1
                if d[c] == 0:
                    counter -= 1
            end += 1
            """
            counter value reaching 0 means:
            - we have exhausted all keys, check
              if we have encountered an anagram
              until now
            - make keys available again by evaulating
              the begin ptr and incrementing counter
              accordingly
            """
            while counter == 0:
                # WINDOW CONTRACTION
                temp_c = s[begin]
                if temp_c in d:
                    d[temp_c] = d.get(temp_c) + 1
                    if d[temp_c] > 0:
                        # we bail out as soon as
                        # counter becomes > 0
                        counter += 1
                if end - begin == len(p):
                    res.append(begin)
                begin += 1
        return res
