# 2405. Optimal Partition of String

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        l = 0
        r = 0
        li = set()
        while r < len(s):
            if s[r] in li:
                l = r
                count+=1
                li.clear()
            else:
                li.add(s[r])
                r +=1
        return count
