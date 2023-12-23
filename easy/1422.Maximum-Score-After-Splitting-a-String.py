# 1422. Maximum Score After Splitting a String

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        for i in range(1, len(s)):
            m = max(m, s[:i].count('0')+ s[i:].count('1'))
        return m
