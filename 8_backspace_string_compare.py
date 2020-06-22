class Solution(object):
    def helper(self, input):
        input = list(input)
        pop = 0
        for i in range(len(input)-1, -1, -1):
            if input[i] == '#':
                pop += 1
                del input[i]
            elif input[i].isalpha() and pop != 0 and input:
                del input[i]
                pop -= 1
        return input

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S = ''.join(self.helper(S))
        T = ''.join(self.helper(T))

        if S == T:
            return True
        return False
        
