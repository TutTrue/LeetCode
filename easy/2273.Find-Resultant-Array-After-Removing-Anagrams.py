# 2273. Find Resultant Array After Removing Anagrams

class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        i = 0
        s = set(words)
        while i < len(words) - 1:
            if sorted(words[i]) == sorted(words[i+1]):
                s.remove(words[i+1])
            else:
                i+=1
        return words
