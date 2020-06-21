class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        solos = []
        d = defaultdict(list)
        for i, item in enumerate(s):
            d[item].append(i)

        for k, v in d.items():
            if len(d[k]) == 1:
                solos.append(v[0])

        if len(solos):
            return min(solos)
        return -1
