class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        not_colored, blue = 0, 1

        def helper(person, color):
            # replace -1's with blue, basically color the graph
            # for this person
            color_table[person] = color

            """
            check:
            (a) if other_person for this person has same color
            also
            (b) if its not colored and when given green (-ve of blue)
            to helper, helper doesn't return true

            in both (a) and (b) we return False, as for (a) we can't allow
            same color and for (b) helper ought to return True.

            Otherwise we return True
            """
            for other_person in dislike_table [person]:
                if color_table[other_person] == color:
                    return False
                if color_table[other_person] == not_colored and not helper(other_person, -color):
                    return False
            return True

        if N == 1 or not dislikes:
            return True

        # construct dislike table map
        dislike_table = defaultdict(list)
        for person1, person2 in dislikes:
            dislike_table[person1].append(person2)
            dislike_table[person2].append(person1)

        # construct a base color table with all not colored (-1's)
        color_table = [not_colored for _ in range (N + 1)]

        # check liking for all the persons:
        for person in range(1, N + 1):
            if color_table[person] == not_colored and not helper(person, blue):
                return False
        return True
