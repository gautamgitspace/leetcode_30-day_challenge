class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for entity in strs:
            anagrams[tuple(sorted(entity))].append(entity)
        return anagrams.values()
