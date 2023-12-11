# 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        longest = 1
        left = 0
        right = 0
        dic = set()
        while right < len(s):
            if s[right] not in dic:
                dic.add(s[right])
                right+=1
                longest = max(longest, right - left)
            else:
                dic.remove(s[left])
                left +=1
        return longest
