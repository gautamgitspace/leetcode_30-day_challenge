class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        container = []
        for char in s:
            if not char.isdigit():
                if char.isalpha():
                    container.append(char.lower())
            else:
                container.append(char)
        return container == list(reversed(container))
