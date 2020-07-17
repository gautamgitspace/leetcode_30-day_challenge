class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        skim = s.split(' ')
        skim = [i for i in skim if len(i) != 0]
        return ' '.join(skim[::-1]

    def reverseWordsOneLiner(self, s):
        return ' '.join([i for i in s.split(' ') if len(i) != 0][::-1])
