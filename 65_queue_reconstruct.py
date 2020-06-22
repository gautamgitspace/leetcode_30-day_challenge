class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]

        fix the position of tallest and the second tallest
        in the sub list and then insert next smallest as per k

        so for input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

        the sub list at start becomes = [[7,0], [7,1]]. Now we
        pick next smallest to 7 i.e. 6 and insert it at 6th's k
        i.e. index 1.

        To achieve this for the full list we can do one time sort
        and walk the list to just insert the next smallest at its k

        """
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for item in people:
            res.insert(item[1], item)
        return res
