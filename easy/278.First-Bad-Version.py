# 278. First Bad Version

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        e = n
        m = 0
        min = None
        while e >= s:
            m = (s + e) // 2
            if isBadVersion(m):
                min = m
                e = m - 1
            else:
                s = m +1
        return min
