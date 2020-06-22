class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # first lets send all of em to A
        first_city = [i for i, j in costs]
        # calculate diff of fare
        diff = [j - i for i, j in costs]
        # now add up first AND smallest of
        # len(costs)/2
        return sum(first_city) + sum(sorted(diff)[:len(costs)//2])
