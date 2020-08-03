class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        """
        [A A A A B B D E]
        using most frequent first: [A ## A ## A ## A]
        other jobs in idle time:   [A BD A BE A ## A] i.e. 10 intervals

        HEAP            TEMP                    TIME(increment 1 base)
        (-4,A)->        [(-3,A)]                  1
        (-2,B)->        [(-3,A), (-1,B)]          2
        (-1,D)->        [(-3,A), (-1,B)]          3

        *********************COOL TIME COMPLETE************************
        put items in TEMP back to HEAP

        HEAP becomes: [(-3,A), (-1,E), (-1,B)]

        HEAP            TEMP                    TIME
        (-3,A)->        [(-2,A)]                  4
        (-1,B)->        [(-2,A)]                  5
        (-1,E)->        [(-2,A)]                  6

        *********************COOL TIME COMPLETE************************
        put items in TEMP back to HEAP

        HEAP becomes: [(-2,A)]

        HEAP            TEMP                    TIME
        (-2,A)->        [(-1,A)]                  7
        EMPTY                                     8
        EMPTY                                     9

        *********************COOL TIME COMPLETE************************
        put items in TEMP back to HEAP

        HEAP becomes: [(-1,A)]

        HEAP            TEMP                    TIME
        (-1,A)->                                 10
        EMPTY           EMPTY                   break
        """
        curr_time, h = 0, []
        # make count map for all jobs to find most frequent
        # and push all in heap. heap will track most frequent
        # as the pop candidate

        for k, v in Counter(tasks).items():
            heapq.heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x, y = heapq.heappop(h)
                    if x != -1:
                        # we can process other tasks instead staying idle
                        # until the cool-off timer is over
                        temp.append((x+1, y))
                if not h and not temp:
                    break
                else:
                    i += 1
            # push back all items to temp for next round processing
            for item in temp:
                heapq.heappush(h, item)
        return curr_time
