"""
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".
"""
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sc, dc = [], []
        if len(paths) == 1:
            return paths[0][1]
        for item in paths:
            sc.append(item[0])
            dc.append(item[1])
        for item in dc:
            if item not in sc:
                return item
