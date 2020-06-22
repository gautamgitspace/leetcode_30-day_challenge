from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        d = Counter(s)
        d = sorted(d.items(), key = operator.itemgetter(1), reverse = True)

        for k, v in d:
            for i in range(v):
                ret += k
        return ret

    def frequencySortPy3(self, s):
        ret = ''
        c = {k: v for k, v in sorted(Counter(s).items(), key = lambda item : item[1], reverse = True)}
        for k, v in c.items():
            for i in range (v):
                ret += k
        return ret
