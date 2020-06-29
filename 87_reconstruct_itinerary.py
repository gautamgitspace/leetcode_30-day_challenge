from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for s, d in tickets:
            graph[s].append(d)

        # sort destinations for each source
        # here we sort all the vals in the
        # list for a particular key. this
        # is different from sort dict by vals
        # for many f**king obvious reasons
        for source in graph:
            graph[source].sort(reverse = True)

        stack, res = ['JFK'], []

        # keep checking if TOS exists in our dict
        # if it does, pop the value for this key
        # and append back to stack, this way we
        # stitch SOURCE and DEST. When we don't
        # have a hit in the dict, we pop from
        # stack and append to res
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]
