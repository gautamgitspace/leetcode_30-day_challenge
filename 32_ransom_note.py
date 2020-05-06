from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = Counter(ransomNote)
        mag = Counter(magazine)

        for key in note.keys():
            if key in mag.keys():
                if float(mag[key]) / float(note[key]) < 1.0:
                    return False
            else:
                return False
        return True
