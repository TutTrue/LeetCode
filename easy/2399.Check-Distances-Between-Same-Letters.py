# 2399. Check Distances Between Same Letters

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] = i - dic[s[i]] - 1
            else:
                dic[s[i]] = i

        for k, v in dic.items():
            if distance[ord(k) - 97] != v:
                return False
        return True
